"""Immutable public release pins own current bytes; upstream is historical."""
import copy
import json
import unittest
from pathlib import Path
from scripts.validate_catalog import validate
ROOT = Path(__file__).resolve().parents[1]

class ReleaseProvenanceTests(unittest.TestCase):
    def test_current_payload_provenance_matches_canonical_pin(self):
        catalog = json.loads((ROOT/'templates.json').read_text())
        manifest = json.loads((ROOT/'export-manifest.json').read_text())
        entries = {e['path']: e for e in manifest['files']}
        for template in catalog['templates']:
            self.assertIn(template['templateVersion'], ['1.0.1','2.0.1'])
            for f in template['files']:
                e = entries[f['path']]
                self.assertEqual(e['sourceRepository'], template['source']['repository'])
                self.assertEqual(e['sourceRevision'], template['source']['revision'])
                self.assertEqual(e['sourceSha256'], e['sha256'])
                self.assertEqual(e['transformation'], 'none')
                self.assertIn('upstreamProvenance',e)

if __name__ == '__main__': unittest.main()
