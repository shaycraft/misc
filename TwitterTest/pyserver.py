#!/usr/bin/python
__author__ = 'shaycraft'

import cgi
import urllib
import requests
import base64
import json
from mod_python import apache


def htmlheader(req):
    #req.write('Content-type: text/html\n\n')
    req.content_type = 'text/html'
    req.write('<!DOCTYPE HTML>')
    req.write('<html>')
    req.write('<head lang="en">')
    req.write('<meta charset="utf-8"/>')
    req.write('<style type="text/css">')
    req.write('.floated_img')
    req.write('{')
    req.write(' float: left;')
    req.write('}')
    req.write('</style>')
    req.write('</head>')
    req.write('<body>')


def htmlfooter(req):
    req.write('</body>')
    req.write('</html>')


def get_token():
    api_key = urllib.quote('EG256Euv4bVpbcAx6F8QjiCQ3')
    secret_key = 'p19nAu1GmoyJX2EGeN5DRAk4yJ9jDeFZOiqpsL4gWCbp0JEykv'
    str_req = '{0}:{1}'.format(api_key, secret_key)
    base64_str = base64.b64encode(str_req)
    oauthurl = 'https://api.twitter.com/oauth2/token'

    payload = 'grant_type=client_credentials'
    oauthheaders = {'Authorization': 'Basic {0}'.format(base64_str),  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

    r = requests.post(oauthurl, data=payload, headers=oauthheaders)
    response = r.text
    return json.loads(response)['access_token']


def get_recursively(search_dict, field):
    """Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict:

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found


def render_img(media_url):
    print '<div class="floated_img">'
    print '<a href="{0}:large">'.format(media_url)
    print '<img class="floated_img" src="{0}" alt="twit" height="150" width="150"></a>'.format(media_url)
    print '</div>'

def get_media(username, twit_token, last_id):

    svc_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}&count=200&exclude_replies=true '.format(username)
    if last_id is not None:
        svc_url += '&max_id={0}'.format(last_id)
    svc_headers = {'Authorization': 'Bearer {0}'.format(twit_token)}
    r = requests.get(svc_url, headers=svc_headers)
    twit_feed = json.loads(r.text)

    last_id = 1
    for item in twit_feed:
        for entry in item:
            if entry == 'entities':
                for entities in item[entry]:
                    if entities == 'media':

                        twit_med = item[entry][entities][0]
                        media_url = twit_med['media_url']

                        h = 150
                        w = 150
                        render_img(media_url)
                        last_id = twit_med['id']

    return last_id


def handler(req):
    htmlheader(req)

    twit_name = ''
    max_id = None

    req.write(req.args)    
    getReqStr = req.args
    getReqArr = getReqStr.split('&')
    getReqDict = {}

    for item in getReqArr:
        tempArr = item.split('=')            
        getReqDict[tempArr[0]] = tempArr[1]

    twit_name = getReqDict['twit_name']
    max_id = getReqDict.get('maxid', None)

    if max_id is None:
        req.write('max id is none');

    req.write('<h1>twit_name={0}</h1>'.format(twit_name))



    #token = get_token()

    #for x in range(1, 4):
    #    last_id = get_media(twit_name, token, last_id)

    #print '<a href="pyserver.py?max_id={0}&twit_name={1}">Next</a>'.format(last_id, twit_name)

    htmlfooter(req)
    return apache.OK

