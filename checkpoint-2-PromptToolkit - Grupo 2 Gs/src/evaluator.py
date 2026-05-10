import tiktoken


def contar_tokens(texto):

    encoding = tiktoken.get_encoding("cl100k_base")

    tokens = encoding.encode(texto)

    return len(tokens)


def medir_acuracia(resposta, esperado):

    resposta = resposta.strip().upper()

    esperado = esperado.strip().upper()

    if resposta == esperado:
        return 1

    return 0