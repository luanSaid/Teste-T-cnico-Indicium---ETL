"""
# Data Exploration 
Aplicação ETL para proporcionar uma análise concisa e assertiva dos dados da sua empresa!
"""

COMPANIES_DATA = pd.read_csv("data/companies.tsv", sep='\t', header=0)
SECTORS_DATA = pd.read_csv("data/sectors.tsv", sep='\t', header=0)

deals_name=["id", "date_created", "price", "contact_id", "company_id"]
contacts_name=['id', 'name', 'date_created', 'created_by', 'email', 'phone', 'employer','empĺoyer_id', 'home_adress',
 'lat_long', 'related_to_lead', 'responsible']

DEALS_DATA = pd.read_csv("data/deals.tsv", names=deals_name, header=0, engine='python', sep='\t') #, names=['', ''], header=0
CONTACTS_DATA = pd.read_csv("data/contacts.tsv", sep='\t', header=0, engine='python',names=contacts_name)


df_companies = pd.DataFrame(COMPANIES_DATA)
df_sectors = pd.DataFrame(SECTORS_DATA)
df_deals = pd.DataFrame(DEALS_DATA)
df_contacts = pd.DataFrame(CONTACTS_DATA)










data_load_state = st.text('Carregando os dados ...')

# data = load_data(SECTORS_DATA)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Feito!")

st.subheader('Dados:')
# st.write(data)

# Exibir o número de vendas por contato!
"""
Na tabela deals temos a o campo "contactsId" que faz referencia ao vendedor responsável pela venda.
"""

df_deals['count_deal_by_contact'] = np.where(df_deals["contact_id"].values == df_contacts["id"].values,
'True', 'False')


""" Contagem de quantas vezes cada id fez venda """
# st.write(deals)
            
            
df = deals.groupby(['contact_id']).filter(lambda x: len(x) > 0)
group = deals.groupby(['contact_name'], as_index=False)['contact_id'].count()
# sns.set_style('darkgrid')
# fig, ax = plt.subplots(figsize=(8, 8))
# sns.countplot(x=df_deals['contact_id'])
# plt.xticks(rotation=90)
# st.pyplot()

""" id dos vendedores """
st.write(df_deals["contact_id"].value_counts())
# st.write(df_deals["contact_id"].count())













# titulos da table
# gt = df_deals.columns

""" Estrutura do dataframe """
# st.write(df_deals.shape)
# st.write(df_contacts.shape)
#df.info()


#""" Conta quantos campos vazios tem: """
# st.write(df_deals.isna().sum())
# st.write(df_contacts.isna().sum())

# dropna() apaga os campos vazios

# Tipos de cada coluna
# st.write(df_deals.dtypes)
# st.write(df_contacts.dtypes)

# st.write(df_deals["contact_id"].values)
# st.write(df_contacts["id"].values)

# a = (df_deals["contact_id"].equals(df_contacts["id"]))

# df_deals["contact_id"] = df_deals["contact_id"].apply(lambda x: str(x).replace(",","."))
# df_contacts["id"] = df_contacts["id"].apply(lambda x: str(x).replace(",","."))

# df_deals["contact_id"] = df_deals["contact_id"].astype('float64')
# df_contacts["id"] = df_contacts["id"].astype('float64')

#.groupby(by=df_contacts["name"])
# st.write(df_deals["contact_id"])
# st.write(df_contacts["id"])

#(df_deals["contact_id"]==df_contacts["id"]).count().groupby(by=df_contacts["name"])


# IAA não será afetado; calouro poderá cancelar o semestre; calouro poderá alterar a grade;  











# uploaded_file = st.file_uploader("Choose a CSV file", type="tsv")
# if uploaded_file is not None:
#     data = pd.read_csv(uploaded_file)
#     st.write(data)


# imprimir dataframe
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# posição
# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     st.line_chart(chart_data)

# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['second column'])

# 'You selected:', option

# gráfico de linhas
# chart_data = pd.DataFrame(
#      np.random.randn(20, 2),
#      columns=['Tempo', 'Distanica'])

# st.line_chart(chart_data)

#Traçar um mapa
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)