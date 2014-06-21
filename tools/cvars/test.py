import json, cvars
with open('cvarlist.json','w') as f:
    f.write(json.dumps(cvars.cvars('cvarlist.log'),indent=4,sort_keys=True,separators=(',', ': ')))