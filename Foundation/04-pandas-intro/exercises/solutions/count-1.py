def count_chars(text):
    
    l = list(text)
    d = {}
    for char in l:
        if char not in d:
            d[char] = 1
        else:
            d[char] +=1
    return d
    

def count_words(text):
    
    l = text.split()
    d = {}
    for word in l:
        if word not in d:
            d[word] = 1
        else:
            d[word] +=1
            
    return d
    

word_freqs = count_words(text)
n_words = sum(word_freqs.values())
print("Number of Words: ",n_words)
char_freqs = count_chars(text)
n_sents = char_freqs['.']
print("Number of Sentences: ",n_sents)