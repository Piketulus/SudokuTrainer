import pygame

class Button:

    def __init__(self, x, y, width, height, text, color, text_color, font, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font = font
        self.action = action

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, 1, self.text_color)
        win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x < x1 < self.x + self.width and self.y < y1 < self.y + self.height:
            if self.action is not None:
                self.action()