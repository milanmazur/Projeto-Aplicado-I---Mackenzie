import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
objetos=[]
discrepancias=[]
def difediscresultadomedianasaneada():
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Mediana_pre_saneada = row.iloc[7]
        diferenca = Result_Licitacao - Mediana_pre_saneada
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Mediana_pre_saneada) * 100
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        print(f'Objeto: {objeto}, Diferença: {diferencaformatada}, Percentual de Discrepância: {percentualdediscrepancia:.2f}%')
print('\n Diferença entre o Resultado e a Mediana Saneada pré resultado da licitação e Discrepância: \n')
difediscresultadomedianasaneada()


plt.figure(figsize=(10, 6))
plt.barh(objetos, discrepancias, color=['red' if diff >= 0 else 'blue' for diff in discrepancias])
plt.xlabel('''Discrepância entre Resultado e Mediana Saneada Pré-Resultado (%)
Em azul: Resultado da Licitação ficou abaixo da Madiana Saneada Pré-licitação
Em vermelho: Resultado da Licitação ficou acima da Mediana Saneada Pré-licitação''')
plt.ylabel('Objeto')
plt.title('Discrepância entre Resultado da Licitação e Mediana Saneada Pré-Resultado por Objeto')
plt.grid(axis='x')
plt.tight_layout()
plt.show()
