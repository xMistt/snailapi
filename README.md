# snailapi
Fully Asynchronous Python wrapper for Snail API.

[![Downloads](https://pepy.tech/badge/snailapi)](https://pepy.tech/project/snailapi)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/snailapi.svg)](https://pypi.org/project/snailapi/)
[![BenBot Version: 1.0.1](https://img.shields.io/pypi/v/snailapi.svg)](https://pypi.org/project/snailapi/)

## Installing:
Windows: ``py -3 -m pip install snailapi``<br>
Linux/macOS: ``python3 -m pip install snailapi``

After installing, you can check out the documentation for snailapi [here](https://github.com/xMistt/snailapi/wiki).

### Example:
```
import snailapi
import asyncio

snail = snailapi.APIClient()


async def main() -> None:
    shop = await snail.get_shop()

    print('=== FEATURED ===')
    for item in shop.featured:
        print(f'{item.name}: {item.price} V-Bucks')
        
    print('=== DAILY ===')
    for item in shop.featured:
        print(f'{item.name}: {item.price} V-Bucks')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
____
### fortnitepy example:
```
import fortnitepy
import BenBotAsync
import snailapi

snail = snailapi.APIClient()

client = fortnitepy.Client(
    auth=fortnitepy.EmailAndPasswordAuth(
        email='example@email.com',
        password='password123'
    )
)


@client.event
async def event_friend_message(message: fortnitepy.FriendMessage) -> None:
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!skin':
        try:
            skin = await snail.cosmetics.search_cosmetics(
                name=content
            )
            
            await client.user.party.me.set_outfit(asset=skin[0].id)
            await message.reply('Skin set to: {skin[0].name}.')
        except snailapi.exceptions.NotFound:
            await message.reply('Failed to find skin with the name: {content}.')


client.run()
```
