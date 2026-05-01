from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou um bot com inteligência artificial. Me pergunte qualquer coisa! 🤖")

# Responde qualquer mensagem de texto
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_action(action="typing")
    texto = update.message.text
    response = client.models.generate_content(model="gemini-3-flash-preview", contents=texto)
    await update.message.reply_text(response.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot rodando...")
app.run_polling()