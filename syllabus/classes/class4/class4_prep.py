from collections import Counter

def term_frequency(tokens) -> dict:
    token_count = Counter(tokens)
    return {token:count/len(tokens) for token, count in token_count.items()}

def doc_frequency(docs) -> dict:
    all_tokens = []
    for lst in docs:
        all_tokens += lst
    return dict(Counter(all_tokens))


if __name__ == "__main__":
    list_of_lists = [["sa", "dd", "fgj"], ["ffg", "sa"], ["sa", "dd"]]
    list_of_tokens = ["sa", "dd", "fgj", "ffg", "sa", "sa", "dd"]
    print(term_frequency(list_of_tokens))
    print(doc_frequency(list_of_lists))

