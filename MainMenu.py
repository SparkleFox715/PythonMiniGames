import pygame


class Menu:
    def __init__(self, surface, boo):
        self.surface = surface
        self.color = (108, 91, 123)
        self.textColor = (248, 177, 149)
        self.outsideX = 300
        self.insideX = 310
        self.b1OutsideY = 216
        self.b1InsideY = 226
        self.b2OutsideY = 482
        self.b2InsideY = 492
        self.outsideWidth = 200
        self.insideWidth = 180
        self.outsideHeight = 100
        self.insideHeight = 80
        if boo:
            # creating start button
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX, self.b1OutsideY, self.outsideWidth, self.outsideHeight), 10, 10)
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX, self.b1InsideY, self.insideWidth, self.insideHeight))
            # creating end button
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX, self.b2OutsideY, self.outsideWidth, self.outsideHeight), 10, 10)
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX, self.b2InsideY, self.insideWidth, self.insideHeight))
            # Start Text
            textx = 400
            texty = 260
            pygame.display.set_caption("Mini Games")
            font = pygame.font.Font('gillsans.ttf', 32)
            text = font.render('Start', True, self.textColor)
            textRect = text.get_rect()
            textRect.center = (textx, texty)
            surface.blit(text, textRect)
            # End Text
            text = font.render('Exit', True, self.textColor)
            textRect = text.get_rect()
            textRect.center = (textx, texty + 266)
            surface.blit(text, textRect)
        pygame.draw
