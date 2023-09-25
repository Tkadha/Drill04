from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK = load_image('TUK_GROUND.png')


def handle_events():
    global running, LR, UD

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False;
            elif event.key == SDLK_RIGHT:
                LR += 1
            elif event.key == SDLK_LEFT:
                LR -= 1
            elif event.key == SDLK_UP:
                UD += 1
            elif event.key == SDLK_DOWN:
                UD -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                LR -= 1
            elif event.key == SDLK_LEFT:
                LR += 1
            elif event.key == SDLK_UP:
                UD -= 1
            elif event.key == SDLK_DOWN:
                UD += 1


running = True
x = 800 // 2
frame = 0

# fill here


close_canvas()
