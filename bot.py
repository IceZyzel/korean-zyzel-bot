import random
import config
import logging
from aiogram import Bot, Dispatcher, types
import asyncio

# Инициализация бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()

haunted_users = {}

@dp.message()
async def echo(message: types.Message):
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
        if "!хаунт" in message.text.lower():
            temp = message.text.split()
            if len(temp) > 1:
                haunt_text = ' '.join(temp[1:])
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    haunted_users[user_id] = haunt_text
                    await message.answer("пизда тебе ))))0")
                else:
                    await message.answer("реплайни челика зизь")
        if "!схаунт" in message.text.lower() and message.reply_to_message:
            user_id_to_remove = message.reply_to_message.from_user.id
            if user_id_to_remove in haunted_users:
                del haunted_users[user_id_to_remove]
                await message.answer(f"живи браток)")
            else:
                await message.answer(f"нема такого")

    if message.from_user.id in haunted_users:
        haunt_text = haunted_users[message.from_user.id]
        await message.reply(haunt_text)
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
    if "ньорд" in message.text.lower():
        await message.answer('🤓')
    if "нерд" in message.text.lower():
        await message.answer('🤓')
    if "влад рябко" in message.text.lower():
        await bot.send_document(message.chat.id, "CgACAgIAAx0CZcXuUgADq2KZGwABMKI2nRERkEloh6R_5w9L4QAC4hgAAj6t6Uh-U02HP1uiqyQE")
    if "@ultrawtrs" in message.text.lower():
        await bot.send_document(message.chat.id,'CgACAgIAAxkBAAIGa2MI0NghvPHfYYSJg_Im7T8mbOLpAAJUHwACrBhJSMfgkRLPRBC-KQQ')
    if "@caramel_pie" in message.text.lower():
        await bot.send_document(message.chat.id,'CgACAgQAAxkBAAIKs2TT5WUgaPdkr7kHNsL6etW-lwABMwACfwgAApnEIFDe7Unb49LOjTAE')
    if "@icezyzel" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD3mKZHb55fnY5wvRraUV4xPzuZuQaAAKsAgACZ5zNUHr1a9RDJChCJAQ")
    if "@nicourrrn" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgAD42KZHoMPHRumhWL1yJhXGrgGbEBaAAJnAwACPpgFU0nv6hWBbKB7JAQ")
    if "@porki_privat" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD82KZH6NeJhTq8fI8GOu_umG6CNGJAAKYGAACZP6wSFN7dCjBJ6lAJAQ")
    if "@littlegiant_10" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgAD_GKZIHI-D6XZFtpS5cmn_TyQgdUAAwwZAAIzEkhJmOC_UXCST14kBA")
    if "@aez4kmi_h3soy4m" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIJY2TRRc9q864mmt2f4laiRBGljZI1AALCMAACy7thSylxDNM_B6w_MAQ")
    if "@baseowner" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAIJcGTRRvJzAAGcaiVaSLpZTT5L-aadMgACLgMAAqBgBVOXjs1v4XOKDzAE")
    if "@kolyasik_o" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAIJbWTRRorHqhDYXpRQ8V7XTMNUhiMFAAL1AgACTh4sU3c2ZNBhQfKgMAQ")
    if "@a626hd" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIJeWTRSFHsYHgAAVeLCSsCD7wFMNEPtAACESYAAqgFyUmADRnLEMI4KzAE")
    if "@vindyt" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIJg2TRTS1IiysikPA8HZTI0OuOTFRfAAJjIAACF7_RSCrzIBnlOeuHMAQ")
    if "@d_borisovna" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAIJf2TRSxlEO-LmkV3gme4IFIY98WLiAAJ0AwACu3kcUoIsuaLHusqFMAQ")  
    if "@rezzny4" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAxkBAAIJgGTRTFSoJRboe6XoQ93zFoiU-qxdAAJCMQACEmTwSDu26X4pdMEeMAQ")   
    if "@sintipae" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAQximSFWT513RHDqfqyJKKxstXX8RAACfw8AArds0EqjFxb-9jvKCiQE")
    if "@chernyy_banan" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACASBimSHvvgABKwpdrDtoxzAmdMiMwigAArMLAAJzqflI5wYzXsnGC0skBA")
    if "@cold_semen" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAx0CZcXuUgACATBimSNFe39NSsj-XRcV65tRKBk-2QACBwMAAiBovFLWX2-JsvDDnCQE")
    if "@pustostas" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAII4mOi3TNfpP-qWeeGHukIS_p_9gFEAAKdAwACo-FtUG2NMLEZyJYsLAQ")
    if "@michaeloffcherengo" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgIAAx0CZcXuUgACAVhimaqqzW1XcrVPFves25PkMxvzzAACdg0AAnmN2UqOvHiSpMGIciQE")
    if "@BaseOwner" in message.text.lower():
        await bot.send_document(message.chat.id,"CgACAgQAAxkBAAIJRWTRQFkUKh8rLeguKAyiBZ8fUlF8AAIuAwACoGAFU5eOzW_hc4oPMAQ")
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
    if "пидор" in message.text.lower().split():
        test_list = ['CgACAgIAAxkBAAIKuGTY928KyZ1lg1RiEU6mY4LxFzq2AAL4FgACqHcRSyVyURiYfsvCMAQ', 'CgACAgIAAxkBAAIKuWTY93-iITiRnTSWXIQlPPl5NjlIAAL6FwAC0uP5SrktL7X6x29BMAQ', 'CgACAgIAAxkBAAIKumTY9385Dt832UCI1tRblswUSQXHAAKkIAACYfLBS4r7hMSzBQlIMAQ', 'CgACAgIAAxkBAAIKu2TY93-dsz7W9celvSY_0S7bQze9AAJmEQAC0fhZSnej2wsn5g7YMAQ', 'CgACAgIAAxkBAAIKvGTY93-CNRPcPJ4ETKpr2K1aKCR2AAKSEQACTCjJS39TlQMw0gm7MAQ', 'CgACAgIAAxkBAAIKvWTY938skL4lq1OyRJc8-4fy8cJvAAIdIQACG2LhS4R2kFX9yD35MAQ']
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

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
