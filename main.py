from langgraph.graph import StateGraph, END
from agents.ceo_agent import ceo_agent
from agents.research_agent import research_agent
from agents.analyst_agent import analyst_agent
from agents.writer_agent import writer_agent
from agents.editor_agent import editor_agent
from typing import TypedDict
from datetime import datetime

# Define the state that flows between all agents
class ResearchState(TypedDict):
    topics: str
    research: str
    analysis: str
    report: str
    final_report: str

# Build the graph — this is what creates the visual in LangGraph Studio
graph = StateGraph(ResearchState)

# Add each agent as a node
graph.add_node("ceo", ceo_agent)
graph.add_node("researcher", research_agent)
graph.add_node("analyst", analyst_agent)
graph.add_node("writer", writer_agent)
graph.add_node("editor", editor_agent)

# Connect the nodes — this defines the flow
graph.set_entry_point("ceo")
graph.add_edge("ceo", "researcher")
graph.add_edge("researcher", "analyst")
graph.add_edge("analyst", "writer")
graph.add_edge("writer", "editor")
graph.add_edge("editor", END)

# Compile the graph
# LangGraph Studio reads this 'app' variable to render the visual graph
app = graph.compile()

print("=" * 50)
print("🚀 AI Research Corp — Starting Daily Run")
print("=" * 50)

# Run the full pipeline
result = app.invoke({
    "topics": "",
    "research": "",
    "analysis": "",
    "report": "",
    "final_report": ""
})

# Save report to file with today's date
today = datetime.now().strftime("%Y-%m-%d")
filename = f"report_{today}.md"

with open(filename, "w") as f:
    f.write(result["final_report"])

print("\n" + "=" * 50)
print("📄 FINAL REPORT")
print("=" * 50)
print(result["final_report"])
print(f"\n✅ Report saved to {filename}")
