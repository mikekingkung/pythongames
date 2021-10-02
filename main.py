import os

import pygame

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


ROWS = 16

TILE_SIZE = SCREEN_HEIGHT // ROWS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sprite image loader")

def load_images():
    try:
        print("loading images")
        image_list = []
        for count, filename in enumerate(os.listdir("rename_copy")):
            print("filename is:" + filename)
            # store image tiles in a list
            print("got sprite sheet 2")

            img = pygame.image.load(f'rename_copy/{filename}').convert_alpha()
            print("got sprite sheet 3 ")

            # img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
            print("got sprite sheet 4")

            image_list.append(img)
        return image_list

    except():
        print("An exception was thrown loading images")


def print_hi(name):
    print(name)
    print("in print hi")
    done = False
    try:
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            print("in loop")
            count = 1
            images = load_images()
            for row in range(0, 10):
                for column in range(0, 10):

                    print ("loop count: " + str(count))
                    print("got sprite sheet 5 loop")
                    image_rect = images[count].get_rect(topleft=(100, 300))
                    image_rect.x = 10
                    print("got sprite sheet 5a loop")
                    image_rect.y = 20
                    print("got sprite sheet 5b loop")
                    image_rect = images[count].get_rect()

                    print("got sprite sheet 6 loop")
                    image_rect.x = row * 32

                    print("got sprite sheet 7 loop")
                    image_rect.y = column * 32

                    print("got sprite sheet 8 loop")
                    screen.blit(images[count], image_rect)

                    print("got sprite sheet 9 loop")
                    pygame.display.update()
                    count += 1
    except():
        print("An exception was thrown in main loop")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


