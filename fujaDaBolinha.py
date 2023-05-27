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

    def inRange(self, x, y, limit):
        equals = 0
        for i, j in zip(x, y):
            if i in [*range(j-limit, j+limit+1)]:
                equals += 1
        
        return equals == len(x)

    def move(self, x, y):
        self.screen.fill(self.background)
        pygame.draw.circle(self.screen, self.color, self.pos, 10)
        self.pos[0] += self.velo if self.pos[0] < x else -self.velo
        self.pos[1] += self.velo if self.pos[1] < y else -self.velo

    def cursor(self, color, pos, size):
        pygame.draw.circle(self.screen, color, pos, size)
        
    def restart(self):
        self.pos = [20, 20]
        self.start = True
        self.perdeu = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.ini = time()
        self.score = 0

    def text(self, text, font, font_color, size, pos):
        font = pygame.font.SysFont(font, size)
        label = font.render(text, 1, font_color)
        self.screen.blit(label, pos)

    def run(self):
        pygame.init()
        tk = Tk()
        w = tk.winfo_screenwidth()
        h = tk.winfo_screenheight()
        self.width = w * 0.7
        self.height = h * 0.7
        self.background = (0, 0, 0)

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fuja Da Bolinha!")
        self.screen.fill(self.background)

        self.pos = [20, 20]
        self.color = (0, 0, 150)
        self.velo = int(self.height/100) + 3
        pygame.draw.circle(self.screen, self.color, self.pos, 10)

        self.start = False
        self.perdeu = False
        
        text_color = [255-i for i in self.background]
        font = "monospace"
        font_size = 30

        self.score = 1

        while True:

            if self.score%500 == 0:
                self.velo += 1
   
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

            if self.start:
                if not self.inRange(self.pos, self.mouse_pos, self.velo): 
                    self.move(*self.mouse_pos)
                    self.cursor((0, 100, 0), self.mouse_pos, 8)

                else:
                    pygame.display.update()
                    self.perdeu = True
                    
                if self.perdeu:
                    open("record.txt", "w").write(str(self.record))
                    self.move(*self.pos)
                    self.cursor((100, 0, 0), self.pos, 8)
                    self.text(f"YOU LOST!!!", font, 
                        (200, 200, 0), font_size, (4, self.height/2))

                    self.text(f"R to restart", font, 
                        text_color, font_size, (4, self.height/2 + font_size))
                    
            if not self.perdeu and self.start:
                self.score += 0.5
            
            if self.record < self.score:
                self.record = int(self.score)

            self.text(f"score: {self.score:.0f}", font, 
                        text_color, font_size, (2, self.height-font_size))
            
            self.text(f"record: {self.record}", font, 
                        text_color, font_size, (self.width/2, self.height-font_size))
            pygame.display.update()

if __name__ == "__main__":
    Jogo().run()