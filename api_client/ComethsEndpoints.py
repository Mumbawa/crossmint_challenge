class ComethsEndpoints:
    def __init__(self, api_client):
        self.api_client = api_client

    def add_cometh(self, row, column, direction):
        payload = {'row': row, 'column': column, 'direction': direction}
        return self.api_client.post('comeths', payload)

    def delete_cometh(self, row, column):
        payload = {'row': row, 'column': column}
        return self.api_client.delete('comeths', payload)


