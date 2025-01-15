import time
import requests
from rich.console import Console
from rich.table import Table

console = Console()

def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,cardano&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Erro ao obter os preços: {e}[/red]")
        return None

def display_prices():
    console.clear()
    while True:
        prices = get_prices()
        if prices:
            table = Table(title="Preços em Tempo Real")

            # Adicionar colunas
            table.add_column("Criptomoeda", justify="center", style="cyan", no_wrap=True)
            table.add_column("Preço (USD)", justify="center", style="green")

            # Adicionar dados e linhas separadoras
            for i, (coin, data) in enumerate(prices.items()):
                table.add_row(coin.capitalize(), f"${data['usd']:,.2f}")
                if i < len(prices) - 1:  # Adicionar separador, exceto após a última linha
                    table.add_row("---", "---")
            
            console.print(table)
        time.sleep(60)  # Atualiza a cada 60 segundos

if __name__ == "__main__":
    display_prices()