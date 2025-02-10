import requests
import base64
wordpress_user = "user"
wordpress_password = "UDpL atfo zpd7 TDsX Ao6G mAdz"
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {'Authorization': 'Basic ' + wordpress_token.decode('utf-8')}
api_url = 'http://localhost:8080/?rest_route=/wp/v2/posts'

def read_wordpress_posts():
 response = requests.get(api_url)
 response_json = response.json()
 print(response_json)

# Best practice including raise error
# def read_wordpress_posts():
#  """
#  Fetches WordPress posts from the specified REST API endpoint.
#  Handles potential connection errors gracefully.
#  """
#  api_url = 'http://localhost:8080/?rest_route=/wp/v2/posts'  # Corrected Port
#
#  try:
#   response = requests.get(api_url)
#
#   # Raise HTTPError for bad responses (4xx or 5xx)
#   response.raise_for_status()  # This is VERY important
#
#   response_json = response.json()
#   print(response_json)
#
#  except requests.exceptions.RequestException as e:
#   print(f"Error: Could not retrieve data from {api_url}")
#   print(f"Details: {e}")
#  except ValueError as ve:
#   print(f"Error: Could not decode JSON response from {api_url}")
#   print(f"Details: {ve}")
#
# if __name__ == "__main__":
#   read_wordpress_posts()

def create_wordpress_post():
 data = {
  'title': 'Example wordpress post',
  'status': 'publish',
  'slug': 'example-post',
  'content': 'This is the content of the post'
 }
 response = requests.post(api_url,headers=wordpress_header, json=data)
 print(response)

if __name__ == "__main__":
  create_wordpress_post()