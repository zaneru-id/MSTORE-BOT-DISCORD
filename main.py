import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import Embed, ui
from nextcord.interactions import Interaction
import os

TOKEN = 'BOT TOKEN' 
AUTHORIZED_USER_IDS = "USER ID"
GUILD_ID = "GUILD ID"
CATEGORY_ID = "CATEGORY ID"
LOG_CHANNEL_IDS = "LOG CHANNEL ID"
COUNTER_FILE = "ticket_counter.txt"

MANAGE_TICKET_USER_IDS = "PERMISSION USER ID"
 

intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

def get_next_ticket_number():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("1")
    with open(COUNTER_FILE, "r") as f:
        current = int(f.read().strip())
    with open(COUNTER_FILE, "w") as f:
        f.write(str(current + 1))
    return current

async def change_bot_activity():
    activities = [
        nextcord.Activity(type=nextcord.ActivityType.watching, name="MSTORE"),
        nextcord.Activity(type=nextcord.ActivityType.listening, name="Spotify")
    ]

    while True:
        for activity in activities:
            try:
                await bot.change_presence(activity=activity, status=nextcord.Status.do_not_disturb)
            except Exception as e:
                print(f"Failed to change presence: {str(e)}")
            await asyncio.sleep(35)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} Now is online. Made by zaneru.id')
    bot.add_view(PersistentFischView())
    bot.loop.create_task(change_bot_activity())


class PersistentFischView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FischDropdown())

