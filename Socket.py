
import socket
import select



def setup_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 10000))
    s.listen(5)
    print("setup server réussi")
    return s

def start_connexion(s):
    print("start_connexion")
    #s = setup_server(s)    
    client, address = s.accept()
    print("adresse de connexion:")
    print ("{} connected".format( address ))
    return client, address

def socket_earing(client):
    
    ready = select.select([client], [], [], 0.1)
    if ready[0]:
        response = client.recv(255).decode().strip()
        if response:
            print(response)
            return response
    #return None

def socket_sending(message,client,s):
    client.send(message)
    print("message envoye")
    #restart_server(client,s)

def socket_close(client,s):         
    print("Close")
    client.close()
    s.close()

def restart_server(client,s):
     
    socket_close(client,s)
    s = setup_server()
    client, address = s.accept()


