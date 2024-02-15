# 1.შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.

arr = [44, 23, 11, 8, 20, 56, 33, 55]
x = eval(input("გთხოვთ, შეიყვანეთ რიცხვი გადასამოწმებლად:  "))

if x in arr:
    print(f'{x} ეკუთვნის მოცემულ მასივს')
else:
    print(f'{x} არ ეკუთვნის მოცემულ მასივს')

#2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.

x = int(input("\n\nშეიყვანეთ მთელი რიცხვი: "))

if x % 2 == 0:
    print(f'{x} ლუწია')
else:
    print(f'{x} კენტია')

#3შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

str1 = "nini antonashvili"
str2 = "nini antonashvili"

if str1 is str2:
    print(f"\n\n{str1} and {str2} are the same")

else:
    print(f"\n\n{str1} and {str2} are different")


#4შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:
#თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
#თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
#სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
#რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი

num_list =  [44, 23, 11, 8, 20, 56, 33, 55]
x = int(input("\n\nplease, enter an integer: "))

if x > num_list[2] and x < num_list[-1]:
    print("more than list elements")
elif x == num_list[5]:
    print("equal")
else:
    print("none of the conditions were met")
