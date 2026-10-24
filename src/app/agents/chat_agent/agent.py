from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from app.core.config import settings
from app.agents.chat_agent.prompts import instruction, description

root_agent = Agent(
    name=settings.app_name,
    model=LiteLlm(model=settings.ollama_model),
    description=description,
    instruction=instruction,
)