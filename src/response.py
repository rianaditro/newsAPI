class WebResponse:
    """Object to save the response from the web request."""
    def __init__(self, url, status_code, content=None):
        self.url = url
        self.status_code = status_code
        self.content = content

    def __str__(self):
        return f"URL: {self.url}, Status Code: {self.status_code}, Content Length: {len(self.content) if self.content else 0}"
