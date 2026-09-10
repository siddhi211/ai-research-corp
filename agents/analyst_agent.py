from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def analyst_agent(state: dict) -> dict:
    print("\n📊 Analyst Agent: Finding patterns and trends...")

    response = llm.invoke([
        HumanMessage(content=f"""
        You are a Senior AI Research Analyst.
        Analyze the research below and extract:

        1. Top 3 trends emerging today
        2. The single most important breakthrough
        3. What this means practically for engineers

        Research:
        {state["research"]}

        Be direct and opinionated. Engineers want insights, not summaries.
        """)
    ])

    state["analysis"] = response.content
    print("✅ Analyst Agent done")
    return state
