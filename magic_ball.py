import random

answ = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
        "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
        "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
        "Перспективы не очень хорошие", "Весьма сомнительно", "Что пристал?", "Гугл Вам в помощь", "А я от куда знаю?",
        "Наденешь кастрюльку на голову — скажу", "42"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Вас зовут ')
print('Приветствую,', name, '!')

while True:
    print('О чем вопрошаете?')
    b = input()
    print(random.choice(answ))
    print('Еще вопросы? да/нет')
    b = input()
    if b == 'нет':
        print('Возвращайтесь если возникнут вопросы!')
        break
    else:
        continue
