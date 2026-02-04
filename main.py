import asyncio
from telethon import TelegramClient, errors

# Sozlamalar
api_id = 35185177
api_hash = '546cb9da8fb2e31847fa766cb5186033'
chat_username = 'IIllllllIIlll' 
post_id = 98
message_text = '⁣⁣' 

# Termux-da yaratilgan sessiya bilan bir xil nom bo'lishi shart
client = TelegramClient('session_online', api_id, api_hash)

async def start_spamming():
    await client.start()
    print("--- Tizimga kirildi! ---")
    count = 0
    while True:
        try:
            await client.send_message(chat_username, message_text, comment_to=post_id)
            count += 1
            print(f"Yuborildi: {count}-xabar")
            await asyncio.sleep(0.5)
        except errors.FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Xato: {e}")
            break

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(start_spamming())
