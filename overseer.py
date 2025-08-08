import asyncio
from scraper import sentiment_scraper
from sentiment_analyzer import analyze_sentiment
from volatility_predictor import predict_volatility
from cli_interface import DarkSigilCLI
from trade_executor import BitunixExecutor
from vault_manager import VaultSync

async def overseer():
    print("Initializing Sael'Vareth Overseer Protocol...")
    raw_data = sentiment_scraper(["BTCUSDT", "ETHUSDT", "TRUMPUSDT", "DOGEUSDT"])
    sentiment_scores = analyze_sentiment(raw_data)
    volatility = predict_volatility(sentiment_scores)

    cli = DarkSigilCLI(passphrase=":xSaelVarethx:")
    executor = BitunixExecutor(api_key="YOUR_KEY", api_secret="YOUR_SECRET")
    vault = VaultSync()

    vault.save(volatility)
    await cli.start(executor, vault, volatility)

if __name__ == "__main__":
    asyncio.run(overseer())
