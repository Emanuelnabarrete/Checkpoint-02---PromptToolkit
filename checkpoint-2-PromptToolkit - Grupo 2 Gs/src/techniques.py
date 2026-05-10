from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)


def zero_shot(tarefa, texto):

    return montar_prompt(
        tarefa["instrucao"],
        texto,
        tarefa["formato_output"]
    )


def few_shot(tarefa, texto):

    prompt = montar_prompt(
        tarefa["instrucao"],
        texto,
        tarefa["formato_output"]
    )

    return adicionar_exemplos(
        prompt,
        tarefa["exemplos_fewshot"]
    )


def chain_of_thought(tarefa, texto):

    prompt = montar_prompt(
        tarefa["instrucao"],
        texto,
        tarefa["formato_output"]
    )

    return adicionar_cot(
        prompt,
        tarefa["passos_cot"]
    )


def role_prompting(tarefa, texto, persona):

    prompt = montar_prompt(
        tarefa["instrucao"],
        texto,
        tarefa["formato_output"]
    )

    return persona, prompt