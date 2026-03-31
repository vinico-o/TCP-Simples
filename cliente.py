import socket as sk

#sk.socket cria um socket para o cliente
#AF_INET indica o IPv4 (Internet Protocol version 4)
#O parâmetro SOCK_STREAM indica que o socket será TCP
socketCliente = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

#estabelece uma conexão TCP cliente-servidor
#os parâmetros passados são: nome e porta do servidor, respectivamente
#depois desse comando é estabelecida uma apresentação de três vias
socketCliente.connect(("localhost", 6767))

while True:
    #mensagem recebe tudo que o usuário digitar até que seja dado Enter
    mensagem = input("Digite uma mensagem: ")

    #send() envia a mensagem do cliente pelo socket do cliente para a conexão TCP
    #encode() converte a string mensagem para bytes
    #o cliente espera para receber bytes do servidor
    socketCliente.send(mensagem.encode())

    if mensagem.upper() == "FIM":
        #fecha o socket, encerrando a conexão TCP
        socketCliente.close()
        break
    
    #quando a mensagem chega no servidor, atriuims ela em mensagemModificada
    #recv() é receive (receber) a mensagem
    #2048 é o número máximo de bytes que serão lidos (até a tecla Enter)
    mensagemModificada = socketCliente.recv(2048)
    print(f"Resposta do servidor: {mensagemModificada.decode()} \n")
     
