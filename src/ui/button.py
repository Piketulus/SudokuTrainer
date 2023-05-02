import pygame


class Button:
    """
    Class that represents a button on the screen.
    """

    def __init__(self, x, y, width, height, text, normalcolor, hovercolor, text_color, font, action=None, usable=True):
        """
         Initialize the button with the given parameters.

         Args:
                 x: The x position of button.
                 y: The y position of button.
                 width: The width of the button.
                 height: The height of the button.
                 text: The text to display on the button.
                 normalcolor: The color of the button normally.
                 hovercolor: The color of the button when the mouse is hovering over it.
                 text_color: The color of the button's text.
                 font: The font used for the text.
                 action: The action to take when the mouse is clicked.
                 usable: A boolean indicating whether or not the button is usable
        """
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
        self._clicked = False

    def draw(self, screen):
        """
         Draws the object on the screen.

         Args:
                 screen: The screen to draw on
        """
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, 1, self.text_color)
        screen.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                    self.y + (self.height/2 - text.get_height()/2)))

    def process(self):
        """
         Process the event and call the action if it's not None.
        """
        if self.usable:
            mousepos = pygame.mouse.get_pos()
            self.color = self.normalcolor
            if self.x < mousepos[0] < self.x + self.width and self.y < mousepos[1] < self.y + self.height:
                if pygame.mouse.get_pressed()[0] and not self._clicked:
                    self._clicked = True
                    self.color = self.hovercolor
                    if self.action != None:
                        self.action()
                elif not pygame.mouse.get_pressed()[0] and self._clicked:
                    self._clicked = False
                else:
                    self.color = self.hovercolor
