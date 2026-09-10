import arxiv  # pip install arxiv — this is the official ArXiv Python library

def fetch_arxiv_papers(topic: str, max_results: int = 5):
    print(f"📚 Fetching ArXiv papers on: {topic}")

    # This is the actual API call to ArXiv
    # arxiv.Search sends a request to https://arxiv.org/search/
    # and returns the latest papers matching the topic
    search = arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate  # get the newest papers first
    )

    papers = []

    # arxiv.Client().results() fetches the actual data from ArXiv servers
    client = arxiv.Client()
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "summary": result.summary[:500],  # first 500 chars of abstract
            "url": result.entry_id,           # link to the paper
            "published": str(result.published)
        })
        print(f"   Found: {result.title}")

    print(f"✅ Found {len(papers)} papers on '{topic}'")
    return papers
