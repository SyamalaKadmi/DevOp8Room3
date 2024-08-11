firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

fullName = firstName + " " + lastName

print("Hello, " + fullName)

firstNumber = int(input("Please enter the first number to perform calculator operations: "))
secondNumber = int(input("Please enter the second number: "))

addition = firstNumber + secondNumber
subtraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber //  secondNumber

print(f"""
      Numbers {firstNumber} and {secondNumber} calculator results:
      Addition =  {addition}
      subtraction =  {subtraction}
      multiplication = {multiplication}
      Division = {division}
      """)



