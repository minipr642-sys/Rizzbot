from flask import Flask, request
import os
import telegram
import random

app = Flask(__name__)

# Get the Telegram bot token from environment variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")

bot = telegram.Bot(token=TOKEN)

# List of rizz lines
RIZZ_LINES = [
    "Are you a magician? Because whenever you're around, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Is your name Wi-Fi? Because I'm feeling a connection.",
    "You must be tired because you've been running through my mind all day.",
    "Are you French? Because Eiffel for you.",
    "Do you like raisins? How about a date?",
    "If beauty were time, you'd be eternity.",
    "Your hand looks heavy—let me hold it for you.",
    "Are you a parking ticket? Because you've got FINE written all over you.",
    "I must be a snowflake because I've fallen for you.",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "You're like my favorite notification—always making me smile.",
    "If I could rearrange the alphabet, I'd put U and I together.",
    "You must be the reason why the stars shine at night.",
    "Is your aura made of glitter? Because you're absolutely sparkling.",
    "I'd say you're the bomb, but that might be too explosive for a first chat.",
    "You had me at hello—now keep me with that rizz!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "You're the peanut butter to my jelly—irresistibly smooth."
]

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Parse the incoming webhook update
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        if update and update.message:
            chat_id = update.message.chat.id
            # Send a random rizz line
            reply = random.choice(RIZZ_LINES)
            bot.send_message(chat_id=chat_id, text=reply)
        return "ok", 200
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return "error", 500

@app.route("/")
def health():
    return "Bot is running!", 200

# Set webhook on startup (optional)
if __name__ == "__main__":
    # For local testing, you can set the webhook manually or here
    # Replace with your Render URL or use ngrok for local testing
    webhook_url = "https://your-service.onrender.com/webhook"
    bot.set_webhook(url=webhook_url)
    app.run(debug=True)
