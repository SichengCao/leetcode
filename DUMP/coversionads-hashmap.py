clicks = [
    {"user_id": "A", "timestamp": 10, "event_id": "c1"},
    {"user_id": "A", "timestamp": 20, "event_id": "c2"},
    {"user_id": "A", "timestamp": 30, "event_id": "c3"},
    {"user_id": "B", "timestamp": 15, "event_id": "c4"}
]

conversions = [
    {"user_id": "A", "timestamp": 25, "event_id": "v1"},
    {"user_id": "A", "timestamp": 50, "event_id": "v2"},
    {"user_id": "B", "timestamp": 18, "event_id": "v3"},
    {"user_id": "B", "timestamp": 40, "event_id": "v4"}
]

k = 10

from collections import defaultdict

def last_click(clicks, conversions, k):
    user_clicks = defaultdict(list)

    for c in clicks:
        user_clicks[c["user_id"]].append((c["timestamp"], c["event_id"]))

    for u in user_clicks:
        user_clicks[u].sort()

    print(user_clicks)
    res = []

    for conv in conversions:

        user = conv["user_id"]
        t = conv["timestamp"]

        click_id = None
        click_ts = None

        if user in user_clicks:
            arr = user_clicks[user]
            print(arr)

            for i in range(len(arr) - 1, -1, -1):
                ts, eid = arr[i]
                print("ts:", ts)
                print("eid", eid)


                if ts >= t:
                    continue

                if t - ts <= k:
                    click_id = eid
                    click_ts = ts
                    break
                else:
                    break

        res.append({
            "conversion_id": conv["event_id"],
            "conversion_ts": t,
            "user_id": user,
            "click_id": click_id,
            "click_ts": click_ts
        })

    return res

output = last_click(clicks,conversions,k)
print(output)