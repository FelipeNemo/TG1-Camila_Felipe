import pandas as pd
import ast
import plotly.express as px

df_pvp = pd.read_csv("../reports/relatorio_entre_dois.csv")
df_pvp

df_ffa = pd.read_csv("../reports/relatorio_free_for_all.csv")
df_ffa

historico_hp = []

# Itera sobre o DataFrame original
for i, row in df_ffa.iterrows():
    try:
        estado = ast.literal_eval(row['estado geral'])  # Converte string -> lista de dicionários
        for personagem in estado:
            historico_hp.append({
                'rodada': i,
                'nome': personagem['nome'],
                'hp': personagem['hp']
            })
    except (ValueError, SyntaxError):
        print(f"Erro ao processar linha {i}")

# Cria DataFrame expandido
df_hp = pd.DataFrame(historico_hp)

# Gráfico
fig = px.line(df_hp, x='rodada', y='hp', color='nome', markers=True, title='HP por Rodada')
fig.show()
