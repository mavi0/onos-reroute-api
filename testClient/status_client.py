import base64
import json
import requests

# Send JSON


def post_json(url, reroute_JSON):
    try:
        r = requests.post(url, data=reroute_JSON)
        print(r.status_code)
        print(json.dumps(json.loads(r.content), indent=4, sort_keys=True))

    except IOError as e:
        print(e)
        return

# Load JSON from file


def main():
    with open("status.json", 'r') as f:
        reroute_JSON = json.load(f)
        print(reroute_JSON)
        post_json('http://127.0.0.1:5000/api/set_spp', json.dumps(reroute_JSON))


main()
