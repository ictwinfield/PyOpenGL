import glfw

def main():
    if not glfw.init():
        return
        
    win = glfw.create_window(800, 600, "My OpenGL window", None, None)

    if not win:
        glfw.terminate()
        return
    
    glfw.make_context_current(win)

    while not glfw.window_should_close(win):
        glfw.poll_events()
        glfw.swap_buffers(win)
    
    glfw.terminate()

main()