import grpc
from concurrent import futures
import produto_pb2
import produto_pb2_grpc
# Implementação da Classe que atende as necessidades do Skeleton/Serviço
class ProdutoService(produto_pb2_grpc.ProdutoServiceServicer):
    def __init__(self):
        self.estoque = []
    # Implementação da Definição do Skeleton do Produto para Assar
    def Assar(self, request, context):
        self.estoque.append(request.nome)
        mensagem = f"Produto '{request.nome}' produzido com sucesso!"
        return produto_pb2.ProdutoResponse(mensagem=mensagem)
    # Implementação da Definição do Skeleton do Produto para Vender
    def Vender(self, request, context):
        if self.estoque:
            produto = self.estoque.pop(0)
            mensagem = f"{request.solicitante} comprou o produto '{produto}'."
        else:
            mensagem = "Estoque vazio. Nenhum produto para vender."
        return produto_pb2.ProdutoResponse(mensagem=mensagem)
# Execução do Servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Registro da Classe como Serviço relacionado ao gRPC de Produto
    produto_pb2_grpc.add_ProdutoServiceServicer_to_server(ProdutoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
