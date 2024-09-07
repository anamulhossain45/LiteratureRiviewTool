from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    # Use the LSA Summarizer from the sumy library
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    # Summarize to 3 sentences
    summary = summarizer(parser.document, 3)
    return " ".join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    # Example text to summarize
    example_text = "Enter a long medical abstract or text here for testing the summarization."
    print(summarize_text(example_text))
