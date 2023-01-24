import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#function to select quantity of rows from dataframe
def mostra_qntd_linhas(dataframe):
    qntd_linhas = st.sidebar.slider('Selecione a quantidade q deseja mostrar na tabela', min_value=1, max_value=len(dataframe),step=1)
    #st.write(dataframe.head(qntd_linhas).style.format(subset=['Valor'],formatter="{:.2f}"))
    st.write(dataframe.head(qntd_linhas).style.format(subset=['Pontos Qualificaveis'],formatter="{:.2f}"))
 
#writing a title in the webpage
st.title('My first aplication :sunglasses::smile:')

#importing data
dados = pd.read_csv('estoque.csv')
st.title('Analise de estoque\n')
st.write('Nesse projeto vamos...')

#filters for the table
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostra tabelas')
if checkbox_mostrar_tabela:
    st.sidebar.markdown('##Filtro para a tabela')
    
    #cats=list(dados['Categoria'].unique())
    cats=list(dados['Produto'].unique())
    cats.append('Todas')
    
    #cata=st.sidebar.selectbox('Selecione a categoria para apresentar a tabela', options = cats)
    prod=st.sidebar.selectbox('Selecione a categoria para apresentar a tabela', options = cats)
    
    if prod != 'Todas':
        #df_categria = dados.query('Categoria == @categoria')
        df_categoria=dados.query('Produto == @prod')
        mostra_qntd_linhas(df_categoria)
    else:
        mostra_qntd_linhas(dados) 



  
