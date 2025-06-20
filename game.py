import random

class Game:
    def __init__(self):
        self.game_state = self.create_game()
    
    @staticmethod
    def create_game():
        return  [[None for i in range(3)] for i in range(3)]
    
    def reset_game(self):
        self.game_state = self.create_game()
    
    def show_game_state(self):
        tabuleiro = ''
        for i, row in enumerate(self.game_state):
            state = ' | '.join(' ' if cell is None else cell for cell in row)
            print(state)
            if i < len(self.game_state)-1:
                print('-'*3*(len(self.game_state)))
        
    def get_index(self, local):
        local_index = local-1
        size = len(self.game_state)
        
        if local < 1 or local > size*size:
            raise ValueError('o valor não esta no range esperado 1 a 9')
        
        line_index = local_index // size
        colum_index = local_index % size
        return line_index, colum_index
    
    def check_win(self, player):
        win_by_main_diagonal = 0
        win_by_reverse_diagonal = 0
        size = len(self.game_state)
        for i in range(size):
            win_by_line = 0
            win_by_colum = 0
            for j in range(size):
                if player == self.game_state[i][j]:
                    win_by_line += 1
                if player == self.game_state[j][i]:
                    win_by_colum += 1
                if i == j and player == self.game_state[i][j]:
                    win_by_main_diagonal += 1
                if i+j == size-1 and player == self.game_state[i][j]:
                    win_by_reverse_diagonal += 1
            score = [win_by_line, win_by_colum, win_by_main_diagonal, win_by_reverse_diagonal]
            if any(size == i for i in score):
                return True
        return False 

    def check_draw(self):
        return all(cell is not None for row in self.game_state for cell in row)
    
    def put_player(self, player, local):
        line_index, colum_index = self.get_index(local)
        if self.game_state[line_index][colum_index] == None:
            self.game_state[line_index][colum_index] = player
            return True
        return False
    
    def handle_round(self, player, local):
        new_play = self.put_player(player, local)
        self.show_game_state()
        self.handle_game_end(player)
        return new_play
        
    def handle_game_end(self, player):
        end = False
        if self.check_win(player):
            print(f'end of the game player:{player} won')
            end = True
        if self.check_draw():
            print(f'end of the game, it was a draw')
            end = True
        if end:
            self.reset_game()
            self.show_game_state()
    
class HumanvsHuman(Game):
    def __init__(self):
        super().__init__()
        self.player = ['X', 'O']
        self.counter = 0
        
    def create_match(self):
        
        self.show_game_state()
        while True:
            try:  
                
                local = int(input('where are you going to play? choose a place bettwen 1 to 9: '))
                game_status = self.handle_round(self.player[self.counter%2], local)
                if game_status:
                    self.counter += 1
                else: 
                    print('choose a valid position')
                    
            except ValueError:
                print('you must play a number bettwen 1 to 9')


class HumanVsIa(Game):
    def __init__(self):
        super().__init__()
        self.player = ['X', 'O']
        self.counter = 0
        
    def create_match(self):
        
        self.show_game_state()
        while True:
            try:  
                if self.counter%2 == 0:
                    local = int(input('where are you going to play? choose a place bettwen 1 to 9: '))
                    game_status = self.handle_round(self.player[self.counter%2], local)
                    if game_status:
                        self.counter += 1
                    else: 
                        print('choose a valid position')
                else:
                    local = random.randint(1, 9)
                    game_status = self.handle_round(self.player[self.counter%2], local)
                    if game_status:
                        self.counter += 1
                        
            except ValueError:
                print('you must play a number bettwen 1 to 9')

