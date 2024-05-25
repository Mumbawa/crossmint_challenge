
class GoalEndpoints:
    def __init__(self, api_client):
        self.api_client = api_client
        self.api_key = api_client.api_key

    def get_goal(self):
        return self.api_client.get(f'map/{self.api_key}/goal')
