COOPERATE = False
DEFECT = True
import random

class MyPlayer:
    '''Player that moves based on payoff,
        if vs self -> switches to copycat'''
    def __init__(self, payoff_matrix, number_of_iterations=None):
        self.payoff_matrix = payoff_matrix
        self.number_of_iterations = number_of_iterations
        self.history = []
        self.switch_count = 0
        self.number_of_iterations_played = 0
        self.both_cooperate = payoff_matrix[COOPERATE][COOPERATE]
        self.both_defect = payoff_matrix[DEFECT][DEFECT]
        self.was_betrayed = payoff_matrix[COOPERATE][DEFECT]
        self.betrays = payoff_matrix[DEFECT][COOPERATE]
         
    def record_last_moves(self, my_last_move, opponent_last_move):
        self.history.append((my_last_move, opponent_last_move))
     
    def select_move(self):
        opponent_last_move = None
        my_last_move = None

        if len(self.history) != 0:
            last_move = self.history[-1]
            my_last_move = last_move[0]
            opponent_last_move = last_move[1]
        if len(self.history) < 7:
            if len(self.history) == 0:
                return COOPERATE
            elif len(self.history) == 1:
                return COOPERATE
            elif len(self.history) == 2:
                return DEFECT
            elif len(self.history) == 3:
                return DEFECT
            elif len(self.history) == 4:
                return COOPERATE
            elif len(self.history) == 5:
                return COOPERATE
            
        if (self.history[0][0] == COOPERATE and self.history[1][0] == COOPERATE and self.history[2][0] == DEFECT and self.history[3][0] == DEFECT and self.history[4][0] == COOPERATE and self.history[5][0] == COOPERATE and self.both_cooperate >= self.both_defect):
            last_move = self.history[-1]
            opponent_last_move = last_move[1]
            return opponent_last_move
        else:
            if self.number_of_iterations != None:
                self.number_of_iterations_played += 1
                if self.number_of_iterations_played - self.number_of_iterations == 0 and self.betrays >= self.both_cooperate:
                    return DEFECT
            if my_last_move != opponent_last_move:
                self.switch_count += 1
            else:
                self.switch_count = 0
            if self.switch_count >= 5:
                return COOPERATE
            else: 
                if opponent_last_move == COOPERATE:
                    if self.both_cooperate >= self.betrays:
                        return COOPERATE
                    else:
                        return DEFECT
                else:
                    if self.both_defect >= self.was_betrayed:
                        return DEFECT
                    else:
                        return COOPERATE
                


