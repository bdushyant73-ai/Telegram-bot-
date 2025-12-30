from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8575745782:AAHgTbIm8k22Achf1LbaG6wGxAmXraQOwvs
OWNER_ID = 123456789  # apna Telegram user id yahan daalo

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    await update.message.reply_text("✅ Private bot active hai")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    await update.message.reply_text("🏓 Pong")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))

app.run_polling()
