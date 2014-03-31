import urllib
import requests


class Jawbone(object):
    """
    The Jawbone  API python wrapper.
    """

    def __init__(self, client_id, client_secret, redirect_uri, scope = ''):

        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope or 'basic_read'
        self.base_url = "https://jawbone.com/"


    def auth(self, scope=None): 
        '''
        Initial authentication for Jawbone
        '''

        params = { 
            'scope'         : scope or self.scope,
            'client_id'     : self.client_id,
            'redirect_uri'  : self.redirect_uri,
            'response_type' : 'code'  
        }

        context = {
            'base_url': self.base_url,
            'params'  : urllib.urlencode(params)
        }

        # A hard redirect to the authorize page. 
        # User would see either the login to jawbone page, 
        # or authorize page if already logged in.
        return '{base_url}auth/oauth2/auth/?{params}'.format(**context)


    def access_token(self, code, grant_type='authorization_code'):
        '''
        Get the access code for a user with a auth code.
        '''

        params = {
            'code'          : code,
            'client_id'     : self.client_id,
            'client_secret' : self.client_secret,
            'grant_type'    : grant_type
        }

        context = {
            'base_url': self.base_url,
            'params'  : urllib.urlencode(params)
        }
 
        token_url = '{base_url}auth/oauth2/token/?{params}'.format(**context)

        res = requests.get(token_url)
        return res.json()


    def api_call(self, access_token, endpoint, **kwargs):
        '''
        Documentation URL: https://jawbone.com/up/developer/endpoints
        Example 
        endpoint: nudge/api/v.1.0/users/@me/sleep
        '''

        context = {
            'base_url': self.base_url,
            'endpoint': endpoint
        }

        api_call = '{base_url}{endpoint}'.format(**context)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'Host'  : 'https://jawbone.com',
            'Authorization': 'Bearer {0}'.format(access_token)
        }

        res = requests.get(api_call, headers=headers)

        if res.status_code == 200:
            return res.json()

        return {
            'error': res.reason, 
            'status_code': res.status_code  
        }


    def refresh_token_call(self, refresh_code):
        '''
        Get the new access code for a refresh token

        Parse the response, and update your database entries
        with the new auth credentials.
        '''

	return self.access_token(self, refresh_code, 'refresh_token')

