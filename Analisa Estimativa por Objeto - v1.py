import statistics
import locale
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
lista=[]
listaemordem=[]
medialista=0
medialistaformatada=0
mediana=0
medianaformatada=0
x=1
coefvar=0
locale.setlocale(locale.LC_ALL,'pt_BR')
def entrada(lista):
    proposta=input()
    proposta=proposta.replace('.', '').replace(',', '.')
    proposta=float(proposta)
    if proposta<=0:
        print('O valor tem que ser positivo.')
        print ('\n Digite o valor  e depois tecle ENTER (se houver centavos separar com vírgula - exemplos: 1.000.000,25 / 5200,50 / 5000 / 10.000): \n')
        entrada(lista)
    else:
        lista.append(proposta)
        print (lista)
        return lista
def limpalista (lista,listaemordem):
    lista.clear()
    listaemordem.clear()
    return lista,listaemordem
def menu (lista,listaemordem):
    if len(lista)<3:
        print('\n Atenção: O programa funciona de forma satisfatória a partir de 3 valores')
    if len(lista)<1:
        print('\n versão 1.0 \n \n (1) Inserir valor \n (2) Não há mais valores para inserir \n \n Digite o número correspondente à opção e depois tecle ENTER \n')
        op=input()
        op=op.replace('.', '').replace(',', '')
        op=float(op)
        while (op!=1 and op!=2):
            print('Opção inválida')
            op=input('\n (1) Inserir valor \n (2) Não há mais valores para inserir \n \n Digite o número correspondente à opção e depois tecle ENTER \n')
            op=op.replace('.', '').replace(',', '')
            op=float(op)
    if len(lista)>=1:
        print ('\n (1) Inserir valor \n (2) Não há mais valores para inserir \n (3) Exibir valor(es) na lista \n (4) Limpar valor(es) \n \n Digite o número correspondente à opção e depois tecle ENTER \n')
        op=input()
        op=op.replace('.', '').replace(',', '')
        op=float(op)
        while (op!=1 and op!=2 and op!=3 and op!=4):
            print('Opção inválida')
            op=input('\n (1) Inserir valor \n (2) Não há mais valores para inserir \n (3) Exibir valor(es) inserido(s) \n (4) Limpar valor(es) \n \n Digite o número correspondente à opção e depois tecle ENTER \n')
            op=op.replace('.', '').replace(',', '')
            op=float(op)
    return op
def desvpad (x):
    desvio=statistics.pstdev(x)
    return desvio
def quantidadedeentradas(x):
    contador = len(x)
    return contador
