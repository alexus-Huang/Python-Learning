"""
Practice:
- underscores in numbers
- multiple assignment
- constants
- practice writing good comments to explain whats going on in the code
- stripping whitespace
- use the format method to print stuff out
"""

one_thousand = 1_000 # underscores in numbers to make it easier to read numbers
x,y,z=1,2,3 # multiple assignment practice 
THIS_MONTH = 3 # constant variable by using capital letters to indicate that the variable is a constant
filename = "python_file.py" # filename variable containing a string to depict a file name
URL = "https://www.google.com" # constant variable 

print(one_thousand)
print(x,y,z, sep=" ")
print(THIS_MONTH)
print(f"File name: {filename.removesuffix('.py')}")
print(f"URL: {URL.removeprefix('https://')}")