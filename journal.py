# Journal application that stores material covered, daily reflections, and number of programs and lines written in journal.txt. 
import datetime
import textwrap

def main():
    # Gets the current date and current day of the week.
    today_date = date.today()
    week_day = today_date.weekday()
    match week_day:
        case 0:
            week_day = "Monday"
        case 1:
            week_day = "Tuesday"
        case 2:
            week_day = "Wednesday"
        case 3:
            week_day = "Thursday"
        case 4:
            week_day = "Friday"
        case 5:
            week_day = "Saturday"
        case 6:
            week_day = "Sunday"

    # Gets material covered from user
    materialCovered = get_material()
    print()

    # Gets daily reflection from user
    feelingDaily = get_feeling()
    print()

    # Gets number of programs written today
    programs = get_programs()

    # Loops through each program file and reads total number of lines from each file, keeping track of the sum in a total variable
    total = 0
    for _ in range(programs):
        while True:
            filename = input("File Name: ")
            try:
                with open(filename) as filename:
                    total += len(filename.readlines())
            except FileNotFoundError:
                print("File not found")
                continue
            else:
                break

    # Wraps text after 100 characters
    myWrap = textwrap.TextWrapper(width = 100)

    # Opens journal.txt and appends the data from the user to the file according the formatting rules.
    with open("journal.txt", "a") as totalLines:
        totalLines.write(f"Today is {week_day} {today_date}\n\n")
        totalLines.write(myWrap.fill(f"Material Covered: {materialCovered}"))
        totalLines.write("\n\n")
        totalLines.write(myWrap.fill(f"How I'm Feeling: {feelingDaily}"))
        totalLines.write("\n\n")
        totalLines.write(f"Lines/Program(s) Written: {total} lines and {programs} program(s)\n\n")
        totalLines.write("------------------\n\n")

    print()
    print("Entry Saved to journal.txt")
    print()

def get_material() -> str:
    while True:
        materialCovered = input("Material Covered: ")
        if len(materialCovered) == 0:
            continue
        return materialCovered

def get_feeling() -> str:
    while True:
        feelingDaily = input("How are you feeling today: ")
        if len(feelingDaily) == 0:
            continue
        return feelingDaily

def get_programs() -> int:
    while True:
        programs = input("Number of programs written today: ")
        try:
            programs = int(programs)
            if programs < 0:
                raise ValueError
            return programs
        except ValueError:
            pass

if __name__ == "__main__":
    main()
