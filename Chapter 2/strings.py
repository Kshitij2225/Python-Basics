str1 = """Hey Everyone"""   # All the 3 ways of written string is 
str2 = 'Hey Everyone'       # But in Most cases we use the double
str3 = "Hey Everyone"        # quotes ""

Firstname = "Kshitij"
print(len(Firstname))

Lastname = "Jain"
print(len(Lastname))  # Length Function of string.

fullname = Firstname+Lastname
print(len(fullname))
print(fullname) # That Is called Concatenation.


string = "Hey Everyone I am Kshitij Jain."
print(string.endswith("in."))
print(string.capitalize())
print(string.replace("Kshitij","Mohini"))
print(string.find("Kshitij"))
print(string.count("Hey"))