class FischDropdown(nextcord.ui.Select):
    def __init__(self):
        options = [
            nextcord.SelectOption(label="Joki Level", value="joki_level", description="List Joki Level", emoji="📋"),
            nextcord.SelectOption(label="Joki Rod", value="joki_rod", description="List Joki Rod", emoji="📋"),
            nextcord.SelectOption(label="Item Crafting", value="item_craft", description="Bahan Crafting Rod", emoji="📋"),
            nextcord.SelectOption(label="Enchant Relic", value="enchant_relic", description="Enchant Relic & Exalted Relic", emoji="📋"),
            nextcord.SelectOption(label="Order Account", value="order_account", description="Order Account Rod + Enchant", emoji="📋"),
            nextcord.SelectOption(label="Paketan", value="paketan", description="Paketan Rebuff & Paketan Rod", emoji="📋")
        ]
        super().__init__(placeholder="LIST FISCH SHOP - MSTORE", options=options)

    async def callback(self, interaction: nextcord.Interaction):
        selected_value = self.values[0]
        embed = nextcord.Embed(
            title="📋 LIST PRICE FISCH SHOP - MSTORE",
            description="",
            color=0xD3D3D3
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1369612748526321695/1369622169109266452/anjay.gif")

        if selected_value == "joki_level":
            embed.add_field(
                name="🆙 Joki Level",
                value=(
                    "```js\n"
                    "[Level 1 - 100]     :  50P / Level\n"
                    "[Level 101 - 300]   : 100P / Level\n"
                    "[Level 301 - 500]   : 150P / Level\n"
                    "[Level 501 - 750]   : 200P / Level\n"
                    "[Level 750 - 1000]  : 250P / Level\n"
                    "[Level 1000 - 1500] : 300P / Level\n"
                    "[Level 1500 - 2500] : 350P / Level\n"
                    "```"
                ),
                inline=False
            )

        elif selected_value == "joki_rod":
            embed.add_field(
                name="🎣 Joki Rod",
                value=(
                    "```js\n"
                    "[Heaven Rod]             : 3K\n"
                    "[Heaven Rod + Coin]      : 5K\n"
                    "[Rod Off The Deep]       : 7K\n"
                    "[Trident Rod]            : 3K\n"
                    "[Poseidon Rod]           : 5K\n"
                    "[Zeus Rod]               : 3K\n"
                    "[Kraken Rod]             : 5K\n"
                    "[Ethereal Rod (No Coin)] : 15K\n"
                    "[Ethereal Rod (Coin)]    : 8K\n"
                    "```"
                ),
                inline=False
            )

        elif selected_value == "item_craft":
            embed.add_field(
                name="🛠️ Item Crafting",
                value=(
                    "```js\n"
                    "[Lapiz Lazuli] : 2K / 1\n"
                    "[Ruby]         : 1K / 1\n"
                    "[Amethyst]     : 1K / 1\n"
                    "[Opal]         : 2K / 1\n"
                    "[Moon Stone]   : 6K / 1\n"
                    "```"
                ),
                inline=False
            )

        elif selected_value == "enchant_relic":
            embed.add_field(
                name="💠 Enchant Relic",
                value="```css\n[Enchant Relic] : 50P / 1\n```",
                inline=False
            )
            embed.add_field(
                name="🔮 Exalted & Special Relics",
                value=(
                    "```js\n"
                    "[Exalted Relic]     : 500P / 1\n"
                    "[Hexed Relic]       : 1K / 1\n"
                    "[Translucent Relic] : 1K / 1\n"
                    "[Abyssal Relic]     : 1K / 1\n"
                    "[Atlantean Relic]   : 1K / 1\n"
                    "[Mosaic Relic]      : 1K / 1\n"
                    "[Fossilized Relic]  : 1K / 1\n"
                    "[Greedy Relic]      : 2K / 1\n"
                    "[Crystalized Relic] : 2K / 1\n"
                    "```"
                ),
                inline=False
            )

        elif selected_value == "order_account":
            embed.add_field(
                name="📦 Order Account",
                value=(
                    "```js\n"
                    "[Ethereal + Exalted] : 10K\n"
                    "[Ethereal + Enchant] : 8K\n"
                    "[Roteo + Enchant]    : 7K\n"
                    "[Roteo + Exalted]    : 9K\n"
                    "[Acc Polosan Sea2]   : 15K\n"
                    "```"
                ),
                inline=False
            )

        elif selected_value == "paketan":
            embed.add_field(
                name="🧪 Paketan Rebuff",
                value=(
                    "```js\n"
                    "[Paketan Rebuff]  : 7K / 1\n"
                    "```"
                ),
                inline=False
            )
            embed.add_field(
                name="🎣 Paketan Rod",
                value=(
                    "```js\n"
                    "[Rod Of The Exalted One] : 5K / 1\n"
                    "[Rod Of The Depth]       : 2K / 1\n"
                    "```"
                ),
                inline=False
            )

        embed.set_footer(
            text="Made with MSTORE",
            icon_url="https://cdn.discordapp.com/emojis/1273384825801412638.gif?size=512"
        )
        embed.timestamp = nextcord.utils.utcnow()
        await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.command(name="mstore", help="LIST FISCH SHOP - MSTORE")
async def fisch_shop(ctx):
    if ctx.author.id not in AUTHORIZED_USER_IDS:
        await ctx.send("❌ Kamu tidak memiliki izin untuk menggunakan perintah ini.", delete_after=3)
        return

    embed = nextcord.Embed(title="", description=f"## MSTORE - FISCH SHOP <a:Owners:1276242227827441685>", color=0x00CDFF)
    embed.set_author(name="MSTORE", icon_url="https://share.creavite.co/6812cedd9e2f464c8ec9fc1e.gif")
    embed.add_field(name="", value="<:Anjay:1369631567550353450> [Website](https://meonk.vercel.app)", inline=False)
    embed.add_field(name="", value="<:Facebook:1369610410570940446> [Facebook](https://www.facebook.com/meonk.gans.2025)", inline=False)
    embed.add_field(name="", value="<:Instagram:1323673432751341639> [Instagram](https://www.instagram.com/meonk_gans?igsh=bXNyMjJmampoNW51t)", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1078769385868636202/1370796902085427391/mstore.gif?ex=6820cd99&is=681f7c19&hm=16fc3be26b6676e3efe0d7ddde0821439578f11ebee52d99276e870e3e57f70a")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1078769385868636202/1370830045551132713/fisch.gif?ex=6820ec77&is=681f9af7&hm=13fb5fff6653a66a179991131abb8f1aa9eb65a80c0f5322773ad44d311568c6")
    embed.set_footer(text=f"Made by zaneru.id | with MSTORE", icon_url="https://cdn.discordapp.com/emojis/1273384825801412638.gif?size=512")

    await ctx.send(embed=embed, view=PersistentFischView())

class GamepassModal(ui.Modal):
    def __init__(self):
        super().__init__(title="Format Gamepass")
        self.beli_gamepass = ui.TextInput(label="Beli Gamepass Apa?", required=True, max_length=20, placeholder="Contoh: Bloxfruit, Pet Simulator, Dll")
        self.username_roblox = ui.TextInput(label="Username Roblox", required=True, max_length=20)
        self.harga = ui.TextInput(label="Harga Gamepass", required=True, max_length=20, placeholder="Contoh: 499 Robux/50K")
        self.add_item(self.beli_gamepass)
        self.add_item(self.username_roblox)
        self.add_item(self.harga)

    async def callback(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=True)
        await create_ticket(interaction, "gamepass", {
            "Beli Gamepass": self.beli_gamepass.value,
            "Username": self.username_roblox.value or "-",
            "Harga": self.harga.value or "-"
        })

class RobuxModal(ui.Modal):
    def __init__(self):
        super().__init__(title="Format Robux 5 Hari")
        self.jumlah_robux = ui.TextInput(label="Jumlah Robux yang ingin dibeli?", required=True, max_length=20, placeholder="Contoh: 1000 Robux")
        self.link_gamepass = ui.TextInput(label="Link Gamepass", required=True, max_length=100, placeholder="Link Gamepass Kamu")
        self.username_roblox = ui.TextInput(label="Username Roblox", required=True, max_length=20)
        self.add_item(self.jumlah_robux)
        self.add_item(self.link_gamepass)
        self.add_item(self.username_roblox)

    async def callback(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=True)
        await create_ticket(interaction, "robux", {
            "Jumlah Robux": self.jumlah_robux.value,
            "Link Gamepass": self.link_gamepass.value or "-",
            "Username Roblox": self.username_roblox.value or "-"
        })

class JokiModal(ui.Modal):
    def __init__(self):
        super().__init__(title="Format Jasa Joki")
        self.nama_game = ui.TextInput(label="Mau Joki Game Apa?", required=True, max_length=50, placeholder="Contoh: Bloxfruit, Fisch, Dll")
        self.jenis_joki = ui.TextInput(label="Joki Apa?", required=True, style=nextcord.TextInputStyle.paragraph, max_length=300, placeholder="Contoh: Leveling, Get Item, Dll")
        self.username_roblox = ui.TextInput(label="Username Roblox", required=False, max_length=20, placeholder="Opsional")

        self.add_item(self.nama_game)
        self.add_item(self.jenis_joki)
        self.add_item(self.username_roblox)

    async def callback(self, interaction: Interaction):
        await interaction.response.defer(ephemeral=True)
        await create_ticket(interaction, "joki", {
            "Game": self.nama_game.value,
            "Jenis Joki": self.jenis_joki.value,
            "Username Roblox": self.username_roblox.value or "-"
        })

class TicketView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(label="Gamepass", style=nextcord.ButtonStyle.success, emoji="🎫")
    async def gamepass_button(self, button, interaction: Interaction):
        await interaction.response.send_modal(GamepassModal())

    @ui.button(label="Robux 5 Hari Via Link", style=nextcord.ButtonStyle.primary, emoji="⏳")
    async def robux_button(self, button, interaction: Interaction):
        await interaction.response.send_modal(RobuxModal())

    @ui.button(label="Jasa Joki", style=nextcord.ButtonStyle.danger, emoji="⚒️")
    async def joki_button(self, button, interaction: Interaction):
        await interaction.response.send_modal(JokiModal())


@bot.command(name="panel", help="Menampilkan ticket panel")
async def panel(ctx):
    if ctx.author.id not in AUTHORIZED_USER_IDS:
        await ctx.send("❌ Kamu tidak memiliki izin untuk menggunakan perintah ini.", delete_after=3)
        return

    embed = nextcord.Embed(
        title="🎟️ MSTORE - Ticket Order",
        description="**Klik tombol di bawah untuk membuka ticket.**",
        color=0xffffff
    )
    embed.add_field(name="🎫 Gamepass", value="**__Untuk pembelian gamepass__**", inline=False)
    embed.add_field(name="⏳ Robux 5 Hari", value="**__Untuk pembelian Robux via link gamepass__**", inline=False)
    embed.add_field(name="⚒️ Jasa Joki", value="**__Tempat untuk jasa joki akun atau item__**", inline=False)
    embed.add_field(name="⚠️ Penting", value="**__Dilarang membuka ticket jika tidak ada keperluan!__**", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1078769385868636202/1370796902085427391/mstore.gif?ex=6820cd99&is=681f7c19&hm=16fc3be26b6676e3efe0d7ddde0821439578f11ebee52d99276e870e3e57f70a")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1370275222334472232/1370801721697239150/standard.gif?ex=6820d216&is=681f8096&hm=7417d7b3924b5221fe12b3b02a985eb9cf5871c55580cc038de65566028290d5")
    embed.set_footer(text="Made by zaneru.id | with MSTORE", icon_url="https://cdn.discordapp.com/emojis/1273384825801412638.gif?size=512")

    await ctx.send(embed=embed, view=TicketView())

async def create_ticket(interaction: Interaction, tipe: str, data: dict = None):
    guild = interaction.guild
    category = guild.get_channel(CATEGORY_ID[GUILD_ID.index(guild.id)])

    if not category:
        await interaction.followup.send("⚠️ Kategori tidak ditemukan atau tidak valid. Silakan hubungi admin.", ephemeral=True)
        return

    overwrites = {
        guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
        interaction.user: nextcord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
    }

    try:
        ticket_number = get_next_ticket_number()
        ticket_channel = await guild.create_text_channel(
            name=f"ticket-{ticket_number:04d}",
            overwrites=overwrites,
            category=category,
            topic=str(interaction.user.id)
        )
    except Exception as e:
        await interaction.followup.send(f"⚠️ Terjadi kesalahan saat membuat ticket: {e}", ephemeral=True)
        return

    embed = Embed(title="📩 Ticket Dibuat", color=0x00ff00)
    embed.add_field(name="User", value=interaction.user.mention, inline=False)
    embed.add_field(name="Tipe", value=tipe.capitalize(), inline=True)

    if data:
        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)

    await ticket_channel.send(content=interaction.user.mention, embed=embed)
    await ticket_channel.send("Jika transaksi/bertanya telah selesai, silakan klik tombol di bawah untuk menutup tiket.", view=CloseTicketButton())

    for log_channel_id in LOG_CHANNEL_IDS:
        log_channel = guild.get_channel(log_channel_id)
        if log_channel:
            panel = "Order Ticket" if tipe == "gamepass" else "Robux Ticket" if tipe == "robux" else "Bertanya"
            log_embed = Embed(title="Logged Info", description="**Ticket Log**", color=0x008BFF)
            log_embed.add_field(name="Ticket", value=f"Ticket-{ticket_number:04d}", inline=True)
            log_embed.add_field(name="Action", value="Created", inline=True)
            log_embed.add_field(name="Panel", value=panel, inline=True)
            log_embed.add_field(name="Username", value=interaction.user.name, inline=False)
            await log_channel.send(embed=log_embed)

    await interaction.followup.send(f"✅ Ticket kamu sudah dibuat: {ticket_channel.mention}", ephemeral=True)

