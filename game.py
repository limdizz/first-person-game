from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

print('''-----FPS GAME DEMO-----
There is a demonstration of Ursina Engine features and my experience during its learning.\n''')
i = input('What level you want to run? (choose 1 or 2)\n')
if i == '1' or i == '2':

    app = Ursina()

    window.exit_button.visible = False
    window.fps_counter.enabled = False

    Entity.default_shader = lit_with_shadows_shader

    shootables_parent = Entity()
    mouse.traverse_target = shootables_parent

    editor_camera = EditorCamera(enabled=False, ignore_paused=True)
    player = FirstPersonController(z=10, speed=30, origin_y=-5, x=-5)
    player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))


    class Enemy1(Entity):
        def __init__(self, **kwargs):
            super().__init__(parent=shootables_parent,
                             model='assets\\enemy\\source\\bloody.fbx',
                             texture='assets\\enemy\\textures\\bloody.png',
                             scale=0.05, origin_y=-.5, color=color.light_gray,
                             collider='box', **kwargs)
            self.health_bar = Entity(parent=self, y=1.2, model='cube',
                                     color=color.red, world_scale=(1.5, .1, .1))
            self.max_hp = 100
            self.hp = self.max_hp

        def update(self):
            dist = distance_xz(player.position, self.position)
            if dist > 40:
                return

            self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

            self.look_at_2d(player.position, 'y')
            hit_info = raycast(self.world_position + Vec3(0, 1, 0),
                               self.forward, 30, ignore=(self,))
            if hit_info.entity == player:
                if dist > 2:
                    self.position += self.forward * time.dt * 50

        @property
        def hp(self):
            return self._hp

        @hp.setter
        def hp(self, value):
            self._hp = value
            if value <= 0:
                destroy(self)
                return

            self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
            self.health_bar.alpha = 1

        @property
        def hp(self):
            return self._hp

        @hp.setter
        def hp(self, value):
            self._hp = value
            if value <= 0:
                destroy(self)
                return

            self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
            self.health_bar.alpha = 1

    class Enemy2(Entity):
        def __init__(self, **kwargs):
            super().__init__(parent=shootables_parent,
                             model='assets\\enemy\\source\\balljointdoll.fbx',
                             texture='assets\\enemy\\textures\\doll.png',
                             scale=0.3, origin_y=-8, color=color.light_gray,
                             collider='box', **kwargs)
            self.health_bar = Entity(parent=self, y=1.2, model='cube',
                                     color=color.red, world_scale=(1.5, .1, .1))
            self.max_hp = 100
            self.hp = self.max_hp

        def update(self):
            dist = distance_xz(player.position, self.position)
            if dist > 40:
                return

            self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

            self.look_at_2d(player.position, 'y')
            hit_info = raycast(self.world_position + Vec3(0, 1, 0),
                               self.forward, 30, ignore=(self,))
            if hit_info.entity == player:
                if dist > 2:
                    self.position += self.forward * time.dt * 50

        @property
        def hp(self):
            return self._hp

        @hp.setter
        def hp(self, value):
            self._hp = value
            if value <= 0:
                destroy(self)
                return

            self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
            self.health_bar.alpha = 1

        @property
        def hp(self):
            return self._hp

        @hp.setter
        def hp(self, value):
            self._hp = value
            if value <= 0:
                destroy(self)
                return

            self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
            self.health_bar.alpha = 1


    class Level1Class(Entity):
        def __init__(self, **kwargs):
            super().__init__()
            self.blocks = []
            self.enemies = [Enemy1(x=x * 1) for x in range(50)]
            self.audio = Audio('assets\\music\\metal.mp3', volume=0.4)
            window.fullscreen = True

        def environment(self):
            Sky(texture="sky_sunset")
            self.ground = Entity(
                model='plane',
                texture='grass',
                collider='mesh',
                scale=Vec3(100, 1, 100))

            self.wall1 = Entity(parent=scene,
                                scale=0.02,
                                position=Vec3(-50, -0.5, 0),
                                rotation=Vec3(0, 270, 0),
                                model='assets\\wall\\source\\stone-wall.FBX',
                                texture='assets\\wall\\textures\\stonewall.jpeg',
                                collider='box')

            # Front wall
            self.wall2 = duplicate(self.wall1, position=Vec3(-50, -0.50, -10))
            self.wall3 = duplicate(self.wall1, position=Vec3(-50, -0.50, -20))
            self.wall4 = duplicate(self.wall1, position=Vec3(-50, -0.50, -30))
            self.wall5 = duplicate(self.wall1, position=Vec3(-50, -0.50, -40))
            self.wall6 = duplicate(self.wall1, position=Vec3(-50, -0.50, -50))
            self.wall7 = duplicate(self.wall1, position=Vec3(-50, -0.50, 0))
            self.wall8 = duplicate(self.wall1, position=Vec3(-50, -0.50, 10))
            self.wall9 = duplicate(self.wall1, position=Vec3(-50, -0.50, 20))
            self.wall10 = duplicate(self.wall1, position=Vec3(-50, -0.50, 30))
            self.wall11 = duplicate(self.wall1, position=Vec3(-50, -0.50, 40))
            self.wall12 = duplicate(self.wall1, position=Vec3(-50, -0.50, 50))

            # Left side wall
            self.wall13 = duplicate(self.wall1, position=Vec3(-50, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall14 = duplicate(self.wall1, position=Vec3(-40, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall15 = duplicate(self.wall1, position=Vec3(-30, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall16 = duplicate(self.wall1, position=Vec3(-20, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall17 = duplicate(self.wall1, position=Vec3(-10, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall18 = duplicate(self.wall1, position=Vec3(0, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.gates = Entity(parent=scene, scale=0.04,
                                model='assets\\gates\\source\\bigdoor.fbx',
                                texture='assets\\gates\\textures\\big door.png',
                                position=Vec3(10, 2, -36.5),
                                rotation=Vec3(0, 180, 0),
                                collider='box')
            self.wall19 = duplicate(self.wall1, position=Vec3(20, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall20 = duplicate(self.wall1, position=Vec3(30, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall21 = duplicate(self.wall1, position=Vec3(40, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))
            self.wall22 = duplicate(self.wall1, position=Vec3(50, -0.50, -50),
                                    rotation=Vec3(0, 180, 0))

            # Back wall
            self.wall23 = duplicate(self.wall1, position=Vec3(50, -0.50, -10),
                                    rotation=Vec3(0, 90, 0))
            self.wall24 = duplicate(self.wall1, position=Vec3(50, -0.50, -20),
                                    rotation=Vec3(0, 90, 0))
            self.wall25 = duplicate(self.wall1, position=Vec3(50, -0.50, -30),
                                    rotation=Vec3(0, 90, 0))
            self.wall26 = duplicate(self.wall1, position=Vec3(50, -0.50, -40),
                                    rotation=Vec3(0, 90, 0))
            self.wall27 = duplicate(self.wall1, position=Vec3(50, -0.50, -50),
                                    rotation=Vec3(0, 90, 0))
            self.wall28 = duplicate(self.wall1, position=Vec3(50, -0.50, 0),
                                    rotation=Vec3(0, 90, 0))
            self.wall29 = duplicate(self.wall1, position=Vec3(50, -0.50, 10),
                                    rotation=Vec3(0, 90, 0))
            self.wall30 = duplicate(self.wall1, position=Vec3(50, -0.50, 20),
                                    rotation=Vec3(0, 90, 0))
            self.wall31 = duplicate(self.wall1, position=Vec3(50, -0.50, 30),
                                    rotation=Vec3(0, 90, 0))
            self.wall32 = duplicate(self.wall1, position=Vec3(50, -0.50, 40),
                                    rotation=Vec3(0, 90, 0))
            self.wall33 = duplicate(self.wall1, position=Vec3(50, -0.50, 50),
                                    rotation=Vec3(0, 90, 0))

            # Right side wall
            self.wall34 = duplicate(self.wall1, position=Vec3(-50, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall35 = duplicate(self.wall1, position=Vec3(-40, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall36 = duplicate(self.wall1, position=Vec3(-30, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall37 = duplicate(self.wall1, position=Vec3(-20, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall38 = duplicate(self.wall1, position=Vec3(-10, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall39 = duplicate(self.wall1, position=Vec3(0, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall40 = duplicate(self.wall1, position=Vec3(10, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall41 = duplicate(self.wall1, position=Vec3(20, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall42 = duplicate(self.wall1, position=Vec3(30, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall43 = duplicate(self.wall1, position=Vec3(40, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))
            self.wall44 = duplicate(self.wall1, position=Vec3(50, -0.50, 50),
                                    rotation=Vec3(0, 0, 0))

        def weapons(self):
            self.tommygun = Entity(
                parent=camera.ui,
                scale=0.00003,
                model='assets\\weapons\\tommygun\\source\\tommygun.fbx',
                texture='assets\\weapons\\tommygun\\textures\\tommygun.png',
                position=Vec3(0.8, -0.4, 1.4),
                rotation=Vec3(0, 105, -5),
                on_cooldown=False,
                visible=False)

            self.pistol = Entity(
                parent=camera.ui,
                scale=0.025,
                model='assets\\weapons\\pistol\\source\\pistol.fbx',
                texture='assets\\weapons\\pistol\\textures\\pistol.png',
                position=Vec3(0.45, -.35, 0),
                rotation=Vec3(-2, 195, 0),
                on_cooldown=False,
                visible=False)

            self.weapons = [self.tommygun, self.pistol]
            self.current_weapon = 0
            self.change_weapon()

        def change_weapon(self):
            for x, y in enumerate(self.weapons):
                if x == self.current_weapon:
                    y.visible = True
                else:
                    y.visible = False

        def shoot(self):
            from ursina.prefabs.ursfx import ursfx
            if self.current_weapon == 0 and not self.tommygun.on_cooldown:
                self.tommygun.on_cooldown = True
                ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)],
                      volume=1, wave='assets//sounds//tommygun.mp3',
                      speed=3.0)
                invoke(setattr, self.tommygun, 'on_cooldown', False, delay=.15)
            elif self.current_weapon == 1 and not self.pistol.on_cooldown:
                self.pistol.on_cooldown = True
                ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)],
                      volume=1, wave='assets//sounds//pistol.mp3',
                      speed=3.0)
                invoke(setattr, self.pistol, 'on_cooldown', False, delay=.15)

            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 4
                mouse.hovered_entity.blink(color.red)

        def update(self):
            if held_keys['left mouse']:
                self.shoot()

            if held_keys['left mouse']:
                self.tommygun.position = Vec3(0.85, -0.45, 1.35)
                self.pistol.position = Vec3(0.5, -.42, 0.3)
            else:
                self.tommygun.position = Vec3(0.8, -0.4, 1.4)
                self.pistol.position = Vec3(0.45, -.35, 0)

            if player.intersects(self.gates):
                print('Thanks for 1st level playing!'
                      ' If you want to load a 2nd level,'
                      ' run this app again and enter 2')
                quit()

        def input(self, key):
            try:
                self.current_weapon = int(key) - 1
                self.change_weapon()
            except:
                pass

            if key == 'scroll up':
                self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
                self.change_weapon()

            elif key == 'scroll down':
                self.current_weapon = (self.current_weapon - 1) % len(self.weapons)
                self.change_weapon()

    class Level2Class(Entity):
        def __init__(self, **kwargs):
            super().__init__()
            self.blocks = []
            self.enemies = [Enemy2(z=z * 1) for z in range(8)]
            self.enemies2 = [Enemy1(x=x*2) for x in range(10)]
            window.fullscreen = True
            from ursina.prefabs.ursfx import ursfx
            self.audio = Audio('assets\\music\\Lament_Of_The_Ancients.mp3', volume=0.5)

        def environment(self):
            Sky(texture="sky/dark_sky")
            self.ground = Entity(model='plane', collider='box', scale=64,
                                 texture='ursina_logo.png', texture_scale=(10, 10))
            for b in range(7):
                Entity(model='cube', origin_y=-.5, scale=2, texture='brick',
                       texture_scale=(1, 2),
                       x=random.uniform(-8, 8),
                       z=random.uniform(-8, 8) + 8,
                       collider='box',
                       scale_y=random.uniform(2, 3),
                       color=color.hsv(0, 0, random.uniform(.9, 1)))

        def weapons(self):
            self.knife = Entity(
                parent=camera.ui,
                scale=0.001,
                model='assets\\weapons\\knife\\source\\knife.fbx',
                texture='assets\\weapons\\knife\\textures\\knife.png',
                position=Vec3(0.5, -.4, 1),
                rotation=Vec3(0, 0, -5),
                on_cooldown=False,
                visible=False)

            self.sword = Entity(
                parent=camera.ui,
                scale=0.009,
                model='assets\\weapons\\sword\\source\\sword.FBX',
                texture='assets\\weapons\\sword\\textures\\sword.png',
                position=Vec3(0.5, -0.025, 1),
                rotation=Vec3(0, 0, 180),
                on_cooldown=False,
                visible=False)

            self.weapons = [self.knife, self.sword]
            self.current_weapon = 0
            self.change_weapon()

        def change_weapon(self):
            for x, y in enumerate(self.weapons):
                if x == self.current_weapon:
                    y.visible = True
                else:
                    y.visible = False

        def input(self, key):
            try:
                self.current_weapon = int(key) - 1
                self.change_weapon()
            except:
                pass

            if key == 'scroll up':
                self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
                self.change_weapon()

            elif key == 'scroll down':
                self.current_weapon = (self.current_weapon - 1) % len(self.weapons)
                self.change_weapon()

        @staticmethod
        def knife_kick():
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 1
                mouse.hovered_entity.blink(color.red)

        def update(self):
            if held_keys['left mouse']:
                self.knife_kick()

    pause_handler = Entity(ignore_paused=True)
    pause_text = Text('PAUSED', origin=(0, 0), scale=2,
                      enabled=False)  # Make a Text saying "PAUSED"


    def pause_handler_input(key):
        if key == 'escape':
            application.paused = not application.paused  # Pause/unpause the game.
            pause_text.enabled = application.paused  # Also toggle "PAUSED" graphic.


    pause_handler.input = pause_handler_input


    def input(key):
        if key == 'q':
            quit()


    def window_choice():
        if i == '1':
            level = Level1Class()
            level.environment()
            level.weapons()

            sun = DirectionalLight()
            sun.look_at(Vec3(1, -1, -1))

            app.run()

        if i == '2':
            level = Level2Class()
            level.environment()
            level.weapons()

            app.run()

    window_choice()
