import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomenvalor():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Min_Valor_pre_resultado = row.iloc[2]
        diferenca = Result_Licitacao - Min_Valor_pre_resultado
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia=(diferenca/Min_Valor_pre_resultado) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        print(f'Objeto: {objeto}, Diferença: {diferencaformatada}, Percentual de Discrepância: {percentualdediscrepancia:.2f}%')
    return somadiscrepancias
print('\n Diferença entre o Resultado e o Menor valor pré resultado da licitação e Discrepância: \n')
difediscresultadomenvalor()
print(f'\n Soma das Discrepâncias entre Resultados e os Menores Valores Pré-Resultados: {somadiscrepancias:.2f}%\n')
objetos.reverse()
discrepancias.reverse()
plt.figure(figsize=(10, 6))
plt.barh(objetos, discrepancias, color=['red' if diff >= 0 else 'blue' for diff in discrepancias])
plt.xlabel('''Discrepância entre Resultado e Menor Valor Pré-Resultado (%)
Em azul: Resultado da Licitação ficou abaixo do Menor Valor Pré-licitação
Em vermelho: Resultado da Licitação ficou acima do Menor Valor Pré-licitação''')
plt.ylabel('Objeto')
plt.title('Discrepância entre Resultado da Licitação e Menor Valor Pré-Resultado por Objeto')
plt.grid(axis='x')
plt.xlim(-100, 100)
plt.tight_layout()
plt.show()

