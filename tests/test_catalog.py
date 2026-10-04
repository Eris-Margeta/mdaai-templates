import copy
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('catalog', ROOT / 'scripts/validate_catalog.py')
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

class CatalogTests(unittest.TestCase):
    def test_real_catalog(self):
        self.assertEqual(catalog.validate()['templates'], 2)

    def test_safe_path(self):
        self.assertEqual(catalog.safe_path(ROOT, 'templates/mdaai-2/AGENTS.md'), ROOT / 'templates/mdaai-2/AGENTS.md')

    def test_no_provider_entry_payload(self):
        for name in ('CLAUDE.md', 'claude.MD', 'nested/ClAuDe.Md'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                catalog.safe_path(ROOT, 'templates/mdaai-1/' + name)

    def test_traversal(self):
        with self.assertRaises(ValueError):
            catalog.safe_path(ROOT, 'templates/mdaai-2/../../README.md')

    def test_absolute(self):
        with self.assertRaises(ValueError):
            catalog.safe_path(ROOT, '/templates/mdaai-2/AGENTS.md')

    def test_unlisted_family(self):
        with self.assertRaises(ValueError):
            catalog.safe_path(ROOT, 'templates/unknown/AGENTS.md')

    def test_backslash(self):
        with self.assertRaises(ValueError):
            catalog.safe_path(ROOT, 'templates/mdaai-2/a\\b')

    def test_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'templates').mkdir()
            (root / 'templates/mdaai-2').symlink_to(ROOT / 'templates/mdaai-2', target_is_directory=True)
            with self.assertRaises(ValueError):
                catalog.safe_path(root, 'templates/mdaai-2/AGENTS.md')

    def mutate(self, change):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for name in ('templates', 'tests', 'assets'):
                shutil.copytree(ROOT / name, root / name)
            for name in ('templates.json', 'export-manifest.json', 'VERSION'):
                shutil.copyfile(ROOT / name, root / name)
            change(root)
            with self.assertRaises((AssertionError, ValueError)):
                catalog.validate(root)

    def test_catalog_logo_digest(self):
        self.mutate(lambda r: (r / 'assets/brand/logo-black.svg').write_text('changed'))

    def test_no_missing_revision_outside_original_artwork(self):
        def change(root):
            p = root / 'export-manifest.json'
            v = json.loads(p.read_text())
            v['files'][0]['sourceRevision'] = None
            p.write_text(json.dumps(v))
        self.mutate(change)

    def test_readme_theme_logos(self):
        import xml.etree.ElementTree as ET
        readme = (ROOT / 'README.md').read_text()
        for color, theme, fill in [('black', 'light', '#000'), ('white', 'dark', '#fff')]:
            path = 'assets/brand/logo-' + color + '.svg'
            self.assertIn('media="(prefers-color-scheme: ' + theme + ')" srcset="' + path + '"', readme)
            svg = ET.fromstring((ROOT / path).read_bytes())
            self.assertEqual(svg.attrib, {'viewBox': '0 0 512 512', 'fill': fill})
            self.assertEqual([e.tag.rsplit('}', 1)[-1] for e in svg], ['title', 'path', 'path'])
        self.assertIn('src="assets/brand/logo-black.svg"', readme)

    def test_changed_byte(self):
        self.mutate(lambda r: (r / 'templates/mdaai-2/AGENTS.md').write_text('changed'))

    def test_extra_payload(self):
        self.mutate(lambda r: (r / 'templates/mdaai-2/extra.md').write_text('unlisted'))

    def test_duplicate_entry(self):
        def change(root):
            p = root / 'templates.json'
            v = json.loads(p.read_text())
            v['templates'][0]['files'].append(copy.deepcopy(v['templates'][0]['files'][0]))
            p.write_text(json.dumps(v))
        self.mutate(change)

    def test_bad_digest(self):
        def change(root):
            p = root / 'templates.json'
            v = json.loads(p.read_text())
            v['templates'][0]['files'][0]['sha256'] = '0' * 64
            p.write_text(json.dumps(v))
        self.mutate(change)

    def test_link_baseline_not_silent(self):
        self.mutate(lambda r: (r / 'tests/known-source-link-gaps.json').write_text('[]'))

if __name__ == '__main__':
    unittest.main()
