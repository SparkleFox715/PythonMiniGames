import pygame
class Menu:
    def __init__(self, surface):
        self.surface = surface
        color = (108, 91, 123)
        #creating start button
        pygame.draw.rect(self.surface, color, pygame.Rect(300,216, 200, 100),10,10)
        pygame.draw.rect(self.surface, color, pygame.Rect(310,226, 180, 80))
        #creating end button
        pygame.draw.rect(self.surface, color, pygame.Rect(300,482, 200, 100),10,10)
        pygame.draw.rect(self.surface, color, pygame.Rect(310,492, 180, 80))
        #Start Text
        textColor = (248, 177, 149)
        textx = 400
        texty = 260
        pygame.display.set_caption("Mini Games")
        font = pygame.font.Font('gillsans.ttf', 32)
        text = font.render('Start', True, textColor )
        textRect = text.get_rect()
        textRect.center = (textx, texty)
        surface.blit(text, textRect)
        #End Text
        font = pygame.font.Font('gillsans.ttf', 32)
        text = font.render('Exit', True, textColor )
        textRect = text.get_rect()
        textRect.center = (textx, texty+266)
        surface.blit(text, textRect)
        pygame.draw

        
