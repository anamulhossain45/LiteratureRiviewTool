from scraper import scrape_articles
from summarizer import summarize_text
import pandas as pd

def main():
    # Prompt user for a query
    query = input("Enter a search query for medical articles: ")

    # Scrape articles based on user query
    articles = scrape_articles(query)

    # Summarize each article's abstract
    for article in articles:
        article['summary'] = summarize_text(article['abstract'])

    # Save results to a CSV file
    df = pd.DataFrame(articles)
    df.to_csv('articles_summary.csv', index=False)

    print("Results saved to articles_summary.csv")

if __name__ == "__main__":
    main()
