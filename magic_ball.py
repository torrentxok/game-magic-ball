from random import *

answer = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')

userName = input('>')

print(f'Привет {userName}!')

while True:
    print('Жду твой вопрос)\n')
    input('>')
    print()
    print(f'>{choice(answer)}')
    print('Хочешь продолжить? Введи - да, или что-то другое, чтобы закрыть')
    if input('>').lower() == 'да':
        print('Ура! Вперед!!!')
        continue
    else:
        break

print('Возвращайся если возникнут вопросы!')