#1დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip
# ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
#2 დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
#3დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
#4დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა
# ისიც გაითვალისწინეთ.


#1
def group(list1, list2):
    grouped = list(zip(list1, list2))
    return grouped
#magaliti
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

result = group(list1, list2)
print(result)

#2
def calculate_product(numbers):
    try:
        namravli = 1

        # Multiply each number in the list
        for num in numbers:
            namravli *= num

        return namravli
    except TypeError as e:
        print(f"Error: {e}")
        return None


# magaliti:
number_list = [2, 3, 3, 7, 10]

result = calculate_product(number_list)

if result is not None:
    print(f"The product of the numbers is: {result}")
else:
    print("Calculation failed due to TypeError.")

#3
kenti = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

# magaliti:
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = kenti(integer_list)
print(result)

#4
suffix = lambda string_list, suffix: list(filter(lambda s: isinstance(s, str) and s.endswith(suffix), string_list))

# მაგალიტი:
string_list = ["nini", "banani", "komarovi", "paata"]
target = "ni"

result = suffix(string_list, target)
if result:
    print(f"Strings ending with '{target}': {result}")
else:
    print("Filtering failed due to TypeError.")

