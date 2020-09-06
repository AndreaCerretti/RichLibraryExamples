# Rich is a Python library for rich text and beautiful formatting in the terminal.
# The Rich API makes it easy to add color and style to terminal output. 
# Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, 
# tracebacks, and more — out of the box.

from rich import print

print(3)
print({'a': 18, 'b':32})

# Se non vogliamo sovrascrivere il classico print e vogliamo avere più personalizzazione
print("\nRICH.CONSOLE: \n")
from rich.console import Console

console = Console()
console.print("Testo normale :thumbs_up:")
console.print("Testo grassetto", style="bold")
console.print("Testo grassetto sottolineato", style="bold underline")
console.print("Testo grassetto sottolineato verde", style="bold underline green")
console.print("Una sola [underline]parola[/] sottolineata")

# Console log con timestamp e linea di codice del log per debug
print("\nDebug con timestamp e linea del codice che fa il log\n")
import time

for i in range(10):
    console.log(f"I am about to sleep={i}")
    time.sleep(0.2)
    console.log(f"But I am briefly awake now.")


# Console log con variabili locali per debug e eventuale salvataggio in un file separato
print("\nDebug con variabili locali (rich.traceback)")

from rich.traceback import install 
install() 

def add_two(n1, n2):
    console.log("About to add two numbers.", log_locals=True)
    return n1 + n2

console = Console(record=True)
try:
    for i in range(10):
        time.sleep(0.2)
        add_two(1, i)
    add_two(1, 'a')
except:
    console.print_exception
console.save_html("traceback.html")