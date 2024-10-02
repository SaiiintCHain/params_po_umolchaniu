def send_mail(message, recipient, sender = "university.help@gmail.com"):
    if not('@'  in recipient and '@'  in sender and (recipient[-4:] == '.com' or recipient[-3:] == '.ru' or recipient[-4:] == '.net')):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
    elif not(sender[-4:] == '.com' or sender[-3:] == '.ru' or sender[-4:] == '.net'):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender, " на адрес " ,recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " ,sender, " на адрес " ,recipient)

send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

