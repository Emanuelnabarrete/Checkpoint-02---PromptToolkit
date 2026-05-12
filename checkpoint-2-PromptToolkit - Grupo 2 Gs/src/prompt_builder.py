def build_prompt(instruction, input_data, output_format):
    if not instruction or not input_data or not output_format:
        raise ValueError("Invalid prompt: missing required fields.")

    return f"""
INSTRUCTION:
{instruction}

CUSTOMER MESSAGE:
{input_data}

OUTPUT FORMAT:
{output_format}

IMPORTANT:
Answer only in the requested format.
"""


def add_examples(prompt, examples):
    examples_text = "\nEXAMPLES:\n"

    for example in examples:
        examples_text += f"Input: {example['input']}\n"
        examples_text += f"Output: {example['output']}\n\n"

    return examples_text + prompt


def add_cot_steps(prompt, steps):
    steps_text = "\nTHINK STEP BY STEP:\n"

    for index, step in enumerate(steps, start=1):
        steps_text += f"{index}. {step}\n"

    steps_text += "\nFinal answer must contain only the final label.\n"

    return steps_text + prompt