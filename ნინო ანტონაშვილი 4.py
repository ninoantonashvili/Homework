#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას
input_string = input("Enter a string: ")
utf8_result = input_string.encode('utf-8')
print(f"UTF-8 version: {utf8_result}")

#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. ჩამოაშორეთ ზედმეტი ინტერვალები. ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში
# და დაუმატეთ ქვესტრიქონი 'Python'. თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით

string = input("Enter a string: ")

new_string =string.strip().replace(' ', '').lower() + "Python"
#ვიყენებ replace ფუნქცია, რომ შევცვალო python Python-ად
new_string = new_string.replace('python', 'Python')

print(f"Processed string: {new_string}")



#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს
#ახალ სტრიქონს, რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

string = input("Enter a string: ")
#ვიღებ პირველი ნახევრის ინდექსს
index = len(string) // 2
#სტრინგდან მხოლოდ ვტოვებ იმ ნაწილს, რომელიც მიღებულ ინდექსამდეა
half = string[:index]

print(f"First half of the string: {half}")

#დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს. string მოდულის გამოყენებით დაწერეთ შემოწმება. სტრიქონი
# ვალიდურია მაშინ, როდესაც ის შეიცავს ერთ ციფრს და არ არის დამატებითი სიმბოლოები ('!', '~', '#', '$' და ა.შ.)



def string(input_string):
    count_numbers = sum(c.isdigit() for c in input_string)
    has_symbols = any(c in string.punctuation for c in input_string)
    return count_numbers == 1 and not has_symbols

str = input("Enter a string: ")

if string(input_string):
    print("The string is valid.")
else:
    print("The string is not valid.")

 #დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს, სტრიქონი გადაყავს ბაიტებში,
 # ბეჭდავს მნიშვნელობას და შემდეგ კი გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

string = input("Enter a string: ")
#გადავიყვანოთ ბაიტებში encode ფუნქციის გამოყენებით
bytes = string.encode('utf-8')
print(f"Bytes representation: {bytes}")
#ბაიტები გადაგვყავს უკან სტრინგში decode-თი
decoded = bytes.decode('utf-8')
print(f"Decoded string: {decoded}")
