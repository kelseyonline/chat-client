from mode import Mode

# This is concrete state #3

class Compressed(Mode): 
    def process(self, message: str):
        processed = "".join(ch for ch in message if ch.lower() not in "aeiou")
        return f"[SEND] mode=COMPRESSED payload={processed}"