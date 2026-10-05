#!/usr/bin/env python3
"""Validate catalog bytes and safe payload paths; never execute template scripts."""
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def safe_path(root, name):
    p = PurePosixPath(name)
    if not isinstance(name, str) or '\\' in name or p.is_absolute() or '..' in p.parts or str(p) != name:
        raise ValueError('unsafe path')
    if p.name.casefold() == 'claude.md':
        raise ValueError('provider-specific entry payload is not allowed')
    if len(p.parts) < 3 or p.parts[:2] not in [('templates', 'mdaai-1'), ('templates', 'mdaai-2')]:
        raise ValueError('path outside allowlisted template')
    target = root
    for part in p.parts:
        target = target / part
        if target.is_symlink():
            raise ValueError('symlink refused')
    return target

def link_inventory(root, manifest):
    missing = []
    for template in manifest['templates']:
        base = root / 'templates' / template['id']
        for f in template['files']:
            path = root / f['path']
            if path.suffix != '.md':
                continue
            fenced = False
            for number, line in enumerate(path.read_text().splitlines(), 1):
                if line.lstrip().startswith(('```', '~~~')):
                    fenced = not fenced
                    continue
                if fenced:
                    continue
                for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', line):
                    target = target.split()[0].strip('<>')
                    u = urlsplit(target)
                    if u.scheme or u.netloc:
                        continue
                    resolved = (path.parent / unquote(u.path)).resolve()
                    if not resolved.is_relative_to(base.resolve()) or not resolved.exists():
                        missing.append({'path': f['path'], 'line': number, 'target': target})
    return sorted(missing, key=lambda e: (e['path'], e['line'], e['target']))

def validate(root=ROOT):
    catalog = json.loads((root / 'templates.json').read_text())
    provenance = json.loads((root / 'export-manifest.json').read_text())
    assert catalog['schemaVersion'] == provenance['schemaVersion'] == 1
    assert catalog['repository'] == 'Eris-Margeta/mdaai-templates'
    assert 1 <= len(provenance['files']) <= 500
    assert catalog['catalogVersion'] == (root / 'VERSION').read_text().strip()
    assert [t['id'] for t in catalog['templates']] == ['mdaai-1', 'mdaai-2']
    entries = {e['path']: e for e in provenance['files']}
    assert len(entries) == len(provenance['files'])
    seen = set()
    for template in catalog['templates']:
        assert re.fullmatch('[0-9a-f]{40}', template['source']['revision'])
        paths = [f['path'] for f in template['files']]
        assert paths == sorted(paths) and template['entrypoint'] in paths
        for file in template['files']:
            name = file['path']
            assert name not in seen
            seen.add(name)
            target = safe_path(root, name)
            assert name.startswith('templates/' + template['id'] + '/')
            assert target.is_file()
            b = target.read_bytes()
            assert isinstance(file['size'], int) and 0 <= file['size'] <= 1_000_000
            assert len(b) == file['size']
            assert re.fullmatch('[0-9a-f]{64}', file['sha256'])
            assert hashlib.sha256(b).hexdigest() == file['sha256']
            assert file['role'] in {'required', 'optional', 'conditional'}
            e = entries[name]
            assert e['sha256'] == file['sha256'] and e['size'] == file['size']
            assert re.fullmatch('[0-9a-f]{64}', e['sourceSha256'])
            assert e['sourceRepository'] == template['source']['repository']
            assert e['sourceRevision'] == template['source']['revision']
            assert e['sourcePath'] == name.removeprefix('templates/' + template['id'] + '/')
            assert e['sourceSha256'] == e['sha256']
            assert e['transformation'] == 'none'
            assert isinstance(e['upstreamProvenance'], dict)
            assert not re.search(rb'/(?:Users|home)/[^\s/]+/|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN [^-]*PRIVATE KEY', b)
    actual = set()
    for p in (root / 'templates').rglob('*'):
        assert not p.is_symlink()
        if p.is_file():
            actual.add(p.relative_to(root).as_posix())
    assert seen == actual == set(entries)
    assert sum(e['size'] for e in entries.values()) <= 5_000_000
    assets = provenance['catalogAssets']
    assert [a['path'] for a in assets] == ['assets/brand/logo-black.svg', 'assets/brand/logo-white.svg']
    for asset in assets:
        target = root / asset['path']
        assert not target.is_symlink()
        b = target.read_bytes()
        assert len(b) == asset['size'] and hashlib.sha256(b).hexdigest() == asset['sha256']
        assert asset['sourceRepository'] == catalog['templates'][0]['source']['repository']
        assert asset['sourceRevision'] == catalog['templates'][0]['source']['revision']
        assert asset['sourcePath'] == asset['path']
        assert asset['sourceSha256'] == asset['sha256']
        assert b == (root / 'templates/mdaai-1' / asset['path']).read_bytes()
    expected = json.loads((root / 'tests/known-source-link-gaps.json').read_text())
    assert link_inventory(root, catalog) == expected, 'New unresolved source links; review and document, never silently waive'
    v2 = root / 'templates/mdaai-2/PROJECT-INTERNAL/MANAGEMENT/TASKS.json'
    assert json.loads(v2.read_text()) == {'schemaVersion': 1, 'taskPrefix': 'APP', 'tasks': []}
    v1 = json.loads((root / 'templates/mdaai-1/PROJECT-INTERNAL/WORK-ORDERS/registry.json').read_text())
    assert not v1['workOrders'] and not v1['sequenceReservations'] and not v1['agents'] and v1['nextSequence'] == 1
    return {'templates': len(catalog['templates']), 'payloadFiles': len(seen), 'bytes': sum(e['size'] for e in entries.values()), 'documentedSourceLinkGaps': len(expected)}

if __name__ == '__main__':
    print(json.dumps(validate(), sort_keys=True))
