#

fruits = {
    "Apple" : "130",
    "Avocado" : "50",
    "Sweet Cherries" : "100",
    "Tomato" : None
}

question = input("What is your favourite fruit? ")
if question in fruits and fruits[question] is not None:
    print("The amount of calories in", question, "is", fruits[question])