from mode import Mode

# This is concrete state #1

class Plain(Mode): 
    def process(self, message: str):
        # This is redundant but keeping here 
        processed = message
        return f"[SEND] mode=PLAIN payload={processed}"