class CloseTicketButton(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(label="Tutup Ticket", style=nextcord.ButtonStyle.red, emoji="🔒")
    async def close_ticket(self, button: ui.Button, interaction: Interaction):
        if interaction.user.id not in MANAGE_TICKET_USER_IDS:
            await interaction.response.send_message("⚠️ Kamu tidak punya izin untuk menutup ticket ini.", ephemeral=True)
            return

        await interaction.response.send_message("🔒 Ticket ditutup. Akan dihapus dalam 5 detik...", ephemeral=True)
        await interaction.channel.send("🛑 Ticket ini telah ditutup.")
        await asyncio.sleep(5)
        await interaction.channel.delete()

        for log_channel_id in LOG_CHANNEL_IDS:
            log_channel = interaction.guild.get_channel(log_channel_id)
            if log_channel:
                log_embed = Embed(title="Logged Info", description="**Ticket Log**", color=0xFC1216)
                log_embed.add_field(name="Ticket", value=f"{interaction.channel.name}", inline=True)
                log_embed.add_field(name="Action", value="Closed", inline=True)
                log_embed.add_field(name="Panel", value="Ticket Closed", inline=True)
                log_embed.add_field(name="Username", value=interaction.user.name, inline=False)
                await log_channel.send(embed=log_embed)

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"An error occurred while trying to run the bot: {str(e)}")