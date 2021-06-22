import os, sys
from aiogram import executor
from config import *


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=False)


