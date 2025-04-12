import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '8113500779:AAGbkj3qj3ePTziZ_hr3evBe4DJc7CO4TLI'  # 🔒

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
user_states = {}

# --- Главное меню ---
language_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇰🇿 Қазақша")],
    ],
    resize_keyboard=True
)

mode_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍🏫 Помощник по тригонометрии")],
        [KeyboardButton(text="📚 Учебный курс (пошаговое обучение)")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True
)

mode_menu_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍🏫 Тригонометрия бойынша көмекші")],
        [KeyboardButton(text="📚 Оқу курсы (кезеңмен оқыту)")],
        [KeyboardButton(text="🔙 Қайту")],
    ],
    resize_keyboard=True
)

helper_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Тригонометрическая таблица")],
        [KeyboardButton(text="📐 Тригонометрические формулы")],
        [KeyboardButton(text="📈 Тригонометрические функции")],
        [KeyboardButton(text="🧮 Формулы тригонометрических уравнений")],
        [KeyboardButton(text="⚖️ Тригонометрические неравенства")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True
)

helper_menu_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Тригонометриялық кесте")],
        [KeyboardButton(text="📐 Тригонометриялық формулалар")],
        [KeyboardButton(text="📈 Тригонометриялық функциялар")],
        [KeyboardButton(text="🧮 Тригонометриялық теңдеулердің формулалары")],
        [KeyboardButton(text="⚖️ Тригонометриялық теңсіздіктер")],
        [KeyboardButton(text="🔙 Қайту")],
    ],
    resize_keyboard=True
)

# --- Подменю формул ---
trig_formulas_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Основные тождества")],
        [KeyboardButton(text="Формулы приведения")],
        [KeyboardButton(text="Формулы сложения")],
        [KeyboardButton(text="Формулы перехода от произведения к сумме")],
        [KeyboardButton(text="Формулы двойного угла")],
        [KeyboardButton(text="Формулы тройного угла")],
        [KeyboardButton(text="Некоторые суммы")],
        [KeyboardButton(text="Формулы перехода от суммы к произведению")],
        [KeyboardButton(text="Формулы понижения степени")],
        [KeyboardButton(text="Формулы половинного угла")],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True
)

trig_formulas_menu_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Негізгі тепе-теңдіктер")],
        [KeyboardButton(text="Қосу формулалары")],
        [KeyboardButton(text="Көбейтіндіні қосындыға түрлендіру формулалары")],
        [KeyboardButton(text="Қос бұрыштың формулалары")],
        [KeyboardButton(text="Үш еселенген бұрыштың формулалары")],
        [KeyboardButton(text="Кейбір қосындылар")],
        [KeyboardButton(text="Қосындыны көбейтіндіге түрлендіру формулалары")],
        [KeyboardButton(text="Дәрежені төмендету формулалары")],
        [KeyboardButton(text="Жарты бұрыштың формулалары")],
        [KeyboardButton(text="🔙 Қайту")],
    ],
    resize_keyboard=True
)

