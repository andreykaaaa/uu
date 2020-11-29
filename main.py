str = input('введите стоку')
schet=0
for i in str:
    if i != ' ':
        schet+=1
    else:
        word=str[:schet]
        word=word[::-1]
        str=str[schet+1:]
        count = 0
        str2 = str
        for i in str:
            if i != ' ':
                schet +=1
            else:
                if str2.startswith(' '):
                    str2 =str2[1:]
                else:
                    str2 = str
                word2 = str2[:schet]
                schet = 0
                if word==word2:
                    print(word[::-1],word2)
                    word=''
                else:
                    word2=''