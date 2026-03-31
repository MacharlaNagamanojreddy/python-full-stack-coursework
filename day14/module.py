likes = 0

comments = []

def addlike():
    global likes
    likes +=1
    return likes

def comments(com):
    comments.append(com)
    return comments

print(addlike())