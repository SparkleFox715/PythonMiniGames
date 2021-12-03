import pygame


class Menu:
    def __init__(self, surface):
        self.surface = surface
        color = (108, 91, 123)
        textColor = (248, 177, 149)
        outsideX = 300
        insidex = 310
        b1OutsideY = 216
        b1InsideY = 226
        b2OutsideY = 482
        b2InsideY = 492
        outsideWidth = 200
        insideWidth = 180
        outsideHeight = 100
        insideHeight = 80
        # creating start button
        pygame.draw.rect(self.surface, color, pygame.Rect(outsideX, b1OutsideY, outsideWidth, outsideHeight), 10, 10)
        pygame.draw.rect(self.surface, color, pygame.Rect(insidex, b1InsideY, insideWidth, insideHeight))
        # creating end button
        pygame.draw.rect(self.surface, color, pygame.Rect(outsideX, b2OutsideY, outsideWidth, outsideHeight), 10, 10)
        pygame.draw.rect(self.surface, color, pygame.Rect(insidex, b2InsideY, insideWidth, insideHeight))
        # Start Text
        textx = 400
        texty = 260
        pygame.display.set_caption("Mini Games")
        font = pygame.font.Font('gillsans.ttf', 32)
        text = font.render('Start', True, textColor)
        textRect = text.get_rect()
        textRect.center = (textx, texty)
        surface.blit(text, textRect)
        # End Text
        text = font.render('Exit', True, textColor)
        textRect = text.get_rect()
        textRect.center = (textx, texty + 266)
        surface.blit(text, textRect)
        pygame.draw
