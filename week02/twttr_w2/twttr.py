textinput = input("Input: ")
output = ""
for i in range(len(textinput)):
    if not (textinput[i].lower() in 'aeiou'):
        output = output + textinput[i]
print(output);
