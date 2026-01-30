# file_handling_demo.py
# TASK 8: File Handling (TXT & CSV)

import csv

print("===== FILE HANDLING DEMO =====\n")

# -------------------------------
# TEXT FILE HANDLING
# -------------------------------

try:
    # 1 & 2. Create text file and write data
    with open("users.txt", "w") as file:
        file.write("Name: Ashok\n")
        file.write("Course: CSE\n")
        file.write("Year: 2026\n")

    print("Data written to users.txt")

    # 3. Read file contents
    with open("users.txt", "r") as file:
        print("\nReading users.txt:")
        print(file.read())

    # 4. Append data to file
    with open("users.txt", "a") as file:
        file.write("Status: Internship Trainee\n")

    print("Data appended to users.txt")

except FileNotFoundError:
    print("File not found!")
except IOError:
    print("File handling error occurred!")

# -------------------------------
# CSV FILE HANDLING
# -------------------------------

# 6 & 7. Create CSV file and write multiple rows
with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Roll No", "Name", "Course"])
    writer.writerow([101, "Ashok", "CSE"])
    writer.writerow([102, "Ravi", "ECE"])
    writer.writerow([103, "Sita", "IT"])

print("\nCSV file students.csv created")

# 8. Read CSV data
print("\nReading students.csv:")
with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print("\n===== END OF TASK =====")
