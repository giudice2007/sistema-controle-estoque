import json 
try:
    with open("produtos.json", "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

except FileNotFoundError:
    produtos = []
while True:
    print("     =============================    ") 
    print("          SISTEMA DE ESTOQUE          ")
    print("     ==============================   ") 

    print("1 - Cadastrar produtos") 
    print("2 - Listar produtos") 
    print("3 - Consultar produto") 
    print("4 - Atualizar estoque") 
    print("5 - excluir produto") 
    print("6 - Relatório") 
    print("7 - Registrar entrada") 
    print("8 - Registrar saída") 
    print("0 - Sair") 

    opcao = input("Escolha uma opção: ")
    if opcao == "0": 
        print("ENCERRANDO PROGRAMA...") 
        break 
    elif opcao == "1": 
          print("INICIANDO CADASTRO DE PRODUTOS...") 

          nome = input("Digite o nome do produto: ")

          duplicado = False

          for produto in produtos:
              if nome.lower() == produto["nome"].lower():
                  duplicado = True
                  print("Esse produto já está cadastrado!")
                  break

          if duplicado:
              continue 
          while True:
              try:
                  quantidade = int(input("Digite a quantidade: "))

                  if quantidade > 0:
                      break
                  else:
                      print("A quantidade precisa ser maior que zero!")

              except ValueError:
                  print("Digite apenas números inteiros!")
          produto = {
            "nome" : nome,
            "quantidade": quantidade
          } 
          produtos.append(produto) 
          print("Produto cadastrado:", nome) 
    elif opcao == "2":
        for produto in produtos:
               print("Produto:", produto["nome"])
               print("Quantidade:", produto["quantidade"])
               print("----------------------")

    elif opcao == "3": 
        consulta = input("Digite o produto que voce deseja consultar: ") 
        encontrado = False 
        for produto in produtos :
            if consulta.strip().lower() == produto["nome"].strip().lower():
                print("Produto encontrado!")
                print("Nome:", produto["nome"]) 
                print("Quantidade:", produto["quantidade"])
                encontrado = True 
        if encontrado == False: 
            print("Produto não encontrado!") 
    elif opcao == "4": 
        atualizar = input("Qual produto você deseja atualizar?")
        for produto in produtos: 
            print("verificando:", produto["nome"]) 
            if atualizar == produto["nome"]: 
                nova_quantidade = int(input("digite a nova quantidade: "))
                produto["quantidade"] = nova_quantidade 
                print("Estoque atualizado com sucesso!") 
    elif opcao == "5": 
        excluir = input("Qual produto deseja excluir? ") 
        encontrado = False 
        for produto in produtos: 
            if excluir == produto["nome"]: 
                produtos.remove(produto) 
                print("Produto excluído com sucesso!") 
                encontrado = True 
                break 
        if encontrado == False: 
            print("Produto não encontrado!") 
    elif opcao == "6":
        print("======== RELATÓRIO DE ESTOQUE ========")

        total_produtos = len(produtos)
        total_unidades = 0

        for produto in produtos:
            print("-----------------------------")
            print("Produto:", produto["nome"])
            print("Quantidade:", produto["quantidade"])

            total_unidades += produto["quantidade"]

        print("-----------------------------")
        print("Total de produtos:", total_produtos)
        print("Total de unidades:", total_unidades)
    elif opcao == "7":
        entrada = input("Qual produto recebeu mercadoria? ")
        encontrado = False

        for produto in produtos:
            if entrada == produto["nome"]:
                while True:
                    try:
                        quantidade_entrada = int(input("Quantas unidades chegaram? "))

                        if quantidade_entrada > 0:
                            break
                        else:
                            print("A quantidade precisa ser maior que zero!")

                    except ValueError:
                        print("Digite apenas números inteiros!")
                produto["quantidade"] += quantidade_entrada
                print("Entrada registrada com sucesso!")
                print("Novo estoque:", produto["quantidade"])
                encontrado = True
                break

        if encontrado == False:
            print("Produto não encontrado!")

    elif opcao == "8":
        saida = input("Qual produto foi vendido? ") 
        encontrado = False

        for produto in produtos:
            if saida == produto["nome"]:
                print("Produto encontrado!")
                print("Estoque disponível:", produto["quantidade"]) 
                while True:
                    try:
                        quantidade_saida = int(input("Quantas unidades foram vendidas? "))

                        if quantidade_saida > 0:
                            break
                        else:
                            print("A quantidade precisa ser maior que zero!")

                    except ValueError:
                        print("Digite apenas números inteiros!")

                if quantidade_saida <= produto["quantidade"]:
                    produto["quantidade"] -= quantidade_saida
                    print("Venda registrada com sucesso!")
                    print("Estoque restante:", produto["quantidade"])
                else:
                    print("Estoque insuficiente!")
                encontrado = True
                break

        if encontrado == False:
            print("Produto não encontrado!") 

    else:
        print("Opção inválida!")  
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False) 