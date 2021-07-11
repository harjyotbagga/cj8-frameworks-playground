from rich import print as rprint
from rich.panel import Panel
from rich.color import Color
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown

print("Hello World")
rprint("[italic red]Hello[/italic red] World!")
# color = Color.parse("red")
# inspect(color, methods=True)

MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
- Another item
"""

console = Console()
md = Markdown(MARKDOWN)
console.print(md)