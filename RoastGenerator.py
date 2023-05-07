import random

name = input('Hey who are you?\n')
start = "you look like you don't know "
ends = ["how to tie your shoes.", 
        "your abc's", 
        "your mama's first name."]
roast = name + ", " + start + random.choice(ends)

print(roast)
