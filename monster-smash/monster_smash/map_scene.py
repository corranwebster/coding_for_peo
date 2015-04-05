import cocos
from cocos.actions import MoveBy
import pyglet.image
import pyglet.window.key

SIZE = (21, 13)
print SIZE

class Player(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(Player, self).__init__()
        images = pyglet.image.load(
        'hero.png'
        )
        image_grid=pyglet.image.ImageGrid(images, *SIZE)
        print image_grid[10,0]
        
        
        self.player = cocos.sprite.Sprite(
            image_grid[10,0]
        )
        self.player.position = (320, 240)
        self.add(self.player)
        
    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.RIGHT and self.player.position[0] <= 640-32:
            self.player.do(MoveBy((32,0), duration=0.2))
        if key == pyglet.window.key.LEFT and self.player.position[0] >= 32:
            self.player.do(MoveBy((-32,0), duration=0.2))
        if key == pyglet.window.key.UP and self.player.position[1] <= 480-32:
            self.player.do(MoveBy((0,32), duration=0.2))
        if key == pyglet.window.key.DOWN and self.player.position[1] >= 32:
            self.player.do(MoveBy((0,-32), duration=0.2))

class Monster(cocos.layer.Layer):
    def __init__(self):
        super(Monster,self).__init__()
        monster = cocos.sprite.Sprite('zombie.png')
        monster.position = (310, 210)
        self.add(monster)
    
                
if __name__ == '__main__':
    cocos.director.director.init()
    player = Player()
    monster = Monster()
    main_scene = cocos.scene.Scene(player, monster)
    cocos.director.director.run(main_scene)

        