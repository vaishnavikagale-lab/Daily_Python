# Q1. Write a program to read a file and count how number vowels are present in its content.

with open("data.txt", "r") as f:
    content = f.read()

count = 0
for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count) 
