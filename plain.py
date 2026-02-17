from mode import Mode

# This is concrete state #1

class Plain(Mode): 
    def send(self, message: str):
        print(f"[SEND] mode=PLAIN payload={message}")
        return message