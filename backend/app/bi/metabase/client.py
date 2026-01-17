from dotenv import load_dotenv
import requests
import os

load_dotenv()
''' Prove that we can talk to the Metabase running on docker with 'requests' module

import requests

response = requests.get('http://localhost:3000')
print(response.text)
'''
''' Notes
# Authentication to Metabase is going to be via API - create an API key and save it in the environment file.
# Make and authentication GET request
    # Hold a session.
    # attach auth headers/cookies
    # expose simple "Get" method
'''
def get_dashboard(dashboard_id, url = os.getenv("METABASE_URL"), api_key = os.getenv("METABASE_API_KEY")):
    ''' Information on given arguments
    Args:
        url (str): the URL of the Metabase instance (get from .env).
        api_key (str): API key that was produce in Admin settings of Metabase (saved in .env).
        dashboard_id(int): The ID of the dashboard to retrive. We do not want a default with the dashboard ID - put this first as an arguement. non-default parameters can't come after default parameters.
    '''
    # Define the header with an API key - dictionary
    headers = {
        "X-Metabase-Apikey": api_key,
        "Content-Type": "application/json"
    }
    # Construct the API endpoint URL for the specific dashboard from Metabase
    endpoint_url = print(f"{url}/api/dashboard/{dashboard_id}")
    # Use a 'try:' keyword
        # Make the GET request (requests.get) to the Metabase API - make a variable for 'response'
    try:
        response = requests.get(headers, endpoint_url)
        # Check if the request was successful - use 'status.code' method (status code 200) - print failed response if failed.
        if response.status_code == 200:
            print(f"You have successfully connected and retrieved {dashboard_id}")
            return response.json()
        else:
            print(f"We can not retrieve the dashboard: {dashboard_id}.")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    # except with an 'requests.exceptions.RequestExceptions as e' - print
    except requests.exceptions.RequestException as e:
        print(f"An error has occured during an API request: {e}")
        return None

if __name__ == "__main__":
    get_dashboard()