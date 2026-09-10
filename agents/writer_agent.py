from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def writer_agent(state: dict) -> dict:
    print("\n✍️  Writer Agent: Writing the research report...")

    response = llm.invoke([
        HumanMessage(content=f"""
        You are an AI Research Writer. Write a clean daily research brief.

        Use this information:
        Research: {state["research"]}
        Analysis: {state["analysis"]}

        Format it exactly like this:

        # AI Research Brief

        ## Top Trends Today
        (3 bullet points)

        ## Most Important Breakthrough
        (2-3 sentences)

        ## What Engineers Should Know
        (practical takeaways, bullet points)

        ## Papers Worth Reading
        (list with one line description each)

        ## News Roundup
        (quick bullets)

        Keep it tight. Engineers are busy.
        """)
    ])

    state["report"] = response.content
    print("✅ Writer Agent done")
    return state
