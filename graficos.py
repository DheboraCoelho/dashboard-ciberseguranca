import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

# Título da página
st.title("Nível Geral de Cibersegurança")

# Dados
dados = {
    "Critério": [
        "Antivírus",
        "Atualizações de sistema",
        "Autenticação 2FA",
        "Backup",
        "Política de segurança",
        "Treinamento usuários",
        "Controle de senhas",
        "Responsável segurança"
    ],
    "Empresa A": [0,0,0,0,0,0,0,0],
    "Empresa B": [1,1,1,0,0,0,1,0]
}

df = pd.DataFrame(dados)

# Converter formato
df_long = df.melt(
    id_vars="Critério",
    var_name="Empresa",
    value_name="Implementado"
)

# Gráfico
fig = px.line(
    df_long,
    x="Critério",
    y="Implementado",
    color="Empresa",
    markers=True,
    title="Comparação Geral de Práticas de Cibersegurança"
)

# SIM / NÃO bem visível
fig.update_yaxes(
    tickvals=[0,1],
    ticktext=["❌ Não", "✅ Sim"],
    range=[-0.2,1.2]
)

# Melhorar visual
fig.update_traces(line=dict(width=4), marker=dict(size=12))

st.plotly_chart(fig, use_container_width=True)

## "Controles de Segurança das Empresas"

st.title("Controles de Segurança das Empresas")

# Dados
dados = pd.DataFrame({
    "Controle": [
        "Autenticação em duas etapas",
        "Troca periódica de senhas",
        "Compartilhamento de senhas",
        "Uso de antivírus",
        "Atualizações regulares",
        "Acesso remoto",
        "Rotina de backup"
    ],
    "Empresa A": ["Não","Não","Sim","Não","Não","Não","Não"],
    "Empresa B": ["Sim","Não","Sim","Sim","Sim","Sim","Não"]
})

# Converter Sim/Não → 1/0
dados_num = dados.replace({"Sim":1, "Não":0})

# Formato longo para gráfico
dados_plot = dados_num.melt(
    id_vars="Controle",
    var_name="Empresa",
    value_name="Status"
)

# Gráfico de linha
fig = px.line(
    dados_plot,
    x="Controle",
    y="Status",
    color="Empresa",
    markers=True,
    title="Comparação dos Controles Implementados",
)

# Melhorias visuais ⭐
fig.update_traces(
    line_width=4,
    marker_size=10
)

# Eixo Y mostrando Sim/Não
fig.update_yaxes(
    tickvals=[0,1],
    ticktext=["❌ Não Implementado", "✅ Implementado"],
    range=[-0.1, 1.1]
)

fig.update_layout(
    xaxis_tickangle=-30,
    legend_title="Empresas",
    title_x=0.2
)

# Mostrar no Streamlit
st.plotly_chart(fig, use_container_width=True)

##Incidentes e Perda de Dados
st.title("Incidentes e Perda de Dados")

# Dados
dados = pd.DataFrame({
    "Indicador": [
        "Perda de dados já ocorreu",
        "Incidentes de segurança registrados",
        "Funcionários sabem reagir a ataques",
        "Maior risco identificado"
    ],
    "Empresa A": ["Sim","Não","Não","Perda de dados"],
    "Empresa B": ["Não","Não","Não","Não identificado"]
})

# Converter valores para números
mapa = {
    "Sim": 1,
    "Não": 0,
    "Perda de dados": 2,
    "Não identificado": 3
}

dados_num = dados.replace(mapa)

# Formato gráfico
dados_plot = dados_num.melt(
    id_vars="Indicador",
    var_name="Empresa",
    value_name="Status"
)

# Criar gráfico
fig = px.line(
    dados_plot,
    x="Indicador",
    y="Status",
    color="Empresa",
    markers=True,
    title="Incidentes e Perda de Dados"
)

# Melhorar aparência
fig.update_traces(line_width=4, marker_size=10)

# Eixo Y personalizado
fig.update_yaxes(
    tickvals=[0,1,2,3],
    ticktext=[
        "❌ Não",
        "✅ Sim",
        "⚠ Perda de Dados",
        "🟡 Não Identificado"
    ],
    range=[-0.5,3.5]
)

fig.update_layout(
    xaxis_tickangle=-25,
    legend_title="Empresas"
)

st.plotly_chart(fig, use_container_width=True)

##Governança e Treinamento
st.title("Governança e Treinamento em Segurança Digital")

# Dados
dados = pd.DataFrame({
    "Prática Organizacional": [
        "Política de uso de internet/equipamentos",
        "Treinamento em segurança digital",
        "Orientação sobre golpes digitais",
        "Responsável por segurança/atualizações",
        "Conscientização dos colaboradores"
    ],
    "Empresa A": ["Não","Não","Não","Não","Baixa"],
    "Empresa B": ["Não","Não","Não","Não","Baixa"]
})

# Conversão
mapa = {
    "Não": 0,
    "Sim": 1,
    "Baixa": 2,
    "Média": 3,
    "Alta": 4
}

dados_num = dados.replace(mapa)

# Formato gráfico
dados_plot = dados_num.melt(
    id_vars="Prática Organizacional",
    var_name="Empresa",
    value_name="Status"
)

# Gráfico
fig = px.line(
    dados_plot,
    x="Prática Organizacional",
    y="Status",
    color="Empresa",
    markers=True,
    title="Governança e Capacitação em Segurança"
)

# Estilo
fig.update_traces(line_width=4, marker_size=10)

# Eixo Y personalizado
fig.update_yaxes(
    tickvals=[0,1,2,3,4],
    ticktext=[
        "❌ Não Implementado",
        "✅ Implementado",
        "🔴 Baixa Conscientização",
        "🟡 Média Conscientização",
        "🟢 Alta Conscientização"
    ],
    range=[-0.5,4.5]
)

fig.update_layout(
    xaxis_tickangle=-25,
    legend_title="Empresas"
)

st.plotly_chart(fig, use_container_width=True)

##Armazenamento de Dados

st.title("Armazenamento e Proteção de Dados")

# Dados
dados = pd.DataFrame({
    "Aspecto": [
        "Armazenamento em computador local",
        "Uso de nuvem",
        "Uso de servidor dedicado",
        "Rotina de backup",
        "Histórico de perda de dados"
    ],
    "Empresa A": ["Sim","Não","Não","Não","Sim"],
    "Empresa B": ["Sim","Não","Não","Não","Não"]
})

# Converter Sim/Não
dados_num = dados.replace({"Sim":1, "Não":0})

# Formato para gráfico
dados_plot = dados_num.melt(
    id_vars="Aspecto",
    var_name="Empresa",
    value_name="Status"
)

# Criar gráfico
fig = px.line(
    dados_plot,
    x="Aspecto",
    y="Status",
    color="Empresa",
    markers=True,
    title="Armazenamento e Segurança dos Dados"
)

# Estilo visual
fig.update_traces(
    line_width=4,
    marker_size=10
)

# Eixo Y personalizado
fig.update_yaxes(
    tickvals=[0,1],
    ticktext=["❌ Não Implementado", "✅ Implementado"],
    range=[-0.1,1.1]
)

fig.update_layout(
    xaxis_tickangle=-25,
    legend_title="Empresas"
)

# Mostrar no Streamlit
st.plotly_chart(fig, use_container_width=True)