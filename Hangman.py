import random as rd
name = input("enter you name ")
print("hello ", name, " ,welcome! Are you ready to play hangman!\nlets go!")
file = open("file.txt", 'r')
words = []
guessed_list = []
for line in file:
    if len(line) > 6:
        words += [line[:-1]]
select = rd.choice(words)
selected = []
for i in select:
    selected += i
#print(selected)
#print(select)
length = len(select)
for i in range(length):
    guessed_list += ["_"]
tries = 4
char_guessed = []
print("Start guessing !!")
while tries > 0 :
    if guessed_list == selected:
        break
    for i in range(length):
        if guessed_list[i] == '_':
            print("_ ", end=" ")
        else:
            var = guessed_list[i]
            print(var, end=" ")
    print()
    guess = input("enter the character:  ")
    if guess  in char_guessed:
        print("this character is already guessed!")
    else:
        char_guessed += guess
        if guess not in selected:
            tries -= 1
        for i in range(length):
            if guess == selected[i]:
                 guessed_list[i] = guess
    print("\nThe numbers of tries left are ", tries)
if tries > 0:
    print("yay! u guessed it right....", select)
else:
    print("wrong answer.... the word is ", select)
print("thank you")
