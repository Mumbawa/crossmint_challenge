import requests

class APIClient:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def _request(self, method, endpoint, payload=None):

        url = f'{self.base_url}/{endpoint}'
        headers = {'Content-Type': 'application/json'}
        payload['candidateId'] = self.api_key

        try:
            response = requests.request(method, url, json=payload,
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

    def post(self, endpoint, payload):
        return self._request('POST', endpoint, payload)

    def delete(self, endpoint, payload):
        return self._request('DELETE', endpoint, payload)
