import socket as s  # Importa il modulo socket e assegna l'alias 's'

# Crea un socket client UDP
udp_client_socket = s.socket(s.AF_INET, s.SOCK_DGRAM)

# Definisce l'indirizzo del server e la porta
server_address = ("192.168.1.21", 6980)

# Definisce la dimensione del buffer per l'invio e la ricezione dei dati
BUFFER_SIZE = 4092  # La dimensione del buffer è di 4092 byte

for i in range(10):
    # Invia un messaggio al server
    message = f"Ciao, server! Messagio numero {i+1}".encode("utf-8")
    # Invia il messaggio al server utilizzando il metodo sendto
    udp_client_socket.sendto(message, server_address)

# Metto la socket in ascolto e attendo la ricezione di dati
data, server_address = udp_client_socket.recvfrom(BUFFER_SIZE)

#Stampo un messaggio che indica che i dati sono stati ricevuti dal server
print(f"Messaggio ricevuto da server: {data.decode()} da {server_address}")