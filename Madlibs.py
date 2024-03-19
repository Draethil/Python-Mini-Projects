word = "Human"

# 3 ways to print Strings
print("Hello this is a " + word)
print("Hello this is a {}".format(word))
print(f"Hello this is a {word}")    # Best Practice

adj1 = input("Adjective: ")
verb1 = input("Verb: ")

madlib = f"Compute programming is so {adj1}. It makes me so excited all the time because I love to {verb1}."

print(madlib)