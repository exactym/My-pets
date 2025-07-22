import asyncio
from aiogram import Router, F
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums import ChatAction
import app.keyboards as kb
from app.keyboards import community_builder, CommunityPageCallback

router = Router()

#Обработчик команды Start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action = ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer(
        "Вас приветствует бот ФЕОР! Я призван для того, чтобы упростить вашу коммуникацию с ФЕОР.",
        reply_markup = kb.inline_main)

#Обработчик выбор общины 
@router.callback_query(F.data == 'communities')
async def communities(callback: CallbackQuery):
    await callback.answer('Вы выбрали отправку отчета. Пожалуйста, следуйте инструкциям.')
    await callback.message.edit_text('Пожалуйста, выберите вашу общину', reply_markup=await kb.community_builder())
   

@router.callback_query(F.data == 'communities')
async def communities(callback: CallbackQuery):
    await callback.answer('Выберите вашу общину')
    markup = await community_builder(page=0)  # Страница 0 при первом показе
    await callback.message.edit_text('Пожалуйста, выберите вашу общину', reply_markup=markup)

@router.callback_query(CommunityPageCallback.filter())
async def page_handler(callback: CallbackQuery, callback_data: CommunityPageCallback):
    page = callback_data.page
    markup = await community_builder(page=page)
    # Обновляем клавиатуру с новой страницей
    await callback.message.edit_reply_markup(reply_markup=markup)
    await callback.answer()

#Обработчик кнопки "назад" после выбора общины
@router.callback_query(F.data.startswith ('community_'))
async def communities(callback: CallbackQuery):
    await callback.answer('Вы выбрали общину')
    await callback.message.edit_text(f'Вы выбрали {callback.data}',
                                     reply_markup=kb.back)
