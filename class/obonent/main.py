class obonent:
    def __init__(self):
        phonenumber = 'Идентификационный номер:' +input('Введите номер: ')
        name = 'Имя: '+input('Введите имя: ')
        surname = 'Фамилия: '+input('Введите фамилию: ')
        lastname = 'Отчество: '+input('Введите отчество: ')
        addres = 'Адрес проживания:' +input('Введите адрес проживания: ')
        cardnumber = 'Номер карты: '+input('Введите номер кредитной карточки: ')
        calltimecite = 'Время межгородних и городских звонков' +input('Введите продолжительность звонков: ')
        debet = 'дебет' +input('Введите расход')
        credit = 'кредит' +input('Ведите приход')
        self.obonent=[phonenumber, name,surname,lastname,addres,cardnumber,calltimecite,debet,credit]

    def setAttribute(self):
        attrnum=int(input('''Введите номер критерия,который желаете изменить
                          (1- номер телефона,
                          2-имя,
                          3-фамилия,
                          4-отчество,
                          5-адрес,
                          6-номер карты,
                          7-время звонка,
                          8-дебет,
                          9-кредит): '''))
        newattr=input('Введите новое значение критерия: ')
        if attrnum==1:
            self.obonent[attrnum-1]= 'Номер телефона: ' + newattr
        elif attrnum==2:
            self.obonent[attrnum-1]='Имя: '+ newattr
        elif attrnum==3:
            self.obonent[attrnum-1] = 'Фамилия: '+ newattr
        elif attrnum==4:
            self.obonent[attrnum-1] = 'Отчество: '+newattr
        elif attrnum==5:
            self.obonent[attrnum-1] = 'Адрес: '+newattr
        elif attrnum==6:
            self.obonent[attrnum-1] = 'Номер карты: '+newattr
        elif attrnum==7:
            self.obonent[attrnum-1] = 'Время звонка: '+newattr
        elif attrnum == 8:
            self.obonent[attrnum - 1] = 'Дебет: ' + newattr
        elif attrnum==9:
            self.obonent[attrnum-1] = 'Кредит: '+newattr
        else:
            print('Такой номер не найден')

    def seeAttributes(self):
        for i in range(6):
            print(self.obonent[i])