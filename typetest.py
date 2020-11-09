import markov_chain

data = markov_chain.readdata("words.txt")
rule = markov_chain.makerule(data, 8)
output = markov_chain.makestring(rule, 200)

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
