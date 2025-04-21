from telegram import Update
from telegram.ext import ApplicationBuilder, ChatMemberHandler, ContextTypes

TOKEN = "7007734626:AAHPKtSjQVI4IwPzUKybROeU8Xj1Sp8l5zI"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_member = update.chat_member.new_chat_member.user
    if new_member:
        message = (
            f"🍌 Benvenuto/a nella gilda *Banana Joe*, {new_member.first_name}!\n\n"
            "Qui non ci sono obblighi rigidi: siamo una gilda *no-stress*, "
            "quindi rilassati e gioca al tuo ritmo.\n"
            "Se vuoi e puoi investire, fallo nel cuore della gilda.\n\n"
            "⚠️ *Nota importante:*\n"
            "Se resti offline per più di *5 giorni* senza avvisare, potresti essere rimosso.\n"
            "Quindi, per favore, non sparire senza dire nulla!\n\n"
            "Per il resto, è solo un gioco: *divertiti!*\n"
            "💬 Se hai domande, trovi quasi sempre qualcuno online pronto ad aiutarti!"
        )
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=message,
            parse_mode="Markdown"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
app.run_polling()
