word = "Human"

# 3 ways to print Strings
print("Hello this is a " + word)
print("Hello this is a {}".format(word))
print(f"Hello this is a {word}")    # Best Practice

adj1 = input("Adjective: ")
verb1 = input("Verb: ")
noun1 = input("Noun: ")

madlib = f"Batman is {adj1}. He is {verb1} every Night and knows how to {noun1}."

print(madlib)