def coefvarmaiorque25(lista,listaemordem,coefvar,medialista,dpad):
    while coefvar>0.25:
        listacommedia=[medialista]*len(listaemordem)
        listadedesvpad=[dpad]*len(listaemordem)
        lista=listaemordem
        contador=quantidadedeentradas(listaemordem)
        listavariacaoporproposta = ([(x-y)/z for x,y,z in zip (listaemordem, listacommedia, listadedesvpad)])
        listavariacaoporpropostavaloresabsolutos=([abs(valor) for valor in listavariacaoporproposta])
        print('O resultado da divisão das diferenças entre os valores e a média dos valores, pelo desvio padrão, resulta, para cada valor, na ordem crescente, em:',', '.join(map(str, listavariacaoporproposta)),'de forma que os módulos obtidos são:',', '.join(map(str, listavariacaoporpropostavaloresabsolutos)),'.')
        if listavariacaoporpropostavaloresabsolutos[contador-1]==max(listavariacaoporpropostavaloresabsolutos) and len(listaemordem)>3:
            valoraserdescartado=listaemordem[contador-1]
            valoraserdescartadoformatado=locale.currency(valoraserdescartado,grouping=True)
            print(f'Tendo em vista que houve um coeficiente de variação geral maior que 0.25, o valor mais discrepante, que é de {valoraserdescartadoformatado}, será descartado.')
            del listaemordem[contador-1]
            contador=quantidadedeentradas(listaemordem)
            listaemordem=sorted(listaemordem)
            lista=listaemordem
            dpad=desvpad(listaemordem)
            desvioformatado=locale.currency(dpad,grouping=True)
            valoresformatados=[locale.currency(valor, grouping=True) for valor in listaemordem]
            contador = quantidadedeentradas(listaemordem)
            print (f'Os valores remanescentes, em número de {contador:.0f}, são, em ordem crescente: {", ".join(valoresformatados)}.')
            print (f'O desvio padrão resulta em {desvioformatado}.')
            medialista=sum(listaemordem)/len(listaemordem)
            medialistaformatada=locale.currency(medialista,grouping=True)
            mediana=statistics.median(lista)
            medianaformatada=locale.currency(mediana,grouping=True)
            coefvar=dpad/medialista
            if coefvar==0.25:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.') 
            elif coefvar>0.25 and coefvar<0.26:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.4f}.')
            else:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.')
        elif listavariacaoporpropostavaloresabsolutos[0]==max(listavariacaoporpropostavaloresabsolutos) and len(listaemordem)>3:
            valoraserdescartado=listaemordem[0]
            valoraserdescartadoformatado=locale.currency(valoraserdescartado,grouping=True)
            print (f'Tendo em vista que houve um coeficiente de variação geral maior que 0.25, o valor mais discrepante, que é de {valoraserdescartadoformatado}, será descartado.')
            del listaemordem[0]
            lista=listaemordem
            contador=quantidadedeentradas(listaemordem)
            listaemordem=sorted(listaemordem)
            dpad=desvpad(listaemordem)
            desvioformatado=locale.currency(dpad,grouping=True)
            valoresformatados=[locale.currency(valor, grouping=True) for valor in listaemordem]
            contador=quantidadedeentradas(listaemordem)
            print (f'Os valores remanescentes, em número de {contador:.0f}, são, em ordem crescente: {", ".join(valoresformatados)}.')
            print (f'O desvio padrão resulta em {desvioformatado}.')
            medialista=sum(listaemordem)/len(listaemordem)
            medialistaformatada=locale.currency(medialista,grouping=True)
            mediana=statistics.median(lista)
            medianaformatada = locale.currency(mediana,grouping=True)
            coefvar=dpad/medialista
            if coefvar==0.25:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.') 
            elif coefvar>0.25 and coefvar<0.26:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.4f}.')
            else:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.')
        else:
            print('Apesar do coeficiente de variação geral manter-se acima de 0.25, alcançou-se o mínimo de 3 valores válidos, de forma que não é recomendado desconsiderar qualquer valor ora elencado.')
            mediana=statistics.median(lista)
            medialistaformatada=locale.currency(medialista,grouping=True)
            mediana=statistics.median(lista)
            medianaformatada=locale.currency(mediana,grouping=True)
            valores_iteracao=listaemordem
            indices=list(range(1, len(valores_iteracao) + 1))
            plt.plot(indices, valores_iteracao, marker='o', linestyle='-')
            plt.xlabel('Valores (em ordem crescente)')
            plt.ylabel('Valor em R$')
            plt.title('Gráfico dos valores válidos remanescentes')
            plt.subplots_adjust(left=0.14)
            indicesinteirosx = list(range(1, len(valores_iteracao) + 1))
            plt.xticks(indicesinteirosx)
            plt.axhline(y=medialista, color='r', linestyle='--', label=f'Média: {medialistaformatada}')
            plt.axhline(y=mediana, color='g', linestyle='dotted', label=f'Mediana: {medianaformatada}')
            linhadelegenda1=Line2D([0],[0],color='red',linestyle='--',label=f'Média: {medialistaformatada}')
            linhadelegenda2= Line2D([0],[0],color='green',linestyle='dotted',label=f'Mediana: {medianaformatada}')
            linhadelegenda3=Line2D([0],[0],linestyle='-',marker='o',label=f'{len(lista)} valores utilizados')
            plt.legend(handles=[linhadelegenda1,linhadelegenda2,linhadelegenda3], title='Legenda')
            plt.show()
            main(lista,listaemordem)
    if coefvar<0.25:
        print('O índice encontra-se dentro dos parâmetros desejados e não é recomendado desconsiderar qualquer valor ora elencado.')
        medialistaformatada=locale.currency(medialista,grouping=True)
        mediana=statistics.median(lista)
        medianaformatada=locale.currency(mediana,grouping=True)
        valores_iteracao=listaemordem
        indices=list(range(1, len(valores_iteracao) + 1))
        plt.plot(indices, valores_iteracao, marker='o', linestyle='-')
        plt.xlabel('Valores (em ordem crescente)')
        plt.ylabel('Valor em R$')
        plt.title('Gráfico dos valores válidos remanescentes')
        plt.subplots_adjust(left=0.14)
        indicesinteirosx = list(range(1, len(valores_iteracao) + 1))
        plt.xticks(indicesinteirosx)
        plt.axhline(y=medialista, color='r', linestyle='--', label=f'Média: {medialistaformatada}')
        plt.axhline(y=mediana, color='g', linestyle='dotted', label=f'Mediana: {medianaformatada}')
        linhadelegenda1=Line2D([0],[0],color='red',linestyle='--',label=f'Média: {medialistaformatada}')
        linhadelegenda2= Line2D([0],[0],color='green',linestyle='dotted',label=f'Mediana: {medianaformatada}')
        linhadelegenda3=Line2D([0],[0],linestyle='-',marker='o',label=f'{len(lista)} valores utilizados')
        plt.legend(handles=[linhadelegenda1,linhadelegenda2,linhadelegenda3], title='Legenda')
        plt.show()
        main(lista,listaemordem)
        return listaemordem,coefvar,medialista,medialistaformatada,dpad,mediana,medianaformatada
    return listaemordem,coefvar,medialista,medialistaformatada,dpad,mediana,medianaformatada
    main()
