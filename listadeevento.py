# Exibe o título do programa na tela
print("=== LISTA DE CONVIDADOS ===")
# Cria uma lista vazia que vai armazenar os nomes dos convidados
convidados = []
# Solicita a primeira opção do usuário.
# int() converte o texto digitado em número inteiro.
# O menu é exibido com \n para quebrar linha entre cada opção.
opcao = (int(input("\n1 - Adicionar convidado: \n2 - Visualizar lista de convidados: \n3 - Ver quantidade de convidados \n4 - Verificar se um convidado está na lista \n5 - Remover convidado \n0 - Sair \nEscolha uma opção:")))
# Loop principal: continua enquanto o usuário NÃO escolher 0 (sair)
while (opcao != 0):  
    # Estrutura match/case 
    # Compara o valor de "opcao" com cada caso abaixo.    
    match (opcao):
         # Caso 1: ADICIONAR convidado
        case 1:
            # Lê o nome, .title() coloca a 1ª letra de cada palavra em maiúscula,
            # .strip() remove espaços extras no início e no fim.            
            nome = (input("Insira o nome do convidado: ")).title().strip()
            # Verifica se o nome ainda NÃO está na lista (evita duplicadas)
            if (nome not in convidados):
                convidados.append(nome) # Adiciona o nome ao final da lista
                print(f"{nome} incluso na lista!") # f-string: insere a variável na mensagem
            else:
                print("Convidado já cadastrado!") # Aviso de duplicada    
        # Caso 2: VISUALIZAR a lista        
        case 2:
            # Se a lista estiver vazia (tamanho 0), avisa o usuário
            if (len(convidados) == 0):
                print("Ainda não há nomes confirmados.")
            else:
                # Mostra a lista completa
                print(f"Convidados confirmados: {convidados}")    
        # Caso 3: VER QUANTIDADE de convidados
        case 3:
            # len() retorna o número de elementos da lista
            print(f"A lista possui {(len(convidados))} convidado(s) confirmado(s).")
        # Caso 4: VERIFICAR se um convidado está na lista
        case 4:
            # Lê o nome a consultar (com a mesma normalização usada no cadastro)
            consultaconv = (input("Qual convidado deseja verificar? ")).title().strip()
            # O operador "in" verifica se o nome existe dentro da lista
            if (consultaconv in convidados):
                print(f"O convidado {consultaconv} está na lista!")
            else:
                print(f"O convidado {consultaconv} não está na lista!")
        # Caso 5: REMOVER um convidado           
        case 5:
            # Lê o nome a ser removido
            nomerem = (input("Digite um nome de um convidado para remover: ")).title().strip()
            # Só remove se o nome realmente existir (evita erro do .remove())
            if nomerem in convidados:
                convidados.remove(nomerem) # Remove o primeiro item igual a "nomerem"
                print(f"{nomerem} removido com sucesso!")
            else:
                print(f"{nomerem} não encontrado na lista de convidados.")
        # Caso padrão (_): cobre qualquer opção que não seja 1, 2, 3, 4 ou 5        
        case _:
            print(f"Opção inválida. Tente novamente!")     
    # Após executar a ação, pede uma NOVA opção para continuar o loop.
    # É isso que faz o menu reaparecer a cada iteração.       
    opcao = (int(input("\n1 - Adicionar convidado: \n2 - Visualizar lista de convidados: \n3 - Ver quantidade de convidados \n4 - Verificar se um convidado está na lista \n5 - Remover convidado \n0 - Sair \nEscolha uma opção: ")))

# Quando o usuário digita 0, o while termina e cai aqui:
print(f"Encerrando a lista de convidados. Até logo!")    