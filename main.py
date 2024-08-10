import traitement_image
import Photo
import Production_Coordonnée
import Socket
import SerialCom 

running = False #état de fonctionnement du scan
address=None
client=None
s=None
arduinoconnection = None
#Lancement du programme 
#positionnement du moteur au pas 0
arduinoconnection = SerialCom.Serialstart(arduinoconnection) #démarre la liaison série avec arduino
s=Socket.setup_server() #démarrage du socket serveur
message="d"
SerialCom.SerialEnvoi(message.encode(encoding='utf-8'),arduinoconnection)#envoie du message d(Down) désactivation du laser !.
client, address = Socket.start_connexion(s)
while True:
    
    
    socket_message =Socket.socket_earing(client) #écoute les messages socket
    
    print("socket_message: ",socket_message)    
            
    
    if socket_message == "stop":
        running = False
        print("Arrêt demandé.")
    if socket_message == "start":
        print("start")

    print("boucle principale")

    if socket_message == "start" and not running:
        running = True
        print("start reçu, lancement du scan")
        Socket.socket_sending("ok\n".encode(),client,s) #envoie le message encodé: ok en socket tcp
        
        for number_img in range(200):  # Modification ici pour 200 itérations
            #envoit une demande d'odre au pc

            #pendant qu'il a rien recu
                #ecoute sur la connection
            
            #test de message
            
            #Socket.socket_sending("order\n".encode(),client,s)
           
            socket_message = Socket.socket_earing(client) #écoute les messages socket
                
            print("test socket_message: ", socket_message)
            if socket_message:
                if socket_message == "stop":
                    running = False
                    print("Arrêt demandé.")
        
            

            
            if not running:
                print("arret not-running") # Sortie anticipée si arrêt demandé
                break 
                
            
            paslaser=Photo.Photos()
            #Prise de la photo avec laser éteint
            print("Photos pas laser ",number_img," | OK ")
            message = "u"
            SerialCom.SerialEnvoi(message.encode(encoding='utf-8'),arduinoconnection)#envoie du message u(Up)
            laser=Photo.Photos()#Photos avec laser 
            print("Photos laser ",number_img," | OK ")
            traitement_image.traitement_images(number_img,laser,paslaser)
            print("Traitement_images ",number_img," | OK ")
            message="+"
            SerialCom.SerialEnvoi(message.encode(encoding='utf-8'),arduinoconnection)#envoie du message d(Down) désactivation du laser !.
            message="d"
            SerialCom.SerialEnvoi(message.encode(encoding='utf-8'),arduinoconnection)#envoyer le message + rotation de 1.8°

            # Vérification périodique pour un message STOP
            #socket_message =Socket.socket_earing(client)
            if socket_message == "stop":
                running = False
                print("Arrêt demandé pendant le traitement.")
                break


        if running:
            Production_Coordonnée.Production_coordonees_3D()
            socket_message_transmit = "fini"
            Socket.socket_sending(socket_message_transmit,client,s)
            running = False
            print("Scan Done")
            Socket.restart_server(client,s)
    

Socket.socket_sending("arret\n".encode())
Socket.socket_close(client,s)
