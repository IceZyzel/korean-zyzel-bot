
import json
import random
import config 
import logging 
from aiogram import Bot, Dispatcher , executor , types 
import asyncio
logging.basicConfig(level=logging.INFO)
PROXY_URL = "http://proxy.server:3128"

bot = Bot(token=config.token,proxy=PROXY_URL)
dp = Dispatcher(bot)

    
@dp.message_handler()
async def echo(message:types.Message):
    if message.from_user.id == 490557903:#zyzel
        if "!json" == message.text.lower():
            doc = open('linkedin' + '.json', 'rb')
            doc1 = open('github' + '.json', 'rb')
            await message.reply_document(doc)
            await message.reply_document(doc1)
        if "!алло" in message.text.lower().split():
            temp = message.text.split()
            for i in range(10):
                await asyncio.sleep(0.1)
                await message.answer(temp[1])           
        if "!pin" in message.text.lower():
            await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id) 
        if "!unpin"  in message.text.lower():
            await bot.unpin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
        if "иди нахуй" in message.text.lower():
            await bot.send_document(message.chat.id,'CgACAgIAAx0CZcXuUgACAzdiomH4Q2YIpJtimzGnVDvFMK9PowACRhAAAnxZeUp5RLAY5TaYgyQE')

        if "стфу" in message.text.lower().split():
            await bot.send_document(message.chat.id,'BAACAgIAAxkBAAIGaGMIzqiu10nfXN7BxZ546BllVdfuAALsHgACY_FJSIY7W5TNTMrhKQQ')

        if "завали ебало" in message.text.lower():
            await bot.send_document(message.chat.id,'BAACAgIAAxkBAAIGaGMIzqiu10nfXN7BxZ546BllVdfuAALsHgACY_FJSIY7W5TNTMrhKQQ')
    if "артур" in message.text.lower():
        await message.answer('гей.')
    if "зуз" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, сучка.')
    if "зизя" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, тварь.')
    if "жизель" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, мудила.')
    if "зайзел" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, выблядок.')
    if "зюз" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, хуесос.')
    if "зюб" in message.text.lower():
        await message.reply('моего хозяина зовут зизел, долбаёб.')
    if "пон" in message.text.lower().split():
        test_list = ['CgACAgIAAx0CWXhUCAABAbizYqNRB-_6BHTuuT1bTz59ptDHPugAAoQTAALYDJhI_LlxEhT3fu4kBA', 'CgACAgIAAx0CWXhUCAABAbi0YqNRB7NX6-IcLsHVXJB7CmRgGT4AAqobAALyA2lImFjoiOPF1GckBA', 'CgACAgIAAx0CWXhUCAABAbi1YqNRBzKPWNp_tanRoRsiiH8YLUQAAj4XAAIbpsFK3_zDNXQoOrMkBA', 'CgACAgIAAx0CWXhUCAABAbi2YqNRBzPBO_q20or9itDgVkdC3PcAAr0XAAIWuJhIJCOR8cYaJSMkBA',"CgACAgIAAxkBAAICuGL1Xa73R7rOF5NmnARTVSzpBkXlAAJXGgACbrZgSnbkkHj9tim0KQQ"]
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_document(message.chat.id,test_list[random_index])
    if "зизел" in message.text.lower().split():
        await message.answer('wassup on zyzel nu i hule')
    if "зизель" in message.text.lower().split():
        await message.answer('вассап он зизель ну и хуле')        
    if "нёрд" in message.text.lower():
        await message.answer('🤓')
    if "влад рябко" in message.text.lower():
        await bot.send_document(message.chat.id, "CgACAgIAAx0CZcXuUgADq2KZGwABMKI2nRERkEloh6R_5w9L4QAC4hgAAj6t6Uh-U02HP1uiqyQE")
    if "@yukateki" in message.text.lower():
        await bot.send_document(message.chat.id,'CgACAgIAAxkBAAIGa2MI0NghvPHfYYSJg_Im7T8mbOLpAAJUHwACrBhJSMfgkRLPRBC-KQQ')
    if "@icezyzel" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD3mKZHb55fnY5wvRraUV4xPzuZuQaAAKsAgACZ5zNUHr1a9RDJChCJAQ")
    if "@nicourrrn" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD42KZHoMPHRumhWL1yJhXGrgGbEBaAAJnAwACPpgFU0nv6hWBbKB7JAQ")
    if "@el_pokora" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD82KZH6NeJhTq8fI8GOu_umG6CNGJAAKYGAACZP6wSFN7dCjBJ6lAJAQ")
    if "@littlegiant_10" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD_GKZIHI-D6XZFtpS5cmn_TyQgdUAAwwZAAIzEkhJmOC_UXCST14kBA")
    if "@sintipae" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAQximSFWT513RHDqfqyJKKxstXX8RAACfw8AArds0EqjFxb-9jvKCiQE")
    if "@chernyy_banan" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACASBimSHvvgABKwpdrDtoxzAmdMiMwigAArMLAAJzqflI5wYzXsnGC0skBA")
    if "@fuerzzzaa" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgACATBimSNFe39NSsj-XRcV65tRKBk-2QACBwMAAiBovFLWX2-JsvDDnCQE")
    if "@pustostas" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAII4mOi3TNfpP-qWeeGHukIS_p_9gFEAAKdAwACo-FtUG2NMLEZyJYsLAQ")
    if "@michaeloffcherengo" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAVhimaqqzW1XcrVPFves25PkMxvzzAACdg0AAnmN2UqOvHiSpMGIciQE")
    if "я стал сильнее" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAZ9im6imXIEHcBEC7sGmKMaqj-a0zwACQxwAAotY2EgW-___vFbCRCQE")
    if "вахуи" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAfdinvVvXPDgFpoW04JtRQXZDCwYMQACGh0AAn-UEEgUCCzcx3vXbyQE")
    if "@s1uns1337" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAfhin1Cup_f-nrlFv-tCC-emFtapVgAC5BkAAsBcAUks0B0e6E_23CQE")
    if "@cyganboy13" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAflioPoybPYU_wZzFgJi3sbZHONw9AACAw8AAn-JSEiP1kAYpTJlRiQE")
    if 'тильт' in message.text.lower():
        await bot.send_video(message.chat.id,"BAACAgIAAx0CZcXuUgACB5dits21_MOMjgvn65aJHmNZ7cWI9AACZxsAAh9xuEnpOCdX-xHCmCkE")
    if "лмао" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIBAmLIiNr_49BKfE8_kfl6YJu6yLuMAAJkCQAC1QGJSwSkXkrsXBvJKQQ")
    if "тазашо" in message.text.lower():
        await bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAIGxGMZ4a4vCT27b1Lnvclt5ffns3NaAAJqFQACVyvZSsvjJsaP91x4KQQ")
    if "алло ебать" in message.text.lower():
        await bot.send_document(message.chat.id,"BAACAgIAAx0CZcXuUgACAaRim69M8uxsS_WnJHakgld1Aae9FAACNQkAAjM7GEkoykGzR-96XCQE")
    if "отчислен" in message.text.lower():
        await bot.send_video(message.chat.id,'BAACAgIAAxkBAAIIGGNlVUhCNP1POscBdMFAZ01mljFFAAIKKAAC3mwpSwP0rJyZiaUfKgQ')
    if "ви ка" == message.text.lower():
        await bot.send_document(message.chat.id,"BAACAgIAAx0CZcXuUgACAapim7F0cE79h6ovdNJO8mo0c3VmuwACZhcAAuqs4EirMbHq4GuUHiQE")
    if "база" in message.text.lower().split():
        test_list = ["CgACAgIAAx0CZcXuUgACATlimSXwuoscWUkQltdmo0Tk6aGbzgACmxcAAu42YUtuO4SZI7w50iQE", "CgACAgIAAx0CZcXuUgACATpimSZSMZ2M8DFiT4UON7Qkmbbg5gACjxsAAiA3IEidnGeSKrmmTCQE", "CgACAgIAAx0CZcXuUgACATtimSdfkNDdoLfcTu040ELgrTNskgACRhUAAmsMeEtxNWPqeg7RQSQE",'CgACAgIAAx0CZcXuUgACATximSgPz29lkHaihwfnsZY1SEyL2AACKBoAAkyc6EoAAfyJFjgwAAHGJAQ','CgACAgQAAx0CZcXuUgACAUtimSkHuktKILXdj82NE5bJmFSMDAACGgMAAklQBVP0ZLyfgsgkOCQE','CgACAgIAAx0CZcXuUgACAzRiomEYobbK_u6H5EEAAbf7LjUQEpIAAh0YAAJZJllL9JdwsC7ZP2AkBA', 'CgACAgIAAx0CZcXuUgACAzViomEYAhJwI4vVG9mp66Tb60FHQQACDRgAAoNjWUvroCwN-II5BiQE']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_document(message.chat.id,test_list[random_index])
    if "кринж" in message.text.lower().split():
        test_list = ['CgACAgIAAx0CZcXuUgACAxNiol_ZtJU3O1wtRC6AX5EO15rWpgACaRMAAunIaEgleZnx5BWgAAEkBA', 'CgACAgIAAx0CZcXuUgACAxRiol_ZQYeWi091c0rakyG8_p5PxQADGQACWUphS1W5V6vxpzTVJAQ', 'CgACAgIAAx0CZcXuUgACAxViol_ZKunX6vWdcjdm6HwLMmyr5gACjBYAAjsuWUtwwSFHwIil3CQE', 'CgACAgIAAx0CZcXuUgACAxZiol_ZX1mZz8IL_gzSu9ZI1RYgNgACDxsAAl8oGEgoqi7DhyYBriQE','CgACAgIAAx0CZcXuUgACAzNiomCbmLYOxQLSVfHPT0ZUUQWXgwACWhgAArr44Uq49WZr2BJkJiQE']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_document(message.chat.id,test_list[random_index])
    if "я не буду это комент" in message.text.lower():
        await bot.send_document(message.chat.id, "CgACAgIAAx0CZcXuUgACBpBiqK6-h73Tq1fWi6AEDK2yAkIOkAACnSYAAsCMuUgdo5ObtVy33CQE")
    if "помянем" in message.text.lower().split():
        test_list = ['CAACAgIAAxkBAAIDp2L5aD5RIhPxKaz8VEWzSA2pSRgIAAKFAANlogMsD-IBskLS9VQpBA', 'CAACAgIAAxkBAAIDqGL5aD7vOf6mJvIRePtgwJbaLZWJAAKZAQACPHbiFt2GdX-_DndrKQQ', 'CAACAgIAAxkBAAIDqWL5aD6k09cKXTZ0DhH28y8mflZIAAI1AANmS8sWgI3Dny1JWHcpBA']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_sticker(message.chat.id,test_list[random_index])
    if "вумен" in message.text.lower().split():
        test_list = ['CAACAgIAAxkBAAIGxWMZ4yn6XtBMY36B3yleNnIM4z4pAAL8HAAC1k-oSBQUeDMCTAmnKQQ', 'CAACAgIAAxkBAAIGxmMZ4ynsiBYpKgWI6sYAAb0ukpTcAgAC1BgAAmD7qEhMwshGiPStjikE', 'CAACAgIAAxkBAAIGx2MZ4yrpYxdAGgfXLh-hEAMarc4MAAKRGQACOgeoSBFGGxhpwCU8KQQ', 'CAACAgIAAxkBAAIGyGMZ4yvjLWb-T1Z92iZUt2KlEo6JAAI2GwACWC-pSGo2wNWyvr46KQQ', 'CAACAgIAAxkBAAIGyWMZ4yumVuL96dJa2C9EJS575mLqAAJXGgACnAKgSGBvcAsIIgiZKQQ', 'CAACAgIAAxkBAAIGymMZ4yzHmB2Va7X_eCdmHHWs-KjUAAI9GQACqaqgSGxXbTuPBYYOKQQ', 'CAACAgIAAxkBAAIGy2MZ4y0OA3xe_lB6ctg1pj3iSQMxAAKFGwACHQyoSP_gdoxB3m4OKQQ', 'CAACAgIAAxkBAAIGzGMZ4y3kdQRQewmzMmEAATs7Ikv2QwACdBgAAhPXoEjcK-hfrqv4fSkE', 'CAACAgIAAxkBAAIGzWMZ4y4LqE0MOKFuSQABXvV2kHcLEwACZhcAAtqjqUh0oftJO3WtGSkE', 'CAACAgIAAxkBAAIGzmMZ4y_OUMIkvRqjL2MqL_EqPvdxAAL2FwACRBmpSNj4BRfGmoy1KQQ', 'CAACAgIAAxkBAAIGz2MZ4zCw6RbH_LdBFFlaE3EiwXgiAALkGQACU7WpSICRrN5YOHC4KQQ', 'CAACAgIAAxkBAAIG0GMZ4zDuEx00zchgU2rrxJFNs3kwAAKPFQACtoagSC8rOhLCAeWpKQQ', 'CAACAgIAAxkBAAIG0WMZ4zJJhSeYh9kOrPyXG1DvstGlAAK6HAACpQmpSE11cS1XxGzpKQQ', 'CAACAgIAAxkBAAIG0mMZ4zVInECaNdi-HkvAobwMGJSlAAIGGQAC8N6oSDNIpcPBM1ldKQQ', 'CAACAgIAAxkBAAIG02MZ4zXDQOFn861FVGnMScpBNuvEAAIwGwACmRepSLvwsEyr_QXLKQQ', 'CAACAgIAAxkBAAIG1GMZ4zbQOp8odT3ujahIrq_fzRCiAALqFwAC3fqoSMygnQUBWL0VKQQ', 'CAACAgIAAxkBAAIG1WMZ4zc2PS_EDCegH-2Wv3zDsaORAALYHAACzyegSGXkXANQaBhXKQQ', 'CAACAgIAAxkBAAIG1mMZ4zeVbIKORBNntpyUt8rOfD4hAAIpGwAClw6gSCKFIae5gr0AASkE', 'CAACAgIAAxkBAAIG12MZ4zjXHkRNbhd5bAiucgxHIIgeAAIQGwACYy-pSBV8dQJ0ICxPKQQ', 'CAACAgIAAxkBAAIG2GMZ4zkCly6XgF8XOKqK9WaXTLmWAAI8GQAC_N6oSDldO9vWsVXBKQQ']
        random_index = random.randint(0, len(test_list) - 1)
        await bot.send_sticker(message.chat.id,test_list[random_index])
    if "скрин души" == message.text.lower():
        await bot.send_document(message.chat.id,"AwACAgQAAxkBAAIISWOiZFORjuPMMgIIMoDC2v5hWIqSAAKHDAACSQYQUUJN2T4QKpu1LAQ")
    if "f" == message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIGsWMRzR6zCHgqcaE8RwLkIT0mIl9VAALbAQACC694SzsjDdHw_t_rKQQ")
    if "ф" == message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIGsWMRzR6zCHgqcaE8RwLkIT0mIl9VAALbAQACC694SzsjDdHw_t_rKQQ")
    if "@vivileetrn" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAIIvmOi25bGy1f0K5HtRo1gX9D9VerCAAKOCAACInBgUfMoxt_5QxH3LAQ")
    if "!линк" == message.text.lower():
        await message.reply('СПИСКИ ВСЕХ ПРЕДМЕТОВ СОКРАЩЁННО \n тймс \n вдоит \n бд \n лмвз \n гейдев \n кп \n аккм')
    if "!линк" in message.text.lower().split():
        temp = message.text.split()
        if temp[1]=='тймс'.lower():
            await message.answer("https://meet.google.com/ttj-gprj-guf")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=302859")
        if temp[1]=='вдоит'.lower():
            await message.answer("https://meet.google.com/tkw-zozt-uug")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=303249")
        if temp[1]=='бд'.lower():
            await message.answer("https://meet.google.com/zqd-xgqu-hxh")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=314827")
        if temp[1]=='лмвз'.lower():
            await message.answer("https://meet.google.com/frb-ovub-gfg")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=303129")
        if temp[1]=='гейдев'.lower():
            await message.answer("https://meet.google.com/tjh-drdd-owh")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=303123")
        if temp[1]=='кп'.lower():
            await message.answer("https://meet.google.com/fzx-omeg-iee")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=302925")
        if temp[1]=='аккм'.lower():
            await message.answer("https://meet.google.com/wja-srgz-ktq")
            await message.reply("отметься сразу😉 \n https://dl.nure.ua/mod/attendance/view.php?id=302715")    
    if "!linkedin" == message.text.lower():
            with open ('linkedin.json') as f:
                data = json.load(f)
            out = '\n'.join(data)
            await message.answer(out)
    if "!linkedin" in message.text.lower().split():
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
                await message.reply('такая линка уже есть')
        else:
            await message.reply('аллоу деревенский кусок дерьма кинь линку линкедина долбаёб сука а не высер свой ебучий')
    if message.new_chat_members[0]:
        await message.reply_video(message.chat.id, 'BAACAgIAAxkBAAIBe2L09W7Yew8fSTOoy5m9l9TamVaIAAJ7HgACNKypS230eFjJoOEDKQQ')
    if "!github" == message.text.lower():
            with open ('github.json') as f:
                data = json.load(f)
            out = '\n'.join(data)
            await message.answer(out)
    if "!github" in message.text.lower().split():
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
                await message.reply('такая линка уже есть')
        else:
            await message.reply('аллоу деревенский кусок дерьма кинь линку гитхаба долбаёб сука а не высер свой ебучий')

    else:
        pass    



@dp.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message:types.Message):
    new_member = message.new_chat_members[0]
    await bot.send_video(message.chat.id, 'BAACAgIAAxkBAAIBf2L0-T_vyWsTlav5x8PXAAH06uzNGQACex4AAjSsqUtt9HhYyaDhAykE')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

