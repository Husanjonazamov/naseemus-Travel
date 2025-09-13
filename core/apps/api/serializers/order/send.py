import telebot
from django.conf import settings
from config.env import env
from core.apps.api.models import OrderModel, TourModel

bot = telebot.TeleBot(env.str("BOT_TOKEN"), parse_mode="HTML")


def order_created_handler(order, image_url):
    if not order:
        return

    # Tourni olish
    tour = None
    try:
        tour = TourModel.objects.get(id=order.tour_id)
    except TourModel.DoesNotExist:
        pass

    tour_info = ""
    print(image_url)
    print(tour)
    if tour:
        tour_info = (
            f"\n<b>🗺 Tur ma'lumotlari</b>\n"
            f"🏷 Nomi: <b>{tour.title}</b>\n"
            f"💵 Narxi: <b>{tour.price} $</b>\n"
        )
        if image_url:
            print(image_url)
            try:
                bot.send_photo(env("ADMIN"), image_url, caption=f"Tur rasmi: {tour.title}")
            except Exception as e:
                print(f"Tour rasmi yuborilmadi: {e}")

    # Order xabari
    message = (
        f"🆕 <b>Yangi buyurtma!</b>\n\n"
        f"👤 Ism: <b>{order.name}</b>\n"
        f"📞 Telefon: <b>{order.phone}</b>\n"
        f"📦 Soni: <b>{order.quantity}</b>\n"
        f"📅 Sana: <b>{order.data}</b>\n"
        f"💬 Izoh: <b>{order.comment or 'Yo‘q'}</b>\n"
        f"{tour_info}"
    )

    # Asosiy xabar yuborish
    try:
        bot.send_message(env.int("ADMIN"), message)
    except Exception as e:
        print(f"Telegram xato: {e}")
