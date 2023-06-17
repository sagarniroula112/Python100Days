# Strings are immutable
a = "sAmvu Har Har!!!!!!!!!!!"
print(len(a))

print(a.upper()) # existing string lai change gardaina
print(a.lower())
print(a.rstrip("!"))
print(a)
print(a.replace("Har", "Sagaru"))
print(a.split(" "))
print(a.capitalize())
print(a.center(100))

b = "Sagar!!!!!!"
print(b.split("a"))
print(b.count("a"))
print(a.endswith("!!"))
print(a.find("Har"))

c="bandariya1"
print(c.isalnum())
print(c.isalpha())
print(c.islower())

str1 ="we wish you a Merry Christmas"
print(str1.isprintable())
str1 = "Shambhu"
print(str1.isspace())
print(str1.istitle())
str2 ="saru"
print(str2.startswith("saru"))


a = int(input("Enter your age:: "))
if(a>=18):
    print("You can drive")
else:
    print("You can't drive")
