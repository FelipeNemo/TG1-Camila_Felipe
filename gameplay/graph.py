
import pandas as pd
import ast
import plotly.express as px

# Leitura dos arquivos
df_pvp = pd.read_csv("../reports/relatorio_entre_dois.csv")
df_ffa = pd.read_csv("../reports/relatorio_free_for_all.csv")

def gerar_grafico_hp(df, titulo):
    historico_hp = []

    for i, row in df.iterrows():
        try:
            estado = ast.literal_eval(row['estado geral'])
            atacante = row.get('atacante')  # pode ser 'Saruman', por exemplo
            defensor = row.get('defensor')
            sucesso = row.get('sucesso')

            for personagem in estado:
                nome_base = personagem['nome']

                # Se esse personagem é o atacante da rodada, incluir info extra
                if nome_base == atacante:
                    nome = f"{nome_base} (atacou {defensor}, {'sucesso' if sucesso else 'falha'})"
                else:
                    nome = nome_base

                historico_hp.append({
                    'rodada': i,
                    'nome': nome,
                    'hp': personagem['hp']
                })
        except (ValueError, SyntaxError):
            print(f"Erro ao processar linha {i}")

    df_hp = pd.DataFrame(historico_hp)

    fig = px.line(
        df_hp,
        x='rodada',
        y='hp',
        color='nome',
        markers=True,
        title=titulo
    )
    fig.update_layout(xaxis=dict(range=[0, df_hp['rodada'].max() +1 ]))  # eixo X começa no 0
    fig.show()

# Gera gráficos
gerar_grafico_hp(df_ffa, "HP por Rodada - Free For All")
gerar_grafico_hp(df_pvp, "HP por Rodada - PvP")
