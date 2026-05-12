import os
import pandas as pd
import matplotlib.pyplot as plt


def prepare_output_folders():
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/charts", exist_ok=True)


def generate_table(results, filename="output/results.csv"):
    prepare_output_folders()

    df = pd.DataFrame(results)

    df.to_csv(
        filename,
        index=False,
        encoding="utf-8"
    )

    return df


def chart_accuracy(df):
    data = df.groupby("technique")["accuracy"].mean()

    data.plot(kind="bar")

    plt.title("Average Accuracy by Technique")
    plt.xlabel("Technique")
    plt.ylabel("Accuracy")
    plt.tight_layout()

    plt.savefig("output/charts/accuracy.png")

    plt.close()


def chart_tokens(df):
    data = df.groupby("technique")["total_tokens"].mean()

    data.plot(kind="bar")

    plt.title("Average Tokens by Technique")
    plt.xlabel("Technique")
    plt.ylabel("Tokens")
    plt.tight_layout()

    plt.savefig("output/charts/tokens.png")

    plt.close()


def chart_time(df):
    data = df.groupby("technique")["time_ms"].mean()

    data.plot(kind="bar")

    plt.title("Average Response Time by Technique")
    plt.xlabel("Technique")
    plt.ylabel("Time in ms")
    plt.tight_layout()

    plt.savefig("output/charts/time.png")

    plt.close()


def chart_temperature(df_temperature):
    data = df_temperature.groupby("temperature")["consistency"].mean()

    data.plot(kind="bar")

    plt.title("Consistency by Temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Consistency")
    plt.tight_layout()

    plt.savefig("output/charts/temperature.png")

    plt.close()


def recommend_best_technique(df):
    summary = df.groupby("technique").agg({
        "accuracy": "mean",
        "total_tokens": "mean",
        "time_ms": "mean"
    }).reset_index()

    summary = summary.sort_values(
        by=["accuracy", "total_tokens", "time_ms"],
        ascending=[False, True, True]
    )

    best = summary.iloc[0]

    recommendation = f"""
Best overall technique: {best["technique"]}

Reason:
This technique achieved an average accuracy of {best["accuracy"]:.2f},
used an average of {best["total_tokens"]:.2f} tokens,
and had an average response time of {best["time_ms"]:.2f} ms.
"""

    with open("output/recommendation.txt", "w", encoding="utf-8") as file:
        file.write(recommendation)

    return recommendation