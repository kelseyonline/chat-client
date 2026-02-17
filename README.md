### Design choice
Hello Omar, 

To refactor the chat client, I chose the STATE pattern. 

The reason why I chose it is because the behavior depends on an internal 'mode' variable, as described in the homework instructions. Because it is an internal change of state that is determined by the client, rather than a choice by the user, STATE would be the better choice for this task. If I was mistaken, please let me know!

### PUML diagram
Please see below for my PUML diagram.

![PUML diagram for state pattern refactor](/state.png)