import time

from aiogram import types, Dispatcher
from create_bot import bot
import asyncio
from database.profile_db import check_args, create_profile, get_profile_language
from keyboards.client_kb import create_first_kb, create_second_kb, create_third_kb
from database.check_click_btn import get_data_from_button_clicks, insert_in_button_clicks, delete_data_from_button_clicks, increase_in_clicks
first_msg = {
    'ru': 'Добрый день! Рады приветствовать вас в официальном боте от топовой студии NRX🔥\n\nМы славимся самыми интересными и качественными видео с русскими подростками💕\n\nТакими как групповуха, глубокий анал, моча, грубость и многое другое другие! \n\nВы обязательно найдете для себя что-то, что вам понравится😎',
    'en': 'Good afternoon! We are glad to welcome you to the official bot from the top studio NRX🔥\n\nWe are famous for the most interesting and high-quality videos with Russian teens💕\n\nSuch as gangbang, deep anal, pissdrink, rough and many others! \n\nYou will definitely find something for yourself that you will like😎',
    'de': 'Guten Tag! Wir freuen uns, Sie im offiziellen Bot des Top-Studios NRX begrüßen zu dürfen 🔥\n\nWir sind bekannt für die interessantesten und qualitativ hochwertigsten Videos mit russischen Teenagern💕 \n\nWie Gangbang, Deep Anal, Pissdrink, Rough und viele mehr andere!\n\nSie werden bestimmt etwas für sich finden, das Ihnen gefällt😎',
    'es': '¡Buenas tardes! Nos complace darle la bienvenida al bot oficial del excelente estudio NRX 🔥\n\nSomos famosos por los videos más interesantes y de alta calidad con adolescentes rusos💕 \n\nComo gangbang, anal profundo, bebida de orina, sexo duro y muchos más. ¡Otros!\n\nDefinitivamente encontrarás algo para ti que te gustará😎',
    'pt': 'Boa tarde! Temos o prazer de recebê-lo no bot oficial do estúdio top NRX 🔥\n\nSomos famosos pelos vídeos mais interessantes e de alta qualidade com adolescentes russos💕 \n\nComo gangbang, anal profundo, pissdrink, áspero e muitos outros!\n\nVocê certamente encontrará algo de que irá gostar😎',
    'iw': 'אחר הצהריים טובים! אנו שמחים לארח אותך אל הבוט הרשמי מהאולפן המוביל NRX 🔥 \n\n אנו מפורסמים בזכות הסרטונים המעניינים והאיכותיים ביותר עם בני נוער רוסים💕 \n\n כגון gangbang, deep anal, pissdrink, rough ורבים אחרים!\n\n בהחלט תמצא משהו לעצמך שתאהב😎',
    'zh': '下午好！ 我們很高興歡迎您來到來自頂級工作室 NRX 的官方機器人 🔥\n\n我們以與俄羅斯青少年最有趣和高質量的視頻而聞名💕 \n\n如輪姦、深肛、小便、粗暴等等其他！\n\n你一定會找到自己喜歡的東西😎',
    'fr': "Bon après-midi! Nous sommes heureux de vous accueillir sur le bot officiel du meilleur studio NRX 🔥\n\nNous sommes célèbres pour les vidéos les plus intéressantes et de haute qualité avec des adolescents russes💕 \n\nTelles que gangbang, anal profond, pissdrink, rugueux et bien d'autres les autres !\n\nVous trouverez certainement quelque chose pour vous qui vous plaira😎",
    'it': 'Buon pomeriggio! Siamo lieti di darti il benvenuto nel bot ufficiale dello studio NRX 🔥\n\nSiamo famosi per i video più interessanti e di alta qualità con adolescenti russi💕 \n\nCome gangbang, anal profondo, pissdrink, violenti e molti altri altri!\n\nTroverai sicuramente qualcosa per te che ti piacerà😎',
}
second_msg = {
    'ru': 'У нас выгодное предложение, всего за 22$ вы можете получить доступ к более чем 700 полноценным 4к видео😎 \n\nТакже вы будете первыми, кто получит доступ к новым видео, каждый месяц мы снимаем и публикуем для вас более 20 новых видео ❗',
    'en': 'We have a favorable offer, for just $22 you can get access to more than 700 full 4k videos😎\n\nYou will also be the first to get access to new videos, every month we shoot and post more than 20 new videos for you❗️',
    'de': 'Wir haben ein günstiges Angebot, für nur 22 US-Dollar erhalten Sie Zugriff auf mehr als 700 vollständige 4K-Videos. 😎 \n\nSie erhalten außerdem als Erster Zugriff auf neue Videos. Jeden Monat drehen und veröffentlichen wir mehr als 20 neue Videos für Sie ❗',
    'es': 'Tenemos una oferta favorable, por solo $22 puedes obtener acceso a más de 700 videos completos en 4k😎 \n\nTambién serás el primero en obtener acceso a nuevos videos, cada mes grabamos y publicamos más de 20 videos nuevos para ti. ❗',
    'pt': 'Temos uma oferta favorável, por apenas US$ 22 você pode ter acesso a mais de 700 vídeos completos em 4k😎 \n\nVocê também será o primeiro a ter acesso a novos vídeos, todos os meses filmamos e publicamos mais de 20 novos vídeos para você ❗',
    'iw': 'יש לנו הצעה משתלמת, תמורת $22 בלבד תוכלו לקבל גישה ליותר מ-700 סרטונים מלאים ב-4K😎 \n\n גם אתם תהיו הראשונים לקבל גישה לסרטונים חדשים, בכל חודש אנו מצלמים ומפרסמים יותר מ-20 סרטונים חדשים עבור אתה❗',
    'zh': '我們有優惠，只需$22你就可以觀看超過700個完整的4k視頻😎 \n\n你也將是第一個獲得新視頻的人，每個月我們都會為你拍攝和發布超過20個新視頻❗',
    'fr': 'Nous avons une offre avantageuse, pour seulement 22 $, vous pouvez accéder à plus de 700 vidéos 4K complètes😎 \n\nVous serez également le premier à avoir accès à de nouvelles vidéos, chaque mois nous tournons et publions plus de 20 nouvelles vidéos pour vous ❗',
    'it': "Abbiamo un'offerta vantaggiosa, per soli $ 22 puoi avere accesso a più di 700 video completi in 4K😎 \n\nSarai anche il primo ad avere accesso a nuovi video, ogni mese giriamo e pubblichiamo più di 20 nuovi video per te ❗",
}
fourth_msg = {
    'ru': ', доброго времени суток! \nУспейте получить доступ к нашим видео, пока действует акция🕖',
    'en': ', good time of day! \nHave time to get access to our videos while the promotion is in effect🕖',
    'de': ', gute Zeit! \nHaben Sie Zeit, Zugriff auf unsere Videos zu erhalten, während die Aktion in Kraft ist🕖',
    'es': ', buen momento del día! \nTen tiempo para acceder a nuestros videos mientras la promoción esté vigente🕖',
    'pt': ', boa hora do dia! \nTenha tempo para ter acesso aos nossos vídeos enquanto a promoção estiver em vigor🕖',
    'iw': "ג'ון, שעה טובה ביום! \nתהיה לך זמן לקבל גישה לסרטונים שלנו בזמן שהמבצע בתוקף🕖",
    'zh': '，今天的好時光！ \n促銷期間有時間觀看我們的視頻🕖',
    'fr': ", bon moment de la journée ! \nAyez le temps d'accéder à nos vidéos pendant que la promotion est en vigueur🕖",
    'it': ', buon momento della giornata! \nAvere tempo per accedere ai nostri video mentre la promozione è in vigore🕖'
}
five_msg = {
    'ru': 'Переходи по ссылке',
    'en': 'Follow the link',
    'de': 'Klicke auf den Link',
    'es': 'Sigue el enlace',
    'pt': 'Clique aqui',
    'iw': 'עקוב אחר הקישור',
    'zh': '按照链接',
    'fr': 'Suivez le lien',
    'it': 'Segui il link'
}

