import os
import yaml
from openai import OpenAI

def load_ci_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def generate_tests(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior DevOps engineer. Suggest relevant automated tests based on the CI pipeline."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    config = load_ci_config("ci.yml")
    prompt = f"Suggest automated tests for this CI/CD pipeline:\n{config}"
    tests = generate_tests(prompt)
    with open("suggested_tests.txt", "w") as f:
        f.write(tests)
    print("✅ Suggested tests written to suggested_tests.txt")

