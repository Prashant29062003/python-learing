# yield keyword

def evenGenerator(n):
    i = 0
    while i<=n:
        if i%2 == 0:
            yield i
        i += 1

for i in evenGenerator(10):
    print(i)


# string operation
def find_super(words):
    for word in words:
        if word == "super":
            yield word

text = "super heros do the super things, and they do the super stuff.".split()
print("Count: ", sum(1 for _ in find_super(text)))
