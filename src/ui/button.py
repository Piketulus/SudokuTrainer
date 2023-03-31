import pygame

class Button:

    def __init__(self, x, y, width, height, text, normalcolor, hovercolor, text_color, font, action=None, usable=True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = normalcolor
        self.normalcolor = normalcolor
        self.hovercolor = hovercolor
        self.text_color = text_color
        self.font = font
        self.action = action
        self.usable = usable


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, 1, self.text_color)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    

    def process(self):
        if self.usable:
            mousepos = pygame.mouse.get_pos()
            self.color = self.normalcolor
            if self.x < mousepos[0] < self.x + self.width and self.y < mousepos[1] < self.y + self.height:
                if pygame.mouse.get_pressed()[0]:
                    self.color = self.hovercolor
                    if self.action != None:
                        self.action()
                else:
                    self.color = self.hovercolor
