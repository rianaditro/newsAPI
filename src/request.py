import asyncio
import aiohttp

from response import WebResponse

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
