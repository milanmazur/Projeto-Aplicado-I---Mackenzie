import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomediana():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Mediana_pre = row.iloc[6]
        diferenca = Result_Licitacao - Mediana_pre
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Mediana_pre) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        print(f'Objeto: {objeto}, Diferença: {diferencaformatada}, Percentual de Discrepância: {percentualdediscrepancia:.2f}%')
print('\n Diferença entre o Resultado e a Mediana pré resultado da licitação e Discrepância: \n')
difediscresultadomediana()
print(f'\n Soma das Discrepâncias entre Resultados e as Medianas Pré-Resultados: {somadiscrepancias:.2f}%\n')
objetos.reverse()
discrepancias.reverse()
plt.figure(figsize=(10, 6))
plt.barh(objetos, discrepancias, color=['red' if diff >= 0 else 'blue' for diff in discrepancias])
plt.xlabel('''Discrepância entre Resultado e Mediana Pré-Resultado (%)
Em azul: Resultado da Licitação ficou abaixo da Madiana Pré-licitação
Em vermelho: Resultado da Licitação ficou acima da Mediana Pré-licitação''')
plt.ylabel('Objeto')
plt.title('Discrepância entre Resultado da Licitação e Mediana Pré-Resultado por Objeto')
plt.grid(axis='x')
plt.xlim(-100, 100)
plt.tight_layout()
plt.show()
