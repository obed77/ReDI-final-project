#Creating an empty dictionary to store users details
person_list = {}
input_activity = True

#Testing condition for inputs
while input_activity:
    cont = input("\nDo you want to add a person?\
        \nType Y to add or N to go ahead with the calculation or end the program: ")

    if cont == "":
        print("Oops! No input received.")
        cont = input("Oops! Type Y to add name and amount or type N to end the program: ")

    elif cont == "Y":
        name = input("\nEnter a person's name: ")
        while name == "" or name.isalpha() == False:
            print('\nError! A name cannot be empty nor digits. Input the correct name.')
            name = input("\nEnter a correct name: ")

        amount_paid = input('\nEnter the amount paid by the person: ')
        while amount_paid == "" or not amount_paid.isdigit():
            print('\nError! Amount paid cannot be alphabets. Input amount in number format.')
            amount_paid = input("\nEnter amount paid in numbers: ")

        person_list[name] = float(amount_paid)

    elif cont == "N":
        break

    else:
        print("Oops! Type Y to add name and amount or type N to end the program: ")
    

if person_list == {}:
    print("Oops! You did not enter any name and amount.\
        \nTry again and type Y if you want to add an input.\
        \nIf you are ok, then, thank you for using Sabed Money Split.")

else:
    #Displaying all members in a group and amount entered per user
    print("\nThe group: ",person_list)

    group_total_amount = sum(person_list.values())
    print("\nThe total amount contributed by the group: ",group_total_amount,'€')

    num_of_group_members = len(person_list.keys())
    print("The total number of persons in the group: ",num_of_group_members)

    #Displaying the average amount to be paid by each user
    avg_amount_to_be_paid_per_user = round(group_total_amount/num_of_group_members,2)
    print("The average gross amount per person in the group: ",avg_amount_to_be_paid_per_user,'€')

    person_list_avg_amount = person_list.copy()

    person_list_avg_amount = {
        person_list_avg_amount:avg_amount_to_be_paid_per_user 
        for person_list_avg_amount in person_list_avg_amount
        }

    person_list_amount_to_pay_or_receive = {
        key: round(person_list[key] - person_list_avg_amount.get(key, 0), 2) 
        for key in person_list
        }

    print("\n")

    #Displaying the net balance
    print("Name\t\tNet balance")
    for key in person_list_amount_to_pay_or_receive:
        if person_list_amount_to_pay_or_receive[key] < 0:
            print(key,'\t\towes',abs(person_list_amount_to_pay_or_receive[key]),'€')
        else :
            print(key,'\t\treceives',abs(person_list_amount_to_pay_or_receive[key]),'€')

    print("\n")
    print("Thank you for using Sabed Money Split. See you soon!") 
