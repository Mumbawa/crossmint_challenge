class SoloonEndpoints:
    def __init__(self, api_client):
        self.api_client = api_client

    def add_soloon(self, row, column, color):
        payload = {'row': row, 'column': column, 'color': color}
        return self.api_client.post('soloons', payload)

    def delete_soloon(self, row, column):
        payload = {'row': row, 'column': column}
        return self.api_client.delete('soloons', payload)


