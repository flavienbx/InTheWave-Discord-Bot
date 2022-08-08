import discord
import json
import asyncio
from discord.ext import commands
from discord import Client, Intents, Embed
from discord_components import Button, Select, SelectOption, ComponentsBot, ButtonStyle

bot = ComponentsBot("¤")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)

@bot.command()
async def setup_ticket(ctx):
    created_em = discord.Embed(title="WaveTicket", description="Pour contacter notre support clic sur le bouton ci-dessous !", color=0x00a8ff)
    await ctx.send(embed=created_em, components=[Button(label="Ouvrir un ticket", custom_id="open_ticket", emoji="📩")])

@bot.command()
async def setup_rank(ctx):
    created_em = discord.Embed(title="WaveRank", description="Pour trouver un mate parfait améliore ton profil en y ajoutant ton Rank ; clic sur le bouton ci-dessous !", color=0x00a8ff)
    await ctx.send(embed=created_em, components=[Button(label="Choisir le jeu", custom_id="choose_game_rank", emoji=bot.get_emoji(869587112037589022))])

@bot.event
async def on_button_click(interaction):
    if interaction.component.custom_id == "close_ticket":
        with open('data.json') as f:
            data = json.load(f)
        if interaction.channel.id in data["ticket-channel-ids"]:

            channel_id = interaction.channel.id
            await interaction.channel.delete()

            index = data["ticket-channel-ids"].index(channel_id)

            del data["ticket-channel-ids"][index]

            with open('data.json', 'w') as f:
                json.dump(data, f)

    elif interaction.component.custom_id == "choose_game_rank":

        await interaction.send(components=[Button(label="Valorant", custom_id="valo_rank", emoji=bot.get_emoji(904833755884158976)), Button(label="Rocket League", custom_id="rocketleague_rank", emoji=bot.get_emoji(905136269565255692)), Button(label="OverWatch", custom_id="overwatch_rank", emoji=bot.get_emoji(904833767540146237))])

    elif interaction.component.custom_id == "valo_rank":
            await interaction.send(components=[Select(placeholder="Veuillez choisir votre rank.", options=[SelectOption(label="Iron", value="role_valo_fer", emoji=bot.get_emoji(999688779537334372)), SelectOption(label="Bronze", value="role_valo_bronze", emoji=bot.get_emoji(999688790002110465)), SelectOption(label="Silver", value="role_valo_argent", emoji=bot.get_emoji(999688785019293696)), SelectOption(label="Gold", value="role_valo_gold", emoji=bot.get_emoji(999688786550194237)), SelectOption(label="Plat", value="role_valo_plat", emoji=bot.get_emoji(999688788446027817)), SelectOption(label="Diamond", value="role_valo_diamant", emoji=bot.get_emoji(999688793202368512)), SelectOption(label="Ascendant", value="role_valo_ascendant", emoji=bot.get_emoji(999688794825564220)), SelectOption(label="Immortal", value="role_valo_immo", emoji=bot.get_emoji(999688781076635660)), SelectOption(label="Radiant", value="role_valo_radiant", emoji=bot.get_emoji(999688791730159666))], custom_id="select_valo_rank",)],)
               
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select_valo_rank"
            )
            user = interaction.author
            if interaction.values[0] == "role_valo_fer":
                role = discord.utils.get(interaction.guild.roles, id=999699958062129282)
            elif interaction.values[0] == "role_valo_bronze":
                role = discord.utils.get(interaction.guild.roles, id=999700059597836328)
            if interaction.values[0] == "role_valo_argent":
                role = discord.utils.get(interaction.guild.roles, id=999700125947535532)
            if interaction.values[0] == "role_valo_gold":
                role = discord.utils.get(interaction.guild.roles, id=999700256704975030)
            if interaction.values[0] == "role_valo_plat":
                role = discord.utils.get(interaction.guild.roles, id=999700388141867130)
            if interaction.values[0] == "role_valo_diamant":
                role = discord.utils.get(interaction.guild.roles, id=999700465363198002)
            if interaction.values[0] == "role_valo_ascendant":
                role = discord.utils.get(interaction.guild.roles, id=999700530316202126)
            if interaction.values[0] == "role_valo_immo":
                role = discord.utils.get(interaction.guild.roles, id=999700789620641802)
            if interaction.values[0] == "role_valo_radiant":
                role = discord.utils.get(interaction.guild.roles, id=999700603968163890)
            if role in user.roles:
                await user.remove_roles(role)
                await interaction.send("Rank retiré avec succès.")
            else:
                await user.add_roles(role)
                await interaction.send("Rank ajouté avec succès.")

    elif interaction.component.custom_id == "overwatch_rank":
            await interaction.send(components=[Select(placeholder="Veuillez choisir votre rank.", options=[SelectOption(label="Bronze", value="role_overwatch_bronze", emoji=bot.get_emoji(999706718994964480)), SelectOption(label="Silver", value="role_overwatch_silver", emoji=bot.get_emoji(999706751253356555)), SelectOption(label="Gold", value="role_overwatch_gold", emoji=bot.get_emoji(999706782861639841)), SelectOption(label="Platinum", value="role_overwatch_platinum", emoji=bot.get_emoji(999706804525211659)), SelectOption(label="Diamond", value="role_overwatch_diamond", emoji=bot.get_emoji(999706815887581295)), SelectOption(label="Master", value="role_overwatch_master", emoji=bot.get_emoji(999707298446450708)), SelectOption(label="Grandmaster", value="role_overwatch_grandmaster", emoji=bot.get_emoji(999707318700744815)), SelectOption(label="Top 500", value="role_overwatch_top500", emoji=bot.get_emoji(999707330293809152))], custom_id="select_overwatch_rank",)],)
               
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select_overwatch_rank"
            )
            user = interaction.author
            if interaction.values[0] == "role_overwatch_bronze":
                role = discord.utils.get(interaction.guild.roles, id=999718400181940305)
            elif interaction.values[0] == "role_overwatch_silver":
                role = discord.utils.get(interaction.guild.roles, id=999718403172487199)
            if interaction.values[0] == "role_overwatch_gold":
                role = discord.utils.get(interaction.guild.roles, id=999718406444023918)
            if interaction.values[0] == "role_overwatch_platinum":
                role = discord.utils.get(interaction.guild.roles, id=999718409140965499)
            if interaction.values[0] == "role_overwatch_diamond":
                role = discord.utils.get(interaction.guild.roles, id=999718411775004782)
            if interaction.values[0] == "role_overwatch_master":
                role = discord.utils.get(interaction.guild.roles, id=999718414237048962)
            if interaction.values[0] == "role_overwatch_grandmaster":
                role = discord.utils.get(interaction.guild.roles, id=999718416917205012)
            if interaction.values[0] == "role_overwatch_top500":
                role = discord.utils.get(interaction.guild.roles, id=999718418804646049)
            if role in user.roles:
                await user.remove_roles(role)
                await interaction.send("Rank retiré avec succès.")
            else:
                await user.add_roles(role)
                await interaction.send("Rank ajouté avec succès.")

    elif interaction.component.custom_id == "rocketleague_rank":
            await interaction.send(components=[Select(placeholder="Veuillez choisir votre rank.", options=[SelectOption(label="Bronze", value="role_rocketleague_bronze", emoji=bot.get_emoji(999706718994964480)), SelectOption(label="Silver", value="role_rocketleague_silver", emoji=bot.get_emoji(999706751253356555)), SelectOption(label="Gold", value="role_rocketleague_gold", emoji=bot.get_emoji(999706782861639841)), SelectOption(label="Platine", value="role_rocketleague_platinum", emoji=bot.get_emoji(999706804525211659)), SelectOption(label="Diamant", value="role_rocketleague_diamond", emoji=bot.get_emoji(999706815887581295)), SelectOption(label="champion", value="role_rocketleague_champion", emoji=bot.get_emoji(999707298446450708)), SelectOption(label="grand champion", value="role_rocketleague_grandchampion", emoji=bot.get_emoji(999707318700744815)), SelectOption(label="Super Sonic Legend", value="role_rocketleague_ssl", emoji=bot.get_emoji(999707330293809152))], custom_id="select_rocketleague_rank",)],)
               
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select_rocketleague_rank"
            )
            user = interaction.author
            if interaction.values[0] == "role_rocketleague_bronze":
                role = discord.utils.get(interaction.guild.roles, id=999718400181940305)
            elif interaction.values[0] == "role_rocketleague_silver":
                role = discord.utils.get(interaction.guild.roles, id=999718403172487199)
            if interaction.values[0] == "role_rocketleague_gold":
                role = discord.utils.get(interaction.guild.roles, id=999718406444023918)
            if interaction.values[0] == "role_rocketleague_platinum":
                role = discord.utils.get(interaction.guild.roles, id=999718409140965499)
            if interaction.values[0] == "role_rocketleague_diamond":
                role = discord.utils.get(interaction.guild.roles, id=999718411775004782)
            if interaction.values[0] == "role_rocketleague_champion":
                role = discord.utils.get(interaction.guild.roles, id=999718414237048962)
            if interaction.values[0] == "role_rocketleague_grandchampion":
                role = discord.utils.get(interaction.guild.roles, id=999718416917205012)
            if interaction.values[0] == "role_rocketleague_ssl":
                role = discord.utils.get(interaction.guild.roles, id=999718418804646049)
            if role in user.roles:
                await user.remove_roles(role)
                await interaction.send("Rank retiré avec succès.")
            else:
                await user.add_roles(role)
                await interaction.send("Rank ajouté avec succès.")

    elif interaction.component.custom_id == "open_ticket":
        with open("data.json") as f:
            data = json.load(f)

        ticket_number = int(data["ticket-counter"])
        ticket_number += 1

        ticket_channel = await interaction.guild.create_text_channel("ticket_{}".format(ticket_number))
        await ticket_channel.set_permissions(interaction.guild.get_role(interaction.guild.id), send_messages=False, read_messages=False)
        for role_id in data["valid-roles"]:
            role = interaction.guild.get_role(role_id)

            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
        
        await ticket_channel.set_permissions(interaction.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)

        created_em = discord.Embed(title="Ticket", description="Votre ticket a bien été crée -> {}".format(ticket_channel.mention), color=0x00a8ff)

        await interaction.respond(embed=created_em)
        created_em = discord.Embed(title="WaveTicket", description="Vous venez d'ouvrir une demande de ticket à notre support ! Pour que nous puissions vous répondre avec le plus de rapidité nous vous demandons de choisir le sujet de ce ticket !", color=0x00a8ff)
        created_em.set_footer(text="( Si ce ticket a été ouvert malencontreusement veuillez cliquer sur 'Supprimer' )")
        await ticket_channel.send(embed=created_em, components=[Button(style=ButtonStyle.red, label="Supprimer", custom_id="close_ticket", emoji="🗑"), Select(placeholder="veuillez choisir le sujet de votre ticket", options=[SelectOption(label="Signalez un bug", value="signalez_bug", emoji="🚧"), SelectOption(label="Rejoindre la wave", value="wave_join", emoji="🗃"), SelectOption(label="Partenariat", value="partenariat", emoji="🧾"), SelectOption(label="Autre", value="autre", emoji="🔍")], custom_id="select_ticket_etape_1",)],)


        interaction = await bot.wait_for(
            "select_option", check=lambda inter: inter.custom_id == "select_ticket_etape_1"
        )
        if ((f"{interaction.values[0]}") == "wave_join"):
            await interaction.respond(content=f"🟦 **__Pour devenir modérateur :__**\n\n🔹 **Âge :**\n\n🔹 **Expérience :**\n\n🔹 **Description de vous même :**\n\n🔹 **Pourquoi vous et pas un autre :**\n\n🟦 **__Mise en situation :__**\n\n🔹 **Une personne spam sans arrêt le même emoji, que faites-vous :**\n\n🔹 **Une personne vient d'insulter une autre personne dans le channel discussion, l'autre personne l'insulte à son tour, que faites-vous :**\n\n🔹 **Un lien dangereux vient d'être mis sur notre serveur, que faites-vous :**\n\n🔹 **Un lien publicitaire vient d'être mis sur notre serveur, que faites-vous :**\n\n🟦 **__Pour finir :__**\n\n🔹 **Décrivez le serveur, en quoi consiste-t-il. Comme si vous étiez entrain de le montrer à une personne inconnue :**\n\n**Copié ce message et répondez ensuite.**\n")
        elif ((f"{interaction.values[0]}") == "signalez_bug"):
            await interaction.respond(content=f"Veuillez nous détailler votre bug le plus possible pour que nous puissions mieux comprendre et y remédier au plus vite !")
        elif ((f"{interaction.values[0]}") == "facturation"):
            await interaction.respond(content=f"Veuillez nous expliquer votre problème en détail pour que notre service comptabilité puisse vous répondre et vous aidez au mieux !")
        elif ((f"{interaction.values[0]}") == "partenariat"):
            await interaction.respond(content=f"Veuillez expliquer votre demande de partenariat de la façon la plus détaillée possible l'équipe de modération traitera votre ticket au plus vite !")
        elif ((f"{interaction.values[0]}") == "autre"):
            await interaction.respond(content=f"Veuillez précisé de la raison de votre ticket le plus en détail possible pour que le support puisse agir au plus vite.")
        elif ((f"{interaction.values[0]}") == "probleme_offre"):
            created_em = discord.Embed(title="Ticket", description="Veuillez choisir l'offre avec le quelle vous rencontrez un problème.", color=0x00a8ff)
            await ticket_channel.send(embed=created_em, components=[Select(placeholder="Veuillez choisir l'offre", options=[SelectOption(label="Web", value="web_bug", emoji="🌐"), SelectOption(label="Minecraft", value="minecraft_bug", emoji="🎮"), SelectOption(label="Discord Bot", value="discord_bug", emoji="💻"), SelectOption(label="VPS", value="vps_bug", emoji=bot.get_emoji(903249150991298582))], custom_id="select_bug_etape_2",)],)
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select_bug_etape_2"
            )
            if ((f"{interaction.values[0]}") == "web_bug"):
                created_em = discord.Embed(title="Résumé du ticket", description="Bug : Web Hosting", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "minecraft_bug"):
                created_em = discord.Embed(title="Résumé du ticket", description="Bug : Minecraft Serveur", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "discord_bug"):
                created_em = discord.Embed(title="Résumé du ticket", description="Bug : Discord Serveur", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "vps_bug"):
                created_em = discord.Embed(title="Résumé du ticket", description="Bug : VPS", color=0x00a8ff)
            await ticket_channel.send(embed=created_em)
        elif ((f"{interaction.values[0]}") == "information_offre"):
            created_em = discord.Embed(title="Ticket", description="Veuillez choisir l'offre avec le quelle vous voulez des informations.", color=0x00a8ff)
            await ticket_channel.send(embed=created_em, components=[Select(placeholder="Veuillez choisir l'offre", options=[SelectOption(label="Web", value="web_info", emoji="🌐"), SelectOption(label="Minecraft", value="minecraft_info", emoji="🎮"), SelectOption(label="Discord Bot", value="discord_info", emoji="💻"), SelectOption(label="VPS", value="vps_info", emoji=bot.get_emoji(903249150991298582))], custom_id="select_info_etape_2",)],)
            interaction = await bot.wait_for(
                "select_option", check=lambda inter: inter.custom_id == "select_info_etape_2"
            )
            if ((f"{interaction.values[0]}") == "web_info"):
                created_em = discord.Embed(title="Résumé du ticket", description="Information : Web Hosting", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "minecraft_info"):
                created_em = discord.Embed(title="Résumé du ticket", description="Information : Minecraft Serveur", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "discord_info"):
                created_em = discord.Embed(title="Résumé du ticket", description="Information : Discord Serveur", color=0x00a8ff)
            elif ((f"{interaction.values[0]}") == "vps_info"):
                created_em = discord.Embed(title="Résumé du ticket", description="Information : VPS", color=0x00a8ff)
            await ticket_channel.send(embed=created_em)
        else:
            await interaction.respond("Une erreur est survenue...")



bot.run("TOKEN") 
