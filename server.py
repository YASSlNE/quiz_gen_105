from fastapi import Body, FastAPI
from httpx import AsyncClient, Timeout
from typing import Any
import random

app = FastAPI()

data_dict = {
    "Databases": r"""NoSQL, or "Not Only SQL," represents a paradigm shift in database management... (your content here)""",
    "Binary Search Trees": r"""A Binary Search Tree (BST) is a fundamental data structure in computer science... (your content here)""",
    "Electromagnetic Coupling": r"""In the domain of physics, electromagnetic coupling stands as a foundational concept... (your content here)""",
    "Introduction to Linear Algebra": r"""In the realm of linear algebra, vectors represent a fundamental and versatile concept... (your content here)""",
    "Real Time Operating System": r"""Real-Time Operating Systems (RTOS) play a pivotal role in embedded systems... (your content here)""",
}

@app.post("/generate_quizzes")
async def generate_quizzes():
    # Randomly select a key from the dictionary
    random_key = random.choice(list(data_dict.keys()))
    # Get the corresponding text
    text = data_dict[random_key]
    
    api_url = "https://dashboard.questgen.ai/api/generate-quizzes"
    request_body = {
        "text": text,
        "aiModelQuality": "High Quality (Slower)",
        "count": 10,
        "difficultylevel": "Medium",
        "mcqOptionsCount": 3,
        "type": "MCQ"
    }

    try:
        async with AsyncClient() as client:
            response = await client.post(api_url, json=request_body, timeout=Timeout(timeout=10.0))
        
        # Append the selected key to the response
        response_data = response.json()
        response_data["source_key"] = random_key
        return response_data
    except Exception as e:
        return {
    "ques_ans_pairs": [
        {
            "question": "What is the key characteristic of NoSQL databases?",
            "answers": [
                "Strict relational structure",
                "Schema flexibility",
                "Predefined data schemas",
                "Centralized data storage"
            ],
            "correct_choices": [
                "Schema flexibility"
            ]
        },
        {
            "question": "Which type of NoSQL database is most suitable for storing semi-structured data?",
            "answers": [
                "Wide-column stores",
                "Document-oriented",
                "Graph databases",
                "Key-value stores"
            ],
            "correct_choices": [
                "Document-oriented"
            ]
        },
        {
            "question": "Which type of NoSQL database organizes data as key-value pairs?",
            "answers": [
                "Key-value stores",
                "Wide-column stores",
                "Document-oriented databases",
                "Graph databases"
            ],
            "correct_choices": [
                "Key-value stores"
            ]
        },
        {
            "question": "What is a major advantage of NoSQL databases over traditional relational databases?",
            "answers": [
                "Strict data consistency",
                "Single-server deployment",
                "Predefined data schemas",
                "Horizontal scalability"
            ],
            "correct_choices": [
                "Horizontal scalability"
            ]
        },
        {
            "question": "Which use case could benefit from NoSQL databases?",
            "answers": [
                "Internal employee databases",
                "Real-time analytics",
                "Static website hosting",
                "Transaction processing systems"
            ],
            "correct_choices": [
                "Real-time analytics"
            ]
        },
        {
            "question": "What is a defining feature of NoSQL databases?",
            "answers": [
                "Strict data normalization",
                "Diverse and unstructured data types",
                "Centralized data storage",
                "Predetermined data models"
            ],
            "correct_choices": [
                "Diverse and unstructured data types"
            ]
        },
        {
            "question": "How do NoSQL databases address the need for rapid development and iteration?",
            "answers": [
                "Predefined data schemas",
                "Centralized data storage",
                "Strict relational structure",
                "Schema flexibility"
            ],
            "correct_choices": [
                "Schema flexibility"
            ]
        },
        {
            "question": "Which type of NoSQL database is specialized in representing and querying relationships between entities?",
            "answers": [
                "Graph databases",
                "Key-value stores",
                "Wide-column stores",
                "Document-oriented databases"
            ],
            "correct_choices": [
                "Graph databases"
            ]
        },
        {
            "question": "In which direction do many NoSQL systems scale to accommodate growing data volumes?",
            "answers": [
                "Diagonally",
                "Both horizontally and vertically",
                "Horizontally",
                "Vertically"
            ],
            "correct_choices": [
                "Horizontally"
            ]
        },
        {
            "question": "What is one common use case for NoSQL databases?",
            "answers": [
                "Local file storage",
                "Financial transaction systems",
                "Static website hosting",
                "Content management systems"
            ],
            "correct_choices": [
                "Content management systems"
            ]
        }
    ]
}
