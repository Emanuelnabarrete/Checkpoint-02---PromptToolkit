import json

from src.tasks import tasks
from src.llm_client import LLMClient

from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)

from src.evaluator import (
    count_tokens,
    measure_accuracy,
    measure_consistency
)

from src.report import (
    generate_table,
    chart_accuracy,
    chart_tokens,
    chart_time,
    chart_temperature,
    recommend_best_technique
)


client = LLMClient()


with open("data/inputs.json", "r", encoding="utf-8") as file:
    input_data = json.load(file)


with open("prompts/system_prompts.json", "r", encoding="utf-8") as file:
    personas = json.load(file)


results = []
temperature_results = []


for task in tasks:
    task_name = task["name"]
    task_inputs = input_data[task_name]

    for item in task_inputs:
        text = item["input"]
        expected = item["expected"]

        persona = personas[task["persona"]]

        techniques = {
            "zero_shot": zero_shot(task, text),
            "few_shot": few_shot(task, text),
            "chain_of_thought": chain_of_thought(task, text),
            "role_prompting": role_prompting(task, text, persona)
        }

        for technique_name, technique_content in techniques.items():
            system_prompt, user_prompt = technique_content

            response = client.chat(
                prompt=user_prompt,
                system=system_prompt,
                temperature=0.5,
                max_tokens=20
            )

            answer = response["answer"]

            prompt_tokens = count_tokens(user_prompt)
            answer_tokens = count_tokens(answer)
            total_tokens = prompt_tokens + answer_tokens

            accuracy = measure_accuracy(
                answer,
                expected
            )

            results.append({
                "task": task_name,
                "technique": technique_name,
                "input": text,
                "expected": expected,
                "answer": answer,
                "accuracy": accuracy,
                "prompt_tokens": prompt_tokens,
                "answer_tokens": answer_tokens,
                "total_tokens": total_tokens,
                "time_ms": response["time_ms"]
            })


first_task = tasks[0]
first_input = input_data[first_task["name"]][0]["input"]
first_persona = personas[first_task["persona"]]

system_prompt, user_prompt = role_prompting(
    first_task,
    first_input,
    first_persona
)


for temperature in [0.1, 0.5, 1.0]:
    answers = []

    for _ in range(3):
        response = client.chat(
            prompt=user_prompt,
            system=system_prompt,
            temperature=temperature,
            max_tokens=20
        )

        answers.append(response["answer"])

    consistency = measure_consistency(answers)

    temperature_results.append({
        "temperature": temperature,
        "consistency": consistency,
        "answers": answers
    })


df_results = generate_table(
    results,
    filename="output/results.csv"
)

chart_accuracy(df_results)
chart_tokens(df_results)
chart_time(df_results)

df_temperature = generate_table(
    temperature_results,
    filename="output/temperature.csv"
)

chart_temperature(df_temperature)

recommendation = recommend_best_technique(df_results)

print(df_results)
print(recommendation)