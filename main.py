import asyncio

from src.request import WebRequests
from src.response import WebResponse


async def main(urls:list):
    # create request for all urls
    fetcher = WebRequests(urls)
    # fetch concurrently
    await fetcher.fetch_all()

    for result in fetcher.get_result():
        print(result)


if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/photos"
    ]
    asyncio.run(main(urls))