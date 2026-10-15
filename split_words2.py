# Q4. Read a file,split its content into words and store them in a list.
    # i.Print the total number of words
    # ii.Print all unique words


with open("list.txt", "r") as f:
    content = f.read()

words = content.split()

print("Total number of words:", len(words))
print("Unique words:", set(words))