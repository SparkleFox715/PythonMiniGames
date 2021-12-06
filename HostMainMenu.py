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
        while(boo):
            if not n.connect()==None:
                print(n.connect())
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
                    n.send("Closing")
                    run = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b1OutsideY<pygame.mouse.get_pos()[1] < self.b1OutsideY+self.outsideHeight:
                        print("begin")
                        n.send(self.username)
                        n.send("Begin")
                        return
                    elif self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b2OutsideY<pygame.mouse.get_pos()[1] < self.b2OutsideY+self.outsideHeight:
                        pygame.quit()
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
                     
            if self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b1OutsideY<pygame.mouse.get_pos()[1] < self.b1OutsideY+self.outsideHeight:
                self.screenstate1 = 1
            elif self.outsideX < pygame.mouse.get_pos()[0] < self.outsideX+self.outsideWidth and self.b2OutsideY<pygame.mouse.get_pos()[1] < self.b2OutsideY+self.outsideHeight:
                self.screenstate1 = 2
            else:
                self.screenstate1 = 0        
            if self.screenstate1 ==1:
                # creating start button
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX-5, self.b1OutsideY-5, self.outsideWidth+10, self.outsideHeight+10), 10, 10)
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX-5, self.b1InsideY-5, self.insideWidth+10, self.insideHeight+10))
                # creating end button
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX, self.b2OutsideY, self.outsideWidth, self.outsideHeight), 10, 10)
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX, self.b2InsideY, self.insideWidth, self.insideHeight))
            elif self.screenstate1 ==2:
                # creating start button
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX, self.b1OutsideY, self.outsideWidth, self.outsideHeight), 10, 10)
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX, self.b1InsideY, self.insideWidth, self.insideHeight))
                # creating end button
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.outsideX-5, self.b2OutsideY-5, self.outsideWidth+10, self.outsideHeight+10), 10, 10)
                pygame.draw.rect(self.surface, self.color, pygame.Rect(self.insideX-5, self.b2InsideY-5, self.insideWidth+10, self.insideHeight+10))
            else:
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
            pygame.display.update()
            try:
                data = n.client.recv(2048).decode()
                if not (data == None or data=="time out"):
                    print(data)
                    if self.username2 =="":
                        self.username2 = data  
                     
            except:
                pass
        
