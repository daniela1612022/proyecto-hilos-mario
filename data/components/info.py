import pygame as pg
import threading
from .. import setup
from .. import constants as c
from . import flashing_coin

class Character(pg.sprite.Sprite):
    """Clase principal para todos los caracteres utilizados 
    para la información del nivel superior"""
    def __init__(self, image):
        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()


class OverheadInfo(object):
    """Clase para información de nivel como puntuación, total de monedas,
         y tiempo restante"""
    def __init__(self, game_info, state):
        self.sprite_sheet = setup.GFX['text_images']
        self.coin_total = game_info[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        self.total_lives = game_info[c.LIVES]
        self.top_score = game_info[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_info = game_info

        self.create_image_dict()
        self.create_score_group()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_countdown_clock()
        self.create_coin_counter()
        self.create_flashing_coin()
        self.create_mario_image()
        self.create_game_over_label()
        self.create_time_out_label()
        self.create_main_menu_labels()


    def create_image_dict(self):
        """Crea las imágenes iniciales para la partitura."""
        self.image_dict = {}
        image_list = []

        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))

        image_list.append(self.get_image(83, 230, 7, 7))
        image_list.append(self.get_image(91, 230, 7, 7))
        image_list.append(self.get_image(99, 230, 7, 7))
        image_list.append(self.get_image(107, 230, 7, 7))
        image_list.append(self.get_image(115, 230, 7, 7))
        image_list.append(self.get_image(123, 230, 7, 7))
        image_list.append(self.get_image(3, 238, 7, 7))
        image_list.append(self.get_image(11, 238, 7, 7))
        image_list.append(self.get_image(20, 238, 7, 7))
        image_list.append(self.get_image(27, 238, 7, 7))
        image_list.append(self.get_image(35, 238, 7, 7))
        image_list.append(self.get_image(44, 238, 7, 7))
        image_list.append(self.get_image(51, 238, 7, 7))
        image_list.append(self.get_image(59, 238, 7, 7))
        image_list.append(self.get_image(67, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        image_list.append(self.get_image(83, 238, 7, 7))
        image_list.append(self.get_image(91, 238, 7, 7))
        image_list.append(self.get_image(99, 238, 7, 7))
        image_list.append(self.get_image(108, 238, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(123, 238, 7, 7))
        image_list.append(self.get_image(3, 246, 7, 7))
        image_list.append(self.get_image(11, 246, 7, 7))
        image_list.append(self.get_image(20, 246, 7, 7))
        image_list.append(self.get_image(27, 246, 7, 7))
        image_list.append(self.get_image(48, 248, 7, 7))

        image_list.append(self.get_image(68, 249, 6, 2))
        image_list.append(self.get_image(75, 247, 6, 6))



        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image


    def get_image(self, x, y, width, height):
        """Extrae la imagen de la hoja de sprites"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey((92, 148, 252))
        image = pg.transform.scale(image,
                                   (int(rect.width*2.9),
                                    int(rect.height*2.9)))
        return image


    def create_score_group(self):
        """Crea la partitura vacía inicial (000000)"""
        self.score_images = []
        self.create_label(self.score_images, '000000', 75, 55)


    def create_info_labels(self):
        """Crea las etiquetas que describen cada información."""
        self.mario_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []


        self.create_label(self.mario_label, 'MARIO', 75, 30)
        self.create_label(self.world_label, 'NIVEL', 450, 30)
        self.create_label(self.time_label, 'TIEMPO', 625, 30)
        self.create_label(self.stage_label, '1-1', 472, 55)

        self.label_list = [self.mario_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]


    def create_load_screen_labels(self):
        """Crea etiquetas para la información central de una pantalla de carga."""
        world_label = []
        number_label = []

        self.create_label(world_label, 'MUNDO', 280, 200)
        self.create_label(number_label, '1-1', 430, 200)

        self.center_labels = [world_label, number_label]


    def create_countdown_clock(self):
        """Crea el reloj de cuenta regresiva para el nivel."""
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)


    def create_label(self, label_list, string, x, y):
        """Crea una etiqueta (NIVEL, TIEMPO, MARIO)"""
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))

        self.set_label_rects(label_list, x, y)


    def set_label_rects(self, label_list, x, y):
        """Establecer la ubicación de cada personaje individual"""
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2


    def create_coin_counter(self):
        """Crea la información que rastrea la cantidad de monedas que Mario recolecta."""
        self.coin_count_images = []
        self.create_label(self.coin_count_images, '*00', 300, 55)


    def create_flashing_coin(self):
        """Crea la moneda parpadeante junto al total de monedas."""
        self.flashing_coin = flashing_coin.Coin(280, 53)


    def create_mario_image(self):
        """Obtener la imagen de mario"""
        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center=(378, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives),
                          450, 285)

        self.sprite_sheet = setup.GFX['mario_bros']
        self.mario_image = self.get_image(178, 32, 12, 16)
        self.mario_rect = self.mario_image.get_rect(center=(320, 290))


    def create_game_over_label(self):
        """Crea la etiqueta para la pantalla GAME OVER"""
        game_label = []
        over_label = []

        self.create_label(game_label, 'JHON PERDISTE', 280, 300)
        self.create_label(over_label, 'LA NOTA ES 50', 280, 350)

        self.game_over_label = [game_label, over_label]


    def create_time_out_label(self):
        """Crea la etiqueta para la pantalla de tiempo de espera."""
        time_out_label = []

        self.create_label(time_out_label, 'SE ACABO EL TIEMPO', 290, 310)
        self.time_out_label = [time_out_label]


    def create_main_menu_labels(self):
        """Crear etiquetas para la pantalla MENÚ PRINCIPAL"""
        player_one_game = []
        player_two_game = []
        top = []
        top_score = []

        self.create_label(player_one_game, '1 JUGADOR', 272, 360)
        self.create_label(player_two_game, '2 JUGADORES', 272, 405)
        self.create_label(top, 'TOP - ', 290, 465)
        self.create_label(top_score, '000000', 400, 465)

        self.main_menu_labels = [player_one_game, player_two_game,
                                 top, top_score]


    def update(self, level_info, mario=None):
        """Actualiza toda la información general"""
        self.mario = mario
        self.handle_level_state(level_info)


    def handle_level_state(self, level_info):
        """Actualiza la información según el estado en el que se encuentra el juego."""
        if self.state == c.MAIN_MENU:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_score_images(self.main_menu_labels[3], self.top_score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.LOAD_SCREEN:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.LEVEL:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            if level_info[c.LEVEL_STATE] != c.FROZEN \
                    and self.mario.state != c.WALKING_TO_CASTLE \
                    and self.mario.state != c.END_OF_LEVEL_FALL \
                    and not self.mario.dead:
                self.update_count_down_clock(level_info)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.TIME_OUT:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.GAME_OVER:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.FAST_COUNT_DOWN:
            level_info[c.SCORE] += 50
            self.score = level_info[c.SCORE]
            self.update_count_down_clock(level_info)
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])
            if self.time == 0:
                self.state = c.END_OF_LEVEL

        elif self.state == c.END_OF_LEVEL:
            self.flashing_coin.update(level_info[c.CURRENT_TIME])


    def update_score_images(self, images, score):
        """Actualiza qué números se van a borrar para la puntuación."""
        index = len(images) - 1

        for digit in reversed(str(score)):
            rect = images[index].rect
            images[index] = Character(self.image_dict[digit])
            images[index].rect = rect
            index -= 1


    def update_count_down_clock(self, level_info):
        """Actualiza la hora actual"""
        if self.state == c.FAST_COUNT_DOWN:
            self.time -= 1

        elif (level_info[c.CURRENT_TIME] - self.current_time) > 400:
            self.current_time = level_info[c.CURRENT_TIME]
            self.time -= 1
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)
        if len(self.count_down_images) < 2:
            for i in range(2):
                self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)
        elif len(self.count_down_images) < 3:
            self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)


    def update_coin_total(self, level_info):
        """Actualiza el total de monedas y ajusta la etiqueta en consecuencia."""
        self.coin_total = level_info[c.COIN_TOTAL]

        coin_string = str(self.coin_total)
        if len(coin_string) < 2:
            coin_string = '*0' + coin_string
        elif len(coin_string) > 2:
            coin_string = '*00'
        else:
            coin_string = '*' + coin_string

        x = self.coin_count_images[0].rect.x
        y = self.coin_count_images[0].rect.y

        self.coin_count_images = []

        self.create_label(self.coin_count_images, coin_string, x, y)


    def draw(self, surface):
        """Dibuja información general según el estado."""
        if self.state == c.MAIN_MENU:
            self.draw_main_menu_info(surface)
        elif self.state == c.LOAD_SCREEN:
            self.draw_loading_screen_info(surface)
        elif self.state == c.LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.GAME_OVER:
            self.draw_game_over_screen_info(surface)
        elif self.state == c.FAST_COUNT_DOWN:
            self.draw_level_screen_info(surface)
        elif self.state == c.END_OF_LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.TIME_OUT:
            self.draw_time_out_screen_info(surface)
        else:
            pass



    def draw_main_menu_info(self, surface):
        """Dibuja información para el menú principal."""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_loading_screen_info(self, surface):
        """Dibuja información para la pantalla de carga."""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.mario_image, self.mario_rect)
        surface.blit(self.life_times_image, self.life_times_rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_level_screen_info(self, surface):
        """Extrae información durante el juego normal."""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for digit in self.count_down_images:
                surface.blit(digit.image, digit.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)


    def draw_game_over_screen_info(self, surface):
        """Dibuja información cuando termina el juego."""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_time_out_screen_info(self, surface):
        """Dibuja información cuando está en la pantalla de tiempo de espera"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

def update_and_print(overhead_info, level_info):
    """Actualiza la información y muestra mensajes en consola"""
    print("Estado actual:", overhead_info.state)
    overhead_info.update(level_info)
    overhead_info.draw(pg.display.get_surface())