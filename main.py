from telegram import Bot
import asyncio

TOKEN = "8667987742:AAHJ2bg-yHesjWCMBZCu7LgaZvoCxiL7EAI"

GROUP_IDS = [
    --1003823759558,
    --1003740539352,
    --1001693541154
]

MESSAGE = """‼️‼️HELT ANONYMA BETALNINGAR

(Via paypal,klarna,apple pay,kort)

Grupper finns få grupperna direkt när betalning är gjort om vi inte svarar😊

• 1 GRUPP
https://telegram-grupper-2.myshopify.com/products/1-gruppsvensk

• 5 GRUPPER
https://telegram-grupper-2.myshopify.com/products/utan-namn-28feb-_12-38

• DANSKED EXPOSÉ
https://telegram-grupper-2.myshopify.com/products/1-danmark-group

@ghettograbb2 @ghettograbb3
"""

bot = Bot(8667987742:AAHJ2bg-yHesjWCMBZCu7LgaZvoCxiL7EAI)

async def main():
    while True:
        for group_id in GROUP_IDS:
            try:
                await bot.send_message(group_id, MESSAGE)
            except Exception as e:
                print(f"Fel i grupp {group_id}: {e}")

        await asyncio.sleep(300)  # 5 minuter

asyncio.run(main())
