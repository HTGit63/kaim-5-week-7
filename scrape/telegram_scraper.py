# scrape/telegram_scraper.py

import os
import json
import asyncio
from datetime import datetime
from telethon import TelegramClient, errors
from scrape.utils import load_config, get_logger

# List of channels to scrape
CHANNELS = [
    'lobelia4cosmetics',
    'tikvahpharma',
    # add more channel usernames here
]

async def scrape_channel(client, channel_username, logger):
    """
    Fetches all messages from a channel and writes to data/raw/YYYY-MM-DD/channel.json.
    """
    date_str = datetime.utcnow().strftime('%Y-%m-%d')
    out_dir = os.path.join('data', 'raw', date_str, channel_username)
    os.makedirs(out_dir, exist_ok=True)

    logger.info(f"Scraping @{channel_username} into {out_dir}")
    all_messages = []
    try:
        async for message in client.iter_messages(channel_username, limit=None):
            all_messages.append({
                'id': message.id,
                'date': message.date.isoformat(),
                'text': message.message,
                'has_media': bool(message.media),
                # you can extend with more fields if desired
            })
    except errors.ChannelPrivateError:
        logger.error(f"Channel @{channel_username} is private or forbidden.")
        return
    except Exception as e:
        logger.exception(f"Error fetching @{channel_username}: {e}")
        return

    # Write JSON
    out_path = os.path.join(out_dir, f"{channel_username}.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_messages, f, ensure_ascii=False, indent=2)

    logger.info(f"Saved {len(all_messages)} messages for @{channel_username}")

async def main():
    config = load_config()
    logger = get_logger('telegram_scraper')

    client = TelegramClient(config['session_name'],
                            int(config['api_id']),
                            config['api_hash'])

    await client.start()
    logger.info("Telegram client started.")

    for channel in CHANNELS:
        await scrape_channel(client, channel, logger)

    await client.disconnect()
    logger.info("Scraping complete, client disconnected.")

if __name__ == '__main__':
    asyncio.run(main())
