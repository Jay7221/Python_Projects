birthdays={}
while True:
    print("Enter a name<blank to quit>")
    name=input()
    if name=="":
        break
    if name in birthdays:
        print(birthdays[name]+ " is the birthdate of "+ name)
    else:
        print("The given name does not exist in the database. Kindly provide the birthdate:")
        bday=input()
        birthdays[name]=bday
        print("Database updated successfully!")
