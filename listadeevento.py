print("=== LISTA DE CONVIDADOS ===")

convidados = []

opcao = (int(input("\n1 - Adicionar convidado: \n2 - Visualizar lista de convidados: \n3 - Ver quantidade de convidados \n4 - Verificar se um convidado está na lista \n5 - Remover convidado \n0 - Sair \nEscolha uma opção:")))

while (opcao != 0):  
    match (opcao):
        case 1:
            nome = (input("Insira o nome do convidado: ")).title().strip()
            if (nome not in convidados):
                convidados.append(nome)
                print(f"{nome} incluso na lista!")
            else:
                print("Convidado já cadastrado!")    
                
        case 2:
            if (len(convidados) == 0):
                print("Ainda não há nomes confirmados.")
            else:
                print(f"Convidados confirmados: {convidados}")    
        
        case 3:
            print(f"A lista possui {(len(convidados))} convidado(s) confirmado(s).")
        
        case 4:
            consultaconv = (input("Qual convidado deseja verificar? ")).title().strip()
            if (consultaconv in convidados):
                print(f"O convidado {consultaconv} está na lista!")
            else:
                print(f"O convidado {consultaconv} não está na lista!")
                    
        case 5:
            nomerem = (input("Digite um nome de um convidado para remover: ")).title().strip()
            if nomerem in convidados:
                convidados.remove(nomerem)
                print(f"{nomerem} removido com sucesso!")
            else:
                print(f"{nomerem} não encontrado na lista de convidados.")
                
        case _:
            print(f"Opção inválida. Tente novamente!")        
            
    opcao = (int(input("\n1 - Adicionar convidado: \n2 - Visualizar lista de convidados: \n3 - Ver quantidade de convidados \n4 - Verificar se um convidado está na lista \n5 - Remover convidado \n0 - Sair \nEscolha uma opção: ")))

print(f"Encerrando a lista de convidados. Até logo!")    