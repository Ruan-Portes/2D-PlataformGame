import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
        def __init__(self,pos):
            super().__init__()
            self.import_character_assets()
            self.frame_index = 0
            self.animation_speed = 0.15
            self.current_animation = 'idle'
            self.image = self.animations[self.current_animation][self.frame_index]
            self.rect = self.image.get_rect(topleft = pos)

            # player movement
            self.direction = pygame.math.Vector2(0,0)
            self.speed = 8
            self.gravity = 0.8
            self.jump_speed = -16

        def import_character_assets(self):
            character_path = '../graphics/character/'
            self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

            for animation in self.animations.keys():
                full_path = character_path + animation
                self.animations[animation] = import_folder(full_path)
        
        def get_input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.direction.x = 1
            elif keys[pygame.K_a]:
                self.direction.x = -1
            else:
                self.direction.x = 0
            if keys[pygame.K_SPACE]:
                self.jump()

        def apply_gravity(self):
            self.direction.y += self.gravity
            self.rect.y += self.direction.y

        def jump(self):
            self.direction.y = self.jump_speed

        def update(self):
            self.get_input()
            # Update the animation framw on the animation speed
            self.frame_index += self.animation_speed

            # Check if the animation needs to loop
            if self.frame_index >= len(self.animations[self.current_animation]):
                 self.frame_index = 0
            
            # Update the image based on the current animation frame index
            self.image = self.animations[self.current_animation][int(self.frame_index)]

