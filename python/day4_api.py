import requests

url = "https://api.github.com"
r = requests.get(url, timeout=10)

print("Status:", r.status_code)

data = r.json()
print("current_user_url:", data.get("current_user_url"))
print("rate_limit_url:", data.get("rate_limit_url"))

