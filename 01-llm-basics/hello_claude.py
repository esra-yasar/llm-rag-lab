"""First API call: verify that the Claude API key and LangSmith tracing work."""
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-5-5")
response = llm.invoke("Hello! Introduce yourself in one sentence.")
print(response.content)