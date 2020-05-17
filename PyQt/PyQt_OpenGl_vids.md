### vid1.py
The opening class make the the window an OpenGl context.  A lot of the code just does the rendering and listens for events (window resize).  This class can be left alone to do its stuff.

The second class is where we do our OpenGl programming.
The __init__ function just calls the __init__ for our previous OpenGLWindow class and makes place holders for each of the shader attributes and the the shader itself.

The initialize function compiles the sources to the shader and gets the positions of the attributes in the shader program.

The render function is where we do all our work.  In this example of the render function we have the vertices followed by the colours.

### vid2.py
The main change here is that we have added the layout location to vertex_src