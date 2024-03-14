user_input= input("Enter in a URL:")
print(user_input.removeprefix("https://"))
print(user_input.removesuffix(".com"))