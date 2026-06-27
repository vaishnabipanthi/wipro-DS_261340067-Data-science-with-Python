import re
import requests

def extract_html():
    try:
        r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
        html_text = r.text
        
        # Regex to extract text between > and < tags
        portions = re.findall(r'>([^<]+)<', html_text)
        
        # Clean up whitespace and newlines, filter out empty strings
        desired_output = [p.strip() for p in portions if p.strip()]
        
        print(f"desired_output = {desired_output}")
    except Exception as e:
        print(f"Error fetching HTML: {e}")

if __name__ == "__main__":
    extract_html()