from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def editor_agent(state: dict) -> dict:
    print("\n📝 Editor Agent: Reviewing and polishing report...")

    response = llm.invoke([
        HumanMessage(content=f"""
        You are a senior editor. Review this report and:
        - Fix any unclear sentences
        - Make it more concise where possible
        - Ensure technical accuracy
        - Keep the same format and structure
        - Do not add new information

        Report:
        {state["report"]}

        Return the improved report only, no commentary.
        """)
    ])

    state["final_report"] = response.content
    print("✅ Editor Agent done")
    return state
