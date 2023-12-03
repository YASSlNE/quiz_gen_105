# FastAPI Quiz Generator

This FastAPI application generates quizzes on various topics by utilizing the Questgen AI service. Each quiz is dynamically created from informative content related to different subjects. The generated quizzes consist of multiple-choice questions (MCQs) with a moderate difficulty level.

## Installation

To run this FastAPI application, make sure to install the required dependencies. You can use the following command:

```bash
pip install fastapi httpx
```

## Usage

1. Run the FastAPI application using the following command:

```bash
uvicorn your_file_name:app --reload
```

Replace `your_file_name` with the actual filename containing the FastAPI application.

2. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger documentation. You can use the provided endpoint `/generate_quizzes` to generate quizzes dynamically.

3. Click on the `/generate_quizzes` endpoint, and then click the "Try it out" button.

4. Execute the request to generate a set of quizzes based on randomly selected topics.

## Example

Here is an example response from the `/generate_quizzes` endpoint:

```json
{
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
        // ... (additional quiz questions)
    ],
    "source_key": "Databases"
}
```

## Topics Available for Quizzing

- **Databases**: NoSQL, or "Not Only SQL," represents a paradigm shift in database management...
- **Binary Search Trees**: A Binary Search Tree (BST) is a fundamental data structure in computer science...
- **Electromagnetic Coupling**: In the domain of physics, electromagnetic coupling stands as a foundational concept...
- **Introduction to Linear Algebra**: In the realm of linear algebra, vectors represent a fundamental and versatile concept...
- **Real Time Operating System**: Real-Time Operating Systems (RTOS) play a pivotal role in embedded systems...

Feel free to extend the `data_dict` with additional topics and content to diversify the quizzes.

## Note

Ensure that you have an active internet connection to interact with the Questgen AI service for quiz generation.

Happy quizzing!
