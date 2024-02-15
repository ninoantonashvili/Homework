#1 დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

#2 დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები.
# (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით).
# მაგ.: race და care ანაგრამებია.

#3 დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

#4 დაწერეთ პითნის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს.
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.



#1 რადგან, ამ ლექციის დავალების დროს რეკურსია არ გვქონდა ნასწავლი, გავაკეთებ ციკლებით

def fibonacci(n):
    fib = []
    a, b = 1, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib

n = eval(input("please enter an integer: "))
result = fibonacci(n)
print(result)


#2
def anagram(str1, str2):
    #დაშორებები წავშალოთ და პატარა ასოებში გადავიყვანოთ, რაიმე რომ არ გამოგვეპაროს
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # გვიბრუნებს ბულეანს, არის თუ არა ეს ორი სტრინგი ერთმანეთის ტოლი დასორტვის შემდგომ
    return sorted(str1) == sorted(str2)

string1 = input("insert a string: ")
string2 = input("insert another string: ")
result = anagram(string1, string2)
#ახლა, მიღებული ბულეანის შემდეგ ვაბეჭდინებთ სტრინგები ანაგრამებია თუ არა
if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

#3
#კვლავ რეკურსიის გარეშე, ვაკეთებ ამ სავარჯიშოს

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = eval(input("insert an integer: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")

#4
def count(string, symbol):
    count = 0
    for char in string:
        if char == symbol:
            count += 1
    return count

my_string = input("insert a string: ")
my_symbol = input("insert a symbol to check: ")
result = count(my_string, my_symbol)
print(f"The symbol '{my_symbol}' appears {result} times in the string.")

