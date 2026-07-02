import json
def extract(txt):
 d=json.loads(txt);return d.get('intent'),d.get('key'),d.get('value')
