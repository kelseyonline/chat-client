# Please see my README for my PUML diagram and explanation of
# my design choice.

# Allows type annotations
from __future__ import annotations

# Hook up the classes to this main file 
from chatclient import Client
# from mode import Mode 
# from plain import Plain 
from encrypted import Encrypted 
from compressed import Compressed

def main() -> None: 
    client = Client()

    client.send("Hello world")

    client.set_mode(Encrypted())
    client.send("Hello world")

    client.set_mode(Compressed())
    client.send("Hello world")

if __name__ == "__main__":
    main()