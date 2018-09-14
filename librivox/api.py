# librivox/api.py

import socket

from . import session

class API(object):

    def __init__(self, timeout=5):
        self.api_root = 'https://librivox.org/api/feed/'
        self.timeout = timeout
    
    def _create_request(self, resource, method='GET', params=None):
        uri = self.api_root + resource

        try:
            response = session.request(method, uri, timeout=self.timeout, params=params)
        except socket.timeout as e:
            print('The request timed out: {}'.format(e))

        assert response.status_code == 200, "Unexpected response: {}".format(response.reason)

        return response.json()

    def _clean_params(self, params):
        # TODO: Implement

        return params

    def get_audiobooks(self, params):
        resource = 'audiobooks/'
        params = self._clean_params(params)
        return self._create_request(resource, params=params)

    def get_audiotracks(self, params):
        resource = 'audiotracks/'
        params = self._clean_params(params)
        return self._create_request(resource, params=params)

    def get_authors(self, params):
        resource = 'authors/'
        params = self._clean_params(params)
        return self._create_request(resource, params=params)