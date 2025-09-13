import os
import random
import logging
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,   # ✅ You were missing this import
    filters,
    ContextTypes,
)

# Set up logging for debugging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable (set on Render)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not set in environment variables")

# List of rizz lines (pickup lines/compliments)
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
    "You're the peanut butter to my jelly—irresistibly smooth.",
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming text messages and reply with a random rizz line."""
    rizz_reply = random.choice(RIZZ_LINES)
    await update.message.reply_text(rizz_reply)
    logger.info(f"Replied to {update.effective_user.id} with: {rizz_reply}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command with a welcome message."""
    await update.message.reply_text(
        f"Hey {update.effective_user.first_name}! I'm the Rizz Bot—here to spice up your chats with some charm. "
        "Send me any message, and I'll hit you with my best rizz! 😎"
    )

def main() -> None:
    """Set up and run the bot."""
    try:
        # Create the Application
        application = Application.builder().token(TOKEN).build()

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Start polling
        print("Rizz Bot is starting... 🚀")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()
