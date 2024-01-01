# Declarar as variáveis
contador=0
soma_idade=0
IMC=0
soma_IMC=0
pequeno_almoco=0
almoco=0
jantar=0
sim_carne=0
sim_vegetais=0
sim_frutas=0
sim_doces=0
nao_carne=0
nao_frutas=0
nao_vegetais=0
nao_doces=0

# Declarar as funções
def cadastrar():
    global contador, soma_idade, soma_IMC, pequeno_almoco, almoco, jantar
    global sim_carne, sim_vegetais, sim_frutas, sim_doces, nao_carne, nao_frutas, nao_vegetais, nao_doces  
    contador+=1
    idade=int(input('1. Qual a idade?'))
    soma_idade+=idade
    massa=float(input('2. Qual o peso?'))
    altura=float(input('3. Qual a altura?'))
    IMC=massa/(altura*altura)
    soma_IMC+=IMC
    print('4. Que refeição considera ser a sua principal refeição do dia?')
    refeicao=int(input('  (1)Pequeno-almoço\n  (2)Almoço\n  (3)Jantar\n  Resposta:'))
    while True:
        if refeicao==1 or refeicao==2 or refeicao==3:
            if refeicao==1:
                pequeno_almoco+=1
            if refeicao==2:
                almoco+=1
            if refeicao==3:
                jantar+=1
            break
        print('Resposta invalida')
        refeicao=int(input('  (1)Pequeno-almoço\n  (2)Almoço\n  (3)Jantar\n  Resposta:'))
    print('5. Por favor, responda o seguinte de acordo com os seus hábitos alimentares:')
    carne=0
    while True:
        carne=int(input('  Como carnes?\n  Sim(1) ou Não(2)'))
        if carne==1:
            sim_carne+=1
            break 
        if carne==2:
            nao_carne+=1
            break
        else:
            print('Resposta invalida')        

    vegetais=0
    while True:
        vegetais=int(input('  Como vegetais?\n  Sim(1) ou Não(2)'))
        if vegetais==1:
            sim_vegetais+=1
            break 
        if vegetais==2:
            nao_vegetais+=1
            break
        else:
            print('Resposta invalida')        

    frutas=0
    while True:
        frutas=int(input('  Como frutas?\n  Sim(1) ou Não(2)'))
        if frutas==1:
            sim_frutas+=1
            break 
        if frutas==2:
            nao_frutas+=1
            break
        else:
            print('Resposta invalida')        

    doces=0
    while True:
        doces=int(input('  Como doces?\n  Sim(1) ou Não(2)'))
        if doces==1:
            sim_doces+=1
            break 
        if doces==2:
            nao_doces+=1
            break
        else:
            print('Resposta invalida')
    return('Fim cadastro')

def porcentagem(porcao,quantidade_total):
    porcentagem=round(porcao/quantidade_total*100,2)
    return(porcentagem)

def resultados():
    if contador==0:
        print('Não tem participantes')
    if contador!=0:
        print('Quantidade total de participantes:',contador)
        print('Idade média dos participantes',round(soma_idade/contador,2))
        print('IMC médio:',round(soma_IMC/contador,2))
        print('Porcentagem de participantes por refeição:')
        print('Pequeno-almoço:',porcentagem(pequeno_almoco,contador),'%')
        print('Almoço:',porcentagem(almoco,contador),'%')
        print('Jantar:',porcentagem(jantar,contador),'%')
        print('Quantidade de participantes por hábito alimentar')
        print('Come carne:',sim_carne,'\nNão come carne:',nao_carne)
        print('Come vegetais:',sim_vegetais,'\nNão come vegetais:',nao_vegetais)
        print('Come frutas:',sim_frutas,'\nNão come frutas:',nao_frutas)
        print('Come doces:',sim_doces,'\nNão come doces:',nao_doces)
    return('Fim resultados')

# Pesquisa    

print('Pesquisa sobre hábitos alimentares\n\nMENU\n[1] Cadastrar a pesquisa\n[2] Gerar resultados\n[3] Sair')
opcao=0
while True:
    opcao=int(input('Digite sua opção:'))
    if opcao==1:
        print(cadastrar())
        print('MENU\n[1] Cadastrar a pesquisa\n[2] Gerar resultados\n[3] Sair')
    elif opcao==2:
        print(resultados())
        print('MENU\n[1] Cadastrar a pesquisa\n[2] Gerar resultados\n[3] Sair')
    elif opcao==3:
        print('Obrigada pela participação!\nAutor: Amanda Lima Bezerra')
        break 
    else:
        print('Opção inválida')
        
