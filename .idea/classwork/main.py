import time

def printLetters(str):
    while True:
        for i in str:
            print(i)
            time.sleep(0.3)
        print("\n")

printLetters("Егор Петух".upper())