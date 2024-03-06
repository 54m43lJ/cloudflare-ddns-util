import requests
import json
import subprocess
from os import path

def mod_rec(domain, zone, record, type, address, token):
    data = {
      "content": address,
      "name": domain,
      "type": type,
      "ttl": 120
    }
    res = requests.patch(f"https://api.cloudflare.com/client/v4/zones/{zone}/dns_records/{record}", data=json.dumps(data), headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }).json()
    if res["success"]:
        print("successfully updated ", domain)
    else:
        print("request failed for ", domain)

def add_rec(domain, zone, type, address, token):
    data = {
      "content": address,
      "name": domain,
      "type": type,
      "ttl": 120
    }
    res = requests.post(f"https://api.cloudflare.com/client/v4/zones/{zone}/dns_records", data=json.dumps(data), headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        }).json()
    if res["success"]:
        print("successfully updated ", domain)
        return res["result"]["id"]
    else:
        print("request failed for ", domain)
        return None

def getaddr4(root):
    return subprocess.run(['sh', path.join(root, 'addr4.sh')], stdout=subprocess.PIPE).stdout.decode('utf-8')

def getaddr6(root):
    return subprocess.run(['sh', path.join(root, 'addr6.sh')], stdout=subprocess.PIPE).stdout.decode('utf-8')

if __name__ == "__main__":
    root = path.dirname(path.abspath(__file__))
    print("working with ", root)
    rec_id = {}
    rec_id6 = {}
    with open(path.join(root, "config.json"), "r") as f:
        config = json.load(f)
    print(config)
    res = requests.get(f"https://api.cloudflare.com/client/v4/zones/{config['zoneid']}/dns_records", headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config["token"]}'
        }).json()
    if res["success"] != True:
        print("unable to access dns record!")
        exit()
    for r in res["result"]:
        if r["type"] == "A":
            rec_id[r["name"]] = r["id"]
        if r["type"] == "AAAA":
            rec_id6[r["name"]] = r["id"]
    addr4 = getaddr4(root)
    addr6 = getaddr6(root)
    for d in config["domains"]:
        if d in rec_id and rec_id[d] != None:
            mod_rec(d, config["zoneid"], rec_id[d], "A", addr4, config["token"])
        else:
            id = add_rec(d, config["zoneid"], "A", addr4, config["token"])
            if id != None:
                rec_id[d] = id
        if d in rec_id6 and rec_id6[d] != None:
            mod_rec(d, config["zoneid"], rec_id6[d], "AAAA", addr6, config["token"])
        else:
            id = add_rec(d, config["zoneid"], "AAAA", addr6, config["token"])
            if id != None:
                rec_id6[d] = id
