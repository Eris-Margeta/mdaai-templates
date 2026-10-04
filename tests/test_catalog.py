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
            for name in ('templates', 'tests'):
                shutil.copytree(ROOT / name, root / name)
            for name in ('templates.json', 'export-manifest.json', 'VERSION'):
                shutil.copyfile(ROOT / name, root / name)
            change(root)
            with self.assertRaises((AssertionError, ValueError)):
                catalog.validate(root)

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
