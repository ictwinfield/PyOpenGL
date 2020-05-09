import glfw

def key_pressed(window, key, scancode, action, mods):
    if key == 69:
        print("You pressed E")
    else:
        print("A key was pressed")

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