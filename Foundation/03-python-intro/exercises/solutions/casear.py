def casear(text,key,encrypt=True):

    if not encrypt:
        key = -key
    
    char2num = {k:i for i,k in enumerate(string.ascii_lowercase)}
    num2char = {k:i for k,i in enumerate(string.ascii_lowercase)}
    CHAR2NUM = {k:i for i,k in enumerate(string.ascii_uppercase)}
    NUM2CHAR = {k:i for k,i in enumerate(string.ascii_uppercase)}
    
    result = []
    
    for char in text:
        if char.isupper():
            result.append(NUM2CHAR[(CHAR2NUM[char] + key) % 26]) 
        elif char.islower():
            result.append(num2char[(char2num[char] + key) % 26]) 
        else:
            result.append(char)
    
    return "".join(result)

