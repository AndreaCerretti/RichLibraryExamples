# Rich is a Python library for rich text and beautiful formatting in the terminal.
# The Rich API makes it easy to add color and style to terminal output. 
# Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, 
# tracebacks, and more — out of the box.

from rich.console import Console
from rich.table import Table

table = Table(title="Pandas Versions")

table.add_column("Released", style="cyan")
table.add_column("Version Number", justify="right", style="magenta")
table.add_column("Description", style="green")

table.add_row("May 29, 2020", "v1.0.4", "Just an update.")
table.add_row("Mar 18, 2020", "v1.0.3", "Just an update.")
table.add_row("Mar 15, 2020", "v1.0.2", "Just an update.")
table.add_row("Feb 05, 2020", "v1.0.1", ":thumbs_up: [underline]Big[/] update.")

console = Console()
console.print(table)