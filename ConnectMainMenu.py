import pygame
import sys

class Menu:
    def __init__(self, surface, boo, n):
        self.surface = surface
        self.color = (108, 91, 123)
        self.textColor = (248, 177, 149)
        self.textBoxBackground = (255,140,148)
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
        self.screenstate1 =0
        self.username = "USERNAME"
        self.username2 = ""
        self.active = False
        self.n = n
        self.num = 0
        while(boo):
            
            self.surface.fill((246, 114, 128))
            #Username textbox
            inputrect = pygame.Rect(self.outsideX,self.b1OutsideY-130,self.outsideWidth,self.outsideHeight-50)
            pygame.draw.rect(self.surface, self.textBoxBackground, inputrect)
            font = pygame.font.Font('gillsans.ttf', 30)
            text = font.render(self.username, True, (255,211,181))
            textRect = text.get_rect()
            textRect.center = (self.outsideX+self.outsideWidth/2, self.b1OutsideY-130+(self.outsideHeight-50)/2)
            surface.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # if self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b1OutsideY<pygame.mouse.get_pos()[1] < self.b1OutsideY+self.outsideHeight:
                    #     print("begin")
                    #     n.send(self.username)
                    #     return
                    # elif self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b2OutsideY<pygame.mouse.get_pos()[1] < self.b2OutsideY+self.outsideHeight:
                    #     pygame.quit()
                    if inputrect.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                if event.type == pygame.KEYDOWN:
                        if self.active:
                            if event.key == pygame.K_BACKSPACE:
                                self.username = self.username[:-1]
                            else:
                                if(textRect.w<171):
                                    self.username += event.unicode
                pygame.display.update()
                try:
                    data = n.client.recv(2048).decode()
                    if not (data == None or data=="time out"):
                        self.username2 = data.split("Begin")[0]
                        n.send(self.username)
                        return
                except:
                    pass
                     
            
        
