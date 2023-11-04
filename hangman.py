import time
import random


def mask(string1, string2):
    result = ''
    for char in string1:
        if char in string2:
            result += char
        else:
            result += '_'
    
    return result


def all_characters_present(string1, string2):
    for char in string1:
        if char not in string2:
            return False
    return True


word_list = [
    "python",
    "programming",
    "example",
    "awesome",
    "knowledge",
    "language",
    "computer",
    "science",
    "intelligence",
    "machine",
    "data",
    "analysis",
    "algorithm",
    "development",
    "openai",
    "chatbot",
    "learning",
    "gptthree",
    "generation",
    "artificial",
    "intelligence",
    "challenge",
    "cognitive",
    "knowledgeable",
    "inspiration",
    "incredible",
    "technology",
    "knowledgeable",
    "education",
    "innovation",
]

print("Enter your name")
name = input()
time.sleep(1.0)
print("Hi there @", name)
chosenWord = random.choice(word_list)
recivedCharacters = ""
len = len(chosenWord)
time.sleep(1.0)
print("Chosen Word:", mask(chosenWord, recivedCharacters))
time.sleep(1.0)
print("Enter your guesses letter by letter")

chances = 6
while chances > 0:
    a = input()
    time.sleep(1.0)
    if a in recivedCharacters:
        print(a, "was previously guessed, try a different one")
    else: 
        recivedCharacters += a
        
    if all_characters_present(chosenWord, recivedCharacters):
        print("Congratulations you've guessed the word " + chosenWord)
        break
    elif a in chosenWord :
        print(mask(chosenWord, recivedCharacters))
    else:
        chances -= 1
        print(mask(chosenWord, recivedCharacters))
        if chances > 0:
            print("wrong guess, chances remaining: ", chances)
        if chances == 0:
            print("Failed!, re-execute to Try again.")
            break
    
        
        
        
    
                    



