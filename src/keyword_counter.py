from collections import Counter
import re
import sys

STOP_WORDS = {
    "the", "and", "a", "an", "is", "it", "to", "of", "in", "that",
    "this", "for", "on", "with", "as", "was", "are", "at", "by",
    "be", "from", "or", "not", "but", "have", "has", "had", "you",
    "i", "he", "she", "they", "we", "them", "his", "her", "our",
    "your", "their", "if", "then", "so", "than", "too", "can",
    "will", "just", "about", "into", "up", "down", "out", "over",
    "again", "very", "experience", "re", "work", "working", "high",
    "role", "help", "looking", "who"
}


def remove_emojis(text: str) -> str:
    """
    Removes emojis and other non-text unicode symbols.
    """
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub("", text)


def get_most_common_words(file_name: str, top_n: int=20) -> list[tuple[str, int]]:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    text = remove_emojis(text)

    text = text.lower()

    words = re.findall(r"\b[a-z]+\b", text)
    filtered_words = [
        w for w in words
        if w not in STOP_WORDS
    ]

    word_counts = Counter(filtered_words)
    return word_counts.most_common(top_n)


def main():
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    results = get_most_common_words(file_path)

    print("\nMost Common Words:\n")
    for word, _ in results:
        print(word)


if __name__ == "__main__":
    main()