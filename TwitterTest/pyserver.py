#!/usr/bin/python
__author__ = 'shaycraft'

import cgi
import urllib
import requests
import base64
import json
from cgi import parse_qs

def form_html():
    form = b'''
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Twitter api test</title>

    </head>
    <body>
        <h1>Twitter API Test</h1>
        <span id ="lblDebug" style="color: Red;"></span>
    <form action="/TwitterPhotoFeed/pyserver.py" method="get">
        <p>Enter twitter name:
            <input type="text" id="twit_name" name="twit_name" />
            <input type="submit" value="submit" />
        </p>
        </form>
    </body>
    </html>
    '''
    return form
    


def application(environ, start_response):
    status = '200 OK'

    output = str(get_token())

    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)

    d = parse_qs(environ['QUERY_STRING'])
    twit_name = d.get('twit_name', [])
    if not twit_name:
        return [form_html()] 

    else:
        #return [output + twit_name[0]]
        return handler(twit_name[0])


def htmlheader():
    # req.write('Content-type: text/html\n\n')
    header = [];
    #req.content_type = 'text/html'
    header.append('<!DOCTYPE HTML>')
    header.append('<html>')
    header.append('<head lang="en">')
    header.append('<meta charset="utf-8"/>')
    header.append('<style type="text/css">')
    header.append('.floated_img')
    header.append('{')
    header.append(' float: left;')
    header.append('}')
    header.append('</style>')
    header.append('</head>')
    header.append('<body>')
    return ''.join(header)


def htmlfooter():
    footer = []
    footer.append('</body>')
    footer.append('</html>')
    return ''.join(footer)


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
    req = []
    req.append('<div class="floated_img">')
    req.append('<a href="{0}:large">'.format(media_url))
    req.append('<img class="floated_img" src="{0}" alt="twit" height="150" width="150"></a>'.format(media_url))
    req.append('</div>')
    return ''.join(req)


def get_media(username, twit_token, last_id):
    response = []
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
                        response.append(render_img(media_url))
                        last_id = twit_med['id']

    return last_id, ''.join(response)


def handler(twit_name):
    response = []
    response.append(htmlheader())

    max_id = None

    #twit_name = getreqdict['twit_name']
    #max_id = getreqdict.get('max_id', None)
    max_id = None
    last_id = max_id

    token = get_token()

    for x in range(1, 4):
        #last_id = get_media(req, twit_name, token, last_id)
        last_id, medres = get_media(twit_name, token, last_id)
        response.append(medres)

    response.append('<a href="pyserver.py?max_id={0}&twit_name={1}">Next</a>'.format(last_id, twit_name))

    response.append(htmlfooter())
    #return apache.OK
    return ''.join(response)

