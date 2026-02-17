from mode import Mode

# This is concrete state #3

class Compressed(Mode): 
    def send(self, message: str):
        message = "".join(ch for ch in message if ch.lower() not in "aeiou")
        print(f"[SEND] mode=COMPRESSED payload={message}")
        return message