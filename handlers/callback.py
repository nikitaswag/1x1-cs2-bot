import random
import  aiogram
from aiogram import Router,F
from keyboards.inline import inline_kb, case_o_chek, case_battle, case_r_chek, case_i_chek, case_drop
from aiogram.types import CallbackQuery
import  sqlite3
from database import select_balance,popoln
from aiogram.types import Message
from aiogram.fsm.context import FSMContext



callbacks_router = Router()

@callbacks_router.callback_query(F.data == "query")
async def get_query(callback: CallbackQuery):
    await callback.message.answer(text="------")

@callbacks_router.callback_query(F.data == "case_o")
async def get_case_o(callback: CallbackQuery):
    await callback.message.edit_text(text="<b>🔹 Обычный (49₽)</b>", reply_markup= case_o_chek)

@callbacks_router.callback_query(F.data == "back")
async def get_case_o(callback: CallbackQuery):
    await callback.message.edit_text(text="🎁 Открывай кейсы и выигрывай крутые скины!\n "
                         "Каждый кейс — шанс получить редкий скин CS2 или деньги на баланс! Чем дороже кейс, тем ценнее награда.\n"
                         " 🔥 Открывай и тестируй удачу!",reply_markup= case_battle)

@callbacks_router.callback_query(F.data == "case_r")
async def get_case_o(callback: CallbackQuery):
    await callback.message.edit_text(text="<b>🔺 Редкий <s><i>(150₽)</i></s>(100₽)</b>", reply_markup= case_r_chek)

@callbacks_router.callback_query(F.data == "case_i")
async def get_case_o(callback: CallbackQuery):
    await callback.message.edit_text(text="<b>💎 Элитный (225₽)</b>", reply_markup= case_i_chek)

@callbacks_router.callback_query(F.data == "case_o_open")
async def get_case_o(callback: CallbackQuery):
    await callback.message.delete(text=f'Ваш дроп🔮: {random.randint(1,10000)}', reply_markup= case_drop)
    await callback.message.answer(text=f'Ваш дроп🔮: {random.randint(1, 10000)}', reply_markup=case_drop)

@callbacks_router.callback_query(F.data == "case_r_open")
async def get_case_o(callback: CallbackQuery):
    await callback.message.delete(text=f'Ваш дроп🔮: {random.randint(1, 10000)}', reply_markup=case_drop)
    await callback.message.answer(text=f'Ваш дроп🔮: {random.randint(1, 10000)}', reply_markup=case_drop)

@callbacks_router.callback_query(F.data == "case_i_open")
async def get_case_o(callback: CallbackQuery):
    await callback.message.delete(text=f'Ваш дроп🔮: {random.randint(1, 10000)}', reply_markup=case_drop)
    await callback.message.answer(text=f'Ваш дроп🔮: {random.randint(1, 10000)}', reply_markup=case_drop)



#@callbacks_router.callback_query(F.data == "sell")
#async def get_case_o(callback: CallbackQuery):
 #   await callback.message.answer(text="скин успешно продан! средсва занесены на баланс.")

#@callbacks_router.callback_query(F.data == "add")
#async def get_case_o(callback: CallbackQuery):
 #  await callback.message.answer(text="скин занесен в профиль")




@callbacks_router.callback_query(F.data.in_(["sell","add"]))
async def get_drop(callback: CallbackQuery):
    if callback.data == "sell":
        await callback.message.edit_text(text="скин успешно продан! средсва занесены на баланс.")
    else:
        await callback.message.edit_text(text="скин занесен в профиль")
    await callback.answer()


@callbacks_router.callback_query(F.data.in_(["ezmo","noy"]))
async def get_drop(callback: CallbackQuery,state: FSMContext):
    await callback.answer()
    if callback.data == "ezmo":
        await callback.message.edit_text(text="успешно")
        data = await state.get_data()
        popoln(callback.from_user.id, int(data['money']))
        return
    else:
        await callback.message.edit_text(text="отменено")
        return
#@callbacks_router.callback_query(F.data == "")

