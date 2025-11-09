proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for i, list in enumerate(strings, start=1):
    if "," in list:
        delimiter = "comma"
    elif ";" in list:
        delimiter = "semicolon"
    else:
        delimiter = "space"
    print(f"proto_list{i} uses {delimiter} as the separator")

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.


    word_list = list.split(delimiter)
    
    for j in range(len(word_list)):
        word_list[j] = word_list[j]
    
    if delimiter == ",":
        word_list.reverse()
        new_string = ",".join(word_list)
        print(f"Original string: {list}")
        print(f"Reversed string: {new_string}\n")
    else:
        print(f"{list} uses {delimiter}, no reversal applied\n")

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
