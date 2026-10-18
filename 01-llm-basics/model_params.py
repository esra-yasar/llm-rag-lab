"""Experiment: how temperature and max_tokens change Claude's answers."""
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

prompt = "Give me a creative name for a coffee shop run by robots."

for temperature in [0.0, 1.0]:
    llm = ChatAnthropic(model="claude-haiku-5-5", temperature=temperature, max_tokens=50)
    print(f"\n--- temperature={temperature} ---")
    for _ in range(3):
        print(llm.invoke(prompt).content)