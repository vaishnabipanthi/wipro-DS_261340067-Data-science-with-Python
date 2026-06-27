import re

def extract_emails():
    emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

    # Capturing groups: (user_id) @ (domain_name) . (suffix)
    pattern = re.compile(r'([a-zA-Z0-9_]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)')
    
    matches = pattern.findall(emails)
    for match in matches:
        user_id, domain, suffix = match
        print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")

if __name__ == "__main__":
    extract_emails()