# **kwargs

def hello(**kwargs):
    for key,value in kwargs.items():
        print(value,end="")

hello(first="John",last="Doe")