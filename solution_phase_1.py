from api_client.APIClient import APIClient
from api_client.PolyanetsEndpoints import PolyanetsEndpoints

def create_x_shape(num_rows, num_columns, polyanets_endpoints, row_offset):
    center_cell_row = num_rows // 2
    center_cell_col = num_columns // 2

    # Filling left side of the "X"
    for i in range(row_offset, 5, 1):
        polyanets_endpoints.add_polyanet(i, i)
        polyanets_endpoints.add_polyanet(num_rows - i - 1, i)

    # Filling intersection (middle point) of the "X"
    polyanets_endpoints.add_polyanet(center_cell_row, center_cell_col)

    # Filling right side of the "X"
    for i in range(6, num_rows - row_offset, 1):
        polyanets_endpoints.add_polyanet(i, i)
        polyanets_endpoints.add_polyanet(num_rows - i - 1, i)

def main():

    # Placing a candidate ID here for the sake of simplicity. In a real-world
    # scenario, this would be stored in a secure location(e.g. environment
    # variables)
    CANDIDATE_ID = "bdc83e17-1963-4bca-a911-e71c970a03b7"

    BASE_URL = "https://challenge.crossmint.io/api"

    api_client = APIClient(BASE_URL, CANDIDATE_ID)

    NUM_ROWS = 11
    NUM_COLUMNS = 11
    ROW_OFFSET = 2

    polyanets_endpoints = PolyanetsEndpoints(api_client)

    create_x_shape(NUM_ROWS, NUM_COLUMNS, polyanets_endpoints, ROW_OFFSET)

if __name__ == "__main__":
    main()
