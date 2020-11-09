import markov_chain as m

data = m.readdata("words.txt")
rule = m.makerule(data, 8)
output = m.makestring(rule, 200)

string = output.split()
print(output)

total = len(output)
correct = 0

userInput = str(input("Enter words: \n"))

userInput = userInput.split()

# grade based on what has been submited
for i in range(len(userInput)):
    if (string[i] == userInput[i]):
        correct+=1

print("total correct: " + str(correct/len(userInput)))
