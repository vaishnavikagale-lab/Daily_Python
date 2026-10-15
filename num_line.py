# Q2. Read all lines from a file into a list.Print the total number of lines and display the 2nd and 4th line

with open("lines.txt", "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1].strip())

if len(lines) >= 4:
    print("4th line:", lines[3].strip())