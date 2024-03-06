# Reads number of lines from each file and returns total number of lines and program written with current date in lineswritten.txt file.
from datetime import date
import textwrap

# Gets current date and stores it in today variable
today = date.today()

# Gets material covered from user
materialCovered = input("Material Covered: ")
print()

# Gets daily reflection from user
feelingDaily = input("How are you feeling today: ")
print()

# Gets number of programs written today 
programs = int(input("Number of programs written today: "))

# Loops through each program file and reads total number of lines from each file, keeping track of the sum in a total variable
total = 0
for _ in range(programs):
    filename = input("File Name: ")
    with open(filename) as filename:
        total += len(filename.readlines())

# Wraps text after 100 characters 
myWrap = textwrap.TextWrapper(width = 100)

# Opens journal.txt and appends the data from the user to the file according the formatting rules.  
with open("journal.txt", "a") as totalLines:
    totalLines.write(f"Today is {today}\n\n")
    totalLines.write(myWrap.fill(f"Material Covered: {materialCovered}"))
    totalLines.write("\n\n")
    totalLines.write(myWrap.fill(f"How I'm Feeling: {feelingDaily}\n\n"))
    totalLines.write(f"Lines/Program(s) Written: {total} lines and {programs} program(s)\n\n")
    totalLines.write("------------------\n\n")

print()
print("Entry Saved to journal.txt")
print()
