from pyrogram.types import Message

def get_media_from_message(message: Message):
    media_types = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note")
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media
    return None

def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6] if media else ""

def get_name(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, 'file_name', "") if media else ""
