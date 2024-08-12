import socket
import json

def send_data_to_server(data):
    server_address = ('[::1]', 5000)  # Endereço IPv6 do servidor (localhost)

    # Criação do socket
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect(server_address)

    try:
        # Envio de dados para o servidor
        sock.sendall(data.encode('utf-8'))

        # Recebendo a resposta
        response = sock.recv(4096).decode('utf-8')
        print("Resposta do servidor:", response)

    finally:
        sock.close()

def main():
    data = '''
    [
        {"last_turn": 272, "tstamp_auth_start": 1713369153.8624742, "servers_authenticated": [1, 2, 3, 4], "tstamp_auth_completion": 1713369173.8847864, "getcannons_received": 8, "cannons": [[3, 1], [1, 1], [8, 3], [3, 3], [7, 2], [2, 2], [3, 2], [6, 3]], "getturn_received": 1089, "ship_moves": 4438, "shot_received": 1546, "valid_shots": 1546, "sunk_ships": 716, "escaped_ships": 312, "remaining_life_on_escaped_ships": 491, "tstamp_completion": 1713369232.3878376, "auth": "ifs4:1:2c3bb3f0e946a1afde7d9d0c8c818762a6189e842abd8aaaf85c9faac5b784d2+ifs4:2:cf87a60a90159078acecca4415c0331939ebb28ac5528322ac03d7c26b140b98+e51d06a4174b5385c8daff714827b4b4cb4f93ff1b83af86defee3878c2ae90f", "id": 1},
        {"last_turn": 272, "tstamp_auth_start": 1713369153.8624742, "servers_authenticated": [1, 2, 3, 4], "tstamp_auth_completion": 1713369173.8847864, "getcannons_received": 8, "cannons": [[3, 1], [1, 1], [8, 3], [3, 3], [7, 2], [2, 2], [3, 2], [6, 3]], "getturn_received": 1090, "ship_moves": 4438, "shot_received": 1546, "valid_shots": 1546, "sunk_ships": 716, "escaped_ships": 312, "remaining_life_on_escaped_ships": 491, "tstamp_completion": 1713369232.394351, "auth": "ifs4:1:2c3bb3f0e946a1afde7d9d0c8c818762a6189e842abd8aaaf85c9faac5b784d2+ifs4:2:cf87a60a90159078acecca4415c0331939ebb28ac5528322ac03d7c26b140b98+e51d06a4174b5385c8daff714827b4b4cb4f93ff1b83af86defee3878c2ae90f", "id": 2}
    ]
    '''
    
    send_data_to_server(data)

if __name__ == "__main__":
    main()
