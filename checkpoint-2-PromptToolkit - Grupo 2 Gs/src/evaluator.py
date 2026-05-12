import tiktoken


def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))


def clean_answer(answer):
    return (
        answer
        .strip()
        .upper()
        .replace(".", "")
        .replace(",", "")
        .replace(":", "")
    )


def measure_accuracy(answer, expected):
    cleaned_answer = clean_answer(answer)
    cleaned_expected = clean_answer(expected)

    if cleaned_answer == cleaned_expected:
        return 1

    if cleaned_expected in cleaned_answer:
        return 1

    return 0


def measure_consistency(answers):
    cleaned_answers = [clean_answer(answer) for answer in answers]

    most_common = max(
        set(cleaned_answers),
        key=cleaned_answers.count
    )

    return cleaned_answers.count(most_common) / len(cleaned_answers)