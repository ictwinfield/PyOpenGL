# AT_vid3a.py
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
# AT_vid3b.py
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
