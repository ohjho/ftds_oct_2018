with open("data/PrisonerOfAzkaban.txt","r") as f:
    text = f.read()

with open("data/PrisonerOfAzkabanCopy.txt","w") as f:
    f.write(text)