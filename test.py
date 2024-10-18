import requests

# Define your Vercel API token and project ID
VERCEL_API_TOKEN = 'XXyDfnXfaAXazNQb19QFbp8s'
PROJECT_ID = 'prj_VU9FJg8Ck2DykYsA3ivOqcLNar6C'

# Define the API endpoint to send the logs
API_ENDPOINT = 'https://example.com/logs'

# Function to get the latest deployment ID
def get_latest_deployment_id(project_id):
    url = f'https://api.vercel.com/v6/deployments?projectId={project_id}&limit=1'
    headers = {
        'Authorization': f'Bearer {VERCEL_API_TOKEN}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        deployments = response.json()

        if deployments and 'deployments' in deployments:
            latest_deployment = deployments['deployments'][0]  # Get the latest deployment
            return latest_deployment['uid']  # Return the deployment ID
        else:
            print("No deployments found.")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to get logs for the given deployment ID
def get_vercel_logs(deployment_id):
    url = f'https://api.vercel.com/v2/deployments/{deployment_id}/events'
    headers = {
        'Authorization': f'Bearer {VERCEL_API_TOKEN}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        logs = response.json()  # Parse the response JSON
        return logs

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while fetching logs: {http_err}")
    except Exception as err:
        print(f"Error occurred while fetching logs: {err}")
    return None

# Function to send logs to an external API endpoint
def send_logs_to_api(logs, api_endpoint):
    try:
        print(logs)
        return
        response = requests.post(api_endpoint, json=logs)
        response.raise_for_status()
        print(f"Logs sent successfully: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while sending logs: {http_err}")
    except Exception as err:
        print(f"Error occurred while sending logs: {err}")

# Main process: Fetch latest deployment, get logs, and send to API
def main():
    # Step 1: Get the latest deployment ID
    latest_deployment_id = get_latest_deployment_id(PROJECT_ID)

    if latest_deployment_id:
        # Step 2: Get logs for that deployment
        logs = get_vercel_logs(latest_deployment_id)
        
        if logs:
            # Step 3: Send logs to the API if logs are retrieved successfully
            send_logs_to_api(logs, API_ENDPOINT)

if __name__ == "__main__":
    main()
