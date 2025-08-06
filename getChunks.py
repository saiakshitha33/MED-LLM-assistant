import requests, json, time
API = "https://api.fda.gov/drug/label.json"
payloads = []

for skip in range(0, 5000, 1000):          # 0, 1000, 2000, 3000, 4000
    params = {"limit": 1000, "skip": skip}
    # add your ?api_key=... here if you have one
    r = requests.get(API, params=params, timeout=30)
    r.raise_for_status()
    batch = r.json()["results"]
    payloads.extend(batch)
    print(f"Fetched {len(batch):4} docs (skip={skip})")
    time.sleep(0.25)                        # be polite to the API

print(f"Total docs pulled: {len(payloads)}")
with open("labels_5k.json", "w") as f:
    json.dump(payloads, f, indent=2)
