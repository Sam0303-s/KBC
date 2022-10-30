import speech_recognition as sr
import pyttsx3 as tt
import time as t

# global variables
score = []
total = 0
listener = sr.Recognizer()
alexa = tt.init()

result = ''
# global samuel


def talk(aug):
    alexa.say(aug)
    alexa.runAndWait()


# start__________
print("Welcome to KBC in Physics \n")
talk("Welcome to KBC in Physics")
print('=====================||=====================\n')
print('Enter your name:  ')
talk("Enter your name")
# t.sleep(2)

with sr.Microphone() as source:
    print('speak.....')
    voice = listener.listen(source)
    samuel = listener.recognize_google(voice)


print('Hi {}\n are u ready for quizz game!'.format(samuel))

print('enter yep/nop to continue.......')
talk("Do you want to play quiz yes or no")
try:
    with sr.Microphone() as source:
        print('speak.....')
        voice = listener.listen(source)
        globals()['result'] = listener.recognize_google(voice)
except:
    print("plz try again I did'nt get it.")

if result.lower() == 'yes':
    # ________Questions starts_____________
    talk('ok lets start the quiz now')
    talk('here is your first question')

    print('1) The eye lens is : \n'
          'a) Concave \t b) Convex \t c) Biconcave \t d) Biconvex')
    talk('The eye lens is')
    talk('Concave')
    talk('Convex')
    talk('Biconcave')
    talk('Biconvex')
    talk('ok you have 5 seconds to think the answer')
    t.sleep(5)
    try:
        with sr.Microphone() as source:
            print('speak.....')
            talk('tell your answer now')
            voice = listener.listen(source)
            ans1 = listener.recognize_google(voice)
            # print(ans1)
            talk(f'your locked answer is {ans1}')
            talk('moving to next question')
    except:
        print("plz try again I did'nt get it.")

    print('=====================||=====================\n')
    print('2) This part of the eye dilates and contracts based on the environment : \n'
          'a) Sclera \t b) Cornea \t c) Pupil \t d) Lens')
    talk('This part of the eye dilates and contracts based on the environment')
    talk('Sclera')
    talk('Cornea')
    talk('Pupil')
    talk('Lens')
    talk('ok you have 5 seconds to think the answer')
    t.sleep(5)
    try:
        with sr.Microphone() as source:
            print('speak.....')
            talk('tell your answer now')
            voice = listener.listen(source)
            ans2 = listener.recognize_google(voice)
            # print(ans2)
            talk(f'your locked answer is {ans2}')
            talk('moving to last question')
    except:
        print("plz try again I did'nt get it.")

    print('=====================||=====================\n')
    print('3) Which of these colours is least scattered by dust, fog, smoke? \n'
          'a) Yellow \t b) Blue \t c) Red \t d) Violet')
    talk('Which of these colours is least scattered by dust fog smoke')
    talk('Yellow')
    talk('Blue')
    talk('Red')
    talk('Violet')
    talk('ok you have 5 seconds to think the answer')
    t.sleep(5)
    try:
        with sr.Microphone() as source:
            print('speak...')
            talk('tell your answer now')
            voice = listener.listen(source)
            ans3 = listener.recognize_google(voice)
            # print(ans3)
            talk(f'your locked answer is {ans3}')
    except:
        print("plz try again I did'nt get it.")
    print('=====================||=====================\n')

    if ans1.lower() == 'biconvex':
        score.append(1)
    else:
        score.append(0)

    if ans2.lower() == 'pupil':
        score.append(1)
    else:
        score.append(0)

    if ans3.lower() == 'red':
        score.append(1)
    else:
        score.append(0)

    for i in score:
        total += i
    if total >= 2:
        print(f'Congratulations {samuel}')
        talk(f'Congratulations {samuel}')
    else:
        print(f'Sorry {samuel}')
        talk(f'Sorry {samuel}')
    print(
        f'You have scored {total}/3 !!\n Better luck next time........')
    talk(f'You have scored {total} out of 3 Better luck next time')
elif result.lower() == "no":
    print('Thank u for visiting try again!!')
    talk('Thank u for visiting bye')
print('=====================||=====================\n')
print('samuel')
