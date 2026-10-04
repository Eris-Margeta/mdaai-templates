import hashlib,json,re,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate_registration(t):
 assert set(t["source"]) == {"repository", "revision"}
 assert re.fullmatch("mdaai-[12]", t["id"])
 assert t["source"]["repository"] == "Eris-Margeta/mdaai-template-"+t["id"].split("-")[-1]
 assert re.fullmatch("[0-9a-f]{40}",t["source"]["revision"])
 assert t["license"]=="Apache-2.0" and t["pythonVersion"]=="3.13.14"
 assert len({e["path"] for e in t["files"]})==len(t["files"])
 for e in t["files"]:
  assert e["path"].startswith("templates/"+t["id"]+"/") and ".." not in Path(e["path"]).parts
  assert re.fullmatch("[0-9a-f]{64}",e["sha256"]) and 0<=e["size"]<=1000000
 return True

def verify():
 m=json.loads((ROOT/'templates.json').read_text());seen=set();count=0
 for t in m['templates']:
  validate_registration(t)
  assert t['id'] not in seen;seen.add(t['id'])
  repo=t['source']['repository'];rev=t['source']['revision']
  assert repo=='Eris-Margeta/mdaai-template-'+t['id'].split('-')[-1]
  assert re.fullmatch('[0-9a-f]{40}',rev) and t['license']=='Apache-2.0' and t['pythonVersion']=='3.13.14'
  for e in t['files']:
   path=e['path'].removeprefix('templates/'+t['id']+'/')
   assert '..' not in Path(path).parts and not Path(path).is_absolute()
   url='https://raw.githubusercontent.com/'+repo+'/'+rev+'/'+path
   b=urllib.request.urlopen(url,timeout=30).read()
   assert len(b)==e['size'] and hashlib.sha256(b).hexdigest()==e['sha256'];count+=1
 return count
if __name__=='__main__':print(verify())
