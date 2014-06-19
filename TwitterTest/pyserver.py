#!/usr/bin/python
__author__ = 'shaycraft'

import cgi
import urllib
import requests
import base64
import json


def htmlheader():
    print 'Content-type: text/html\n\n'
    print '<!DOCTYPE HTML>'
    print '<html>'
    print '<head lang="en">'
    print '<meta charset="utf-8"/>'
    print '</head>'
    print '<body>'


def htmlfooter():
    print '</body>'
    print '</html>'


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


def get_media(username, twit_token):
    svc_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}&count=200'.format(username)
    svc_headers = {'Authorization': 'Bearer {0}'.format(twit_token)}
    r = requests.get(svc_url, headers=svc_headers)
    twit_feed = json.loads(r.text)

    for item in twit_feed:
        print item

token = get_token()
get_media('MissJessicaAsh', token)

try:
    htmlheader()

    print '<h2>Your access token is {0}/h2>'.format(token)
    htmlfooter()
except:
    cgi.print_exception()