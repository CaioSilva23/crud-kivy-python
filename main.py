from repositorios import cliente_repositorio
from entidades import cliente

cliente = cliente.Cliente("Silva", 44)

cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente)


cliente_repositorio.ClienteRepositorio.listar_cliente()

# cliente_repositorio.ClienteRepositorio.editar_cliente(1, cliente)
# cliente_repositorio.ClienteRepositorio.remover_cliente(8)






