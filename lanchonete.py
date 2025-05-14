from collections import deque
pedidos = deque([], 10)
encerrarLoop: bool = False


def menu(): 
  while (True): 
    print("""    ###### LANCHONETE ######
    # 1 – INCLUIR PEDIDO   #
    # 2 - ATENDER PEDIDO   #
    # 3 - LISTAR PEDIDOS   #
    # 4 – PESQUISAR PEDIDO #
    # 5 – ENCERRAR         #
    ########################""")

    opcao: int = int(input("Digite uma opção: "))

    if (opcao == 1 ): 
      incluirPedido()
    elif (opcao == 2):
      atenderPedido()
    elif (opcao == 3):
      listarPedidos()
    elif (opcao == 4):
      pesquisarPedido()
    elif (opcao == 5):
      if (encerrar() == True):
        print("Encerrando...")
        break
    else:
      print("Opção inválida.")



def incluirPedido():
  if (len(pedidos) == 10):
    print("""------------------------------------------
Fila Cheia – Não Pode Mais Incluir Pedidos
------------------------------------------
""")
    return

  pedido: int = int(input("Digite o número do pedido: "))

  pedidos.append(pedido)

def atenderPedido():
  if (listaVazia() == True):
    print("""---------------------------------
Lista Vazia – Não Existem Pedidos
---------------------------------""")
    return

  pedidos.popleft()

def listarPedidos():
  if (listaVazia() == True):
    print("""---------------------------------
Lista Vazia – Não Existem Pedidos
---------------------------------""")
    return
  
  print("Pedidos a serem atendidos: ", list(pedidos))

def pesquisarPedido():
  if (listaVazia() == True):
    print("""---------------------------------
Lista Vazia – Não Existem Pedidos
---------------------------------""")
    return
  pedido: int = int(input("Digite o número do pedido que deseja buscar: "))

  try:
    indexPedido: int = pedidos.index(pedido)
  except ValueError:
    print("""-------------------------
Pedido não foi encontrado
-------------------------""")
  else:
    print("O pedido: ", pedido, " está na ", indexPedido+1, "º posição.")

def encerrar():
  if (listaVazia() == False):
    print("""---------------------------------------
Ainda existem pedidos a serem atendidos
---------------------------------------""")
    return False

  return True

def listaVazia():
  if (len(pedidos) == 0):
    return True

  return False

menu()