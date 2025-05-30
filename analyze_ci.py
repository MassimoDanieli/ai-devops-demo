import os
import openai
import yaml

def load_ci_config(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def analyze_with_gpt(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a DevOps expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    config = load_ci_config("ci.yml")
    prompt = f"Analyze this CI/CD pipeline and suggest improvements:\n{config}"
    print(analyze_with_gpt(prompt))