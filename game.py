import pygame;
from pygame.locals import *;

class App:
    def __init__(self):
        self.running = True;
        self._display_surf = None;
        self.size = self.weight, self.height = 640, 400;
    
    def on_init(self):
        pygame.init();
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE);
        self._running = True;

    def on_execute(self):
        pass;

if __name__ == "__main__":
    theApp = App(); 
    theApp.on_execute();