# Reads number of lines from each file and returns total number of lines and program written with current date in lineswritten.txt file.
from datetime import date
today = date.today()

# Gets material covered from user
materialCovered = input("Material Covered: ")
print()

# Gets daily feeling from user
feelingDaily = input("How are you feeling today: ")
print()

# Loops through files and reads number of lines from each program and holds in total variable.
programs = int(input("Number of programs written today: "))
total = 0
for _ in range(programs):
    filename = input("File Name: ")
    with open(filename) as filename:
        total += len(filename.readlines())

# Opens journal.txt and writes input into the file with current date stamp
myWrap = 
with open("journal.txt", "a") as totalLines:
    totalLines.write(f"Today is {today}\n\n")
    totalLines.write(f"Material Covered: {materialCovered}\n\n")
    totalLines.write(f"How I'm Feeling: {feelingDaily}\n\n")
    totalLines.write(f"Lines/Program(s) Written: {total} lines and {programs} program(s)\n\n")

print("\n")
print("Entry Saved to journal.txt")
