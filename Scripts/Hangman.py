import random
words =['А Л Ф А В И Т',
        'Г И П О П О Т А М',
        'Л О Г И К А',
        'К О М П Ь Ю Т Е Р',
        'Ц И К А Д А',
        'Р А Д У Г А',
        'Д Р У Ж Б А',
        'Т Е Л Е Ф О Н',
        'О Д И Н Н А Д Ц А Т Ь',
        'А Н Т А Р К Т И К А',
        'Ф И О Л Е Т О В Ы Й',
        'С О Р О К О Н О Ж К А',
        'К А Л Ь К У Л Я Т О Р',
        'Р Е Б У С',
        'Л А М П О Ч К А',
        "О Б Л А К О",
        "Р Е Ш Е Н И Е",
        "Т Е Л Е С К О П",
        "П У Н К Т И Р",
        "И Н Т Е Р Н Е Т",
        "Г Р А М М А Т И К А",
        "К О Н О Р Е Й К А",
        "К А Р А Н Д А Ш",
        "М Е Л А Т О Н И Н",
        "Г Е М О Г Л О Б И Н",
        "Р А К У Ш К А",
        "У К Р А И Н А",
        "М Е Р К У Р И Й",
        "С Т Е К Л О В А Т А",
        "Г Р А В И Т А Ц И Я",
        "С Е К Р Е Т",
        "М И К Р О С Х Е М А",
        "З А Т М Е Н И Е",
        "Т Е М Н О Т А",
        "Б А Б А Й К А",
        "К О Н Ф Е Т Ы",
        "Б Е Г О Т Н Я",
        "Н Е Б Ы Л И Ц А",
        "З А Г А Д К А",
        "П Р И В И Д Е Н И Е",
        "Г И П Н О З",
        "Т Е Л Е К И Н Е З",
        "П Ч Ё Л Ы",
        "Н О Ж Н И Ц Ы",
        "В Е С Е Л Ь Е",
        "Ж Ё Л Т Ы Й",
        "К Р А С Н Ы Й",
        "З Е Л Ё Н Ы Й",
        "Б Е Р Ё З К А",
        "К А Н И К У Л Ы",
        "С В Е Т И Л Ь Н И К",
        "Ч У П А К А Б Р А",
        "К О С М О Н А Ф Т",
        "М У З Ы К А",
        "К О Л Е Б А Н И Я",
        "Ф У Н К Ц И Я",
        "В О Л Н А",
        "Э Н Ц И К Л О П Е Д И Я",
        "А С Т Р О Н О М И Я",
        "Г Р И М А С С А",
        "К У Б И К",
        "М И К Р О С К О П",
        "К О С Т Ё Р",
        "М Е Д В Е Д Ь",
        "К О Л Ы Б Е Л Ь",
        "А В Т О Б У С",
        "К А С К А Д",
        "К О Ш К А",
        "С О Б А К А",
        "О Т О П Л Е Н И Е",
        "С О Н Л И В О С Т Ь",
        "Н Е Б О",
        "Я З Ы К",
        "С А Д",
        "Д О М",
        "К Р О Т",
        "С О Н",
        "С О М",
        "Ш Е Л Е С Т",
        "Х О Л О Д И Л Ь Н И К",
        "П О Л Я Р Н И К",
        "П И Н Г В И Н",
        "С О В А",
        "М О Р Ж",
        "М О Р Е",
        "Ш Т О Р М",
        "Г Р О М",
        "У Р А Г А Н",
        "Б У К В А Р Ь",
        "И Е Р О Г Л И Ф",
        "Н И Н Д З Я",
        "Т Е Н Ь",
        "М У Д Р О С Т Ь",
        "М Е Д И Т А Ц И Я",
        "С П О К О Й С Т В И Е",
        "П А Н И К А",
        "В О Д А",
        "Ч Ё Р Н Ы Й",
        "С В И Т Е Р",
        "О С Е Н Ь",
        "В Е С Н А",
        "З И М А",
        "Л Е Т О",
        "В Р Е М Я",
        "П Р А В Д А",
        "М Ы С Л Ь",
        "И Л Л Ю З И Я",
        "О Л Е Н Ь",
        "П Л А Н Е Т А",
        "Ф О Н О Т Е К А",
        ]
print(len(words))

def display():
    print(' '*30 + ''.join(table)+' '*25 +'Жизни: ' + ' '.join(lifes))

input(' '*50 + 'Доброго здравия' + 106*' '+ 'Низкий поклон' + 97*' ' + 'Нажмите <ЭНТЕР> чтобы Начать Игру\n')

while True:
    game = True
    lifes = ['<3', '<3', '<3','<3','<3','<3']
    count = 0
    place = 0
    table = []
    used = []
    word = random.choice(words)

    for i in word:
            if count%2==0:
                table.append('_')
            else:
                table.append(' ')
            count += 1
    display()

    while game:
        reply = (input('\n>Буква:')).upper()

        if reply in word and not reply in used:
                for letter in word:
                    if letter == reply and table[place] == '_':
                        table[place] = reply
                    place += 1
                place = 0
                display()
                used.append(reply)
            

        elif not reply in word and not reply in used:
                lifes.pop()
                print(' '*175 + '>>Нет!')
                if len(lifes)>=5 or len(lifes) == 0:
                    print(' '*165 + '>>У вас осталось {} Жизней.\n'.format(len(lifes)))
                elif len(lifes)>=2 and len(lifes)<5:
                    print(' '*165 + '>>У вас осталось {} Жизни.\n'.format(len(lifes)))
                else:
                    print(' '*165 + '>>У вас осталось {} Жизнь.\n'.format(len(lifes)))
                display()
                used.append(reply)

        elif reply in used:
            print(' '*175+'>>Было')

        if ''.join(table) == word:
            print(' '*170 + '>>Победа!')
            words.remove(word)
            used = []
            game = False

        elif len(lifes) == 0:
            print(' '*172 + '>>Поражение :(')
            print(' '*157 + '>> А   С Л О В О   Б Ы Л О  :  '+ word)
            used = []
            game = False
    
    replay = input(' '*170+ '>>Хотите сыграть ещё?\n>').lower()
    if replay == 'да' or replay == "":
        print('\n'*100)
        continue
    else:
        break