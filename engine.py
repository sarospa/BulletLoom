def tokenize(filename):
    file = open(filename)
    data = file.read()
    file.close()
    
    token = ''
    for char in data:
        if isspace(char):
            if len(word) > 0:
                #handle conversion to token
        else if isalnum(char):
            token = token + char
        else
            #handle conversion to token
            