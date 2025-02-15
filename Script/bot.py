from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup # type: ignore
from telegram.ext import Application, CommandHandler, CallbackContext # type: ignore

# Remplace par ton token API
TOKEN = "7278624833:AAHpzcQrIHb2u-xC99HlGckd2Qe8UBqVTF0"

# URL de ton application AFRIQUE MONEY game
APP_URL = "https://t.me/Afriqueearnmoney_bot/gamebot"  # Remplace avec ton vrai lien

# Fonction pour démarrer le bot
async def start(update: Update, context: CallbackContext) -> None:
    """Répond au /start avec un message et un bouton vers l'application."""
    chat_id = update.message.chat_id
    message = "Bienvenue sur AFRIQUE MONEY, le bot qui vous récompense pour vos activités 😊 \n \n 🌍 AFRIQUE MONEY a été conçu dans le but d'aider les Africains à gagner de l'argent de façon simple et accessible à tous. \n 💰 0,5 FCFA par Tap. \n 🎮 Jouer à des mini-jeux afin d'augmenter vos revenus. \n 👬 Parrainez des amis et obtenu des bonus sur votre solde. \n 📝 Accomplissez des Tâches simples pour booster vos revenus. \n \n Lancez-vous dès maintenant et transformez chaque tap en une avancée vers votre réussite financière ! \n 🚀 Appuyez sur Start et convertissez chaque instant en opportunité de gains ! \n \n ✨ Avec AFRIQUE MONEY, chaque clic vous rapproche de la réussite financière !"

    # Bouton vers l'application
    keyboard = [[InlineKeyboardButton("🎮 DÉMARRER LE JEU ", url=APP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup, parse_mode="Markdown")

# Fonction pour afficher les infos du bot
async def info(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("ℹ️ *Informations du bot :*\n- Jouez à des mini-jeux\n- Gagnez des récompenses\n- Invitez des amis et gagnez plus !", parse_mode="Markdown")

# Fonction pour générer l'URL de parrainage
async def parrainage(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    referral_link = f"https://t.me/AfriqueMoneyBot?start={user_id}"
    await update.message.reply_text(f"🔗 *Votre lien de parrainage :*\n{referral_link}", parse_mode="Markdown")

# Fonction pour afficher le solde (à relier à ta base de données)
async def solde(update: Update, context: CallbackContext) -> None:
    fake_balance = 1000  # Remplace avec une requête à ta base de données
    await update.message.reply_text(f"💰 *Votre solde actuel :* {fake_balance} AFRI COINS", parse_mode="Markdown")

# Fonction pour indiquer où retirer les gains
async def retirer(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("📤 *Retrait :*\nVeuillez vous rendre sur l'application *AFRIQUE MONEY game* pour effectuer un retrait.", parse_mode="Markdown")

# Fonction pour afficher le menu avec les 4 boutons
async def menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["ℹ️ Info", "👥 Parrainage"],
        ["💰 Solde", "📤 Retirer"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🔽 *Menu principal* :", reply_markup=reply_markup, parse_mode="Markdown")

# Configurer le bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Ajouter les commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("parrainage", parrainage))
    app.add_handler(CommandHandler("solde", solde))
    app.add_handler(CommandHandler("retirer", retirer))
    app.add_handler(CommandHandler("menu", menu))

    # Lancer le bot
    print("✅ Bot en cours d'exécution...")
    app.run_polling()

if __name__ == '__main__':
    main()
