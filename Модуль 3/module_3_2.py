import re


def send_email(message: str, recipient: str, *, sender: str = 'university.help@gmail.com') -> int:
    email_pattern = r'.+@.+\.(ru|com|net)'
    if (not re.search(email_pattern, recipient)) or (not re.search(email_pattern, sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return 1

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return 2

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    return 0


send_email('123', 'vap42.t@mail.r')
send_email('123', 'university.help@gmail.com')
send_email('123', 'vap42.t@mail.ru')
send_email('123', 'vap42.t@mail.ru', sender='vlad.popov.99.t@gmail.com')
