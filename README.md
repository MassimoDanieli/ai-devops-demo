# AI DevOps Demo

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/MassimoDanieli/ai-devops-demo/ci.yml?branch=main)](https://github.com/MassimoDanieli/ai-devops-demo/actions)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![OpenAI Powered](https://img.shields.io/badge/GPT-4-enabled-blueviolet)](https://platform.openai.com/)

> ⚙️ Analyze your GitHub Actions CI pipeline using GPT-4 and generate test suggestions + HTML report.

## 🚀 Usage

```bash
# Create and activate virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install openai pyyaml

# Export your OpenAI API key
export OPENAI_API_KEY=sk-...

# Run the analysis and generate report
python generate_tests.py
python report_generator.py
```

## 📁 Files

- `ci.yml`: example GitHub Actions workflow
- `analyze_ci.py`: pipeline analyzer using GPT
- `generate_tests.py`: test suggestion with GPT
- `report_generator.py`: HTML report from test output

---

**Made with ❤️ by Massimo Danieli**
