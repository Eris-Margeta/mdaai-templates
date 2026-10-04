import copy,json,unittest
from scripts.verify_sources import validate_registration
from pathlib import Path
class AdmissionTests(unittest.TestCase):
 def entry(self):return json.loads((Path(__file__).resolve().parents[1]/'templates.json').read_text())['templates'][0]
 def test_valid(self):self.assertTrue(validate_registration(self.entry()))
 def test_untrusted_repo(self):
  t=self.entry();t['source']['repository']='evil/repo'
  with self.assertRaises(AssertionError):validate_registration(t)
 def test_moving_revision(self):
  t=self.entry();t['source']['revision']='main'
  with self.assertRaises(AssertionError):validate_registration(t)
 def test_duplicate_files(self):
  t=self.entry();t['files'].append(copy.deepcopy(t['files'][0]))
  with self.assertRaises(AssertionError):validate_registration(t)
 def test_bad_hash(self):
  t=self.entry();t['files'][0]['sha256']='invalid'
  with self.assertRaises(AssertionError):validate_registration(t)

 def test_no_provider_entry_payload(self):
  for name in ('CLAUDE.md', 'claude.MD', 'nested/ClAuDe.Md'):
   t=self.entry();t['files'][0]['path']='templates/mdaai-1/'+name
   with self.subTest(name=name), self.assertRaises(AssertionError):validate_registration(t)
