from aiogram.fsm.state import State, StatesGroup
from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import random
from keyboards.inline import buyy, case_battle
from database import popoln

fsm_router = Router()
class Form(StatesGroup):
    plusdenga = State()
    win = State()
    matches = State()
    win_money = State()
    money = State()
    winstreak = State()
    vivod = State()
    perevod = State()

@fsm_router.message(F.text == "Пополнить баланс 💸")
async def buy(message: Message, state: FSMContext):
    await message.answer("напишите сумму пополнения")
    await state.set_state(Form.money)


@fsm_router.message(Form.money)
async def buy(message: Message, state: FSMContext):
    try:
        if int(message.text) > 30:
            await state.update_data(money=message.text)
            data = await state.get_data()
            await message.answer(text=f"вы готовы оплатить счет стоимостью {data['money']}.{random.randint(10,99)}₽?",reply_markup=buyy)
            popoln(message.from_user.id, int(message.text))
        else:
            await message.answer(text="минимальная сумма пополнения 30₽")
            await message.answer("напишите сумму пополнения")

    except:
        await message.answer(text="ошибка. введите корректную цифру")
        await message.answer("напишите сумму пополнения")


@fsm_router.message(F.text == "Поддержка 🚔")
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Поддержка 24/7 \n'
                         f'Возникли вопросы или проблемы? \n'
                         f'@cs2duel_support\n'
                         f'\n'
                         f' Решаем любые вопросы')


@fsm_router.message(F.text == "Вывод средств 💰")
async def buy(message: Message, state: FSMContext):
    await message.answer("напишите сумму вывода")
    await state.set_state(Form.vivod)


@fsm_router.message(Form.vivod)
async def buy(message: Message, state: FSMContext):
    try:
        if int(message.text) > 30:
            await state.update_data(money=message.text)
            data = await state.get_data()
            await message.answer(text=f"успешно выведено {data['money']}₽")
        else:
            await message.answer(text="минимальная сумма вывода 30₽")
            await message.answer("напишите сумму вывода")
    except:
        await message.answer(text="ошибка. введите корректную цифру")
        await message.answer("напишите сумму вывода")