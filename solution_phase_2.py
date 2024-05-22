from api_client.APIClient import APIClient
from api_client.GoalEndpoints import GoalEndpoints
from api_client.PolyanetsEndpoints import PolyanetsEndpoints
from api_client.SoloonsEndpoints import SoloonEndpoints
from api_client.ComethsEndpoints import ComethsEndpoints


def make_crossmint_logo(goal, polyanets_endpoints, soloons_endpoints,
                        comeths_endpoints):

    for i in range(0, len(goal)):
        print(f'Processing row {i}')
        for j in range(0, len(goal[i])):

            if goal[i][j] == 'POLYANET':
                polyanets_endpoints.add_polyanet(i, j)

            elif goal[i][j] == 'BLUE_SOLOON' or goal[i][j] == 'RED_SOLOON' or \
                 goal[i][j] == 'PURPLE_SOLOON' or goal[i][j] == 'WHITE_SOLOON':

                color = goal[i][j].split('_')[0].lower()
                soloons_endpoints.add_soloon(i, j, color)

            elif goal[i][j] == 'UP_COMETH' or goal[i][j] == 'DOWN_COMETH' or \
                    goal[i][j] == 'LEFT_COMETH' or goal[i][j] == 'RIGHT_COMETH':

                direction = goal[i][j].split('_')[0].lower()
                comeths_endpoints.add_cometh(i, j, direction)

def main():

    # I placed the candidate ID here for the sake of simplicity. In a real-world
    # scenario, this would be stored in a secure location(e.g. environment
    # variables)
    CANDIDATE_ID = "bdc83e17-1963-4bca-a911-e71c970a03b7"

    BASE_URL = "https://challenge.crossmint.io/api"

    api_client = APIClient(BASE_URL, CANDIDATE_ID)

    goal_endpoints = GoalEndpoints(api_client, CANDIDATE_ID)

    goal = goal_endpoints.get_goal()['goal']

    polyanets_endpoints = PolyanetsEndpoints(api_client)
    soloons_endpoints = SoloonEndpoints(api_client)
    comeths_endpoints = ComethsEndpoints(api_client)

    make_crossmint_logo(goal, polyanets_endpoints, soloons_endpoints,
                        comeths_endpoints)

if __name__ == "__main__":
    main()
