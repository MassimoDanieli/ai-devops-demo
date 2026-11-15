> [!WARNING]
> **Progetto archiviato (novembre 2026).** Questo prototipo del 2025 chiamava `gpt-4`, che OpenAI ha spento il 23 ottobre 2026: non funziona più.
> Le sue funzioni ora vivono in **[ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit)**: review del diff della PR e proposte di test (`aikit review`, `aikit testgen`), con qualsiasi fornitore (Anthropic, OpenAI o un modello locale).
>
> *Archived (November 2026): this 2025 prototype called `gpt-4`, shut down by OpenAI on 23 October 2026. Its features live on in [ai-devops-starter-kit v2](https://github.com/MassimoDanieli/ai-devops-starter-kit) (`aikit review / aikit testgen`).*

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
