print('''In order to enjoy our app use the following key words:
add - to add notes;
earliest - to display the notes in a chronological order from old to new;
latest - to display the notes in a chronological order from new to old;
longest - to display the notes in length from longest to shortest;
shortest - to display the notes in length from shortest to longest
Exit - to exit the program''')

key_word = input('\nInput the key-word: ')
allowed_words = 'add', 'earliest', 'latest', 'longest', 'shortest'
notes_list = []

while key_word != 'Exit':
    if key_word == 'add':
        notes = input('Input a note: ')
        notes_list.append(notes)
    elif key_word == 'earliest':
        print(notes_list)
    elif key_word == 'latest':
        notes_list.reverse()
        print(notes_list)
    elif key_word == 'longest':
        notes_list.sort(key=len, reverse=True)
        print(notes_list)
    elif key_word == 'shortest':
        notes_list.sort(key=len)
        print(notes_list)
    elif key_word not in allowed_words:
        print('Wrong key-word.\nUse the key-words from the list\n')
    key_word = input('Input the key-word: ')