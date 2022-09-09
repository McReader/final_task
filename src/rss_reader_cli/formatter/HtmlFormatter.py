from .Formatter import Formatter


class HtmlFormatter(Formatter):
    """Format the feed entries as HTML"""

    def format(self, entries: list[dict]) -> str:
        """Format the feed entries as HTML"""

        html = f"""
<html>
    <head>
        <title>News Feed</title>
    </head>
    <body>
        <ul>
            {self._render_items(entries)}
        </ul>
    </body>
</html>
        """
        return html

    def _render_items(self, entries: list[dict]) -> str:
        """Render the feed entries as HTML"""

        return '\n'.join([self._render_item(entry) for entry in entries])

    def _render_item(self, entry: dict) -> str:
        """Render the feed entry as HTML"""

        return f"""
            <li>
                <a href={entry.get('link')}>
                    <h2>
                        {entry.get('title')}
                    </h2>
                </a>
                <p>{entry.get('description')}</p>
                <p>{entry.get('published')}</p>
            </li>
        """
