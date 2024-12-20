from settings import *

from random import randint, choice
from functions.import_folder import importFolder


class TargetLine(pygame.sprite.Sprite):
    def __init__(self, battleClass):
        super().__init__()
        self.slashSound = pygame.mixer.Sound('assets/sounds/slash.wav')
        self.frames = importFolder('assets/images/gui/target_line')
        self.battleClass = battleClass
        self.animationSpeed = 0.2
        self.frameIndex = 0

        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
        self.direction = choice([-1, 1])
        if self.direction > 0: self.rect.topleft = (38, 235)
        else: self.rect.topright = (602, 235)

        self.pressed = False
        self.done = False
        self.stay = None
        self.speed = 0

    def move(self):
        self.rect.x += self.speed * self.direction
        if self.speed < 8: self.speed += 0.5
        if self.rect.right > 602 or self.rect.left < 38:
            dealtDamageLabel = damageFont.render('ПР0МАХ', False, '#bfbfbf')
            dealtDamageFill = damageFillFont.render('ПР0МАХ', False, 'Black')
            missImage = pygame.Surface(dealtDamageLabel.get_size(), pygame.SRCALPHA)
            missImage.blit(dealtDamageLabel, (1, 1))
            missImage.blit(dealtDamageFill, (1, 12))

            missTip = pygame.sprite.Sprite()
            missTip.image = missImage
            missTip.rect = missImage.get_rect()
            missTip.rect.topleft = (screenSize[0] / 2 - dealtDamageLabel.get_width() / 2, self.battleClass.enemy.rect.top - 40)

            missTip.update = lambda: (setattr(missTip, 'frame', getattr(missTip, 'frame', 0) + 1),
                                      missTip.kill() if getattr(missTip, 'frame', 0) >= fps * 2 else None)

            self.battleClass.misc.add(missTip)
            self.done = True

    def animate(self):
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(self.frames):
            self.frameIndex = 0
        self.image = self.frames[int(self.frameIndex)]
        if self.stay is not None:
            if self.stay > 0:
                self.stay -= 1
            else:
                self.done = True

    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] and not self.pressed:
            self.slashSound.play()
            accuracy = abs(self.rect.center[0] - 320)
            accMult = 2.2 if accuracy <= 12 else (273 - accuracy) / 273 * 2
            dealtDamage = round((self.battleClass.soul.atk - self.battleClass.enemy.df + randint(0, 2)) * accMult)
            dealtDamage = max(dealtDamage, 0)
            self.battleClass.lastHpProgress = self.battleClass.enemy.hp / self.battleClass.enemy.maxHp * 100
            self.battleClass.enemy.hp -= dealtDamage
            print('Accuracy:', accuracy)
            print('Multiplier:', accMult)
            print('Total:', round(dealtDamage))
            print()

            if dealtDamage > 0:
                dealtDamageLabel = damageFont.render(str(dealtDamage), False, '#d90b06')
                dealtDamageFill = damageFillFont.render(str(dealtDamage), False, 'Black')
            else:
                dealtDamageLabel = damageFont.render('ПР0МАХ', False, '#bfbfbf')
                dealtDamageFill = damageFillFont.render('ПР0МАХ', False, 'Black')
            self.dealtDamage = (pygame.Surface(dealtDamageLabel.get_size(), pygame.SRCALPHA), dealtDamage)
            self.dealtDamage[0].blit(dealtDamageLabel, (1, 1))
            self.dealtDamage[0].blit(dealtDamageFill, (1, 12))

            self.slashSound.play()
            self.pressed = True
            self.stay = fps * 2

    def update(self):
        if self.pressed:
            self.animate()
        else:
            self.move()
            self.getInput()

    def reset(self):
        self.frameIndex = 0

        self.image = self.frames[self.frameIndex]
        self.rect = self.image.get_rect()
        self.direction = choice([-1, 1])
        if self.direction > 0: self.rect.topleft = (38, 235)
        else: self.rect.topright = (602, 235)

        self.pressed = False
        self.done = False
        self.stay = None
        self.speed = 0