import asyncio

from datetime import date, datetime
from src.request import WebRequests
from src.parse import Parser


async def run_concurrently(urls:list):
    # get date and time
    data_date = date.today().strftime("%d/%m/%Y")
    data_time = datetime.now().strftime("%H:%M:%S")

    # create request for all urls
    fetcher = WebRequests(urls)
    # fetch concurrently
    await fetcher.fetch_all()

    # api response format
    responses_result = {
        "url": urls,
        "status_code": 200,
        "message": "ok",
        "date": data_date,
        "time": data_time,
        "count": 0,
        "data": []
    }

    for result in fetcher.get_result():
        extracted_urls = Parser.list_urls(result.content)
        
        # add total data count
        responses_result["count"] += len(extracted_urls)
        responses_result["data"].extend(extracted_urls)

    return responses_result

def main(urls:list):
    return asyncio.run(run_concurrently(urls))


if __name__ == "__main__":
    urls = [
        "https://news.detik.com/indeks",
        "https://www.detik.com/edu/indeks"
    ]
    
    data = main(urls)
    print(data)