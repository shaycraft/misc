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
    print '<style type="text/css">'
    print '.floated_img'
    print '{'
    print ' float: left;'
    print '}'
    print '</style>'
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

    #print type(twit_feed)

    #print get_recursively(twit_feed,'media_url')
    last_id = 1
    for item in twit_feed:
        for entry in item:
            #print entry
            if entry == 'entities':
                #print type(entry)
                for entities in item[entry]:
                    #print entities
                    if entities == 'media':
                        #print type(entities)
                        #print item[entry][entities]
                        twit_med = item[entry][entities][0]
                        media_url = twit_med['media_url']
                        #print twit_med
                        h = 150
                        w = 150
                        render_img(media_url)
                        #print twit_med['id']
                        last_id = twit_med['id']

    #for property,value in vars(twit_feed).iteritems():
    #    print property
    return last_id

try:
    form = cgi.FieldStorage()
    #cgi.MiniFieldStorage("max_id");

    # Get data from fields
    if 'max_id' in form:
    	last_id = form['max_id'].value
    else:
        last_id = None

    #print 'last_id = '
    #print last_id

    htmlheader()

    token = get_token()

    #print '<h2>Your access token is {0}/h2>'.format(token)

    last_id = get_media('MissJessicaAsh', token, last_id)

    print '<a href="pyserver.py?max_id={0}">Next</a>'.format(last_id)

    htmlfooter()
except:
    cgi.print_exception()
