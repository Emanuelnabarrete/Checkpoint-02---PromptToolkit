import json

from src.tasks import tarefas
from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought
)

from src.llm_client import LLMClient
from src.evaluator import medir_acuracia
from src.report import gerar_tabela, grafico_acuracia

client = LLMClient()

with open("data/inputs.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

resultados = []

for tarefa in tarefas:

    nome = tarefa["nome"]

    inputs = dados[nome]

    for item in inputs:

        texto = item["input"]

        esperado = item["esperado"]

        tecnicas = {
            "zero_shot": zero_shot(tarefa, texto),
            "few_shot": few_shot(tarefa, texto),
            "cot": chain_of_thought(tarefa, texto)
        }

        for nome_tecnica, prompt in tecnicas.items():

            resposta = client.chat(prompt)

            acuracia = medir_acuracia(
                resposta["resposta"],
                esperado
            )

            resultados.append({
                "tarefa": nome,
                "tecnica": nome_tecnica,
                "resposta": resposta["resposta"],
                "esperado": esperado,
                "acuracia": acuracia,
                "tempo_ms": resposta["tempo_ms"]
            })

df = gerar_tabela(resultados)

grafico_acuracia(df)

print(df)
