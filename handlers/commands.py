from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.inline import inline_kb
from keyboards.reply import menu_keyboard
from keyboards.inline import case_battle, buy
#from handlers.callback import

win =0
matches =0
win_money=0
money=0
winstreak=0

command_router = Router()

@command_router.message(F.text == "Профиль 👤")
async def command_start_handler(message: Message) -> None:
    await message.answer(f'игрок {message.from_user.first_name}                 \n'
                         f'\n'
                         f'баланс {money}₽\n'
                         f'\n'
                         f'побед: {win}                                      \n'
                         f'максимальный винстрик: {winstreak}🔥\n'
                         f'всего матчей: {matches}                         \n'
                         f'призовые: {win_money}₽                          \n'
                         f'\n'  
                         f'/skins')

@command_router.message(F.text == "Пригласить соперника⚔️")
async def command_start_handler(message: Message) -> None:
    await message.answer("строго")

@command_router.message(F.text == "Кейсы 🎰")
async def command_start_handler(message: Message) -> None:
    await message.answer("🎁 Открывай кейсы и выигрывай крутые скины!\n "
                         "Каждый кейс — шанс получить редкий скин CS2 или деньги на баланс! Чем дороже кейс, тем ценнее награда.\n"
                         " 🔥 Открывай и тестируй удачу!", reply_markup=case_battle)

@command_router.message(F.text == "Поддержка 🚔")
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Поддержка 24/7 \n'
                         f'Возникли вопросы или проблемы? \n'
                         f'@cs2duel_support\n'
                         f'\n'
                         f' Решаем любые вопросы')

@command_router.message(F.text == "Пополнить баланс 💸")
async def give_money(message: Message) -> None:
    await message.answer("введите сумму которую хотите пополнить")
    try:
        if message >= 30:
            await message.answer(f'вы готовы оплатить сделку стоимостью{message}₽?', reply_markup=buy)
        else:
            await message.answer("введите корректную сумму больше чем 30₽!")
    except:
        await message.answer("некорректная сумма платежа!")



@command_router.message(F.text == "Вывод средств 💰")
async def command_start_handler(message: Message) -> None:
    await message.answer("строго")

@command_router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f'БОТ ЕЩЕ НЕ ГОТОВ!!!!✨ Добро пожаловать {message.from_user.first_name}!\n '
                         f'Здесь можно зарабатывать выигрывая дуэли в Conter-Strike 2\n'
                         f'❗️Чтобы продолжить, выбери команду на клавиатуре\n'
                         f'\n'
                         f'или используйте меню /menu',reply_markup=menu_keyboard)

@command_router.message(Command("about"))
async def command_start_handler(message: Message) -> None:
    await message.answer("я бот для дуэлей в кс2 на деньги", reply_markup=inline_kb)

@command_router.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    await message.answer("/start - начало работы\n"
                         "/about - о боте")

@command_router.message(Command("menu"))
async def command_start_handler(message: Message) -> None:
    await message.answer("/about - вас приветствует бот для дуэлей в \n"
                         "/help - о боте")

@command_router.message(F.sticker)
async def command_start_handler(message: Message) -> None:
    await message.answer("хахахахахаах")

@command_router.message(F.text == "😈")
async def command_start_handler(message: Message) -> None:
    await message.answer("строго")

@command_router.message(Command("about"))
async def command_start_handler(message: Message) -> None:
    await message.answer("я бот для дуэлей в кс2 на деньги", reply_markup=menu_keyboard)




