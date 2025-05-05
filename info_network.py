#Import
import datetime

now = datetime.datetime.now()

#Print full name, studID, and current date and time
print("Full name: Ralph Jieian I. Sebastian")
print("Student ID: 211-1077")
print(f"Date/Time: {now}")

#Prompt user to describe a networking issue
issue = input("\nDescribe a networking  issue : ")

#Save the response into network_issue.txt
file = open("./network_issue.txt", "a")
file.write(issue + "\n")
file.close()
