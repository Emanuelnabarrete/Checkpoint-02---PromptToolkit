from src.prompt_builder import build_prompt, add_examples, add_cot_steps


def zero_shot(task, text):
    prompt = build_prompt(
        task["instruction"],
        text,
        task["output_format"]
    )

    return "", prompt


def few_shot(task, text):
    prompt = build_prompt(
        task["instruction"],
        text,
        task["output_format"]
    )

    prompt = add_examples(
        prompt,
        task["few_shot_examples"]
    )

    return "", prompt


def chain_of_thought(task, text):
    prompt = build_prompt(
        task["instruction"],
        text,
        task["output_format"]
    )

    prompt = add_cot_steps(
        prompt,
        task["cot_steps"]
    )

    return "", prompt


def role_prompting(task, text, persona):
    prompt = build_prompt(
        task["instruction"],
        text,
        task["output_format"]
    )

    return persona, prompt