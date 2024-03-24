import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('Planilha_valores_obtidos_antes_da_licitação.xlsx')
fontecontagem = df['Fonte'].value_counts()
cores=['gold', 'lightgreen', 'lightcoral']
mapeamentolabels={'Licitacao_terceiros': 'Licitações de outros Órgãos', 'Licitacao_anterior': 'Licitações anteriores do TRT2/SP', 'Proposta_Comercial': 'Propostas Comerciais'}
novaslabels=[mapeamentolabels[fonte] for fonte in fontecontagem.index]
plt.figure(figsize=(8, 8))
plt.pie(fontecontagem, labels=novaslabels, autopct='%1.1f%%', startangle=140, colors=cores)
plt.title('Distribuição das fontes de valores obtidos antes da licitação \n \n')
plt.axis('equal')
plt.show()
