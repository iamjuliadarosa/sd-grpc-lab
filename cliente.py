import grpc
import produto_pb2
import produto_pb2_grpc

def run():
    # Estabelecendo conexão com o servidor.
    canal = grpc.insecure_channel('localhost:50051')
    # Obtendo Stub do Produto
    stub = produto_pb2_grpc.ProdutoServiceStub(canal)

    nome = input("Digite seu nome: ")
    # Executando chamada do Stub relacionada a necessidade do Cliente
    resposta = stub.Vender(produto_pb2.VenderRequest(solicitante=nome))
    print("Servidor respondeu:", resposta.mensagem)

if __name__ == '__main__':
    run()
