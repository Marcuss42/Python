# Tutorial: https://www.instructables.com/Python-coding-for-Minecraft/
from mine import Minecraft, block
from sys import argv
from random import choice
from time import sleep
import input

class Cube:
    def __init__(self, mine):
        self.mine = mine

        self.x, self.y, self.z = self.mine.player.getPos() 
        self.height = 3
        self.y = self.y + self.height

        self.cube = {
            'U': [[block.WOOL_YELLOW for _ in range(3)] for _ in range(3)],  # Face superior (Up)
            'L': [[block.WOOL_CYAN for _ in range(3)] for _ in range(3)],  # Face esquerda (Left)
            'F': [[block.WOOL_RED for _ in range(3)] for _ in range(3)],  # Face frontal (Front)
            'R': [[block.WOOL_LIME for _ in range(3)] for _ in range(3)],  # Face direita (Right)
            'B': [[block.WOOL_ORANGE for _ in range(3)] for _ in range(3)],  # Face traseira (Back)
            'D': [[block.WOOL_WHITE for _ in range(3)] for _ in range(3)]   # Face inferior (Down)
        }

        """
        self.movs = {
            'U': self.U,
            'I': self.U_reverse,
            'L': self.L,
            'K': self.L_reverse,
            'F': self.F,
            'G': self.F_reverse,
            'R': self.R,
            'T': self.R_reverse,
            'B': self.B,        
            'V': self.B_reverse, 
            'D': self.D,
            'C': self.D_reverse,
            'M': self.M,
            'N': self.M_reverse,
            'S': self.S,
            'A': self.S_reverse,
            'E': self.E,
            'W': self.E_reverse,
            'X': self.X,
            'Y': self.Y,
            'Z': self.Z
        }
        """

        self.movs = {
            'U': self.U,
            'I': self.U_reverse,
            'L': self.L,
            'K': self.L_reverse,
            'F': self.F,
            'G': self.F_reverse,
            'R': self.R,
            '4': self.R_reverse,
            'B': self.B,
            'V': self.B_reverse,
            'O': self.D,
            'P': self.D_reverse,
            'M': self.M,
            'N': self.M_reverse,
            'H': self.S,
            'J': self.S_reverse,
            '1': self.E,
            '2': self.E_reverse,
            'X': self.X,
            'Y': self.Y,
            'Z': self.Z,
            '3': self.shuffle,
            '5': self.reset
        }
        

    def reset(self):
        self.cube = {
            'U': [[block.WOOL_YELLOW for _ in range(3)] for _ in range(3)],  # Face superior (Up)
            'L': [[block.WOOL_CYAN for _ in range(3)] for _ in range(3)],  # Face esquerda (Left)
            'F': [[block.WOOL_RED for _ in range(3)] for _ in range(3)],  # Face frontal (Front)
            'R': [[block.WOOL_GREEN for _ in range(3)] for _ in range(3)],  # Face direita (Right)
            'B': [[block.WOOL_ORANGE for _ in range(3)] for _ in range(3)],  # Face traseira (Back)
            'D': [[block.WOOL_WHITE for _ in range(3)] for _ in range(3)]   # Face inferior (Down)
        }

        return self

    def display_cube(self, end='\n\n'):
        
        # U & D
        U = self.cube['U']
        D = self.cube['D'][::-1]

        for i in range(len(U)):
            for j in range(len(U[i])):
                self.mine.setBlock(self.x+2-j, self.y+4, self.z+4-i, U[i][j])
                self.mine.setBlock(self.x+2-j, self.y, self.z+4-i, D[i][j]) 
        
        # R & L
        R = self.cube['R']
        L = self.cube['L']

        for i in range(len(R)):
            for j in range(len(L[i])):
                self.mine.setBlock(self.x-1, self.y+3-i, self.z+2+j, R[i][j])
                self.mine.setBlock(self.x+3, self.y+3-i, self.z+4-j, L[i][j]) 
                
        # F & B
       
        F = self.cube['F']
        B = self.cube['B']

        for i in range(len(F)):
            for j in range(len(B[i])):
                self.mine.setBlock(self.x+2-j, self.y+3-i, self.z+1, F[i][j])
                self.mine.setBlock(self.x+j, self.y+3-i, self.z+5, B[i][j]) 
                
        # Board
        for i in range(3):
            self.mine.setBlock(self.x+i, self.y+4, self.z+1, block.WOOL_BLACK)
            self.mine.setBlock(self.x+i, self.y+4, self.z+5, block.WOOL_BLACK)
            
            self.mine.setBlock(self.x+i, self.y, self.z+1, block.WOOL_BLACK)
            self.mine.setBlock(self.x+i, self.y, self.z+5, block.WOOL_BLACK)

            self.mine.setBlock(self.x+3, self.y+4, self.z+4-i, block.WOOL_BLACK)
            self.mine.setBlock(self.x-1, self.y+4, self.z+4-i, block.WOOL_BLACK)

            self.mine.setBlock(self.x+3, self.y, self.z+4-i, block.WOOL_BLACK)
            self.mine.setBlock(self.x-1, self.y, self.z+4-i, block.WOOL_BLACK)

            self.mine.setBlock(self.x+3, self.y+3-i, self.z+5, block.WOOL_BLACK)
            self.mine.setBlock(self.x-1, self.y+3-i, self.z+1, block.WOOL_BLACK)

            self.mine.setBlock(self.x+3, self.y+3-i, self.z+1, block.WOOL_BLACK)
            self.mine.setBlock(self.x-1, self.y+3-i, self.z+5, block.WOOL_BLACK)

        # Seletor face dianteira
        self.mine.setBlock(self.x+1, self.y+4, self.z+1, block.WOOL_GRAY)
        self.mine.setBlock(self.x+1, self.y, self.z+1, block.WOOL_GRAY)
        self.mine.setBlock(self.x-1, self.y+2, self.z+1, block.WOOL_GRAY)
        self.mine.setBlock(self.x+3, self.y+2, self.z+1, block.WOOL_GRAY)

        return self
        
    def tutorial(self, end='\n\n'):
        movs = ['Q - Quit']
        for k, v in self.movs.items():
            mov = f'''{k} - {v.__name__.replace("_reverse", "'")}'''
            movs.append(mov)
            self.mine.postToChat(mov)
            
        print('\n'.join(movs), file=open('cubo_tutorial.txt', 'w'))
        
        return self
            
    def shuffle(self, steps = 20):
        shuffle_seq = []
        for _ in range(steps):
            mov = choice([*self.movs.keys()][:-3])
            shuffle_seq.append(mov)
            self.movs[mov]()

        return shuffle_seq
    
    def test_movs(self, shuffle_steps = 20):
        shuffle_seq = cubo.shuffle(shuffle_steps)[::-1]
        movs_items = [*cubo.movs.items()]
        movs_keys = [*cubo.movs.keys()]
        reverse_shuffle_seq = []

        for s in shuffle_seq:
            for k, v in movs_items:
                if k == s:
                    if 'reverse' in v.__name__ :
                        mov = movs_keys[movs_keys.index(k)-1]

                    else:
                        mov = movs_keys[movs_keys.index(k)+1]
                    cubo.movs[mov]()
                    reverse_shuffle_seq.append(mov)
        return shuffle_seq, reverse_shuffle_seq

    def rotate_face(self, face, orientation='right', steps=1):
        matrix = self.cube[face]
        num_rows = 3
        num_cols = 3
        
        steps %= 4

        rotated_face = [[0] * num_rows for _ in range(num_cols)]
        
        for i in range(num_rows):
            for j in range(num_cols):
                if orientation == 'right':
                    if steps == 1:
                        rotated_face[j][num_rows - 1 - i] = matrix[i][j]
                    elif steps == 2:
                        rotated_face[num_rows - 1 - i][num_cols - 1 - j] = matrix[i][j]
                    elif steps == 3:
                        rotated_face[num_cols - 1 - j][i] = matrix[i][j]
                elif orientation == 'left':
                    if steps == 1:
                        rotated_face[num_cols - 1 - j][i] = matrix[i][j]
                    elif steps == 2:
                        rotated_face[num_rows - 1 - i][num_cols - 1 - j] = matrix[i][j]
                    elif steps == 3:
                        rotated_face[j][num_rows - 1 - i] = matrix[i][j]
        
        self.cube[face] = rotated_face
        return rotated_face

    def X(self):
        self.rotate_face('L', orientation='left')
        self.rotate_face('R')

        backup_F = self.cube['F']
        backup_D = self.cube['D']
        backup_U = self.cube['U']
        backup_B = self.cube['B']
        
        self.cube['F'] = backup_D
        self.cube['D'] = backup_B[::-1]
        self.cube['B'] = backup_U[::-1]
        self.cube['U'] = backup_F

        return self

    def Y(self): 
        self.rotate_face('D', orientation='left')
        self.rotate_face('U')

        backup_F = self.cube['F']
        backup_R = self.cube['R']
        backup_B = self.cube['B']
        backup_L = self.cube['L']
        
        self.cube['F'] = backup_R
        self.cube['R'] = backup_B
        self.cube['B'] = backup_L
        self.cube['L'] = backup_F
        
        return self

    def Z(self): 
        self.rotate_face('B', orientation='left')
        self.rotate_face('F')

        backup_U = self.cube['U']
        backup_R = self.cube['R']
        backup_D = self.cube['D']
        backup_L = self.cube['L']
        
        self.cube['U'] = backup_L
        self.rotate_face('U')
        self.cube['L'] = backup_D
        self.rotate_face('L')
        self.cube['D'] = backup_R
        self.rotate_face('D')
        self.cube['R'] = backup_U
        self.rotate_face('R')

        return self

    def U(self):
        self.rotate_face('U')
        
        backup_F = self.cube['F'][0]
        backup_L = self.cube['L'][0]
        backup_R = self.cube['R'][0]
        backup_B = self.cube['B'][0]
        
        self.cube['F'][0] = backup_R
        self.cube['L'][0] = backup_F
        self.cube['B'][0] = backup_L
        self.cube['R'][0] = backup_B

        return self

    def U_reverse(self):
        self.rotate_face('U', orientation='left')
        
        backup_F = self.cube['F'][0]
        backup_L = self.cube['L'][0]
        backup_R = self.cube['R'][0]
        backup_B = self.cube['B'][0]
        
        self.cube['F'][0] = backup_L
        self.cube['R'][0] = backup_F
        self.cube['B'][0] = backup_R
        self.cube['L'][0] = backup_B

        return self

    def R(self):
        self.rotate_face('R')
        backup_F = [self.cube['F'][i][2] for i in range(3)]
        backup_U = [self.cube['U'][i][2] for i in range(3)]
        backup_D = [self.cube['D'][i][2] for i in range(3)]
        backup_B = [self.cube['B'][i][0] for i in range(3)]
        
        self.cube['F'][0][2], self.cube['F'][1][2], self.cube['F'][2][2] = backup_D
        self.cube['U'][0][2], self.cube['U'][1][2], self.cube['U'][2][2] = backup_F
        self.cube['B'][0][0], self.cube['B'][1][0], self.cube['B'][2][0] = backup_U[::-1]
        self.cube['D'][0][2], self.cube['D'][1][2], self.cube['D'][2][2] = backup_B[::-1]

        return self

    def R_reverse(self):
        self.rotate_face('R', orientation='left')

        backup_F = [self.cube['F'][i][2] for i in range(3)]
        backup_U = [self.cube['U'][i][2] for i in range(3)]
        backup_D = [self.cube['D'][i][2] for i in range(3)]
        backup_B = [self.cube['B'][i][0] for i in range(3)]
        
        self.cube['F'][0][2], self.cube['F'][1][2], self.cube['F'][2][2] = backup_U
        self.cube['U'][0][2], self.cube['U'][1][2], self.cube['U'][2][2] = backup_B[::-1]
        self.cube['B'][0][0], self.cube['B'][1][0], self.cube['B'][2][0] = backup_D[::-1]
        self.cube['D'][0][2], self.cube['D'][1][2], self.cube['D'][2][2] = backup_F
    
        return self

    def F(self): 
        self.rotate_face('F')

        backup_R = [self.cube['R'][i][0] for i in range(3)]
        backup_U = self.cube['U'][2]
        backup_D = self.cube['D'][0]
        backup_L = [self.cube['L'][i][2] for i in range(3)]
        
        self.cube['U'][2] = backup_L[::-1]
        self.cube['L'][0][2], self.cube['L'][1][2], self.cube['L'][2][2] = backup_D
        self.cube['D'][0] = backup_R[::-1]
        self.cube['R'][0][0], self.cube['R'][1][0], self.cube['R'][2][0] = backup_U
        
        return self

    def F_reverse(self): 
        self.rotate_face('F', orientation='left')

        backup_R = [self.cube['R'][i][0] for i in range(3)]
        backup_U = self.cube['U'][2]
        backup_D = self.cube['D'][0]
        backup_L = [self.cube['L'][i][2] for i in range(3)]
        
        self.cube['U'][2] = backup_R
        self.cube['R'][0][0], self.cube['R'][1][0], self.cube['R'][2][0] = backup_D[::-1]
        self.cube['D'][0] = backup_L
        self.cube['L'][0][2], self.cube['L'][1][2], self.cube['L'][2][2] = backup_U[::-1]
        
        return self

    def L_reverse(self):
        self.rotate_face('L', orientation='left')

        backup_F = [self.cube['F'][i][0] for i in range(3)]
        backup_U = [self.cube['U'][i][0] for i in range(3)]
        backup_D = [self.cube['D'][i][0] for i in range(3)]
        backup_B = [self.cube['B'][i][2] for i in range(3)]
        
        self.cube['F'][0][0], self.cube['F'][1][0], self.cube['F'][2][0] = backup_D
        self.cube['U'][0][0], self.cube['U'][1][0], self.cube['U'][2][0] = backup_F
        self.cube['B'][0][2], self.cube['B'][1][2], self.cube['B'][2][2] = backup_U[::-1]
        self.cube['D'][0][0], self.cube['D'][1][0], self.cube['D'][2][0] = backup_B[::-1]
        
        return self

    def L(self):
        self.rotate_face('L')

        backup_F = [self.cube['F'][i][0] for i in range(3)]
        backup_U = [self.cube['U'][i][0] for i in range(3)]
        backup_D = [self.cube['D'][i][0] for i in range(3)]
        backup_B = [self.cube['B'][i][2] for i in range(3)]
        
        self.cube['F'][0][0], self.cube['F'][1][0], self.cube['F'][2][0] = backup_U
        self.cube['U'][0][0], self.cube['U'][1][0], self.cube['U'][2][0] = backup_B[::-1]
        self.cube['B'][0][2], self.cube['B'][1][2], self.cube['B'][2][2] = backup_D[::-1]
        self.cube['D'][0][0], self.cube['D'][1][0], self.cube['D'][2][0] = backup_F

        return self

    def D(self):
        self.rotate_face('D')
        
        backup_F = self.cube['F'][2]
        backup_L = self.cube['L'][2]
        backup_R = self.cube['R'][2]
        backup_B = self.cube['B'][2]
        
        self.cube['F'][2] = backup_L
        self.cube['R'][2] = backup_F
        self.cube['B'][2] = backup_R
        self.cube['L'][2] = backup_B
        
        return self

    def D_reverse(self):
        self.rotate_face('D', orientation='left')
        
        backup_F = self.cube['F'][2]
        backup_L = self.cube['L'][2]
        backup_R = self.cube['R'][2]
        backup_B = self.cube['B'][2]
        
        self.cube['F'][2] = backup_R
        self.cube['L'][2] = backup_F
        self.cube['B'][2] = backup_L
        self.cube['R'][2] = backup_B


        return self

    def B(self): 
        self.rotate_face('B')

        backup_R = [self.cube['R'][i][2] for i in range(3)]
        backup_U = self.cube['U'][0]
        backup_D = self.cube['D'][2]
        backup_L = [self.cube['L'][i][0] for i in range(3)]
        
        self.cube['U'][0] = backup_R
        self.cube['R'][0][2], self.cube['R'][1][2], self.cube['R'][2][2] = backup_D[::-1]
        self.cube['D'][2] = backup_L[::-1]
        self.cube['L'][0][0], self.cube['L'][1][0], self.cube['L'][2][0] = backup_U[::-1]

        return self

    def B_reverse(self): 
        self.rotate_face('B', orientation='left')

        backup_R = [self.cube['R'][i][2] for i in range(3)]
        backup_U = self.cube['U'][0]
        backup_D = self.cube['D'][2]
        backup_L = [self.cube['L'][i][0] for i in range(3)]
        
        self.cube['U'][0] = backup_L[::-1]
        self.cube['R'][0][2], self.cube['R'][1][2], self.cube['R'][2][2] = backup_U
        self.cube['D'][2] = backup_R[::-1]
        self.cube['L'][0][0], self.cube['L'][1][0], self.cube['L'][2][0] = backup_D[::-1]

        return self

    def M(self):
        backup_F = [self.cube['F'][i][1] for i in range(3)]
        backup_U = [self.cube['U'][i][1] for i in range(3)]
        backup_D = [self.cube['D'][i][1] for i in range(3)]
        backup_B = [self.cube['B'][i][1] for i in range(3)]
        
        self.cube['F'][0][1], self.cube['F'][1][1], self.cube['F'][2][1] = backup_D
        self.cube['U'][0][1], self.cube['U'][1][1], self.cube['U'][2][1] = backup_F
        self.cube['B'][0][1], self.cube['B'][1][1], self.cube['B'][2][1] = backup_U[::-1]
        self.cube['D'][0][1], self.cube['D'][1][1], self.cube['D'][2][1] = backup_B[::-1]
        
        return self

    def M_reverse(self):
        backup_F = [self.cube['F'][i][1] for i in range(3)]
        backup_U = [self.cube['U'][i][1] for i in range(3)]
        backup_D = [self.cube['D'][i][1] for i in range(3)]
        backup_B = [self.cube['B'][i][1] for i in range(3)]

        self.cube['F'][0][1], self.cube['F'][1][1], self.cube['F'][2][1] = backup_U
        self.cube['U'][0][1], self.cube['U'][1][1], self.cube['U'][2][1] = backup_B[::-1]
        self.cube['B'][0][1], self.cube['B'][1][1], self.cube['B'][2][1] = backup_D[::-1]
        self.cube['D'][0][1], self.cube['D'][1][1], self.cube['D'][2][1] = backup_F

        return self

    def S(self): 
        backup_R = [self.cube['R'][i][1] for i in range(3)]
        backup_U = self.cube['U'][1]
        backup_D = self.cube['D'][1]
        backup_L = [self.cube['L'][i][1] for i in range(3)]
        
        self.cube['U'][1] = backup_L[::-1]
        self.cube['L'][0][1], self.cube['L'][1][1], self.cube['L'][2][1] = backup_D
        self.cube['D'][1] = backup_R[::-1]
        self.cube['R'][0][1], self.cube['R'][1][1], self.cube['R'][2][1] = backup_U

        return self

    def S_reverse(self): 
        backup_R = [self.cube['R'][i][1] for i in range(3)]
        backup_U = self.cube['U'][1]
        backup_D = self.cube['D'][1]
        backup_L = [self.cube['L'][i][1] for i in range(3)]
        
        self.cube['U'][1] = backup_R
        self.cube['R'][0][1], self.cube['R'][1][1], self.cube['R'][2][1] = backup_D[::-1]
        self.cube['D'][1] = backup_L
        self.cube['L'][0][1], self.cube['L'][1][1], self.cube['L'][2][1] = backup_U[::-1]

        return self

    def E(self): 
        backup_F = self.cube['F'][1]
        backup_L = self.cube['L'][1]
        backup_R = self.cube['R'][1]
        backup_B = self.cube['B'][1]
        
        self.cube['F'][1] = backup_L
        self.cube['R'][1] = backup_F
        self.cube['B'][1] = backup_R
        self.cube['L'][1] = backup_B

        return self

    def E_reverse(self): 
        backup_F = self.cube['F'][1]
        backup_L = self.cube['L'][1]
        backup_R = self.cube['R'][1]
        backup_B = self.cube['B'][1]
        
        self.cube['F'][1] = backup_R
        self.cube['L'][1] = backup_F
        self.cube['B'][1] = backup_L
        self.cube['R'][1] = backup_B

        return self


def main():
    mine = Minecraft()
    cube = Cube(mine)
    cube.tutorial().shuffle()
    
    while not input.wasPressedSinceLast(input.KEY_Q):
        for mov in cube.movs.keys():
            if input.wasPressedSinceLast(getattr(input, f'KEY_{mov}')):
                retorno = cube.movs[mov]()
                if isinstance(retorno, list):
                    shuffle_seq = []
                    for mov in retorno:
                        shuffle_seq.append(cube.movs[mov].__name__.replace("_reverse", "'"))
                    mine.postToChat(f"Shuffle Sequence: {' '.join(shuffle_seq)}")
        cube.display_cube()
        sleep(.2)
        
if __name__ == '__main__':
    main()
