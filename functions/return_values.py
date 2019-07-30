
# a function that returns a well-formatted message
def getMessage(body, recipient):
    stars = "*" * 30
    message = stars + "\n" + body + "\n- " + recipient + "\n" + stars

    return message

body = input("Please enter a message body: ")
recipient = input("Please enter a recipient: ")
wellFormattedMsg = getMessage(body, recipient)
print(wellFormattedMsg)