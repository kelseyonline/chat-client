from mode import Mode

# This is concrete state #2

class Encrypted(Mode): 
    def send(self, message: str):
        message = message[::-1]
        print(f"[SEND] mode=ENCRYPTED payload={message}")
        return message