#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using requests package"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
