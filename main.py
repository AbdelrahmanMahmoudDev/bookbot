def count_words(text):
    return len(text.split())

def sort_on(d):
    return d["count"]

def count_letters(text):
    dict = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
    val_list = []
    for ch in dict:
        val_list.append({"ch": ch, "count": dict[ch]})
        val_list.sort(reverse=True, key=sort_on)
    return val_list
    
def main():
    with open("books/frankenstein.txt") as file:
        contents = file.read()
    print(f"{count_words(contents)} words found in the document")
    val_list = count_letters(contents)
    for val in val_list:
        print(f"The '{val['ch']} character was found {val['count']} times'")
    print("--- End report ---")


main()