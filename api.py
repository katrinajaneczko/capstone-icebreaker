import json
import urllib.request as urllib
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

"""
Functions for querying the following REST API:

https://courses.ianapplebaum.com/public/docs/
"""

BEARER_KEY = "xSM5HL16IcmT9U81ODk1q6xqDf1I2IkgQ81TkQWk"

def query_api(path, headers={}):
    """
    Core HTTP code for the API, incl auth & content type
    takes:
        path: URL path to request
        headers: dict of headers (header name => header value)
    returns:
        tuple: (http status code, returned JSON data)
    """
    req = urllib.Request("https://courses.ianapplebaum.com{}".format(path))
    req.add_header('Accept', 'application/json')
    req.add_header('Content-Type', 'application/json; charset=UTF-8')
    req.add_header('Authorization', 'Bearer {}'.format(BEARER_KEY))
    for k,v in headers.items():
        req.add_header(k, v)
    resp = urllib.urlopen(req)
    return resp.status, json.loads(resp.read())

def get_user():
    """
    Returns the authenticated user.
    """
    return query_api('/api/user')

def get_syllabi():
    """
    Lists all the syllabi in the API
    """
    return query_api('/api/syllabus')

def get_syllabus(s_id):
    """
    Gets the list of events representing the syllabus.
    """
    return query_api("/api/syllabus/{}".format(s_id))

# Proof of concept: python3 api.py
if __name__ == '__main__':
    from pprint import pprint
    pprint(get_syllabi())
    pprint(get_syllabus(1))
