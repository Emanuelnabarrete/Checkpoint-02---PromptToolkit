tarefas = [

    {
        "nome": "classificacao_sentimento",

        "instrucao": "Classifique o sentimento.",

        "formato_output": "POSITIVO, NEGATIVO ou NEUTRO",

        "exemplos_fewshot": [
            {
                "input": "Muito bom",
                "output": "POSITIVO"
            },
            {
                "input": "Muito ruim",
                "output": "NEGATIVO"
            }
        ],

        "passos_cot": [
            "Analise o texto",
            "Veja palavras positivas",
            "Veja palavras negativas",
            "Classifique"
        ],

        "persona": "analista_cx"
    }

]