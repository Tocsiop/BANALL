from pyrogram import Client

# Your bot token
API_ID = "ENTER_API_ID"
API_HASH = "ENTER_HASH_ID"
BOT_TOKEN = "ENTER_BOT_TOKEN"

# Initialize the pyrogram client
bot = Client(
    "channel_ban_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message()
async def ban_all_members(bot, message):
    if message.text.startswith("/start"):
        await message.reply_photo(
                            photo = f"https://telegra.ph/file/fff2ee6f504bc061cb7d3.jpg",
                            caption = f'''
нєү folks,

тнιѕ ιѕ α ѕιмρℓє вαи αℓℓ вσт ωнι¢н ιѕ вαѕє∂ σи ρуяσgяαм ℓιвєяαяу тσ вαи σя ∂єѕтяσү αℓℓ тнє мємвєяѕ ғяσм α gяσυρ ωιтн ιи α ғєω ѕє¢σи∂ѕ!

тσ ¢нє¢к му αвιℓιту gιв мє ғυℓℓ ρσωєяѕ

туρє /ʙᴀɴᴀʟʟ тσ ѕєє мαgι¢ ιи gяσυρ & ¢нαииєℓ
''',
)
# Handler to ban all members of the channel & group
@bot.on_message()
async def ban_all_members(bot, message):
    if message.text.startswith("/banall"):
        # Get the channel ID
        channel_id = message.chat.id
        
        # Get all members of the channel
        async for member in bot.get_chat_members(channel_id):
            try:
                # Ban each member
                await bot.ban_chat_member(channel_id, member.user.id)
            except Exception as e:
                print(f"Failed to ban user: {member.user.username}, Error: {e}")

# Start the bot
bot.run()