# --- Картинки формул ---
formula_images = {
    "📊 Тригонометрическая таблица": "AgACAgIAAyEFAASegP1XAAMDZ_pCDBiGAAGfjLYJbgSDFz0N9EoGAALY7zEbEtzQS4kmmcDa3O4nAQADAgADeQADNgQ" ,
    "Основные тождества": "AgACAgIAAxkBAAPGZ_pc15laEIA7Tu-HXsHqmMBMY7YAApzuMRsVr9FLyoRE5LAdT7sBAAMCAAN4AAM2BA",
    "Формулы приведения": "AgACAgIAAxkBAAPWZ_peUsk587A8aOCXRiCzGByQDjQAApvuMRsVr9FLID02cSbULDkBAAMCAAN5AAM2BA",
    "Формулы сложения": "AgACAgIAAxkBAAPeZ_pfsq_0-NpJwEYJvEW4FPVeGbsAAm_uMRsVr9FL5hLinf7FxL8BAAMCAAN4AAM2BA",
    "Формулы перехода от произведения к сумме": "AgACAgIAAxkBAAPgZ_pfvtHgMpS8uCjgXFu8JpsKdn4AAnXuMRsVr9FLvcDg9n93XjYBAAMCAAN4AAM2BA",
    "Формулы двойного угла": "AgACAgIAAxkBAAPiZ_pfzXK720kgOPdeaiC2hLeWgoEAAnbuMRsVr9FLYMDq2S5slL4BAAMCAAN4AAM2BA",
    "Формулы тройного угла": "AgACAgIAAxkBAAPmZ_pf4xUtHa5768QL0ihym6OtQQQAAnnuMRsVr9FLq-r2dAMNnrcBAAMCAAN4AAM2BA",
    "Некоторые суммы": "AgACAgIAAxkBAAPaZ_pfcJx9PXt1pIW9Or2Lqg5LugoAAl_1MRt2ctFL4QjzIsxn96QBAAMCAAN4AAM2BA",
    "Формулы перехода от суммы к произведению": "AgACAgIAAxkBAAPkZ_pf1tcTJbooue_N052VQEIU-8UAAnfuMRsVr9FLV6caYSFui0wBAAMCAAN5AAM2BA",
    "Формулы понижения степени": "AgACAgIAAxkBAAPoZ_pf8qBWBqsOVqT8vcBkcWT5QLsAAn_uMRsVr9FL_jkCPvu4MpgBAAMCAAN4AAM2BA",
    "Формулы половинного угла": "AAgACAgIAAxkBAAPqZ_pf-x8Vy0F0DGMjWhwvwSjBfo0AAoHuMRsVr9FLJ3Q7x7z67fwBAAMCAAN5AAM2BA",
    "📊 Тригонометриялық кесте": "AgACAgIAAyEFAASegP1XAAMDZ_pCDBiGAAGfjLYJbgSDFz0N9EoGAALY7zEbEtzQS4kmmcDa3O4nAQADAgADeQADNgQ" ,
    "Негізгі тепе-теңдіктер": "AgACAgIAAxkBAAPGZ_pc15laEIA7Tu-HXsHqmMBMY7YAApzuMRsVr9FLyoRE5LAdT7sBAAMCAAN4AAM2BA",
    "Қосу формулалары": "AgACAgIAAxkBAAPeZ_pfsq_0-NpJwEYJvEW4FPVeGbsAAm_uMRsVr9FL5hLinf7FxL8BAAMCAAN4AAM2BA",
    "Көбейтіндіні қосындыға түрлендіру формулалары": "AgACAgIAAxkBAAPgZ_pfvtHgMpS8uCjgXFu8JpsKdn4AAnXuMRsVr9FLvcDg9n93XjYBAAMCAAN4AAM2BA",
    "Қос бұрыштың формулалары": "AgACAgIAAxkBAAPiZ_pfzXK720kgOPdeaiC2hLeWgoEAAnbuMRsVr9FLYMDq2S5slL4BAAMCAAN4AAM2BA",
    "Үш еселенген бұрыштың формулалары": "AgACAgIAAxkBAAPmZ_pf4xUtHa5768QL0ihym6OtQQQAAnnuMRsVr9FLq-r2dAMNnrcBAAMCAAN4AAM2BA",
    "Кейбір қосындылар": "AgACAgIAAxkBAAPaZ_pfcJx9PXt1pIW9Or2Lqg5LugoAAl_1MRt2ctFL4QjzIsxn96QBAAMCAAN4AAM2BA",
    "Қосындыны көбейтіндіге түрлендіру формулалары": "AgACAgIAAxkBAAPkZ_pf1tcTJbooue_N052VQEIU-8UAAnfuMRsVr9FLV6caYSFui0wBAAMCAAN5AAM2BA",
    "Дәрежені төмендету формулалары": "AgACAgIAAxkBAAPoZ_pf8qBWBqsOVqT8vcBkcWT5QLsAAn_uMRsVr9FL_jkCPvu4MpgBAAMCAAN4AAM2BA",
    "Жарты бұрыштың формулалары": "AAgACAgIAAxkBAAPqZ_pf-x8Vy0F0DGMjWhwvwSjBfo0AAoHuMRsVr9FLJ3Q7x7z67fwBAAMCAAN5AAM2BA",
}

