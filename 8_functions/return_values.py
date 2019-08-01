
# a function that returns a well-formatted message
def getMessage(body, recipient):
    stars = "*" * 30
    message = stars + "\n" + body + "\n- " + recipient + "\n" + stars

    return message

body = input("Please enter a message body: ")
recipient = input("Please enter a recipient: ")
wellFormattedMsg = getMessage(body, recipient)
print(wellFormattedMsg)

# a function that checks whether a number falls within a range
def between(number, low, high):
    if number >= low and number <= high:
        return True
    else:
        return False

number = int(input("Enter a number between [1, 20]: "))
if between(number, 1, 20):
    print("Number is within range!")
else:
    print("Number outside range!")

# create a function that calculates factorials
def factorial(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

print("factorial(4):", factorial(4))
print("factorial(3):", factorial(3))
print("factorial(10):", factorial(10))