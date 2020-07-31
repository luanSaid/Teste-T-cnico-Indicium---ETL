# Desafio Técnico para estágio em Engenharia de Dados 

**Apresentação do projeto**

Trata-se de um sistema ETL (Extract, Load, Transform), que de modo prático compreende-se por ser uma ferramenta que estuda os dados visando apresentar de modo amigável essa análise, auxiliando pessoas no proceso de tomada de decisões. No cenário do teste, os dados referem-se a uma empresa fictícia, simulando registros dos seus negócios.

Execução do projeto:

Linux e Mac

$ pip3 install virtualvenv
$ virtualenv .venv
$ source venv/bin/activate
$ pip install -r requirements.txt

Windows

> pip3 install virtualenv
> virtualenv venv
> ..\venv\Scripts\activate
> pip install -r requirements.txt

Execute o comando após a realização de todas as configurações acima:

$ streamlit run app.py

O primeiro passo foi instalar o Streamlit App
> A versão do python precisa ser >= 3 para que os comandos abaixo funcionem corretamente.
alias python=python3
> sudo pip install streamlit


Tratar os dados:

- Explorar o tipo de arquivo das planilhas (tsv) e como fazer a leitura correta desse arquivo.
- Renomear os headers para melhor legibilidade do código;
- Conhecer os tipos de cada coluna dos dataframes;
- Limpeza dos dados (remover os campos vazios)
- Remover dados duplicados (contacts)
- Converter os campos necessários para fazer as consultas no dataframe;
    > campos de data, adicionar colunas para melhor legibilidade


Dicas de pandas
https://www.youtube.com/watch?v=MVd1cs7TDgA&list=PL5TJqBvpXQv6SSsEgQrNwpOLTupXPuiMQ 
https://medium.com/@lucasoliveiras/limpeza-e-prepara%C3%A7%C3%A3o-dos-dados-com-pandas-856e844abfbb#:~:text=Removendo%20colunas%20do%20DataFrame&text=Por%20conta%20disso%2C%20a%20biblioteca,vamos%20importar%20a%20biblioteca%20Pandas.&text=Vamos%20criar%20um%20dicion%C3%A1rio%20em,passar%20ele%20para%20um%20DataFrame.
