import pygame
from time import time
from tkinter import Tk
from glob import glob

__AUTHOR__ = "Marcuss42"
__DATE__ = "02/11/2022"
__VERSION__ = 1.0

class Jogo:
    def __init__(self):
        if "record.txt" not in glob("*") or not open("record.txt").read():
            open("record.txt", "w").write("0")
        
        self.record = int(open("record.txt").read())
        self.initialize_game()
    
    def getScreenSize(self):
        tk = Tk()
        width, height = tk.winfo_screenwidth(), tk.winfo_screenheight()
        tk.destroy()
        return  width, height
        
    def initialize_game(self):
        pygame.init()
        self.width, self.height = [size*0.7 for size in self.getScreenSize()]
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        pygame.display.set_caption("Fuja Da Bolinha!")
        
        self.background = (0, 0, 0)
        self.screen.fill(self.background)

        self.pos = [20, 20]
        self.color = (0, 0, 150)
        self.velocidade = int(self.height/100) + 3
        pygame.draw.circle(self.screen, self.color, self.pos, 10)

        self.start = False
        self.perdeu = False
        
        self.text_color = [255-i for i in self.background]
        self.font = "monospace"
        self.font_size = 30
        self.score = 1

    def inRange(self, x, y, limit):
        equals = 0
        for i, j in zip(x, y):
            if i in [*range(j-limit, j+limit+1)]:
                equals += 1
        
        return equals == len(x)

    def move(self, x, y):
        self.screen.fill(self.background)
        pygame.draw.circle(self.screen, self.color, self.pos, 10)
        self.pos[0] += self.velocidade if self.pos[0] < x else -self.velocidade
        self.pos[1] += self.velocidade if self.pos[1] < y else -self.velocidade

    def cursor(self, color, pos, size):
        pygame.draw.circle(self.screen, color, pos, size)
        
    def restart(self):
        self.pos = [20, 20]
        self.start = True
        self.perdeu = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.ini = time()
        self.score = 0

    def text(self, text, pos):
        font = pygame.font.SysFont(self.font, self.font_size)
        label = font.render(text, 1, self.text_color)
        self.screen.blit(label, pos)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    __import__("sys").exit(0)

                if self.perdeu:
                    if event.type == pygame.KEYDOWN:
                        key = event.key
                        if key in [ord("r"), ord("R")]:
                            self.restart()

                elif event.type == pygame.MOUSEMOTION:
                    if not self.start:
                        self.start = True
                    self.mouse_pos = pygame.mouse.get_pos()

            self.update_game()

    def update_game(self):
        if self.score % 500 == 0:
            self.velocidade += 1

        if self.start:
            if not self.inRange(self.pos, self.mouse_pos, self.velocidade): 
                self.move(*self.mouse_pos)
                self.cursor((0, 100, 0), self.mouse_pos, 8)
            else:
                pygame.display.update()
                self.perdeu = True

        if self.perdeu:
            open("record.txt", "w").write(str(self.record))
            self.move(*self.pos)
            self.cursor((100, 0, 0), self.pos, 8)
            self.text("YOU LOST!!!", (4, self.height/2))
            self.text("R to restart", (4, self.height/2 + self.font_size))
                    
        if not self.perdeu and self.start:
            self.score += 0.5
            
        if self.record < self.score:
            self.record = int(self.score)

        self.text(f"score: {self.score:.0f}", (2, self.height-self.font_size))
        self.text(f"record: {self.record}", (self.width/2, self.height-self.font_size))
        pygame.display.update()

if __name__ == "__main__":
    Jogo().run()
