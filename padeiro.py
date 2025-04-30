import grpc
import produto_pb2
import produto_pb2_grpc

def run():
    canal = grpc.insecure_channel('localhost:50051')
    stub = produto_pb2_grpc.ProdutoServiceStub(canal)

    produto = input("Digite o nome do produto a ser adicionado ao estoque da padaria: ")
    resposta = stub.Assar(produto_pb2.ProdutoRequest(nome=produto))
    print("Servidor respondeu:", resposta.mensagem)

if __name__ == '__main__':
    run()