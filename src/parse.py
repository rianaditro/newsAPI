from bs4 import BeautifulSoup as bs


class Parser:
    @staticmethod
    def list_urls(content:str):
        soup = bs(content, "html.parser")

        list_content = soup.find("div", {"class": "grid-row list-content"})
        list_content = list_content.find_all("h3", {"class": "media__title"})

        urls = []
        for content in list_content:
            url = content.find("a").get("href")
            title = content.text.replace('"', '').strip()
            urls.append(
                {
                    "url": url,
                    "title": title
                }
            )

        return urls