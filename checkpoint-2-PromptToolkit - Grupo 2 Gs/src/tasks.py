tasks = [
    {
        "name": "sentiment_classification",

        "instruction":
        "Classify the sentiment of the customer message.",

        "output_format":
        "Answer only with: POSITIVE, NEGATIVE or NEUTRAL.",

        "few_shot_examples": [
            {
                "input": "Amazing product",
                "output": "POSITIVE"
            },
            {
                "input": "Terrible service",
                "output": "NEGATIVE"
            },
            {
                "input": "Average experience",
                "output": "NEUTRAL"
            }
        ],

        "cot_steps": [
            "Identify positive words.",
            "Identify negative words.",
            "Check if the text is neutral.",
            "Choose only one final classification."
        ],

        "persona": "customer_expert"
    },

    {
        "name": "urgency_classification",

        "instruction":
        "Classify the urgency level of the customer message.",

        "output_format":
        "Answer only with: HIGH, MEDIUM or LOW.",

        "few_shot_examples": [
            {
                "input": "I need this fixed today",
                "output": "HIGH"
            },
            {
                "input": "Can you check this later?",
                "output": "MEDIUM"
            },
            {
                "input": "Just a quick question",
                "output": "LOW"
            }
        ],

        "cot_steps": [
            "Check if there is a critical deadline.",
            "Evaluate customer impact.",
            "Choose the urgency level."
        ],

        "persona": "customer_expert"
    }
]