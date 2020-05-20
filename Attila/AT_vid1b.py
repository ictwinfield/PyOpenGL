import glfw


states = [0, 0, 0, 0]
def key_pressed(window, key, scancode, action, mods):
    
    print(key)
    if key == 65 and action == 1 and states[1] == 0:
        states[0] = 8
    if key == 83 and action == 1 and states[0] == 0:
        states[1] = 4
    if key == 80 and action == 1 and states[3] == 0:
        states[2] = 2
    if key == 76 and action == 1 and states[2] == 0:
        states[3] = 1
    if key == 65 and action == 0:
        states[0] = 0
    if key == 83 and action == 0:
        states[1] = 0
    if key == 80 and action == 0:
        states[2] = 0
    if key == 76 and action == 0:
        states[3] = 0
    
    direction = sum(states)
    if direction == 0:
        print("Not moving")
    elif direction == 10:
        print("Moving NW")
    elif direction == 9:
        print("Moving SW")
    elif direction == 8:
        print("Moving W")
    else:
        print("Another direction")

def main():
    if not glfw.init():
        return
        
    win = glfw.create_window(800, 600, "My OpenGL window", None, None)
    glfw.set_key_callback(win, key_pressed)
    if not win:
        glfw.terminate()
        return
    
    glfw.make_context_current(win)

    while not glfw.window_should_close(win):
        glfw.poll_events()
        glfw.swap_buffers(win)
        
    
    glfw.terminate()




main()