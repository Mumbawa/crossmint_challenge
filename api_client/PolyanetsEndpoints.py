class PolyanetsEndpoints:
    def __init__(self, api_client):
        self.api_client = api_client

    def add_polyanet(self, row, column):
        payload = {'row': row, 'column': column}
        return self.api_client.post('polyanets', payload)

    def delete_polyanet(self, row, column):
        payload = {'row': row, 'column': column}
        return self.api_client.delete('polyanets', payload)


