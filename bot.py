
import json

import random
import config 
import logging 
from aiogram import Bot, Dispatcher , executor , types 
import json
from itertools import groupby
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message:types.Message):
    if "артур" in message.text.lower():
        await message.answer('гей.')
    elif "шарп" in message.text.lower():
        await message.answer('шарпы - хуйня.')
    elif "питон" in message.text.lower():
        await message.answer('питон - лучший яп в мире кто не согласен Я САМ ЛИЧНО СВОИМ ТЯНОЧЬЕЙ КОРЕЯНСКОЙ ПИЗДОЙ ВЫЕБУ!!!😡🤬')
    elif "зуз" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, сучка.')
    elif "зизя" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, тварь.')
    elif "жизель" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, мудила.')
    elif "зайзел" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, выблядок.')
    elif "зюз" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, хуесос.')
    elif "зюб" in message.text.lower():
        await message.answer('моего хозяина зовут зизел, долбаёб.')
    elif "зизел" in message.text.lower().split():
        await message.answer('wassup on zyzel nu i hule')
    elif "зизель" in message.text.lower().split():
        await message.answer('вассап он зизель ну и хуле')        
    elif "лиза" in message.text.lower().split():
        await bot.send_photo(message.chat.id, "AgACAgIAAxkBAANHYpkZAnAIgpRXp9UHztleRnxMeP0AAjy-MRv9_8hI9g0qlT_9AZsBAAMCAANzAAMkBA")
    elif "нёрд" in message.text.lower():
        await message.answer('🤓')
    elif "влад рябко" in message.text.lower():
        await bot.send_document(message.chat.id, "CgACAgIAAx0CZcXuUgADq2KZGwABMKI2nRERkEloh6R_5w9L4QAC4hgAAj6t6Uh-U02HP1uiqyQE")
    elif "@yukateki" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD1mKZHIrefzvPBG-Oy2UWBczjNlvXAAI3AwAC8esMU6XYAwSp8MBzJAQ")
    elif "@icezyzel" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD3mKZHb55fnY5wvRraUV4xPzuZuQaAAKsAgACZ5zNUHr1a9RDJChCJAQ")
    elif "@nicourrrn" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD42KZHoMPHRumhWL1yJhXGrgGbEBaAAJnAwACPpgFU0nv6hWBbKB7JAQ")
    elif "@el_pokora" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD82KZH6NeJhTq8fI8GOu_umG6CNGJAAKYGAACZP6wSFN7dCjBJ6lAJAQ")
    elif "@littlegiant_10" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD_GKZIHI-D6XZFtpS5cmn_TyQgdUAAwwZAAIzEkhJmOC_UXCST14kBA")
    elif "@sintipae" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAQximSFWT513RHDqfqyJKKxstXX8RAACfw8AArds0EqjFxb-9jvKCiQE")
    elif "@chernyy_banan" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACASBimSHvvgABKwpdrDtoxzAmdMiMwigAArMLAAJzqflI5wYzXsnGC0skBA")
    elif "@fuerzzzaa" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgACATBimSNFe39NSsj-XRcV65tRKBk-2QACBwMAAiBovFLWX2-JsvDDnCQE")
    elif "@pustostas" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgACATZimSOsmqHFVN2CJd8a44QaaE3DCAACuQIAAjjvDFMtwbt_R8qPNyQE")
    elif "@michaeloffcherengo" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAVhimaqqzW1XcrVPFves25PkMxvzzAACdg0AAnmN2UqOvHiSpMGIciQE")
    elif "я стал сильнее" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAZ9im6imXIEHcBEC7sGmKMaqj-a0zwACQxwAAotY2EgW-___vFbCRCQE")
    elif "вахуи" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAfdinvVvXPDgFpoW04JtRQXZDCwYMQACGh0AAn-UEEgUCCzcx3vXbyQE")
    elif "@s1uns1337" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAfhin1Cup_f-nrlFv-tCC-emFtapVgAC5BkAAsBcAUks0B0e6E_23CQE")
    elif "@cyganboy13" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAflioPoybPYU_wZzFgJi3sbZHONw9AACAw8AAn-JSEiP1kAYpTJlRiQE")
    elif message.from_user.id == 490557903:#zyzel
        if "!delete" in message.text.lower().split():
            temp = message.text.lower().split()
            with open ('linkedin.json') as f:
                data = json.load(f)
            data.remove(temp[1])
            new_data = [el for el, _ in groupby(data)] 
            await message.answer('хозяин я делетнула линку (чтоб эти тупые долбаёбы умерли нахуй): ' + temp[1])
            with open ('linkedin.json','w') as f:
                json.dump(new_data,f)
        if "!gdelete" in message.text.lower().split():
            temp = message.text.lower().split()
            with open ('github.json') as f:
                data = json.load(f)
            data.remove(temp[1])
            new_data = [el for el, _ in groupby(data)] 
            await message.answer('хозяин я делетнула линку (чтоб эти тупые долбаёбы умерли нахуй): ' + temp[1])
            with open ('github.json','w') as f:
                json.dump(new_data,f)
        elif "иди нахуй" in message.text.lower():
            await bot.send_document(message.chat.id,'CgACAgIAAx0CZcXuUgACAzdiomH4Q2YIpJtimzGnVDvFMK9PowACRhAAAnxZeUp5RLAY5TaYgyQE')
    elif "алло ебать" in message.text.lower():
        await bot.send_document(message.chat.id,"BAACAgIAAx0CZcXuUgACAaRim69M8uxsS_WnJHakgld1Aae9FAACNQkAAjM7GEkoykGzR-96XCQE")
    elif "ви ка" == message.text.lower():
        await bot.send_document(message.chat.id,"BAACAgIAAx0CZcXuUgACAapim7F0cE79h6ovdNJO8mo0c3VmuwACZhcAAuqs4EirMbHq4GuUHiQE")
    elif "база" in message.text.lower().split():
        test_list = ["CgACAgIAAx0CZcXuUgACATlimSXwuoscWUkQltdmo0Tk6aGbzgACmxcAAu42YUtuO4SZI7w50iQE", "CgACAgIAAx0CZcXuUgACATpimSZSMZ2M8DFiT4UON7Qkmbbg5gACjxsAAiA3IEidnGeSKrmmTCQE", "CgACAgIAAx0CZcXuUgACATtimSdfkNDdoLfcTu040ELgrTNskgACRhUAAmsMeEtxNWPqeg7RQSQE",'CgACAgIAAx0CZcXuUgACATximSgPz29lkHaihwfnsZY1SEyL2AACKBoAAkyc6EoAAfyJFjgwAAHGJAQ','CgACAgQAAx0CZcXuUgACAUtimSkHuktKILXdj82NE5bJmFSMDAACGgMAAklQBVP0ZLyfgsgkOCQE','CgACAgIAAx0CZcXuUgACAzRiomEYobbK_u6H5EEAAbf7LjUQEpIAAh0YAAJZJllL9JdwsC7ZP2AkBA', 'CgACAgIAAx0CZcXuUgACAzViomEYAhJwI4vVG9mp66Tb60FHQQACDRgAAoNjWUvroCwN-II5BiQE']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_document(message.chat.id,test_list[random_index])
    elif "кринж" in message.text.lower().split():
        test_list = ['CgACAgIAAx0CZcXuUgACAxNiol_ZtJU3O1wtRC6AX5EO15rWpgACaRMAAunIaEgleZnx5BWgAAEkBA', 'CgACAgIAAx0CZcXuUgACAxRiol_ZQYeWi091c0rakyG8_p5PxQADGQACWUphS1W5V6vxpzTVJAQ', 'CgACAgIAAx0CZcXuUgACAxViol_ZKunX6vWdcjdm6HwLMmyr5gACjBYAAjsuWUtwwSFHwIil3CQE', 'CgACAgIAAx0CZcXuUgACAxZiol_ZX1mZz8IL_gzSu9ZI1RYgNgACDxsAAl8oGEgoqi7DhyYBriQE','CgACAgIAAx0CZcXuUgACAzNiomCbmLYOxQLSVfHPT0ZUUQWXgwACWhgAArr44Uq49WZr2BJkJiQE']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_document(message.chat.id,test_list[random_index])
    elif "!linkedin" == message.text.lower():
            with open ('linkedin.json') as f:
                data = json.load(f)
            out = '\n'.join(data)
            await message.answer(out)
    elif "!linkedin" in message.text.lower().split():
        temp = message.text.split()
        if 'https://www.linkedin.com/' in temp[1]:
            with open ('linkedin.json') as f:
                data = json.load(f)
            if temp[1] not in data:
                data.append(temp[1])        
                out = '\n'.join(data)
                await message.answer(out)
                with open ('linkedin.json','w') as f:
                    json.dump(data,f)
            else:
                await message.answer('такая линка уже есть')
        else:
            await message.answer('аллоу деревенский кусок дерьма кинь линку линкедина долбаёб сука а не высер свой ебучий')
    elif "!gihub" == message.text.lower():
            with open ('github.json') as f:
                data = json.load(f)
            out = '\n'.join(data)
            await message.answer(out)
    elif "!github" in message.text.lower().split():
        temp = message.text.split()
        if 'https://github.com/' in temp[1]:
            with open ('github.json') as f:
                data = json.load(f)
            if temp[1] not in data:
                data.append(temp[1])        
                out = '\n'.join(data)
                await message.answer(out)
                with open ('github.json','w') as f:
                    json.dump(data,f)
            else:
                await message.answer('такая линка уже есть')
        else:
            await message.answer('аллоу деревенский кусок дерьма кинь линку гитхаба долбаёб сука а не высер свой ебучий')
    elif "!json" == message.text.lower():
        doc = open('linkedin' + '.json', 'rb')
        doc1 = open('github' + '.json', 'rb')
        await message.reply_document(doc+doc1)
    elif "пон" in message.text.lower().split():
            test_list = ['CgACAgIAAx0CWXhUCAABAbizYqNRB-_6BHTuuT1bTz59ptDHPugAAoQTAALYDJhI_LlxEhT3fu4kBA', 'CgACAgIAAx0CWXhUCAABAbi0YqNRB7NX6-IcLsHVXJB7CmRgGT4AAqobAALyA2lImFjoiOPF1GckBA', 'CgACAgIAAx0CWXhUCAABAbi1YqNRBzKPWNp_tanRoRsiiH8YLUQAAj4XAAIbpsFK3_zDNXQoOrMkBA', 'CgACAgIAAx0CWXhUCAABAbi2YqNRBzPBO_q20or9itDgVkdC3PcAAr0XAAIWuJhIJCOR8cYaJSMkBA']
            random_index = random.randint(0, len(test_list) - 1)
            await bot.send_document(message.chat.id,test_list[random_index])



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
