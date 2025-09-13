import os
import random
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not set")

# Flask app
app = Flask(__name__)

RIZZ_LINES = [
    "Are you a magician? Because whenever you're around, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "If you were a vegetable, you'd be a cute-cumber.",
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rizz_reply = random.choice(RIZZ_LINES)
    await update.message.reply_text(rizz_reply)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! I'm Rizz Bot. Send me a message!")

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Flask route for Telegram webhook
@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put_nowait(update)
    return "ok", 200

# Health check route
@app.route("/")
def home():
    return "Rizz Bot is live!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
