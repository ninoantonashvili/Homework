#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს

n = int(input("please insert a number: "))
jami = 0

for i in range(1, n + 1):
    jami += i

print(f'{jami} is the sum of numbers from 1 to {n}')

#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს და შემდეგ იყენებს
# "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

n = int(input("please insert a number: "))
while n > 0:
    print(n)
    n -= 1

#დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს გამოიცნოს წინასწარ
# განსაზღვრული რიცხვი. როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს, დაასრულებს პროგრამა მუშაობას.

# Predetermined number
correct_number = 42
while True:
    n = int(input("Guess the number: "))
    if n == correct_number:
        print(f"Congratulations! it is {n}")
        break  #
    else:
        print("Try again")

#დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი total_sum = 0,
# შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
# ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც დაიბეჭდება
# შეყვანილი დადებითი რიცხვების ჯამი.

sum = 0
while True:
    n = input("Enter a number (type 'sum' to finish): ")

    # Check if the input is 'sum' to end the loop
    if n == 'sum':
        break

    number = int(n)
    if number > 0:
            sum += number
    else:
            print("enter a positive number")

print(f"The sum of positive numbers entered is: {sum}")




