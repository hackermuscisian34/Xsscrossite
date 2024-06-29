import requests
from bs4 import BeautifulSoup

def detect_xss(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')
            forms = soup.find_all('form')
            
            print(f"Scanning {url} for XSS vulnerabilities...\n")
            
            if scripts:
                print(f"Found {len(scripts)} <script> tags:")
                for script in scripts:
                    print(script)
            else:
                print("No <script> tags found.")

            print("\n")
            
            if forms:
                print(f"Found {len(forms)} <form> tags:")
                for form in forms:
                    action = form.get('action')
                    method = form.get('method', 'GET').upper()
                    print(f"Form action: {action}, method: {method}")
                    for input_tag in form.find_all('input'):
                        input_name = input_tag.get('name')
                        input_type = input_tag.get('type', 'text')
                        print(f"Input name: {input_name}, type: {input_type}")
            else:
                print("No <form> tags found.")
                
        else:
            print(f"Failed to retrieve {url} (status code: {response.status_code})")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://asia.google.com/search?btnI&q=http://www.indusface.com/blog"  # Replace with the URL you want to scan
detect_xss(url)