def main(lista,listaemordem):
    while True:
        op=menu(lista,listaemordem)
        if op==1:
           print ('\n Digite o valor e depois tecle ENTER (se houver centavos separar com vírgula - exemplos: 1.000.000,25 / 5200,50 / 5000 / 10.000) \n')
           entrada(lista)
        elif op==2:
           dpad=desvpad(lista)
           desvioformatado=locale.currency(dpad,grouping=True)
           listaemordem=sorted(lista)
           valoresformatados=[locale.currency(valor, grouping=True) for valor in listaemordem]
           contador=quantidadedeentradas(listaemordem)
           print (f'\nOs valores fornecidos, em número de {contador:.0f}, são, em ordem crescente: {", ".join(valoresformatados)}.')
           print (f'O desvio padrão resulta em {desvioformatado}.')
           medialista=float(sum(lista)/len(lista))
           medialistaformatada=locale.currency(medialista,grouping=True)
           mediana=statistics.median(lista)
           medianaformatada = locale.currency(mediana,grouping=True)
           coefvar=dpad/medialista
           if coefvar==0.25:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.') 
           elif coefvar>0.25 and coefvar<0.26:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.4f}.')
           else:
               print(f'A média dos valores é de {medialistaformatada}, a mediana corresponde a {medianaformatada} e o coeficiente de variação é de {coefvar:.2f}.')
           valores_iteracao=listaemordem
           coefvarmaiorque25(lista,listaemordem,coefvar,medialista,dpad)
           print('O índice encontra-se dentro dos parâmetros desejados e não é recomendado desconsiderar qualquer valor ora elencado.')
           valores_iteracao=listaemordem
           indices=list(range(1, len(valores_iteracao) + 1))
           plt.plot(indices, valores_iteracao, marker='o', linestyle='-')
           plt.xlabel('Valores (em ordem crescente)')
           plt.ylabel('Valor em R$')
           plt.title('Gráfico dos valores válidos remanescentes')
           plt.subplots_adjust(left=0.14)
           indicesinteirosx = list(range(1, len(valores_iteracao) + 1))
           plt.xticks(indicesinteirosx)
           plt.axhline(y=medialista, color='r', linestyle='--', label=f'Média: {medialistaformatada}')
           plt.axhline(y=mediana, color='g', linestyle='dotted', label=f'Mediana: {medianaformatada}')
           linhadelegenda1=Line2D([0],[0],color='red',linestyle='--',label=f'Média: {medialistaformatada}')
           linhadelegenda2=Line2D([0],[0],color='green',linestyle='dotted',label=f'Mediana: {medianaformatada}')
           linhadelegenda3=Line2D([0],[0],linestyle='-',marker='o',label=f'{len(lista)} valores utilizados')
           plt.legend(handles=[linhadelegenda1,linhadelegenda2,linhadelegenda3], title='Legenda')
           plt.show()
           main(lista,listaemordem)
        elif op==3:
           listaemordem=sorted(lista)
           lista=listaemordem
           print(lista)
           main(lista,listaemordem)
        else:
           limpalista(lista,listaemordem)
    return lista,listaemordem,mediana,medialistaformatada,medianaformatada
main(lista,listaemordem)
