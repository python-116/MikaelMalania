# name = input("Enter your name: ")

# if name == "nika":
#     print("Hello Nika")
# elif name == "giorgi":
#     print("Opps, I thought you were Nika")
# else:
#     print("Hello stranger")


# დაწერეთ პროგრამა სადაც მომხმარებელს მოსთხოვთ შეიტანოს საკუთარი
# დაბადების წელი და გამოიანაგრიშეთ ამ ინფორმაციით მისი ასაკი
# გამოიტანეთ შედეგი ეკრანზე

# თუ მომხმარებელი 18 წელზე ზევით იქნა გამოიტანეთ რომ ხმის მიცემა შეუძლია
# თუ არადა გამოიტანეთ რომ არ შეუძლია ხმის მიცემა
# >
# <
# >=
# <=

year = int(input("Enter your birth year: "))
age = 2024 - year

print("Your age is:", age)

if age >= 18:
    print("You can vote")
elif age >= 16 and age < 18:
    remaining_years = 18 - age
    print(f"You will be eligible to vote in {remaining_years} years")
else:
    print("You can't vote")
