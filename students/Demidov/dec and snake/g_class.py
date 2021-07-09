class Snake():
    import pygame

    size: int
    pos = tuple
    block_size: int

    blocks: list

    directions = {
        'right': (-1, 0),
        'down': (0, -1),
        'left': (1, 0),
        'up': (0, 1),
    }
    
    def __init__(self, screen, size=4, pos=(100, 100,), block_size=20, direction='right'):
        self.size = size
        self.pos = pos
        self.block_size = block_size
        self.screen = screen
        self.direction = direction
        self.blocks = [
            (pos[0]+(block_size*part*self.directions[self.direction][0]),    # X
             pos[1]+(block_size*part*self.directions[self.direction][1]))    # Y
            for part in range(self.size)
        ]

    def draw(self):
        i = True
        for x, y in self.blocks:
            self.pygame.draw.rect(self.screen, (255, 0, 0) if i else (255, 255, 255),
                                (x, y, self.block_size, self.block_size))
            i = False
        self.pygame.display.update()

    def make_step(self):
        self.blocks.insert(0,
            (
                self.blocks[0][0] + (self.block_size * self.directions[self.direction][0]*-1),
                self.blocks[0][1] + (self.block_size * self.directions[self.direction][1]*-1)
            )
        )
        self.blocks.pop(-1)
        self.draw()