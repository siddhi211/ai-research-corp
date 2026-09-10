import urllib.request
import xml.etree.ElementTree as ET

# RSS feeds from top AI news sources — no API key needed, completely free
RSS_FEEDS = {
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "MIT Tech Review": "https://www.technologyreview.com/feed/",
}

def fetch_ai_news(max_per_source: int = 3):
    print("📰 Fetching latest AI news from RSS feeds...")

    all_news = []

    for source, url in RSS_FEEDS.items():
        try:
            # This is the actual API call — fetching the RSS feed from each news site
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            response = urllib.request.urlopen(req, timeout=10)
            xml_data = response.read()

            # Parse the RSS XML
            root = ET.fromstring(xml_data)
            channel = root.find("channel")
            items = channel.findall("item")[:max_per_source]

            for item in items:
                title = item.findtext("title", "No title")
                description = item.findtext("description", "")
                link = item.findtext("link", "")

                # Clean HTML tags from description
                import re
                description = re.sub(r"<[^>]+>", "", description)[:300]

                all_news.append({
                    "source": source,
                    "title": title,
                    "description": description,
                    "url": link
                })
                print(f"   [{source}] {title}")

        except Exception as e:
            print(f"   ⚠️ Could not fetch from {source}: {e}")

    print(f"✅ Fetched {len(all_news)} news articles")
    return all_news
