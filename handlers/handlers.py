from aiogram import Router, F
from keyboards.keyboards import keys
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, Update
from aiogram.filters import Command
from config.models import CSVFile
from aiogram import Dispatcher

class BotRouter(Router):
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        super().__init__()
        self.init_handlers()
        self.dp.message(self.dp.message.handlers, self.dp.message.filter)

    def init_handlers(self):
        self.message(Command("start"))(self.start_command)
        self.message(Command("xiaomi"))(self.parse_xiaomi)


    async def start_command(self, message: Message):
        await message.answer("Выбери бренд для парсинга?", reply_markup=keys.TASK_TYPE)


    async def parse_xiaomi(self, message: Message):
        await message.answer("Test")