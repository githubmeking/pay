from telegram import Update, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Telegram API bilgileri
API_ID = '21507798'
API_HASH = 'c8bd80ec22e3d92c0ee4561cbf7d6611'
BOT_TOKEN = '8157852847:AAH6X4hutw5nPMQdWbyJ4PkCgh-h0eFIKTk'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hoş Geldin! /pay ile ödeme seçeneklerini görebilirsiniz.")

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("200 Star", callback_data='200')],
        [InlineKeyboardButton("400 Star", callback_data='400')],
        [InlineKeyboardButton("1600 Star", callback_data='1600')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Lütfen bir ödeme seçeneği seçin:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    amount = int(query.data)
    title = f"{amount} Star"
    description = f"{amount} Star için ödeme"
    payload = "{}"
    currency = "XTR"
    prices = [LabeledPrice(label=title, amount=amount)]

    invoice_link = await context.bot.create_invoice_link(
        title,
        description,
        payload,
        "",
        currency,
        prices,
    )

    await query.message.reply_text(f"{amount} Star için ödeme yapmak için [buraya tıklayın]({invoice_link})", parse_mode='Markdown')

# Uygulamayı oluştur
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Komutları ekle
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pay", pay))
app.add_handler(CallbackQueryHandler(button))

# Botu çalıştır
app.run_polling()
