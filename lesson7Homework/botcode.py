import os
import pdfplumber
import asyncio
from telegram import Bot
from telegram.error import TelegramError

TOKEN = '7833581443:AAEtEKr79uKkMVqxetm5L3wH46Yi8tCAnWY'

CHANNEL_ID = '@boooks_page_and_itself'

BOOKS_FOLDER = './books'

bot = Bot(token=TOKEN)

async def send_first_page_and_pdf_to_channel(book_path):

    try:
        if book_path.endswith('.pdf'):

            with pdfplumber.open(book_path) as pdf:
                first_page = pdf.pages[0].to_image()
                first_page_path = 'first_page.jpg'
                first_page.save(first_page_path)

                with open(first_page_path, 'rb') as photo:
                    await bot.send_photo(chat_id=CHANNEL_ID, photo=photo)
                os.remove(first_page_path)

            with open(book_path, 'rb') as document:
                await bot.send_document(chat_id=CHANNEL_ID, document=document)
            print(f"Sent first page and full PDF of {book_path} to the channel.")

        else:
            print(f"Skipping non-PDF file: {book_path}")

    except TelegramError as e:
        print(f"Telegram error occurred: {e}")
    except Exception as e:
        print(f"Error processing the book {book_path}: {e}")

async def process_books_in_folder():
    for filename in os.listdir(BOOKS_FOLDER):
        book_path = os.path.join(BOOKS_FOLDER, filename)
        if os.path.isfile(book_path) and filename.lower().endswith('.pdf'):
            print(f"Processing book: {filename}")
            await send_first_page_and_pdf_to_channel(book_path)

if __name__ == '__main__':
    asyncio.run(process_books_in_folder())
