def count_words(text_to_count):
    count = len(text_to_count.split())
    return count

def count_letters(text_to_count):
    letter_dict = dict()
    text = text_to_count.lower()
    for letter in text:
        # remove debugging
        if letter in letter_dict:
            letter_dict[letter] += 1
            # print debugging
            #print("Incremented existing")
        else:
            letter_dict.update({letter: 1})
            # print debugging
            #print("Added new")
        # print debugging
        #print(letter_dict)
    return letter_dict

