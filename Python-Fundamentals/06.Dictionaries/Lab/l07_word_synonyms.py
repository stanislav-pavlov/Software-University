term_count = int(input())
syn_dictionary = {}

for n in range(term_count):
    term = input()
    synonym = input()

    if term not in syn_dictionary:
        syn_dictionary[term] = list()

    syn_dictionary[term].append(synonym)

for term in syn_dictionary.keys():
    print(f"{term} - {', '.join(syn_dictionary[term])}")