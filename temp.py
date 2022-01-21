import subprocess, re, discord, time
from threading import Timer
token = "ここにBOTのトークンを入力"
client = discord.Client()
any_channel_id = "送信させたいチャンネルのID"
repsec = #ここに繰り返し送信する間隔(秒数)を入力する


@client.event
async def on_ready():
  global channel_sent 
  channel_sent = client.get_channel(any_channel_id)
  print('ログインしました')

@client.event
async def on_message(message):
  tof = False
  if message.author.bot:
    return
  elif message.content == '/temp':
    if tof == True:
      tof = False
    elif tof == False:
      tof = True
    while tof:
      cmd = "cat /sys/class/thermal/thermal_zone0/temp"
      temp = subprocess.check_output(cmd.split())
      temp = temp.decode("utf-8")
      temp = int(temp) / 1000
      now = time.ctime()
      cnvtime = time.strptime(now)
      await message.channel.send("サーバーの温度は" + str(temp) + "度です。")
      await message.channel.send(time.strftime("%Y/%m/%d %H:%M", cnvtime))
      time.sleep(repsec)


client.run(token)