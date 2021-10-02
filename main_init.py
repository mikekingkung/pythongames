import pygame

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FRAME_WIDTH = 32
FRAME_HEIGHT = 32



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("spritesheets")
print("getting sprite sheet")
sprite_sheet_image = pygame.image.load("img/Nh32.png").convert_alpha()
print("got sprite sheet")

def get_image(sprite_sheet_image, xpos, ypos):
    image = pygame.Surface((32, 32)).convert_alpha()
    image.blit(sprite_sheet_image, (0, 0), (xpos , ypos,  32, 32))
    return image

def save_image(filename, xpos, ypos):
    print("getting image from sprite sheet")
    print("xpos:" + str(xpos))
    print("ypos:" + str(ypos))
    frame = get_image(sprite_sheet_image, xpos, ypos)
    print("saving image")
    pygame.image.save(frame, filename)
    print("saved image" + filename)

def print_hi(name):

    try:
        xpos = 0
        ypos = 0
        for row in range(1, 38):
            for column in range(1, 31):
                filename = f'img/{column}_{row}.png'
                print("filename is:" + filename)
                save_image(filename, xpos, ypos)
                xpos = column * FRAME_WIDTH
                ypos = row * FRAME_HEIGHT
    except():
        print("An exception was thrown")








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
