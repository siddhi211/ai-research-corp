from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from tools.arxiv_tool import fetch_arxiv_papers
from tools.news_tool import fetch_ai_news
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def research_agent(state: dict) -> dict:
    print("\n🔬 Research Agent: Gathering papers and news...")

    topics = state["topics"].strip().split("\n")
    all_papers = []

    # Fetch ArXiv papers for each topic the CEO decided
    for topic in topics:
        topic = topic.strip()
        if topic:
            papers = fetch_arxiv_papers(topic, max_results=3)
            all_papers.extend(papers)

    # Fetch latest AI news from RSS feeds
    news = fetch_ai_news(max_per_source=3)

    # Ask Claude to summarize everything clearly
    response = llm.invoke([
        HumanMessage(content=f"""
        You are a Research Agent. Summarize the following findings clearly for engineers.

        ARXIV PAPERS:
        {all_papers}

        LATEST NEWS:
        {news}

        For each paper write:
        - Title
        - What it does in 2 sentences
        - Why it matters for engineers

        For news write:
        - Headline
        - Key point in 1 sentence

        Keep it concise and technical.
        """)
    ])

    state["research"] = response.content
    print("✅ Research Agent done")
    return state
