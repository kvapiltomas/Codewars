def to_jaden_case(string):
    words = string.split()
    words_capital = []

    for word in words:
        words_capital.append(word[0].title()+word[1:])
       
    sentence = ' '.join(words_capital)
    return sentence
