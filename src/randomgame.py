import time
from src.agents import QLearningAgent, MonteCarloAgent
from src.players import Player
from src.turn import Turn
from src.cards import Card, Deck
from src.utils import check_win, block_print, enable_print, bold
import config as conf


class RandomGame(open_card, our_hand, opp_hand, played_cards):
    """
    Randomly plays feasible moves from the two hands and returns a winner. 
    Create two plays and set_hand to our_hand and opp_hand
    1. start with opponent
    while no winner:
    """
    
    def __init__ (self, open_card, our_hand, opp_hand, played_cards):
        
        self.player_1 = Player(1, agent=randomPlay)
        self.player_2 = Player(2, agent=randomPlay)
        self.player_1.set_hand(our_hand)
        self.player_2.set_hand(opp_hand)
        self.turn = Turn(
            deck = Deck().discardList(pdlayed_cards),
            player_1=self.player_1,
            player_2=self.player_2,
            agent=randomPlay
        )
        self.turn_no = 0
        self.winner = 0 #will be 1 if player 1 wins, and 2 if opponent wins
        
        while self.winner == 0:
            self.turn_no += 1
            if (self.turn_no == 1):
                card_open = open_card
            else:
                card_open = self.turn.card_open
            
            if self.turn_no%2 == 1: player_act, player_pas = self.player_1, self.player_2
            else:                   player_act, player_pas = self.player_2, self.player_1
            
            player_act.show_hand()
            player_act.show_hand_play(card_open)
            self.turn.action(
                player=player_act, 
                opponent=player_pas, 
                agent=agent,
                #algorithm=algorithm
            )
            
            if check_win(player_act) == True:
                self.winner = player_act.name
                print (f'{player_act.name} has won!')
                break
                
            if check_win(player_pas) == True:
                self.winner = player_pas.name
                print (f'{player_pas.name} has won!')
                break
                
            if player_act.card_play.value in ["REV", "SKIP"]:
                print (f'{player_act.name} has another turn')
                self.turn_no = self.turn_no-1
                
            if (self.turn.count > 0) and (self.turn.count %2 == 0):
                print (f'Again it is {player_act.name}s turn')
                self.turn_no = self.turn_no-1
        

        self.player_1.identify_state(card_open)
        agent.update(self.player_1.state, self.player_1.action)