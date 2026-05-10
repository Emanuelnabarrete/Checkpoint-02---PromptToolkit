def montar_prompt(instrucao, input_dados, formato_output):

    prompt = f"""
Instrucao:
{instrucao}

Texto:
{input_dados}

Formato:
{formato_output}
"""

    return prompt


def adicionar_exemplos(prompt, exemplos):

    texto_exemplos = "\nEXEMPLOS:\n"

    for exemplo in exemplos:

        texto_exemplos += f"""
Input: {exemplo['input']}
Output: {exemplo['output']}
"""

    return texto_exemplos + prompt


def adicionar_cot(prompt, passos):

    texto = "\nAnalise passo a passo:\n"

    for passo in passos:
        texto += f"- {passo}\n"

    return texto + prompt