rollnumbers = [123, 45, 67, 89]
accountnames = ["Nandini", "Dhanalakshmi", "Gowri", "Chinnammi"]

rollnumber = 689
found = False

for i in range(len(rollnumbers)):
    if rollnumbers[i] == rollnumber:
        print("Roll number:", rollnumbers[i])
        print("Account name:", accountnames[i])
        found = True
if not found:
    print("Roll number not found. Adding new account...")
    name = input("Enter account name: ")
    rollnumbers.append(rollnumber)
    accountnames.append(name)
    print("New account added successfully!")

print("Roll Numbers:", rollnumbers)
print("Account Names:", accountnames)