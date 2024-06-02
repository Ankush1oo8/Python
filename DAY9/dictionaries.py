#have key and value pairs
#{key: Value}

dict={
    "bug":"An error in aprogram that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"the action of doing something over and over again.",
}

print(dict["bug"])
print(dict)

#adding in dictionary
dict["Ankush"]="The name of person writing this text"

#creating an empty dictionary
empty_dict={}

#wipe an existing dictionary
dict={}
print(dict)

#edit an item in a dictionary
dict["bug"]="a moth in your computer"
print(dict)

#loop throough a dictionary
for thing in dict:
    print(thing)#just prints out the keys
    print(dict[thing])