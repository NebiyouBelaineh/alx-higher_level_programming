#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    data = {}
    if (len(sys.argv) < 2):
        data['q'] = ""
    else:
        data['q'] = sys.argv[1]
    r = requests.post(url, data=data)
    try:
        response = r.json()
        if (len(response) == 0):
            print("No result")
        else:
            print("[{}] {}".format(response['id'], response['name']))
    except Exception as e:
        print("Not a valid JSON")
