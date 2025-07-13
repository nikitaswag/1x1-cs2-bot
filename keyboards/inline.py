from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть кейс 🔓", callback_data="query")],
        [InlineKeyboardButton(text="Открыть кейс 🔓", url="https://assets.lis-skins.com/market_images/40000_b.png")]
    ]
)

case_battle = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔹 Обычный (49₽)", callback_data="case_o"), InlineKeyboardButton(text="🔺 Редкий (100₽)", callback_data="case_r")],
        [InlineKeyboardButton(text="💎 Элитный (225₽)", callback_data="case_i")]
    ]
)

case_o_chek = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть кейс 🔓", callback_data="case_o_open")],
        [InlineKeyboardButton(text="вернутся назад", callback_data="back")]
    ]
)

case_r_chek = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть кейс 🔓", callback_data="case_r_open")],
        [InlineKeyboardButton(text="вернутся назад", callback_data="back")]
    ]
)

case_i_chek = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть кейс 🔓", callback_data="case_i_open")],
        [InlineKeyboardButton(text="вернутся назад", callback_data="back")]
    ]
)
case_drop = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Продать за ()", callback_data="sell")],
        [InlineKeyboardButton(text="Добавить в профиль➕", callback_data="add")]
    ]
)
buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отменить сделку ❌", callback_data="sell")],
        [InlineKeyboardButton(text="Оплатить✅", callback_data="add")]
    ]
)