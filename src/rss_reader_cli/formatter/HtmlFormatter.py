from .Formatter import Formatter


class HtmlFormatter(Formatter):
    """Format the feed entries as HTML"""

    def format(self, entries: list[dict]) -> str:
        """Format the feed entries as HTML"""

        html = f"""<html>
        <head>
            <title>{data['title']}</title>
        </head>
        <body>
            <h1>{data['title']}</h1>
            <p>{data['description']}</p>
            <p>{data['link']}</p>
            <p>{data['pubDate']}</p>
        </body>
        </html>"""
        return html
