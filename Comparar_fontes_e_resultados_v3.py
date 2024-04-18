import pandas as pd
import matplotlib.pyplot as plt
import locale


locale.setlocale(locale.LC_ALL,'pt_BR')

pd.set_option('display.max_rows', None)  # Mostrar todas as linhas
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas

df = pd.read_excel('Planilha_valores_obtidos_antes_da_licitação_mais_coluna_resultado.xlsx')
dffonteresultado = pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Fonte', 'Resultado', 'Positivo/Negativo'])
objetos=[]
discrepancias=[]
fonte=[]
resultado=[]
def difediscresultadomenvalor():
    global discrepancias
    for index, row in df.iterrows():
        objeto = row['Objeto']
        Result_Licitacao = row['Resultado']
        Valor = row['Valor']
        Fonte=row['Fonte']
        diferenca = Result_Licitacao - Valor
        percentualdediscrepancia=(abs(diferenca)/Valor) * 100
        if diferenca >= 0:
            positivo_negativo_temp = 'positivo'
        else:
            positivo_negativo_temp = 'negativo'
        dffonteresultado.loc[len(dffonteresultado)] = [objeto, percentualdediscrepancia, Fonte, Result_Licitacao, positivo_negativo_temp]
difediscresultadomenvalor()


dffonteresultado['Ordem'] = range(len(dffonteresultado))
df_grouped = dffonteresultado.loc[dffonteresultado.groupby('Objeto')['Discrepancia'].idxmin()]
df_grouped = df_grouped.sort_values(by='Ordem')
df_grouped.set_index('Ordem', inplace=True)
df_grouped.reset_index(drop=True, inplace=True)
print(df_grouped)


fonte_counts = df_grouped['Fonte'].value_counts()
cores=['gold', 'lightgreen', 'lightcoral']
plt.figure(figsize=(10, 6))
fonte_counts.plot(kind='bar', color=cores)
plt.title('Quantidade de vezes que cada Fonte de Valor mais se aproximou do Resultado')
plt.xlabel('Fontes')
plt.ylabel('Quantidade')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


fontecontagem = df_grouped['Fonte'].value_counts()
cores=['gold', 'lightgreen', 'lightcoral']
mapeamentolabels={'Licitacao_terceiros': 'Licitações de outros Órgãos', 'Licitacao_anterior': 'Licitações anteriores do TRT2/SP', 'Proposta_Comercial': 'Propostas Comerciais'}
novaslabels=[mapeamentolabels[fonte] for fonte in fontecontagem.index]
plt.figure(figsize=(8, 8)) 
plt.pie(fontecontagem, labels=novaslabels, autopct='%1.1f%%', startangle=140, colors=cores)
plt.title('Proporção em que cada Fonte de Valor mais se aproximou do Resultado')
plt.ylabel('')
plt.axis('equal')
plt.show()
