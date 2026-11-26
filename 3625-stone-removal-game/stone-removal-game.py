class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        alice_turn = True
        
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn
            
        # If the loop breaks on Bob's turn (alice_turn is False), Bob cannot move and Alice wins.
        return not alice_turn       