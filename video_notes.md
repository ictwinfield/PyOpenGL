# Contents
1. #### Vid1a
    - Draw a window
2. #### Vid1b
    - Introduce looking for key presses
3. #### Vid2a
    - Draw a tiangle using depricated methods
4. #### Vid3a
    - Draw a triangle using modern OpenGl
    - Vertices and colours kept seperate
    - Colour not used
5. #### Vid3b
    - Colour list is now joined to end of vertices list
    - color attribute added to shader
    - Different colours shown
6. #### Vid3c
    - Now a vertex consists of position and colour
7. #### Vid4a
    - Using layout location to refer to attributes
    - GL_TRIANGLE_STRIP used for triangles
8. #### Vid4b
    - Can now change the size of the window
9. #### Vid5a
    - Indices introduced.  This allows the reusing of vertices
    - Now need to use element buffer object
10. #### Vid6a
    - Draw a cube
    - Rotation using pyrr
11. #### Vid7a
    - Texture added
12. #### Vid7b
    - Code simplified by placing blocks of repeated code in outside file.
13. #### Vid9a
   - Projection and translation introduced
14. #### Vid10a
    - How to have more than 1 object
15. #### Vid13a
    - How to have more than 1 kind of object
16. #### Vid13c
    - Ground grid introduced
    - translation moved into while loop to give animation
17. #### Vid13d
    - Cube movement acted on by keys

## AT_vid3a.py
### Lines 6-15
The vertex_src code needs t be told what code is coming in and what code is going out.  here we are told that it will be a vector of 2 elements and it is to be named a_position.  Within in the main function we call the gl_Position function that will tell the shader to generate the screen position that corresponds to the coordinate values we have passed.  In our code the 0.0 in the 4 element vector is set because we are making all 'z' values 0.0.
### Lines 17-26
These are similar to the vertex shader but here all we are doing is defining all the vertices as red.  The vec4 is a set of values which represent rgba.
### Lines 29-44
These create a glfw window and make it the current context (the area where the graphics are created).
### Lines 46-52
These are the values that we will based to the buffer and from there to the shader.
### Lines 54-55
Change the values into a format that can be used.
### Line 58
Make the shader program.  This is done by first compiling each of the sorce codes above into the correct kind and then joining them.  We can pass as many sorces as required, but we have only two.
### Lines 61-65
Here we set up the buffer.
1. (Line 61) Generate the buffers, we are only creating one.
2. (Line 63) Bind the VBO to the type of buffer it is to be.
3. (Line 65) Load the data into the buffer.
   * Buffer type
   * Total size of data
   * The numpy modified data
   * How the buffer changes
### Lines 67-69
1. Get the position location from the shader, we basically give its variable name.
2. We then say this is a vertex array.
3. We get the actual data.
### Line 72
Here we tell the program which shader to use.
### Line 86
Draw the given arrays in the way described in the attributes.  The 3 tells the program that we will be passing a total of 3 vertices.
## AT_vid3b.py
### Line 10
We now take in extra information, in this case color
### Line 12
We are going to export v_color.  The 'v' indicates this variable is being passed.
### Line 29
We are going to use the a_color that was giving the name v_color rather than just red that was hard coded before
### Lines 51-56
We have joined the color information to the vertex information we had before.  The amount of information for each point is up to us.
### Lines 76-78
This makes the color information accessible to the shader program. _Line 78_ says not to include the first 36 bytes.
## AT_vid3c.py
### Lines 51-53
We now have the position and colour on the same line.  The first 12 bytes of each line are position and the next 12 are colour.
### Lines 70 & 75 
Now have been change to take in 24 bytes at a time and the colours start after 12 of those bytes
## AT_vid4a.py
### Lines 9-10
Here we have added layout location, this means that we will not need glGetAttribLocation later.
### Lines 69-74
These lines now use the location of the data
### Line 91
We now use GL_TRIANGLE_STRIP 1st triangle with 3 vertices starting at index 0, next triangle starting at index 1 and so on.
## AT_vid4b.py
### Lines 32-33
We create a function that we will access via a callback.  The function sets the size of the viewport
### Line 50
Here we use the glfw to call the previous function whenever the user attempts to change the size of the window.  The user was always able to change the size of the window, but before the viewport did not change with it.
## AT_vid9a.py
### vertex_src
Two uniforms, one for the transformation which consists of a translation and a rotation and one for the projection onto the world space.
The gl_position is formed by matrix multiplication on the vector.
### vertices Line 62...
Since we are only using texture we have removed the colour values.
### Line 143 
We create a projection matrix effectively makes the world view.
### Line 144
We create the transformation that acts on the cube.
### Lines 146-147
We just get the location of the uniforms within the vertex shader.
### Lines 149 and 163
These are the lines that assign the matrix transformations with vaiables in the shader program