from telethon import TelegramClient
import time


api_id = int(input("Enter api_id from my.telegram.org: "))
api_hash = input("Enter api_hash from my.telegram.org: ")
client = TelegramClient('anon', api_id, api_hash)

chid = input("Enter chat id/@ to hack! : ")

def prow(chid):
	if chid != "@":
		pass
	else:
		chid = "@" + str(chid)
		return chid

async def main():
	megas = await client.send_message(chid, '`Hacking...`')
	time.sleep(1)
	await client.edit_message(megas, '`Hacking... 1% \n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`')
	time.sleep(2)
	await client.edit_message(megas, '`Hacking... 5% \n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`')
	time.sleep(2)
	await client.edit_message(megas, '`Hacking... 30% \n████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`')
	time.sleep(2)
	await client.edit_message(megas, '`Hacking... 70% \n██████████████████████▒▒`')
	time.sleep(2)
	await client.edit_message(megas, '`Hacking... 100% \n████████████████████████`')
	time.sleep(1)
	await client.edit_message(megas, '`Hacked!`')

with client:
    client.loop.run_until_complete(main())
