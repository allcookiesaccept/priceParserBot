from aiogram import Router, F
from keyboards.keyboards import keys
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, Update
from aiogram.filters.text import Text
from aiogram.filters import Command
from config.models import CSVFile
from services.manager import Manager
from aiogram import Dispatcher

class BotRouter(Router):
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        super().__init__()
        self.init_handlers()
        self.dp.message(self.dp.message.handlers, self.dp.message.filter)

    def init_handlers(self):
        self.message(Command("start"))(self.start_command)
        self.message(Text(text=keys.categories))(self.parse_phones)


    async def start_command(self, message: Message):
        await message.answer("Выбери бренд для парсинга?", reply_markup=keys.PHONE_BRANDS)


    async def parse_phones(self, message: Message):

        manager = Manager(message.text)
        file_path = manager()
        input_file = FSInputFile(file_path)

        if input_file:
            await message.answer_document(input_file)
        else:
            await message.answer("Не удалось собрать файл. Попробуйте еще раз.")



