def user_input(prompt):
    user_input = input(prompt)
    return user_input

def findReplaceKeywords(template_input):
    last = ""
    keys = ["NOUN", "ADJECTIVE", "VERB", "ADVERB", "PRONOUN", "SAME"]

    #sort through the template_input for parts of speech keywords.  SAME uses the last input to allow templates to be more flexible
    for index, word in enumerate(template_input):
        if word in keys:
            if word == "SAME":
                template_input[index] = last
            else:
                replacement = user_input("Enter a {} \n: ".format(word.lower()))
                template_input[index] = replacement
                last = replacement

    joined = ' '.join(template_input)
    return joined


# gets and reacts to user input
def getInput():
    choice = user_input("\nC = enter template in console \nF = enter template from file \nQ = quit \n\n")
    code = choice.lower()

    # file I/O to enter templates.  Opens file in default read-only
    if(code == "f"):
        input = user_input("Enter a template file name: \n")
        template = open(input)
        template_input = template.read()
        template.close()

    # console template entry
    elif(code == "c"):
        template_input = user_input("Enter template text: \n")

    # quit
    elif(code == "q"):
        return False

    # prints the new string
    print("\n" + findReplaceKeywords(template_input.split()) + "\n")
    return True


print("Type the part of speech in all caps for the fill-ins, and SAME to use the previous word again")

running = True
while(running):
    running = getInput()
