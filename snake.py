"""
file with snake class
"""
import settings
import pygame

class Snake:
    def __init__(self):
        self.make_snake()
    
    #metod making new snake
    def make_snake(self):
        self.head = BodyPart(192,224)
        self.facing = "left"
        self.body = pygame.sprite.Group()
        self.body.add(BodyPart(208,224))
        self.body.add(BodyPart(224,224))
    
    #updating head and body positions
    def update(self):
        self.move_body()
        self.move_head()

    #move head
    def move_head(self):
        if self.facing == "left":
            self.head.rect.x -= 16
        elif self.facing == "right":
            self.head.rect.x += 16
        elif self.facing == "up":
            self.head.rect.y -= 16
        elif self.facing == "down":
            self.head.rect.y += 16

    #move body parts
    def move_body(self):
        new_pos = self.head.rect
        temp_body = pygame.sprite.Group()
        for part in self.body:
            temp_body.add(BodyPart(new_pos.x,new_pos.y))
            new_pos = part.rect
        self.body = temp_body

    #draw parts on the screen
    def draw(self, window):
        self.head.draw(window)
        self.body.draw(window)

class BodyPart(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x,y,16,16)
        self.image = pygame.Surface((16,16))
        self.image.fill(settings.SNAKE_COLOR)
    
    def draw(self,window):
        window.blit(self.image,self.rect)