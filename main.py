import random

def pick_random_word():
    words = ["яблоко", "банан", "апельсин", "виноград", "ананас", "клубника", "голубика"]
    return random.choice(words)

def display_hangman(tries):
    stages = ["""
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     / \\
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |     / 
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|/
                |      |
                |      
                -
             """,
             """
                --------
                |      |
                |      O
                |     \|
                |      |
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
             """,
             """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
             """,
             """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
             """
    ]
    return stages[tries]

def hangman():
    word = pick_random_word()
    guessed = "_" * len(word)
    guessed_letters = []
    tries = 6

    print("Давайте поиграем в Виселицу!")
    print(display_hangman(tries))
    print(guessed)
    print("\n")

    while tries > 0 and "_" in guessed:
        guess = input("Угадайте букву: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Вы уже угадывали букву", guess)
            elif guess not in word:
                print(guess, "не входит в слово.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично,", guess, "входит в слово!")
                guessed_letters.append(guess)
                word_as_list = list(guessed)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                guessed = "".join(word_as_list)
                if "_" not in guessed:
                    print("Поздравляем, вы угадали слово!")
        else:
            print("Некорректный ввод. Пожалуйста, введите одну букву.")

        print(display_hangman(tries))
        print(guessed)
        print("\n")

    if tries == 0:
        print("Извините, вы исчерпали все попытки. Слово было " + word + ".")
    else:
        print("Поздравляем! Вы угадали слово " + word + "!")

if __name__ == "__main__":
    hangman()