# --- /start ---
@dp.message(F.text == "/start")
async def start(message: types.Message):
    user_id = message.from_user.id
    user_states[user_id] = {"lang": None, "mode": None, "history": []}
    await message.answer("Выберите язык / Тілді таңдаңыз:", reply_markup=language_menu)

# --- Выбор языка ---
@dp.message(F.text.in_(["🇷🇺 Русский", "🇰🇿 Қазақша"]))
async def select_language(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        user_states[user_id] = {"lang": None, "mode": None, "history": []}
    lang = "ru" if message.text == "🇷🇺 Русский" else "kz"
    user_states[user_id]["lang"] = lang
    user_states[user_id]["history"].append("lang_selected")

    if lang == "ru":
        await message.answer("Выберите режим работы:", reply_markup=mode_menu_ru)
    else:
        await message.answer("Жұмыс режимін таңдаңыз:", reply_markup=mode_menu_kz)

# --- Выбор режима ---
@dp.message(F.text.in_([
    "👨‍🏫 Помощник по тригонометрии", "👨‍🏫 Тригонометрия бойынша көмекші",
    "📚 Учебный курс (пошаговое обучение)", "📚 Оқу курсы (кезеңмен оқыту)"
]))
async def select_mode(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_states:
        user_states[user_id] = {"lang": None, "mode": None, "history": []}
    lang = user_states[user_id]["lang"]
    user_states[user_id]["history"].append("mode_selected")

    if "👨‍🏫" in message.text:
        user_states[user_id]["mode"] = "helper"
        if lang == "ru":
            await message.answer("Вы в режиме помощника 📋", reply_markup=helper_menu_ru)
        else:
            await message.answer("Сіз көмекші режиміндесіз 📋", reply_markup=helper_menu_kz)
    else:
        user_states[user_id]["mode"] = "course"
        await message.answer("Учебный курс в разработке 📘\nСкоро будет доступен.")

# --- Открытие подменю формул ---
@dp.message(F.text.in_([
    "📐 Тригонометрические формулы", "📐 Тригонометриялық формулалар"
]))
async def trig_formulas(message: types.Message):
    user_id = message.from_user.id
    lang = user_states.get(user_id, {}).get("lang", "ru")
    menu = trig_formulas_menu_ru if lang == "ru" else trig_formulas_menu_kz
    await message.answer("Выберите категорию формул:", reply_markup=menu)

# --- Отправка формул по кнопке ---
@dp.message(F.text.in_(formula_images.keys()))
async def send_formula(message: types.Message):
    formula = message.text
    file_id = formula_images.get(formula)
    await message.answer_photo(file_id, caption=f"<b>{formula}</b>")

@dp.message(F.text == "📊 Тригонометрическая таблица")
async def trig_table_ru(message: types.Message):
    file_id = formula_images.get("📊 Тригонометрическая таблица")
    if file_id:
        await message.answer_photo(file_id, caption="Тригонометрическая таблица 📊")
    else:
        await message.answer("Извините, таблица пока недоступна.")

@dp.message(F.text == "📊 Тригонометриялық кесте")
async def trig_table_kz(message: types.Message):
    file_id = formula_images.get("📊 Тригонометриялық кесте")
    if file_id:
        await message.answer_photo(file_id, caption="Тригонометриялық кесте 📊")
    else:
        await message.answer("Кесте табылмады.")

# --- Назад ---
@dp.message(F.text.in_(["🔙 Назад", "🔙 Қайту"]))
async def go_back(message: types.Message):
    user_id = message.from_user.id
    state = user_states.get(user_id)
    if not state:
        await message.answer("Вы уже в начале.", reply_markup=language_menu)
        return
    if not state["history"]:
        await message.answer("Вы уже в начале.", reply_markup=language_menu)
        return

    last = state["history"].pop()
    if last == "mode_selected":
        lang = state["lang"]
        await message.answer(
            "Выберите режим работы:" if lang == "ru" else "Жұмыс режимін таңдаңыз:",
            reply_markup=mode_menu_ru if lang == "ru" else mode_menu_kz
        )
    elif last == "lang_selected":
        await message.answer("Выберите язык / Тілді таңдаңыз:", reply_markup=language_menu)

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
