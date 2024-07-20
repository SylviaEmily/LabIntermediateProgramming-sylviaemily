def guess_secretword(secretWord): 
    guessed_letters = []
    chances = 6

    while chances > 0 :
        guess = input ("enter a letter")

        if len(guess) != 1:
            print ("enter a letter")
        elif not guess.isalpha():
            print ("enter a letter ")
        elif guess.lower() in guessed_letters :
            print ("you already guessed that letter")
        else :
            guessed_letters.append(guess.lower()) 
            if guess.lower() in secretWord.lower():
                print("congrast, your letter is correct")
            else :
                chances -=1
                print ("try again. you have {}chances left".format(chances))
        display = ""
        for letter in secretWord :
            if letter.lower() in guessed_letters :
                display += letter
            else :
                display +="-"
        print (display)
        if "_" not in display :
            print ("congratulations!you guessed the word", secretWord)
        if chances == 0 :
            print ("sorry you lose. try again!")    

secretWord = "lampu"
guess_secretword(secretWord)