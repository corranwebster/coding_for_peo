import cocos

class Title(cocos.layer.Layer):

    def __init__(self):
        super(Title, self).__init__()
        
        label = cocos.text.Label(
            'MONSTER SMASH!!!!!!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center',
            anchor_y='center',
        )
        label.position = (320, 240)
        self.add(label)
        
        label = cocos.text.Label(
            'a cubics production by Peo Webster',
            font_name='Times New Roman',
            font_size=22,
            anchor_x='center',
            anchor_y='center',
        )
        label.position = (320, 210)
        self.add(label)
        
if __name__ == '__main__':
    cocos.director.director.init()
    title = Title()
    main_scene = cocos.scene.Scene(title)
    cocos.director.director.run(main_scene)
    
    