async def command_start(message: types.Message):
    args = message.get_args() # /start 123123
    now_time = int(time.time())
    referer = await check_args(args, str(message.from_user.id))
    # await bot.send_message(message.from_user.id, first_msg[referer[1]], reply_markup=(await create_first_kb(language=referer[1])))
    photo_url = 'imgs/first.jpg'
    with open(photo_url, 'rb') as photo_file:
        await bot.send_photo(photo=photo_file, chat_id=message.from_user.id,
                             caption=first_msg[referer[1]],
                             reply_markup=(await create_first_kb(language=referer[1])))

    await message.delete()
    await insert_in_button_clicks(message.from_user.id, message.from_user.first_name, now_time)
    await create_profile(message, my_referer=referer[0], language_interface=referer[1], registration_time=now_time)

async def view_second_text(call: types.CallbackQuery):
    user_id = call.from_user.id
    language = await get_profile_language(user_id)
    await delete_data_from_button_clicks(user_id)
    await increase_in_clicks('click_on_1_button', user_id, int(time.time()))
    # await call.message.answer(second_msg[language], reply_markup=(await create_second_kb(language)))
    photo_url = 'imgs/second.jpg'
    with open(photo_url, 'rb') as photo_file:
        await bot.send_photo(photo=photo_file, chat_id=call.from_user.id,
                             caption=second_msg[language],
                             reply_markup=(await create_second_kb(language)))

    await bot.answer_callback_query(call.id)
async def check_and_send():
    while True:
        # print(f'Метка 1. Время сейчас: {time.time()}')
        for user_id, first_name, click_time in (await get_data_from_button_clicks()):
            current_time = int(time.time())
            # click_time = datetime.fromisoformat(click_time_str)
            # print(f'Метка 2. Время сейчас: {current_time}, current_time - click_time: {current_time} - {click_time}')
            if current_time - int(click_time) >= 10:
                # print(f'Метка 3. Время сейчас: {time.time()}')
                language = await get_profile_language(user_id)
                await bot.send_message(user_id, f"{first_name}{fourth_msg[language]}", reply_markup=(await create_first_kb(language)))
                await delete_data_from_button_clicks(user_id)
        await asyncio.sleep(3)  # Проверка каждые 5 минут
async def view_third_text(call: types.CallbackQuery):
    user_id = call.from_user.id
    language = await get_profile_language(user_id)
    await call.message.answer("👇 " + five_msg[language] + " 👇", reply_markup=(await create_third_kb(language)))
    await increase_in_clicks('click_on_2_button', user_id, int(time.time()))
    await bot.answer_callback_query(call.id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(view_second_text, text=['view_second_text'])
    dp.register_callback_query_handler(view_third_text, text=['view_third_text'])
