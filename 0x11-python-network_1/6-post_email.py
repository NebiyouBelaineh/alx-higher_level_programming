#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response using requests package."""
if __name__ == "__main__":
    import requests
    import sys
    url, email = sys.argv[1], sys.argv[2]
    data = {}
    data['email'] = email
    r = requests.post(url, data=data)
    print(r.text)
