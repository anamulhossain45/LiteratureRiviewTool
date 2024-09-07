import requests
from bs4 import BeautifulSoup

def scrape_articles(query, num_articles=10):
    # Construct the search URL for PubMed (or another database)
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty list to store articles
    articles = []

    # Loop to extract article titles and abstracts
    for item in soup.select('.docsum-content'):
        title = item.select_one('.docsum-title').get_text(strip=True)
        abstract = item.select_one('.full-view-snippet').get_text(strip=True)
        articles.append({'title': title, 'abstract': abstract})

        # Stop if the desired number of articles is reached
        if len(articles) >= num_articles:
            break

    return articles

if __name__ == "__main__":
    # Test the scraper with a query
    query = "COVID-19"
    articles = scrape_articles(query)
    for article in articles:
        print(article)
