import requests

# Your Vercel API token
API_TOKEN = 'iPBrekroAa0ocDQHKKpASzbB'

# The deployment ID you provided
deployment_id = 'dpl_3Vy3uYtUeP24CpGxRmSiWvCT34vo'

# Vercel API URL to fetch deployment logs (Updated to v2)
url = f'https://api.vercel.com/v1/deployments/{deployment_id}/logs'

# Set the headers including the authorization token
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
}

# Make the GET request to fetch the logs
response = requests.get(url, headers=headers)

# Print the exact response for debugging
print(f'Status Code: {response.status_code}')
print(f'Response Text: {response.text}')

# Check if the request was successful
if response.status_code == 200:
    logs = response.json()
    print(logs)  # This will print the logs in JSON format
else:
    print(f'Error: {response.status_code}, {response.text}')
