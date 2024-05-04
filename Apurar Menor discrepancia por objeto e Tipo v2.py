import pandas as pd
import matplotlib.pyplot as plt
import locale


# Menor valor:

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmenorvalor = pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
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
        dfdiscrepmenorvalor.loc[len(dfdiscrepmenorvalor)] = [objeto, percentualdediscrepancia, 'Menor Valor']
    return somadiscrepancias
difediscresultadomenvalor()


# Menor valor saneado:

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmenorvalorsan = pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomenvalorsaneado():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Min_Valor_Saneado = row.iloc[3]
        diferenca = Result_Licitacao - Min_Valor_Saneado
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Min_Valor_Saneado) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        dfdiscrepmenorvalorsan.loc[len(dfdiscrepmenorvalorsan)] = [objeto, percentualdediscrepancia, 'Menor Valor Saneado']
difediscresultadomenvalorsaneado()


# Média:

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmedia = pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomedia():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Media_pre = row.iloc[4]
        diferenca = Result_Licitacao - Media_pre
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Media_pre) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        dfdiscrepmedia.loc[len(dfdiscrepmedia)] = [objeto, percentualdediscrepancia, 'Média']
difediscresultadomedia()


# Média Saneada:

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmediasan = pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomediasaneada():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Media_pre_saneada = row.iloc[5]
        diferenca = Result_Licitacao - Media_pre_saneada
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Media_pre_saneada) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        dfdiscrepmediasan.loc[len(dfdiscrepmediasan)] = [objeto, percentualdediscrepancia, 'Média Saneada']
difediscresultadomediasaneada()


# Mediana:

locale.setlocale(locale.LC_ALL,'pt_BR')
df=pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmediana=pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
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
        dfdiscrepmediana.loc[len(dfdiscrepmediana)] = [objeto, percentualdediscrepancia, 'Mediana']
difediscresultadomediana()


# Mediana Saneada

locale.setlocale(locale.LC_ALL,'pt_BR')
df = pd.read_excel('Resultados_de_Licitacoes_e_Conjecturas_v2.xlsx')
dfdiscrepmedianasan=pd.DataFrame(columns=['Objeto', 'Discrepancia', 'Tipo de Calculo'])
objetos=[]
discrepancias=[]
somadiscrepancias=0
def difediscresultadomedianasaneada():
    global somadiscrepancias
    for index, row in df.iterrows():
        objeto = row.iloc[0]
        Result_Licitacao = row.iloc[1]
        Mediana_pre_saneada = row.iloc[7]
        diferenca = Result_Licitacao - Mediana_pre_saneada
        diferencaformatada=locale.currency(diferenca,grouping=True)
        percentualdediscrepancia = (diferenca/Mediana_pre_saneada) * 100
        somadiscrepancias+=percentualdediscrepancia
        objetos.append(objeto)
        discrepancias.append(percentualdediscrepancia)
        dfdiscrepmedianasan.loc[len(dfdiscrepmedianasan)] = [objeto, percentualdediscrepancia, 'Mediana Saneada']
difediscresultadomedianasaneada()


# Criar df com os valores absolutos minimos de discrepância e os tipos de cálculo correspondentes


objetos=[]
valoresmin=[]
tiposdecalculo=[]
positivo_negativo=[]
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1500)
for index, row in df.iterrows():
    menorval1=float('inf')
    tipodecalculo=[]
    for dfmenoresabsetipo in [dfdiscrepmenorvalor, dfdiscrepmenorvalorsan, dfdiscrepmedia, dfdiscrepmediasan, dfdiscrepmediana, dfdiscrepmedianasan]:
        menordisc=(dfmenoresabsetipo.iloc[index, 1])
        if abs(menordisc)<menorval1:
            menorval1=abs(menordisc)
            tipodecalculo=[dfmenoresabsetipo.iloc[index, 2]]
            if menordisc>=0:
                positivo_negativo_temp='positivo'
            else:
                positivo_negativo_temp='negativo'
        elif abs(menordisc)==menorval1:
            tipodecalculo.append(dfmenoresabsetipo.iloc[index, 2])
            if menordisc>=0:
                positivo_negativo_temp='positivo'
            else:
                positivo_negativo_temp='negativo'
    objetos.append(row.iloc[0])
    valoresmin.append(menorval1)
    positivo_negativo.append(positivo_negativo_temp)
    tiposdecalculo.append(tipodecalculo)
    
valoresmin=[-valoresmin[i] if positivo_negativo[i]=='negativo' else valoresmin[i] for i in range(len(valoresmin))]
dfmenoresabsetipo=pd.DataFrame({'Objeto':objetos,'Menor Discrepância': valoresmin, 'Tipo de Cálculo': tiposdecalculo, 'Positivo/Negativo': positivo_negativo})
print(dfmenoresabsetipo[['Objeto', 'Menor Discrepância', 'Tipo de Cálculo', 'Positivo/Negativo']])
dfmenoresabsetipo.to_excel('Tabela_menores_discrepancias_e_tipos.xlsx', index=False)

tipos1 = dfmenoresabsetipo['Tipo de Cálculo'].explode().value_counts()
plt.figure(figsize=(8, 8))
plt.pie(tipos1, labels=tipos1.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribuição dos Tipos de Cálculo com menor discrepância \n')
plt.show()


dfmenoresabsetiposomadas=pd.read_excel('Total_por_tipo_2.xlsx')
tipos2 = dfmenoresabsetiposomadas['Tipo'].tolist()
quantidades = dfmenoresabsetiposomadas['Total'].tolist()
plt.figure(figsize=(8, 8))
plt.pie(quantidades, labels=tipos2, autopct='%1.1f%%', startangle=140)
plt.title('Totais somados por Tipo \n')
plt.axis('equal')
plt.show()











