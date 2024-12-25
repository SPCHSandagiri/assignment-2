import requests

# Replace with the raw URL of your hello.py file
url = "https://raw.githubusercontent.com/SPCHSandagiri/assignment-2/refs/heads/main/hello.py"

# Fetch the content of the file
response = requests.get(url)

if response.status_code == 200:
    print("File content fetched successfully!")
    print(response.text)
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")
