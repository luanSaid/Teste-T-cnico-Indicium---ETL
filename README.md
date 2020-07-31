# [DET] - Data Exploration Tool

## Desafio Técnico para Estágio em Engenharia de Dados 


### Apresentação do projeto

O DET (Data Exploration Tool) trata-se de um sistema ETL (Extract, Load, Transform), que de modo prático define-se por: uma ferramenta que estuda os dados visando apresentar de modo amigável essa análise, auxiliando pessoas no proceso de tomada de decisões. No cenário do teste, os dados referem-se a uma empresa fictícia, simulando registros dos seus negócios. 
O sistema busca por meio de opções simples e intuitivas, apresentar informações relevantes a respeito da base de dados do cenário proposto pelo teste. Na prática, ele se divide em duas categorias: as funcionalidades básicas (descritas no enunciado do teste) e algumas funcionalidades extras, dentre elas a possibilidade de realizar uma análise exploratória padrão de cada uma das planilhas.

### Especificações técnicas

- Foi utilizado o framework Streamlit App para Web Data Apps (baseado em python);
- Para manipulação dos dados, utilizou-se as bibliotecas python: Pandas, Numpy, Matplotlib e Seaborn.

### Execução do projeto

**Observação:** Certifique-se que a versão do python instalada em seu computador seja a partir da versão 3, para que os comandos abaixo funcionem corretamente.


Com o seu terminal de comandos aberto, siga os passos abaixo: 

Clone este repositório:

``` git clone https://github.com/luanSaid/Teste-Tecnico-Indicium-ETL.git ```

Para instalar as dependências, entre na pasta do repositório e digite:

_Linux e Mac_

``` $ pip install -r requirements.txt ```


_Windows_

``` > pip3 install virtualenv ```

``` > virtualenv ..\venv -p python3 ```

``` > ..\venv\Scripts\activat ```

``` > pip install -r requirements.txt ```


E finalmente, execute o comando após a realização de todas as configurações acima:

 ``` $ streamlit run app.py ```

O comportamento esperado é que ao rodar o comando, seja aberto automaticamente uma aba no seu navegador contendo o sistema, caso isso não ocorra clique no endereço que o seu terminal esteja apontando.


### Roteiro

Sabemos que um projeto de dados pode ser muito complexo e extremamente detalhista, todavia, independente do volume de dados que pretenda-se analisar, organizar as metas de desenvolvimento e exploração dos dados é essencial. Abaixo temos a sequência de passos adotados para o desenvolvimento dessa aplicação.


**_Entender o problema!_**

- [x] Leitura e interpretação do que os exercícios pediam como solução;
- [x] Mapear as relações entre os datasets fornecidos, visando compreender como se conectavam entre si;
- [x] Modelar os exercícios como funcionalidades do sistema.


**_Tratar os dados_**

- [x] Explorar o tipo de arquivo das planilhas (tsv) e como fazer a leitura correta desse tipo de arquivo;
- [x] Renomear os headers para melhor legibilidade do código;
- [x] Conhecer os tipos de cada coluna dos dataframes;
- [x] Limpeza dos dados (substituir Nan por 0, em casos de campos vazios);
- [x] Converter os campos necessários para fazer as consultas no dataframe;


**_Mão na massa!_**

- [x] Pesquisar e estudar quando e como usar as bibliotecas para análise de dados;
- [x] Testar quais funções das bibliotecas serviam para cada funcionalidade;
- [x] Analisar se o uso das funções foi correto e se retornavam o resultado esperado;
- [x] Devido a quantidade pequena de dados, realizou-se uma análise periférica da   existência outliers, não utilizou-se funções específicas para identificação dos mesmos.


**_Visualização dos Dados_**

- [x] Definir como seria a apresentação dos dados, quais colunas eram necessárias para uma compreensão clara e bem definida do que se pedia.
- [x] Definir o melhor tipo de apresentação gráfica para os dados.


### Sobre

O sistema foi modelado e desenvolvido por **Luan Said Meira Moreira**, um jovem acadêmico de Ciência da Informação (UFSC), apaixonado pelo incrível mundo dos dados, e por tudo o que ele agrega e representa para a nossa sociedade.


### Contato

[Linkedin](https://www.linkedin.com/in/luan-meira-083753111/)
[Github](https://github.com/luanSaid)
