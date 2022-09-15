from random import randint


class Cat:
    cat_name = ''
    happy_img = "http://about-telegram.ru/wp-content/uploads/2018/03/kot-persik-stickers-telegram_27.png"
    sad_img = 'http://about-telegram.ru/wp-content/uploads/2018/03/kot-persik-stickers-telegram_03.png'
    sleep_img = 'http://about-telegram.ru/wp-content/uploads/2018/03/kot-persik-stickers-telegram_07.png'
    age = randint(1, 15)
    satiety = 0
    happiness = 0
    activity = 'бодрый'

    @staticmethod
    def set_activity(get_activity):
        if get_activity == 'sleep':
            Cat.activity = 'спит'
            return Cat.activity
        elif get_activity == 'play':
            Cat.activity = 'бодрый'
            return Cat.activity
        return Cat.activity

    @staticmethod
    def change_satiety(action):
        if Cat.satiety < 0:
            Cat.satiety = 0
            return Cat.satiety
        if action == "feed":
            Cat.satiety += 15
            return Cat.satiety
        elif action == "play":
            Cat.satiety -= 10
            return Cat.satiety
        return Cat.satiety

    @staticmethod
    def change_happiness(action):
        if action == "feed":
            Cat.happiness += 5
            return Cat.happiness
        elif action == "play":
            Cat.happiness += 15
            return Cat.happiness
        elif action == "play" and action == 'sleep':
            Cat.happiness -= 15
            return Cat.happiness
        elif Cat.satiety > 100:
            Cat.happiness -= 30
            return Cat.happiness
        elif Cat.satiety == 100:
            Cat.happiness = 0
            return Cat.happiness
        return Cat.happiness

    @staticmethod
    def change_image():
        if Cat.activity == 'спит':
            return Cat.sleep_img
        elif Cat.happiness in range(0, 40):
            return Cat.sad_img
        elif Cat.happiness in range(40, 101):
            return Cat.happy_img


cat = Cat()
