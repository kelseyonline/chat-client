from mode import Mode

# This is concrete state #2

class Encrypted(Mode): 
    def process(self, message: str):
        processed = message[::-1]
        return f"[SEND] mode=ENCRYPTED payload={processed}"