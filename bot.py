import os, logging
import generator as gen
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level = logging.INFO)

printer = os.getenv('PRINTER')
bot = Bot(token = os.getenv('TOKEN'))
dp = Dispatcher(bot)

prev_msg = ''
number_entered = False
last_number = 0
last_messages = []
x, y, z, thickness = 0, 0, 0, 0

async def setup_cmd(dispatcher):
    bot_commands = [
        types.BotCommand(command='set', description='set the dimesnions'),
        types.BotCommand(command='print', description='print the box')
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands = 'start')
async def send_welcome(message: types.Message):
    await message.reply('Hi. I can make and print some box nets for you. Type /set to set the box\'s dimensions.')

@dp.message_handler(commands = 'set')
async def set_dimensions(message: types.Message):
    global prev_msg, x, y, z, thickness, last_messages, number_entered 
    if not number_entered:
        prev_msg = ''
    number_entered = False
    if not prev_msg:
        await message.answer('Please enter the width')
        prev_msg = 'width'
    elif prev_msg == 'width':
        x = last_number
        await message.answer('Please enter the depth')
        prev_msg = 'depth'
    elif prev_msg == 'depth':
        y = last_number
        await message.answer('Please enter the height')
        prev_msg = 'height'
    elif prev_msg == 'height':
        z = last_number
        await message.answer('Please enter the thickness of the material that you\'re going to print on (0 for paper)')
        prev_msg = 'thickness'
    else:
        thickness = last_number
        await message.answer(f'Generated a box {x}x{y}x{z}mm. Use /print to print!')
        prev_msg = ''
        last_messages.clear()

@dp.message_handler(commands = 'print')
async def print(message: types.Message):
    gen.x, gen.y, gen.z, gen.thickness = x, y, z, thickness
    result = gen.main()
    if not result:
        await message.answer('The box is too large for this printer 😥')
        return
    #os.system(f'inkscape --without-gui --export-pdf=output.pdf output.svg&&lp -d {printer} output.pdf')
    await message.answer('OK')

@dp.message_handler(lambda message: message.text.isdigit())
async def get_number(message: types.Message):
    global last_number, last_messages, number_entered 
    last_number = int(message.text)
    last_messages += message 
    number_entered = True
    await set_dimensions(message)

@dp.message_handler()
async def idk(message: types.Message):
    await message.answer('Please enter a *valid* number or a *valid* command!', 'markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = setup_cmd)
