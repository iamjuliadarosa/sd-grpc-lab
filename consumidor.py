import grpc
import produto_pb2
import produto_pb2_grpc

def run():
    canal = grpc.insecure_channel('localhost:50051')
    stub = produto_pb2_grpc.ProdutoServiceStub(canal)

    nome = input("Digite seu nome: ")
    resposta = stub.Consumir(produto_pb2.ConsumirRequest(solicitante=nome))
    print("Servidor respondeu:", resposta.mensagem)

if __name__ == '__main__':
    run()
