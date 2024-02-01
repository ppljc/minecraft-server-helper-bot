# <---------- Python modules ---------->
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


# <---------- Local modules ---------->
from config import TOKEN


# <---------- Main ---------->
storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode='html', disable_web_page_preview=True)
dp = Dispatcher(storage=storage)
