import requests
import base64
wordpress_user = "user"
wordpress_password = "UDpL atfo zpd7 TDsX Ao6G mAdz"
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {'Authorization': 'Basic ' + wordpress_token.decode('utf-8')}
api_url = 'http://localhost:8080/?rest_route=/wp/v2/posts'

def create_wordpress_post(html_content): # Pass html_content as parameter
    data = {
        'title': 'Uploaded HTML Content',  # Or any title you want
        'status': 'publish',  # Or 'draft', 'pending', etc.
        'slug': 'uploaded-html',  # Or a generated slug
        'content': html_content # Use passed in HTML content
    }
    response = requests.post(api_url, headers=wordpress_header, json=data)
    print(response)

# Example Usage
if __name__ == "__main__":
    html_file = 'registration_form_template.html'  #Replace the HTML path.
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    create_wordpress_post(html_content)
