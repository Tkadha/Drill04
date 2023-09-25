from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK = load_image('TUK_GROUND.png')
character = load_image('spritesheet.png')
def handle_events():
    global running, LR, UD, move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            move = 1
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
            move = 0
            if event.key == SDLK_RIGHT:
                LR -= 1
            elif event.key == SDLK_LEFT:
                LR += 1
            elif event.key == SDLK_UP:
                UD -= 1
            elif event.key == SDLK_DOWN:
                UD += 1


running = True
idle_frame = 0
move_frame = 0
LR, UD = 0, 0
move = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

while running:
    clear_canvas()
    TUK.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if move == 1:
        character.clip_draw(move_frame * 130, 0, 120, 120, x, y)
        move_frame = (move_frame + 1) % 10
        pass
    elif move == 0:
        character.clip_draw(idle_frame * 125, 200, 110, 120, x, y)
        idle_frame = (idle_frame + 1) % 8
    update_canvas()
    handle_events()
    if 10 < x + LR * 10 < TUK_WIDTH-10:
        x += LR * 10
    if 25 < y + UD * 10 < TUK_HEIGHT-25:
        y += UD * 10
    delay(0.07)


close_canvas()
