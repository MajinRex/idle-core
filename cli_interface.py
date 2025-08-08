class DarkSigilCLI:
    def __init__(self, passphrase):
        self.passphrase = passphrase

    async def start(self, executor, vault, signals):
        entered = input("Enter passphrase: ")
        if entered != self.passphrase:
            print("Access Denied.")
            return
        print("Dark Sigil CLI Active.")
        print("Signals:", signals)
