
import requests

def find_ip(ip=""):
    if ip.strip():
        url = f"http://ip-api.com/json/{ip.strip()}"
    else:
        url = "http://ip-api.com/json/"

    params = {
        "fields": "status,message,query,city,regionName,country,lat,lon,isp,org"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("status") != "success":
            print("Error:", data.get("message", "Invalid IP"))
            return

        print("\n--- IP Address Details ---")
        print("IP Address:", data.get("query"))
        print("City:", data.get("city"))
        print("Region:", data.get("regionName"))
        print("Country:", data.get("country"))
        print("Latitude:", data.get("lat"))
        print("Longitude:", data.get("lon"))
        print("ISP:", data.get("isp"))

    except requests.RequestException as e:
        print("Unable to connect:", e)


ip = input("Enter an IP address (or leave blank for your own): ")
find_ip(ip)