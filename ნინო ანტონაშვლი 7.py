#1 შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს პარამეტრად
# და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

#2 დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს.
# პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

#3 შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით
# რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას

#4 რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს
# (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

#5 რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ
# (revers) სტრიქონს (მაგალითად input: Hello   Output: olleH)

#1
int_list = [10, 20, 30, 40]

def add(num):
    global int_list
    int_list.append(num)

number = int(input("insert an integer: "))
add(number)

print("Updated int_list:", int_list)

#2
def sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum(numbers[1:])
number_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result = sum(number_list)

print("Sum of the numbers:", result)

#3
gl_str = 'Global'
def localVariable():
    gl_str = 'Local'
    return gl_str

result = localVariable()

print("Global variable:", gl_str)
print("Local variable:", result)

#4
def sum(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum(number // 10)

input_number = eval(input("insert an integer: "))
result = sum(input_number)

print("Sum of digits in", input_number, "is:", result)


#5
def reverse_string(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return input_str[-1] + reverse_string(input_str[:-1])

string = input("enter a string: ")
result = reverse_string(string)

print("Original string:", string)
print("Reversed string:", result)
