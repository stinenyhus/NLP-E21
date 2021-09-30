from collections import Counter

def term_frequency(tokens) -> dict:
    token_count = Counter(tokens)
    return {token:count/len(tokens) for token, count in token_count.items()}

# def doc_frequency(docs) -> dict:
#     all_tokens = []
#     for lst in docs:
#         all_tokens += lst
#     return dict(Counter(all_tokens))

def doc_frequency(docs) -> dict:
    terms = set()
    for lst in docs:
        terms = set.union(terms, set(lst))
    count = {term:0 for term in terms}
    for lst in docs:
        for term in terms:
            if term in lst:
                count[term] += 1
    return count


if __name__ == "__main__":
    list_of_lists = [["sa", "dd", "sa", "fgj"], ["ffg", "sa"], ["sa", "dd"]]
    list_of_tokens = ["sa", "dd", "fgj", "ffg", "sa", "sa", "dd"]
    # print(term_frequency(list_of_tokens))
    # print(doc_frequency(list_of_lists))
    print(doc_frequency(list_of_lists))

