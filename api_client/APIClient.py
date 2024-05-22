import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
class APIClient:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = self._get_session()



    def _request(self, method, endpoint, payload=None):

        url = f'{self.base_url}/{endpoint}'
        headers = {'Content-Type': 'application/json'}

        if payload is not None:
            payload['candidateId'] = self.api_key

        try:
            response = self.session.request(method, url, json=payload,
                                            headers=headers)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            exit(1)

        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
            exit(1)

        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
            exit(1)

        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')
            exit(1)

    @staticmethod
    def _get_session():

        # I had to use a retry strategy because the server was returning
        # 429 status code (Too Many Requests) when I was making too many
        # requests in a short period of time.

        session = requests.Session()

        retry_strategy = Retry(total=20, backoff_factor=0.1,
                               status_forcelist=[429],
                               allowed_methods=['GET', 'POST', 'DELETE'])

        adapter = HTTPAdapter(max_retries=retry_strategy)

        session.mount('https://', adapter)

        return session

    def get(self, endpoint):
        return self._request('GET', endpoint)

    def post(self, endpoint, payload):
        return self._request('POST', endpoint, payload)

    def delete(self, endpoint, payload):
        return self._request('DELETE', endpoint, payload)
