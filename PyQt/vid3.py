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


class TriangleWindow(OpenGLWindow):
    vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_color;

out vec3 v_color;

void main()
{
    gl_Position = vec4(a_position, 1.0);
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

    def initialize(self):
        self.shader = compileProgram(compileShader(TriangleWindow.vertex_src, GL_VERTEX_SHADER), compileShader(TriangleWindow.fragment_src, GL_FRAGMENT_SHADER))

    def render(self, gl):
        glViewport(0, 0, self.width(), self.height())

        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.shader)
                
        vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.0, 1.0, 0.5, 0.0,
                    -0.5,  0.5, 0.0, 1.0, 0.0, 0.5,
                    0.5, 0.5, 0.0, 0.5, 1.0, 0.5]
        indices = [0, 1, 2,
                    1, 2, 3]
        vertices = np.array(vertices, dtype=np.float32)
        indices = np.array(indices, dtype=np.uint32)

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)


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