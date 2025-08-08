class BitunixExecutor:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def place_trade(self, pair, amount, order_type="market"):
        print(f"[Simulated] Placing {order_type} order for {amount} {pair}")
