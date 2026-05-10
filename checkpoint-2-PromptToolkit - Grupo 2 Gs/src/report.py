import pandas as pd
import matplotlib.pyplot as plt


def gerar_tabela(resultados):

    df = pd.DataFrame(resultados)

    df.to_csv("output/resultados.csv", index=False)

    return df


def grafico_acuracia(df):

    media = df.groupby("tecnica")["acuracia"].mean()

    media.plot(kind="bar")

    plt.title("Acuracia por tecnica")

    plt.savefig("output/graficos/acuracia.png")

    plt.close()