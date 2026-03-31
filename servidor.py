import socket as sk

#sk.socket cria um socket para o servidor
#AF_INET indica o IPv4 (Internet Protocol version 4)
#O parâmetro SOCK_STREAM indica que o socket será TCP
socketServidor = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

socketServidor.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1)

#associa o socket dos servidor a um endereço e uma porta respectivamente
#nesse caso, o endereço é a própria máquina, por conta de "localhost"
socketServidor.bind(("localhost", 6767))

#faz com que o servidor escute as requisições da conexão TCP do cliente
#o parâmetro indica o número máximo de conexões em fila
socketServidor.listen(1)
print("Servidor esperando conexão...")

while True:
    #aceita a conexão de um cliente e cria um socket específico para ele
    #accept() então, retorna um novo socket e o endereço do cliente
    #uma conexão TCP é criada entre socketCliente e socketConexao
    socketConexao, endereco = socketServidor.accept()
    print("Conectado por:", endereco)
    
    while True:
        mensagem = socketConexao.recv(2048).decode()
        
        if mensagem.upper() == "FIM":
            print("Servidor encerrado!\n")
            #apenas o socketConexao é fechado, 
            #então outro cliente pode enviar uma mensagem ao servidor
            socketConexao.close()
            break
        else:
            mensagemMaiuscula = mensagem.upper()
            socketConexao.send(mensagemMaiuscula.encode())