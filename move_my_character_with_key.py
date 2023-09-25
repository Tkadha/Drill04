from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')
def handle_events():
    global running, LR, UD, move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
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
frame = 0
LR, UD = 0, 0
move = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    TUK.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 65, 0, 60, 60, x, y)
    frame = (frame + 1) % 10
    update_canvas()
    handle_events()
    if 10 < x + LR * 10 < TUK_WIDTH-10:
        x += LR * 10
    if 25 < y + UD * 10 < TUK_HEIGHT-25:
        y += UD * 10
    delay(0.07)


close_canvas()
