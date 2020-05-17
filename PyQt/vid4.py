# Draw a triangle
from OpenGL.GL import *
import array
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import (QGuiApplication, QMatrix4x4, QOpenGLContext,
        QOpenGLShader, QOpenGLShaderProgram, QOpenGLVersionProfile,
        QSurfaceFormat, QWindow)
from Context import OpenGLWindow
import pyrr


class TriangleWindow(OpenGLWindow):
    vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

uniform mat4 rotation;

out vec3 v_color;

void main()
{
    gl_Position = rotation * vec4(a_position, 1.0);
    v_color = a_color;
}
"""

    fragment_src = """
# version 330

in vec3 v_color;
out vec4 out_color;

void main()
{
    out_color = vec4(v_color, 1.0);
}
"""

    def __init__(self):
        super(TriangleWindow, self).__init__()
        self.shader = 0
        self.m_frame = 0
        self.rotation_loc = 0
        

    def initialize(self):
        vertices = [-0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.5, 1.0, 0.5, 0.0,
                    0.5,  0.5, 0.5, 1.0, 0.0, 0.5,
                    -0.5, 0.5, 0.5, 0.5, 1.0, 0.5,
                    -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
                    0.5, -0.5, -0.5, 1.0, 0.5, 0.0,
                    0.5,  0.5, -0.5, 1.0, 0.0, 0.5,
                    -0.5, 0.5, -0.5, 0.5, 1.0, 0.5]

        self.indices = [0, 1, 2, 0, 2, 3,
                    4, 5, 6, 6, 7, 4,
                    4, 5, 1, 1, 0, 4,
                    6, 7, 3, 3, 2, 6,
                    5, 6, 2, 2, 1, 5,
                    7, 4, 0, 0, 3, 7]

        vertices = np.array(vertices, dtype=np.float32)
        self.indices = np.array(self.indices, dtype=np.uint32)
        self.shader = compileProgram(compileShader(TriangleWindow.vertex_src, GL_VERTEX_SHADER), compileShader(TriangleWindow.fragment_src, GL_FRAGMENT_SHADER))
        self.rotation_loc = glGetUniformLocation(self.shader, "rotation")
        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnable(GL_DEPTH_TEST)
        glUseProgram(self.shader)

    def render(self, gl):
        glViewport(0, 0, self.width(), self.height())

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)        
       
        rot_x = pyrr.Matrix44.from_x_rotation(0.001 * self.m_frame)
        rot_y = pyrr.Matrix44.from_y_rotation(0.002 * self.m_frame)
        glUniformMatrix4fv(self.rotation_loc, 1, GL_FALSE, pyrr.matrix44.multiply(rot_x, rot_y))

        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)


        self.m_frame += 1


if __name__ == '__main__':

    import sys

    app = QGuiApplication(sys.argv)

    format = QSurfaceFormat()
    format.setSamples(4)

    window = TriangleWindow()
    window.setFormat(format)
    window.resize(640, 480)
    window.show()

    window.setAnimating(True)

    sys.exit(app.exec_())