# 01 — LLM Basics & API Usage

## What I learned

### Project setup
- **Virtual environment (`venv`)**: an isolated Python environment per project, so package versions don't conflict.
  - Create: `python -m venv venv`
  - Activate (Git Bash): `source venv/Scripts/activate` · (CMD): `venv\Scripts\activate`
- **`requirements.txt`**: lists the packages the project needs. Install with `pip install -r requirements.txt`.
- **`.gitignore`**: files Git should never track — `.env`, `venv/`, `__pycache__/`, `.idea/`.

### API keys
- An API key is a secret token that lets my code call an LLM provider (Anthropic, OpenAI, Google).
- Usage is billed per token, so a leaked key can cost real money.
- I created a Claude API key in the Claude Console and a LangSmith key for tracing.

### Environment variables with `python-dotenv`
- Real keys and settings (e.g. `IS_DEBUG=True`) go in a `.env` file, which is git-ignored.
- `.env.example` shows which variables are needed, without real values.
- `load_dotenv()` loads `.env` into environment variables → read with `os.getenv("NAME")`.
  LangChain reads keys like `ANTHROPIC_API_KEY` from the environment automatically.
- `dotenv_values(".env")` returns the values as a dict without changing the environment.
- Mistake I made: `load_dotenv()` takes a **file path**, not a key value.

### LangSmith
- LangSmith traces every LLM call: input, output, latency and token usage.
- Tracing is enabled with `LANGSMITH_TRACING=true` in `.env`.

### Python basics
- `if __name__ == "__main__":` runs code only when the file is executed directly, not when it's imported.

## Code
- `hello_claude.py` — first call to Claude (Haiku) through LangChain's `ChatAnthropic`.

## My experiment
- `model_params.py`: compared `temperature=0.0` vs `1.0`. At 0.0 the answers were almost identical; at 1.0 every answer was different. `max_tokens` limits answer length.