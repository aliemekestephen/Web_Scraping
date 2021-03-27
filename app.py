import asyncio
import aiohttp
import async_timeout
import time
import requests

from pages.all_books_page import AllBookPage

page_content = requests.get('http://books.toscrape.com').content
page = AllBookPage(page_content)

books = page.books

loop = asyncio.get_event_loop()


async def fetch_page(session, url):
    page_state = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took  {time.time() - page_state}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks



urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'Total Page request took {time.time() - start}')

for page_content in pages:
    page = AllBookPage(page_content)
    books.extend(page.books)


# for book in books:
# print(book)
