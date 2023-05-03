# インストールした discord.py を読み込む
import discord
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import os

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_TOKEN']

# ローカル
#driver_path = 'C:/Users/kino/Desktop/Selenium/chromedriver.exe'

# Heroku
driver_path = '/app/.chromedriver/bin/chromedriver'	
# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
#options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# 接続に必要なオブジェクトを生成
client = discord.Client()

#適当に返す
rep = ["エコー）音程(70)t) これリーサルあるの？ないの？あるのないのあるのないのあるのないのあるのないのあるのないのあるのないのあるじないのあるじないのあるじないのあるじされあるじされほっけいすけ3", \
       "ほっけええええい", \
       "メンテエエエエエエエエエエ\nhttps://twitter.com/iorbppvyolgzhna/status/1097732863045189634?s=12"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user != message.author:
        # 送り主がBotだった場合反応したくないので
        if message.content.startswith("ぶーちゃん"):
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))
                if text == ('ぶーちゃん'):
                    msg = 'サーバー荒らすっちゃ・・サーバー荒らすっちゃ・・'
                elif text.find('はかいこうせん') > -1:
                    msg = 'カイリュー はかいこうせん ▽ 音程(999)速度(999)残響(800 0.25 750)t)鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛鸛'
                elif text.find('こんにちは') > -1 or text.find('こんちゃ') > -1 or text.find('やあ') > -1 or text.find('おっす') > -1 or text.find('きーたよ') > -1:
                    msg = 'ほっけええええええ'
                elif text.find('自己紹介') > -1:
                    msg = 'どうも豚饅頭と申します!シャドウバースが大好きなのでシャドウバースの配信を常日頃行っております。プレイングミスも多く未熟な部分も多々ありますが、どうか暖かく見守って頂けると幸いで御座います。よく声が特徴的と言われますが、ボイチェンは使用しておりません！後、気を付けてはいるのですが、無意識で突発的に大きな声を出してしまうことがあるので申し訳ございませんが、注意して頂けると幸いで御座います。後、イケボですねって言って頂けると嬉しいです 時折荒らしがくることもありますが、基本的に過疎放送です。こんな僕ですが、たくさんのシャドバプレイヤーの方々と交流を深め、切磋琢磨し、プレイングの向上に努めていきたいと思っておりますので不束者ですが何卒宜しくお願い致します!'
                elif text.find('デッキコード') > -1:
                    #await message.channel.send('ちょっとマテ茶（激寒）')
                    msg = svportal(text)
                else:
                    msg = rep[random.randint(0, len(rep)-1)]
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await message.channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e
        if message.content.startswith("deckcode") and len(message.content) == 12:
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))
                msg = svportal(text)
                await message.channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e
        if message.content.startswith("jokingly"):
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))
                msg = "Yo! I got banned from events, and here's how it went down. I did nothing wrong, man! I did nothing wrong whatsoever! I got banned! I didn't even KNOW I got banned! I didn't get no email, I didn't get no explanation, I didn't get no chance to explain myself. I just got banned. I got a message from Doug Zeeff, that I got banned from Konami. Konami doesn't even message me and tell me I'm banned. So I got banned from my old video I made, Where I jokingly made a video- I jokingly, JOKINGLY, told, the world, that, I stalled for time. I DIDN'T STALL FOR TIME! Anyone with a BRAIN, would realize it was a JOKE! It was a joke, that was- it was a good joke at the time! The new time rules were going on, \"Oh, Ha Ha Cowboy for Game\". It's a JOKE! It's just like Firewall Pass. It's a JOKE!"
                await message.channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e
        if message.content.startswith("Bや？") or message.content.startswith("Bや?") or message.content.startswith("Ｂや？"):
            try:
                user_name = message.author.name
                text = message.content
                print(text)
                print(type(text))
                msg = "豚饅頭「ぼくBなのぉ！？Bは嫌だよおおおおおおおおおお！！！」\nhttps://openrec.tv/capture/r9d2k457d0w"
                await message.channel.send(msg)
                return msg
            except Exception as e:
                print(e)
                raise e
                
def svportal(text): 
    number = text[-4:]
    print(number)
    if len(number) != 4:
        return '例　ぶーちゃんデッキコード4rev'
    driver.get('https://shadowverse-portal.com/deckbuilder/classes?lang=ja')
    deckcode = driver.find_element_by_css_selector('#deckCode')    
    deckcode.send_keys(number)
    button=driver.find_element_by_css_selector('#deckImport')
    button.click()
    time.sleep(1)
    deckurl = driver.current_url
    if deckurl.find('create') <= -1:
        return "invalid deckcode"
    hash=deckurl.find('?hash')
    lang=deckurl.find('&lang')
    result='https://shadowverse-portal.com/deck/' + deckurl[hash+6:lang]  + '?lang=ja'
    print(result)
    return result

client.run(TOKEN)
