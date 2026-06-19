def blood_bot(message):

    msg=message.lower()


    if "available" in msg:
        return "Checking available blood units..."

    elif "donate" in msg:
        return "Thank you for donating blood ❤️"

    elif "emergency" in msg:
        return "Finding nearby donors..."

    else:
        return "I can help with blood donation and requests."


while True:

    user=input("You:")

    print(
    "AI:",
    blood_bot(user)
    )
