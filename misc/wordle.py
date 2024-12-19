import random
import re

# Function to assess a guess against the Wordle answer
def Evaluate(guess: str, answer: str) -> str:
    result = ""
    for pos in range(len(guess)):
        if guess[pos] == answer[pos]:
            result += "C"  # (C)orrect letter in correct position
        elif guess[pos] in answer:
            result += "I"  # Correct letter (I)n wrong position
        else:
            result += "X"  # Letter not in Wordle answer (X)
    return result

# ====================================================================================================
# Function to generate a new guess based on past guesses and evaluations
def GenerateGuess(PastGuesses, PastEvaluations) -> str:

    # Placeholder - new guess is a random word - REPLACE this with more intelligent code based on
    # the past guesses and evaluations
    with open('data/shuffled_real_wordles.txt', 'r') as f:
        print(PastGuesses)
        print(PastEvaluations)
        f = f.read().lower()
        not_possible = ['x']
        guaranteed = ['.', '.', '.', '.', '.']
        place = []

        for i, eval in enumerate(PastEvaluations):
            pos = 0
            if 'C' in eval:
                indexes = [i for i, ch in enumerate(eval) if ch == 'C']
                for index in indexes:
                    guaranteed[index] = PastGuesses[i][index]
            if 'X' in eval:
                indexes = [i for i, ch in enumerate(eval) if ch == 'X']
                for index in indexes:
                    not_possible.append(PastGuesses[i][index])

                # index = eval.index('C')
                # guaranteed[index] = PastGuesses[i][index]
            # if 'C' in eval:
            #     index = eval.index('I')
            #     if PastGuesses[i][index] not in place:
            #         place.append(PastGuesses[i][index])
            #     pos += 1
        print(guaranteed, place)

        for i, char in enumerate(guaranteed):
            if char == '.':
                excluded = ''.join(sorted(set(not_possible)))
                guaranteed[i] = f"[^{excluded}]"

        pattern = rf'{guaranteed[0]}{guaranteed[1]}{guaranteed[2]}{guaranteed[3]}{guaranteed[4]}'


        possible_words = re.findall(pattern, f)
        possible_words = [word for word in possible_words if word not in PastGuesses]
        WordToReturn = random.choice(possible_words)
        print(len(possible_words), possible_words)

    return WordToReturn
#====================================================================================================

# Choose random Wordle answer from textfile
TargetWord = random.choice(open("data/shuffled_real_wordles.txt", 'r').read().lower().split())

# Initiate Variables
MyGuess = "     "
Evaluation = "XXXXX"
NoGuesses = 0
AllGuesses = []
AllEvaluations = []

while Evaluation != "CCCCC":
    # Call function to Generate a new Guess
    MyGuess = GenerateGuess(AllGuesses, AllEvaluations)
    # Housekeeping - increment count, add Guess to list of Guesses, Evaluate Guess
    NoGuesses += 1
    AllGuesses.append(MyGuess)
    Evaluation = Evaluate(MyGuess, TargetWord)
    AllEvaluations.append(Evaluation)
    print(NoGuesses, MyGuess, Evaluation)

print ("The word was", TargetWord, AllGuesses, AllEvaluations)