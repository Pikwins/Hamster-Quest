print("Добро пожаловать в мир бравл старс!!! Вы можете получить много гемов либо остаться без аккаунта")
while True:
    print("Давайте создадим вашего бравляра!")
    name = input("Введите име вашего бравлера!")
    gender = input("какой пол вашего бравлера?:")
    class_bs = input("Выберите класс вашего бравлера:")
    print("Ваш выбор:")
    print("Имя: ", name)
    print("Пол бравлера:", gender)
    print("Класс бравлера:", class_bs)
    start_game = input("Вы хотите начать игру с этим персонажем?  (да/нет)")
    if start_game == "да":
        print("Начнём игру!")
        break
    else:
        print("Сосздадим персонажа заново!")
        continue
print("-" * 50)
while True:
    print("Вы оказались в мире бравл старс.Перед Вами есть три пути: Шд, Горячая зона и Лоби")
    print("Куда вы направитесь?")
    place = input("Напиши название места:")
    if place.lower() == "шд":
        print("Ты попал в шд.Тут бравлеры сражаются за первое место,чтобы поучаствовать ролик мистера биста")
        print("Ты хочешь загрузится в шд?")
        shd = input("Да или нет")
        if shd == "да":
            print("В шд на вас из кустов выбежала шели с ультой и с 10 банками")
            print("вы умерли")
            break
        elif shd == "нет":
            print("Вы видите как диномайка убивает шели с ультой лудше к ней не идти")
            continue
    elif place.lower() == "горячая зона":
        print("теперь ты попал в горячую зону.Тут надо захватывают свою зону и отбиваться от противников")
        print("ты хочешь загрузится в горячую зону")
        hot_point = input("Да или нет")
        if hot_point == "да":
            print("Вы приблизелись к зоне противников")
            print("на вас прыгает элпримо и вас раздавливает")
            break
        elif hot_point == "нет"
            


    elif place.lower() == "лоби":
        print("это лоби.Тут надо прокачивать своего бравлера")
        print("хочешь загрузится в лоби")
    else:
        print("Такого места нет!")
