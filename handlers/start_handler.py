import time

from aiogram import types, Dispatcher
from create_bot import bot
import asyncio
from database.profile_db import check_args, create_profile, get_profile_language
from keyboards.client_kb import create_first_kb, create_second_kb, create_third_kb
from database.check_click_btn import get_data_from_button_clicks, insert_in_button_clicks, delete_data_from_button_clicks, increase_in_clicks
first_msg = {
    'ru': 'Добрый день! Рады приветствовать вас в официальном боте от топовой студии NRX \n\n Мы славимся самыми интересными и качественными видео с русскими тинками! Такие как gangbang, deep anal, pissdrink, rought и многие другие! Вы точно найдете для себя, то, что вам понравится',
    'en': 'Good afternoon! We are glad to welcome you to the official bot from the top studio NRX\n\n We are famous for the most interesting and high-quality videos with Russian tinkies! Such as gangbang, deep anal, pissdrink, rough and many others! You will definitely find something for yourself that you will like',
    'de': 'Guten Tag! Wir freuen uns, Sie im offiziellen Bot vom Top-Studio NRX willkommen zu heißen\n\n Wir sind berühmt für die interessantesten und hochwertigsten Videos mit russischen Tinks! Wie gangbang, deep Anal, pissdrink, rought und viele andere! Sie werden sicher etwas für sich selbst finden, das Ihnen gefällt',
    'es': '¡Buenos días! Estamos encantados de darle la bienvenida al bot oficial del estudio superior NRX\n\n¡Somos famosos por los videos más interesantes y de alta calidad con adolescentes rusos! Como gangbang, anal profundo, pissdrink, rought y muchos más! Seguro que encontrarás por TI mismo algo que te gustará',
    'pt': 'Boa tarde! Bem-vindo ao bot oficial do estúdio top NRX \n\n Nós somos famosos pelos vídeos mais interessantes e de alta qualidade com adolescentes russos! Como gangbang, deep anal, pissdrink, rought e muitos outros! Você definitivamente vai encontrar para si mesmo, o que você vai gostar',
    'iw': 'צהריים טובים! אנו שמחים לקבל את פניכם בבוט הרשמי של הסטודיו העליון של NRX \n\n אנו מפורסמים בסרטונים המעניינים והאיכותיים ביותר עם בני נוער רוסים! כגון gangbang, עמוק אנאלי, pissdrink, rought ורבים אחרים! אתה בהחלט תמצא לעצמך משהו שתאהב',
    'zh': '下午好！ 我们很高兴地欢迎您来到顶级工作室NRX的官方机器人。\n\n 我们是着名的最有趣和高品质的视频与俄罗斯小叮当！ 如钢棒，深肛门，pissdrink，粗糙和其他许多人！ 你一定会为自己找到你会喜欢的东西',
    'fr': "Bonjour! Nous sommes heureux de vous accueillir dans le bot officiel du TOP Studio NRX \n\n Nous sommes célèbres pour les vidéos les plus intéressantes et de haute qualité avec des jeunes russes! Comme gangbang, deep anal, pissdrink, rought et bien d'autres! Vous trouverez exactement pour vous-même quelque chose que vous aimerez",
    'it': 'Buongiorno! Benvenuti nel Bot ufficiale del top studio NRX \n\n Siamo famosi per i video più interessanti e di alta qualità con adolescenti russi! Come gangbang, deep anal, pissdrink, rought e molti altri! Troverai sicuramente per te, qualcosa che ti piacerà'
}
second_msg = {
    'ru': 'У нас есть замечательное предложение, всего за 22$ вы можете получить доступ к более чем 700 полным видео в формате 4к! Также вы первым получите доступ к новым видео, каждый месяц мы снимаем и выкладываем для вас более чем 20 новых роликов!',
    'en': 'We have a wonderful offer, for just $22 you can get access to more than 700 full 4k videos! You will also be the first to get access to new videos, every month we shoot and post more than 20 new videos for you!',
    'de': 'Wir haben ein wunderbares Angebot, für nur $ 22 können Sie auf mehr als 700 volle 4k-Videos zugreifen! Außerdem erhalten Sie als erster Zugang zu neuen Videos, wir filmen und veröffentlichen jeden Monat mehr als 20 neue Videos für Sie!',
    'es': '¡Tenemos una gran oferta, por solo$ 22 puedes acceder a más de 700 videos completos en 4K! Además, usted será el primero en tener acceso a los nuevos videos, cada mes filmamos y publicamos para usted más de 20 nuevos videos!',
    'pt': 'Temos uma oferta maravilhosa, por apenas 22$ Você pode acessar mais de 700 vídeos 4K completos! Além disso, você será o primeiro a ter acesso a novos vídeos, todos os meses gravamos e postamos para você mais de 20 novos vídeos!',
    'iw': 'יש לנו הצעה נפלאה, תמורת 22$ בלבד תוכלו לגשת ליותר מ-700 סרטוני 4k מלאים! כמו כן, תהיה הראשון לגשת לסרטונים חדשים, בכל חודש אנו מצלמים ומפרסמים עבורכם יותר מ -20 סרטונים חדשים!',
    'zh': '我们有一个很好的报价，只需22美元，你就可以获得超过700个完整的4k视频！ 您也将是第一个获得新视频的人，每个月我们都会为您拍摄和发布超过20个新视频！',
    'fr': 'Nous avons une excellente offre, pour seulement 22$ , vous pouvez accéder à plus de 700 vidéos complètes en 4K! En outre, vous êtes le premier à avoir accès à de nouvelles vidéos, chaque mois, nous tournons et postons pour vous plus de 20 nouvelles vidéos!',
    'it': 'Abbiamo una fantastica offerta, per soli$ 22 Puoi accedere a Oltre 700 video 4K completi! Inoltre, sarai il primo ad accedere a nuovi video, ogni mese giriamo e pubblichiamo più di 20 nuovi video per te!',
}
fourth_msg = {
    'ru': ', доброго времени суток! Успевайте получить доступ к нашим видео, пока действует акция!+ кнопка на сайт',
    'en': ', good time of day! Have time to get access to our videos while the promotion is in effect!+ button to the site',
    'de': ', gute Tageszeit! Haben Sie Zeit, auf unsere Videos zuzugreifen, während die Aktion läuft!+ schaltfläche zur Website',
    'es': ', ¡buen día! ¡Accede a nuestros vídeos mientras dure la promoción!+ botón en el sitio',
    'pt': ', bom dia! Acesse nossos vídeos enquanto a campanha está em andamento!+ botão no site',
    'iw': ', יום טוב! זמן לגשת לסרטונים שלנו בזמן שהקידום פועל!+ כפתור לאתר',
    'zh': '一天的好时机！ 在促销活动生效期间，有时间访问我们的视频！+按钮到网站',
    'fr': ", bonne journée! Ayez le temps d'accéder à nos vidéos pendant que l'action est en cours!+ bouton sur le site",
    'it': ', buona giornata! Avere il tempo di accedere ai nostri video mentre la promozione è attiva!+ pulsante al sito'
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
    await bot.send_message(message.from_user.id, first_msg[referer[1]], reply_markup=(await create_first_kb(language=referer[1])))
    await message.delete()
    await insert_in_button_clicks(message.from_user.id, message.from_user.first_name, now_time)
    await create_profile(message, my_referer=referer[0], language_interface=referer[1], registration_time=now_time)

async def view_second_text(call: types.CallbackQuery):
    user_id = call.from_user.id
    language = await get_profile_language(user_id)
    await delete_data_from_button_clicks(user_id)
    await increase_in_clicks('click_on_1_button', user_id, int(time.time()))
    await call.message.answer(second_msg[language], reply_markup=(await create_second_kb(language)))
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
