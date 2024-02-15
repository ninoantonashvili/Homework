#დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს
# სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი;
# 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.
#მომხარებელმა უნდა შეიყვანოს შემდეგი სტრუქტურით ბრძანება "{command} {number}" commands:
#a – append
#r – remove
#e – exit
#მხოლოდ გამოიყენეთ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.
from typing import List


def main():
    my_array = []

    while True:
        print("Current array:", my_array)
        user_input = input("Enter 'a' to add, 'r' to remove, 'e' to exit: ")

        if user_input == 'e':
            print("Exiting the program.")
            break
        elif user_input == 'a':
            try:
                num = int(input("Enter a number to add: "))
                my_array.append(num)
                print(f"{num} added to the array.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif user_input == 'r':
            try:
                num = int(input("Enter a number to remove: "))
                my_array.remove(num)
                print(f"{num} removed from the array.")
            except ValueError:
                print(f"{num} not found in the array.")
        else:
            print("Invalid input. Please enter 'a', 'r', or 'e'.")


if __name__ == "__main__":
    main()


#####################################################################
#დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list = [43, '22', 12, 66, 210, ["hi"], და შეასრულებს შემდეგ ნაბიჯებს:
#a. დაბეჭდავს 210-ის ინდექსს;
#b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
#c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
#d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

#a
my_list = [43, '22', 12, 66, 210, ["hi"]]
index_210 = my_list.index(210)
print(f"Index of 210: {index_210}")
#b
my_list[-1].append("hello")
print(f"List after adding 'hello' to the last element: {my_list}")
#c
remove = my_list.pop(2)
#pop ფუნქციის გამოყენებით წავშალე მეორე ინდექსზე მყოფი ელემენტი
print(f"List after removing element at index 2: {my_list}")
#d
my_list_2 = my_list.copy()
my_list_2.clear()
print(f"my_list : {my_list}")
print(f"my_list_2: {my_list_2}")

#დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა
# "(123) 456-789" ფორმატს, თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.


import re

def number(phone_number):
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{3}$')

    if pattern.match(phone_number):
        print(f"number: {phone_number}")
    else:
        print("Invalid format")


user_input = input("Enter a phone number: ")
number(user_input)

