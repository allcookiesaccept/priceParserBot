from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Keyboard:
    def __init__(self):
        self.categories = ['Смартфоны Xiaomi', 'Смартфоны Realme', 'Смартфоны Honor',]
        self.__activate_keyboard_lists()
        self.__activate_keyboard_chat_objects()
    def __activate_keyboard_lists(self):
        self.tasks = [[KeyboardButton(text=message)] for message in self.categories]


    def __activate_keyboard_chat_objects(self):

        self.TASK_TYPE = ReplyKeyboardMarkup(
            keyboard=self.tasks,
            resize_keyboard=True,
        )


keys = Keyboard()