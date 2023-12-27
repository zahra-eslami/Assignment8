import gtts
import os
# from playsound import playsound
import pygame

# -----------------------------------------------------------------------------

def save_play_voice(output):
    x = gtts.gTTS(output, lang="en", slow=False)
    file_path = "Assignment8/voice.mp3"
    x.save(file_path)
    play_sound(file_path)

# -----------------------------------------------------------------------------
    
def play_sound(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))  # Wait for sound to finish (in milliseconds)
        pygame.mixer.quit()
        pygame.quit()
    except Exception as e:
        print("Error playing audio:", e)

# -----------------------------------------------------------------------------

def read_from_file():
    global words_bank


    file_path = "Assignment8/translate.txt"

    if os.path.exists(file_path):
        f=open(file_path,"r")
        # with open("Assignment8/translate.txt") as f:
        temp_word=f.read().split("\n")
        f.close()
        
        words_bank=[]

        for i in range(0,len(temp_word),2):
            my_dictionary={"en":temp_word[i],"fa":temp_word[i+1]}
            words_bank.append(my_dictionary)
    else:
        print("file does not exist")
        exit(0)
         
# -----------------------------------------------------------------------------
        
def translate_english_to_persian():
    user_text = input("Please enter your English text to translate: ")
    if user_text.endswith("."):
        user_text = user_text[:-1]

    user_sentences = user_text.split(".")
    output = ""

    for sentence in user_sentences:
        user_words = sentence.split(" ")
        translated_sentence = ""

        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    translated_sentence += word["fa"] + " "
                    break
            else:
                translated_sentence += user_word + " "

        output += translated_sentence + ". "

    print("Translated text: ", output)
    save_play_voice(output)

# -----------------------------------------------------------------------------
        
def translate_persian_to_english():
    user_text = input("Please enter your Persian text to translate: ")
    if user_text.endswith("."):
        user_text = user_text[:-1]
        
    user_sentences = user_text.split(".")
    output = ""

    for sentence in user_sentences:
        user_words = sentence.split(" ")
        translated_sentence = ""

        for user_word in user_words:
            for word in words_bank:
                if user_word == word["fa"]:
                    translated_sentence += word["en"] + " "
                    break
            else:
                translated_sentence += user_word + " "

        output += translated_sentence + ". "

    print("Translated text: ", output)
    save_play_voice(output)

# -----------------------------------------------------------------------------

def add_new_word():
    file_path = "Assignment8/translate.txt"

    if os.path.exists(file_path):
            f=open(file_path,"a")
            while True:
                user_English_text = input("Please enter your English text : ")
                user_Persian_text = input("Please enter your Persian text : ")
                
                if(user_English_text!=""or user_Persian_text!=""):
                    
                    f.write(f"\n{user_English_text}\n{user_Persian_text}")
                    choice = input("Do you want to buy more products? (y/n): ")
                    if choice.lower() != 'y':
                        print("\n","-"*30)
                        show_menu()
                        
                        break
                        
# -----------------------------------------------------------------------------

def show_menu():
    print("1. translate english to persian")
    print("2. translate persian to english")
    print("3. add a new word to database")
    print("4. exit")

# -----------------------------------------------------------------------------

read_from_file()

print("welcome to my translate") 

show_menu()

while True:
    try:
    
        choice=int(input("Please enter your choice :"))
        
        if choice==1:
            translate_english_to_persian()

        elif choice==2:
            translate_persian_to_english()

        elif choice==3:
            add_new_word()

        elif choice==4:
            exit(0)

        else:
            print("your choice is not in the list, please choose again")
            show_menu()

    except ValueError:
        print("You must enter an integer number")


        