def main():
    frankenstein_path = "books/frankenstein.txt"
    print_book_report_from_path(frankenstein_path)


def print_book_report_from_path(path):
    print(f"--- Begin report of {path} ---")
    
    text = get_book_text(path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document\n")

    char_counts = get_char_counts(text)
    alpha_char_counts_sorted = sort_alpha_char_counts(char_counts)
    for char_counts in alpha_char_counts_sorted:
        print(f"The \'{char_counts['char']}\' character was found {char_counts['count']} times")

    print("--- End report ---")


def sort_alpha_char_counts(counts: dict) -> list:
    counts_list = [{"char": char, "count": count} for char, count in counts.items() if char.isalpha()]
    counts_list.sort(reverse=True, key=lambda char_counts: char_counts["count"])
    return counts_list


def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        char_counts.setdefault(char, 0)
        char_counts[char] += 1
    return char_counts


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
