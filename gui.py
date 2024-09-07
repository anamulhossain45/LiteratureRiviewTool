import tkinter as tk
from tkinter import scrolledtext, messagebox
from scraper import scrape_articles
from summarizer import summarize_text
import pandas as pd

# Create the main application window
class LiteratureReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Literature Review Tool")

        # Search query label and entry
        tk.Label(root, text="Enter search query:").pack(pady=5)
        self.query_entry = tk.Entry(root, width=40)
        self.query_entry.pack(pady=5)

        # Search button
        tk.Button(root, text="Search and Summarize", command=self.search_and_summarize).pack(pady=10)

        # Scrolled text area to display results
        self.result_text = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
        self.result_text.pack(pady=10)

    def search_and_summarize(self):
        # Get the search query from the user
        query = self.query_entry.get()

        if not query:
            messagebox.showerror("Input Error", "Please enter a search query.")
            return

        # Scrape articles based on user query
        articles = scrape_articles(query)
        if not articles:
            messagebox.showerror("No Results", "No articles found. Try a different query.")
            return

        # Summarize each article's abstract
        for article in articles:
            article['summary'] = summarize_text(article['abstract'])

        # Save results to a CSV file
        df = pd.DataFrame(articles)
        df.to_csv('articles_summary.csv', index=False)

        # Display the results in the text area
        self.result_text.delete(1.0, tk.END)  # Clear previous content
        for article in articles:
            self.result_text.insert(tk.END, f"Title: {article['title']}\n")
            self.result_text.insert(tk.END, f"Abstract: {article['abstract']}\n")
            self.result_text.insert(tk.END, f"Summary: {article['summary']}\n")
            self.result_text.insert(tk.END, "-" * 50 + "\n")

        messagebox.showinfo("Success", "Results saved to articles_summary.csv")

if __name__ == "__main__":
    # Initialize the Tkinter window
    root = tk.Tk()
    app = LiteratureReviewApp(root)
    root.mainloop()
