class PolyanetsEndpoints:
    def __init__(self, client):
        self.client = client

    def add_polyanet(self, row, column):
        payload = {'row': row, 'column': column}
        return self.client.post('polyanets', payload)

    def delete_polyanet(self, row, column):
        payload = {'row': row, 'column': column}
        return self.client.delete('polyanets', payload)


