import requests
import openpyxl

# GoDaddy API credentials (replace with your keys)
API_KEY = "3mM44Ywf7gdwZD_WETT53NKMfUfmwREMXHy82"
API_SECRET = "XpDyQZhXoctMWwkxjPXXFf"

headers = {
    "Authorization": f"sso-key {API_KEY}:{API_SECRET}",
    "Accept": "application/json"
}

def check_domain(domain):
    url = f"https://api.godaddy.com/v1/domains/available?domain={domain}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("available"):
            return (domain, "Available", data.get("price")/1000000)  # price is in micros
        elif data.get("premium"):
            return (domain, "Premium", data.get("price")/1000000)
        else:
            return (domain, "Taken", "N/A")
    else:
        return (domain, "Error", "N/A")

# Read domains from text file
with open("domains.txt", "r") as file:
    domains = [line.strip() for line in file.readlines()]

# Create Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Domain Results"
sheet.append(["Domain", "Status", "Price"])

# Check each domain
for domain in domains:
    result = check_domain(domain)
    sheet.append(result)

# Save Excel file
workbook.save("results.xlsx")

print("✅ Domain check completed. Results saved in results.xlsx")
