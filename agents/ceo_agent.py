from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def ceo_agent(state: dict) -> dict:
    print("\n🏢 CEO Agent: Deciding today's research topics...")

    response = llm.invoke([
        HumanMessage(content="""
        You are the CEO of an AI Research Company.
        Your job is to decide the top 3 AI topics to research today.

        Focus on:
        - Latest breakthroughs in AI and LLMs
        - Trending tools and frameworks engineers are using
        - Important AI research that affects the industry

        Return ONLY the 3 topics, one per line, no numbering, no intro text, no explanation.
        Example output:
        large language model reasoning
        AI agents memory systems
        vector database optimization
        """)
    ])

    state["topics"] = response.content
    print(f"✅ CEO decided topics:\n{response.content}")
    return state
