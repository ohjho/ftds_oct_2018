def encrypt(text,key):
    
    char2num = {k:i for i,k in enumerate(string.ascii_lowercase)}
    num2char = {k:i for k,i in enumerate(string.ascii_lowercase)}
    return "".join([ num2char[(char2num[c] + key) % 26 ] if c.isalpha() else c  for c in text])