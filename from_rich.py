from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Красивые панели
console.print(Panel("ФАЗА АТАКИ ЮНИТА", style="bold green"))
console.print("→ [cyan]Юнит[/cyan] атакует!")
console.print("💥 [red]Хекс теряет 3 HP![/red]")