import asyncio

from src.request import WebRequests
from src.parse import Parser


async def main(urls:list):
    # create request for all urls
    fetcher = WebRequests(urls)
    # fetch concurrently
    await fetcher.fetch_all()

    for result in fetcher.get_result():
        print(result)
        extracted_urls = Parser.list_urls(result.content)

        print({
            "url": result.url,
            "status_code": result.status_code,
            "count": len(extracted_urls),
            "data": extracted_urls
        })



if __name__ == "__main__":
    urls = [
        "https://news.detik.com/indeks"
    ]
    
    asyncio.run(main(urls))