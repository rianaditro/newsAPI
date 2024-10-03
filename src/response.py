import asyncio
import aiohttp



class WebResponse:
    """Object to save the response from the web request."""
    def __init__(self, url, status_code, content=None):
        self.url = url
        self.status_code = status_code
        self.content = content

    def __str__(self):
        return f"URL: {self.url}, Status Code: {self.status_code}, Content Length: {len(self.content) if self.content else 0}"

class WebRequests:
    """Class to make web requests."""
    def __init__(self, urls:list):
        self.urls = urls
        self.responses = [] # list of WebResponse objects

    async def fetch(self, session: aiohttp.ClientSession, url:str):
        """fetch every single url"""        
        try:
            async with session.get(url) as response:
                content = await response.text()
                status_code = response.status

                # store the response as a WebResponse object
                response_result = WebResponse(url, status_code, content)
                self.responses.append(response_result)
        except Exception as e:
            print(e)
            # store failed requests
            response_result = WebResponse(url, "Error", None)
            self.responses.append(response_result)


    async def fetch_all(self):
        """fetch all the urls"""
        async with aiohttp.ClientSession() as session:
            # create a list of tasks
            tasks = [self.fetch(session, url) for url in self.urls]
            # run tasks concurrently
            await asyncio.gather(*tasks)

    def get_result(self):
        return self.responses


# main function
async def main(urls:list):
    # create instance of WebRequests
    fetcher = WebRequests(urls)
    # fetch all urls
    await fetcher.fetch_all()

    # get results
    results = fetcher.get_result()
    for result in results:
        print(result)

def run(urls:list):
    asyncio.run(main(urls))


if __name__ == "__main__":
    urls = [
        "https://news.detik.com/indeks"
    ]

    run(urls)

