from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel("ФАЗА АТАКИ ЮНИТА", style="bold green"))
console.print("[cyan]Юнит[/cyan] атакует!")
console.print("[magenta]Хекс теряет 3 HP![/magenta]")
console.print("[bold red]Юнит наносит 3 очка урона, точно в цель![/bold red]")
console.print("[orange3]И он защищает нужную сторону и получает всего 1 урон![/orange3]")
console.print("[bold green]Бабл активирован! Урона нет![/bold green]")