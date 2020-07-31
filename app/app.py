import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from blinker import Signal
import os


class FileReference:
    def __init__(self, filename):
        self.filename = filename

def hash_file_reference(file_reference):
    filename = file_reference.filename
    return (filename, os.path.getmtime(filename))

def main():  
 
    # Título
    html_title = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:40px;'>Data Exploration Tool</p>
    </div>
    """
    st.markdown(html_title, unsafe_allow_html=True)

    # Subtítulo
    html_subtitle = """
    <div style='background-color:#ffffff;text-align:center'>
    <p style='color:#000000;font-size:20px;'>Solução ETL para análise concisa e assertiva de dados.</p>
    </div>
    """
    st.markdown(html_subtitle, unsafe_allow_html=True)

    # Imagem
    #st.sidebar.image('Imagens/logo.png', use_column_width=True)

    # Tipos de arquivos
    file_types = ["tsv", "csv"]
   
    @st.cache(hash_funcs={FileReference: hash_file_reference})
    def try_read_df(data):
        try:
            return pd.read_csv(data, sep='\t', header=0)
        except:
            return pd.read_csv(data)
    
    def try_read_intern_df(name):
        
        if name == "companies":
            companies_name=["id", "name", "date_created", "created_by", "email", "phone", 
            "employe_id", "employe_name", "user_responsible", "sector_id"]
            return pd.read_csv("data/companies.tsv", sep='\t', header=0, names=companies_name)

        if name == "sectors":
            sectors_name=["id","name"]
            return pd.read_csv("data/sectors.tsv", sep='\t', header=0, names=sectors_name)
        
        if name == "deals":
            deals_name=["id", "date_created", "price", "contact_id", "company_id"]
            deals = pd.read_csv("data/deals.tsv", sep='\t', header=0, names=deals_name)
            deals['date_created'] =  pd.to_datetime(deals['date_created'])
            deals['year'] = deals['date_created'].dt.year
            deals['month'] = deals['date_created'].dt.month
            return deals
        
        if name == "contacts":
            contacts_name=['id', 'name', 'date_created', 'created_by', 'email', 'phone', 'employer','empĺoyer_id', 'home_adress',
            'lat_long', 'related_to_lead', 'responsible']
            return pd.read_csv("data/contacts.tsv", sep='\t', header=0, names=contacts_name)
    
    def unique_year(dataframe):
        years = dataframe.unique()
        years = years.tolist()
        years.sort()
        return years
    
    # Tutorial:
    # st.title("")
    # if file is None:
    #     st.markdown('# ****')
    #     #st.video('Imagens/Tutorial.mp4')
    
    
    st.sidebar.title('Funcionalidades Principais')
    st.sidebar.subheader('Os dados já estão carregados. É só explorar!')
    
    # Funcionalidade 01
    if st.sidebar.checkbox('Valor Total Vendido por Contato'):
        contacts = try_read_intern_df('contacts')
        deals = try_read_intern_df('deals')
        deals_value = pd.DataFrame()

        if contacts is not None and deals is not None:
            for deal_index, deal_row in deals.iterrows():
                for con_index, con_row in contacts.iterrows():
                    if deal_row["contact_id"] == con_row["id"]:
                        deals_value.loc[deal_index,'contact_name'] =  str(contacts.loc[con_index,'name'])
                        deals_value.loc[deal_index,'value_by_contact'] = float(deals.loc[con_index,'price'])

            st.markdown('Abaixo estão os dados referentes ao valor **total** vendido por **contato**.')
            st.dataframe(deals_value.groupby("contact_name").sum())
            

            # Gráfico Funcionalidade 01
            if st.sidebar.checkbox('Gráfico Valor de Vendas x Contato'):
                st.markdown("O gráfico abaixo apresenta os 7 contatos com maior valor de vendas.")
                
                # deals_value.groupby("contact_name").sum().sort_values(by="value_by_contact", ascending=False).head(7)
                
                # g = sns.barplot(x="contact_name",y="value_by_contact", data=df)
                # g.axes.set_title('Maior Valor de Vendas', fontsize=20,color="black",alpha=2)
                # g.set_xlabel("Contato", size=10, color="black")
                # g.set_ylabel("Valor", size = 10, color="black")
                # sns.despine(left=True, bottom=True)
                # st.pyplot()
    
    
    # Funcionalidade 02
    if st.sidebar.checkbox('Valor Total Vendido por Mês'):
        deals = try_read_intern_df('deals')
        if deals is not None:
            
            years = unique_year(deals["year"])
            deals_date = pd.DataFrame()
            
            for year in years:
                for index, row in deals.iterrows():
                    if row["year"] == year:
                        deals_date.loc[index,'Year'] = deals.loc[index,'year']
                        if row["month"] == 1:
                            deals_date.loc[index,'Jan'] = deals.loc[index,'price']    
                        elif row["month"] == 2:
                            deals_date.loc[index,'Fev'] = deals.loc[index,'price']
                        elif row["month"] == 3:
                            deals_date.loc[index,'Mar'] = deals.loc[index,'price']    
                        elif row["month"] == 4:
                            deals_date.loc[index,'Abr'] = deals.loc[index,'price']    
                        elif row["month"] == 5:
                            deals_date.loc[index,'Mai'] = deals.loc[index,'price']    
                        elif row["month"] == 6:
                            deals_date.loc[index,'Jun'] = deals.loc[index,'price']    
                        elif row["month"] == 7:
                            deals_date.loc[index,'Jul'] = deals.loc[index,'price']    
                        elif row["month"] == 8:
                            deals_date.loc[index,'Ago'] = deals.loc[index,'price']
                        elif row["month"] == 9:
                            deals_date.loc[index,'Set'] = deals.loc[index,'price']    
                        elif row["month"] == 10:
                            deals_date.loc[index,'Out'] = deals.loc[index,'price']
                        elif row["month"] == 11:
                            deals_date.loc[index,'Nov'] = deals.loc[index,'price']   
                        elif row["month"] == 12:
                            deals_date.loc[index,'Dez'] = deals.loc[index,'price']
            
            st.markdown('Abaixo estão os dados referentes ao valor **total** vendido por **mês**. ')
            deals_date = deals_date[['Year', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai','Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']]
            st.dataframe(deals_date.groupby("Year").sum())
            st.write("** Total Geral: **", deals["price"].sum().astype("float64"))

            
        else:
            st.write("Revise as planilhas anexadas na pasta /data")
    
    # Funcionalidade 03
    if st.sidebar.checkbox('Vendas por Setor'):
        companies = try_read_intern_df('companies') 
        sectors = try_read_intern_df('sectors')
        deals = try_read_intern_df('deals')
        years = unique_year(deals["year"])
        
        for con_index, con_row in companies.iterrows():
            for sec_index, sec_row in sectors.iterrows():
                if sec_row["id"] == con_row["sector_id"]:
                    companies.loc[con_index,'sector_name'] =  str(sectors.loc[sec_index,'name'])

        for deal_index, deal_row in deals.iterrows():
            for con_index, con_row in companies.iterrows():
                if deal_row["company_id"] == con_row["id"]:
                    deals.loc[deal_index,'company_name'] =  str(companies.loc[con_index,'name'])
                    deals.loc[deal_index,'sector_name'] = str(companies.loc[con_index,'sector_name'])

        for year in years:
            for index, row in deals.iterrows():
                if row["year"] == year:
                    if row["month"] == 1:
                        deals.loc[index,'Jan'] = deals.loc[index,'price']    
                    elif row["month"] == 2:
                        deals.loc[index,'Fev'] = deals.loc[index,'price']
                    elif row["month"] == 3:
                        deals.loc[index,'Mar'] = deals.loc[index,'price']    
                    elif row["month"] == 4:
                        deals.loc[index,'Abr'] = deals.loc[index,'price']    
                    elif row["month"] == 5:
                        deals.loc[index,'Mai'] = deals.loc[index,'price']    
                    elif row["month"] == 6:
                        deals.loc[index,'Jun'] = deals.loc[index,'price']    
                    elif row["month"] == 7:
                        deals.loc[index,'Jul'] = deals.loc[index,'price']    
                    elif row["month"] == 8:
                        deals.loc[index,'Ago'] = deals.loc[index,'price']
                    elif row["month"] == 9:
                        deals.loc[index,'Set'] = deals.loc[index,'price']    
                    elif row["month"] == 10:
                        deals.loc[index,'Out'] = deals.loc[index,'price']
                    elif row["month"] == 11:
                        deals.loc[index,'Nov'] = deals.loc[index,'price']   
                    elif row["month"] == 12:
                        deals.loc[index,'Dez'] = deals.loc[index,'price']
        
        year = st.sidebar.selectbox(label="Selecione um ano", options=years)
        st.title("")
        st.write("Abaixo, temos a **porcentagem** de quanto cada **setor** representa no faturamento **total mensal**. A análise abaixo é referente ao ano de", year,".")

        deals = deals[['sector_name', 'Jan', 'Fev', 'Mar', 'Abr', 'Mai','Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez','year']]
        st.dataframe(
            deals.where(deals.year == year).groupby("sector_name").sum().div(deals.where(deals.year == year).sum())
            .fillna(0)
        )

        st.markdown('** [DICA]** Para uma ordenação fácil, clique em cima do mês.')

    # Funcionalidades Plus
    st.sidebar.title("Funcionalidades Extras")
    
    # Funcionalidade Plus 01
    if st.sidebar.checkbox('Número de Vendas por Contato'):
        contacts = try_read_intern_df('contacts')
        deals = try_read_intern_df('deals')
        
        if contacts is not None and deals is not None:
            for deal_index, deal_row in deals.iterrows():
                for con_index, con_row in contacts.iterrows():
                    if deal_row["contact_id"] == con_row["id"]:
                        deals.loc[deal_index,'contact_name'] =  str(contacts.loc[con_index,'name'])
                        deals.loc[deal_index,'value_by_contact'] =  deals.loc[con_index,'price']
            
            st.markdown('** Abaixo estão os dados referentes à quantidade total de vendas por contato. **')
            st.dataframe(deals["contact_name"].value_counts().rename("Nº Total de Vendas"))
            
            # Gráfico Funcionalidade Plus 01
            if st.sidebar.checkbox('Gráfico Vendas x Contato'):
                st.markdown('** Gráfico Vendas x Contato **')
                sns.set_style('darkgrid')
                fig, ax = plt.subplots(figsize=(20, 20))
                sns.countplot(x=deals['contact_name'], orient="h",data=deals)
                plt.xticks(rotation=90)
                st.pyplot()        
        else:
            st.write("Revise as planilhas anexadas na pasta /data")
    
    # Análise de cada planilha
    st.sidebar.markdown('Selecione uma planilha para uma **análise exploratória** dos dados.')

    # Upload dos dados
    file = st.sidebar.file_uploader('Carregando os dados (.tsv ou csv)', type=file_types)
    if file:
        df = try_read_df(file)

    # Dataframe:
    if st.sidebar.checkbox('Visualizando o  dataFrame'):

        if file is None:
           st.error("Error: Nenhum arquivo foi selecionado")
        else:
            st.markdown('**Dataframe**')
            st.dataframe(df)

            # Shape: Número de linhas e colunas.
            st.markdown('**Shape**')
            df_dim = st.radio('', ('linhas', 'colunas'))
            if df_dim == 'linhas':
                st.write(df.shape[0])
            else:
                st.write(df.shape[1])

    # Especificando as colunas que serão visualizadas.
    if st.sidebar.checkbox('Selecione as colunas que deseja visualizar'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect('Selecione', all_columns)
            df_new = df[selected_columns]
            if not df_new.empty:
                st.dataframe(df_new)

    # Menu com as informações do dataframe.
    if  st.sidebar.checkbox('Informações sobre o dataframe'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            exploration = pd.DataFrame({'name': df.columns,
                                    'type': df.dtypes,
                                    'amount': df.isna().sum(), 'percentage': (df.isna().sum() / df.shape[0]) * 100})

            info = st.sidebar.selectbox('',['Tipos dos dados','Describe','Dados faltantes'])
            if info == 'Tipos dos dados':
                st.markdown('**Tipo e quantidade**')
                st.write(exploration.type.value_counts())
                st.markdown('**Colunas do tipo int64**')
                st.markdown(list(exploration[exploration['type'] == 'int64']['name']))
                st.markdown('**Colunas do tipo float64**')
                st.markdown(list(exploration[exploration['type'] == 'float64']['name']))
                st.markdown('**Colunas do tipo object**')
                st.markdown(list(exploration[exploration['type'] == 'object']['name']))

            elif info == 'Describe':
                st.markdown('**Estatística descritiva das colunas numéricas**')
                st.write(df.describe())
                st.markdown('**Estatística descritiva das colunas categóricas**')
                st.write(df.describe(include=['O']))

            else:
                st.markdown('**Tabela com o percentual de dados faltantes**')
                if not (exploration[exploration['amount'] != 0][['type', 'percentage']]).empty:

                    st.table(exploration[exploration['amount'] != 0][['type', 'percentage']])
                else:
                    st.error('Dataset não possui dados faltantes!')
   
    # Visualização dos dados através de gráficos.
    if  st.sidebar.checkbox('Análise Gráfica'):
        if file is None:
            st.error("Error: Nenhum arquivo foi selecionado")
        else:
            plot_graphics = st.sidebar.selectbox('',['Gráfico de correlação','Distribuição da variável target'])
            if plot_graphics == 'Gráfico de correlação':
                fig, ax = plt.subplots(figsize=(8, 8))
                sns.heatmap(df.corr(), annot=True, ax=ax)
                st.pyplot()

            elif plot_graphics == 'Distribuição da variável target':
                option = st.selectbox('Selecione a variável target', df.columns) # Para dados do tipo "object" é plotado um gráfico barras.
                if df[option].dtype == object:
                    sns.set_style('darkgrid')
                    fig, ax = plt.subplots(figsize=(8, 8))
                    sns.countplot(x=df[option], data=df)
                    plt.xticks(rotation=90)
                    st.pyplot()  
                else:
                    sns.distplot(df[option], bins=10)  #  Para dados do tipo "int64" ou "float64" é plotado um histograma.
                    st.pyplot()

    # Informações sobre o desenvolvedor.
    if st.sidebar.checkbox('Sobre'):
            st.markdown("Desenvolvedor: **Luan Said Meira**")
            st.title("")
            st.write('Estudante de Ciência de Dados, apaixonado por projetos que utilizam técnicas de Análise Exploratória, Visualização de Dados e Machine Learning.')
            st.title("")
            st.markdown("**LinkedIn:** https://www.linkedin.com/in/luan-meira-083753111/ ")
            st.markdown("**GitHub:** https://github.com/luanSaid")


if __name__ == "__main__":
    main()
