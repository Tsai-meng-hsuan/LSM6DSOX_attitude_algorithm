import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# 初始化GLFW并创建一个窗口
def init_window():
    if not glfw.init():
        return None
    window = glfw.create_window(1600, 1200, "Simple OpenGL Cube", None, None)
    if not window:
        glfw.terminate()
        return None
    glfw.make_context_current(window)
    return window

# 设置OpenGL
def setup_opengl():
    glEnable(GL_DEPTH_TEST)  # 启用深度测试
    glClearColor(0.0, 0.0, 0.0, 1.0)  # 设置背景色为黑色

# 绘制立方体
def draw_cube():
    glBegin(GL_QUADS)  # 开始绘制四边形（立方体的一个面）
    
    # 前面（红色）
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)

    # 后面（绿色）
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f(-1.0,  1.0, -1.0)

    # 上面（蓝色）
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0, -1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)

    # 下面（黄色）
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f(-1.0, -1.0,  1.0)

    # 左面（紫色）
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glVertex3f(-1.0,  1.0, -1.0)

    # 右面（青色）
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0,  1.0)
    glVertex3f( 1.0,  1.0,  1.0)
    glVertex3f( 1.0,  1.0, -1.0)

    glEnd()  # 结束绘制

# 主函数
def main():
    window = init_window()
    if not window:
        return
    
    setup_opengl()

    # 进入主循环
    while not glfw.window_should_close(window):
        glfw.poll_events()  # 处理事件
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 清除颜色和深度缓存
        
        glLoadIdentity()  # 载入单位矩阵
        glTranslatef(0.0, 0.0, 0.0)  # 将物体移远一点
        
        # 旋转立方体
        glRotatef(1, 3, 1, 1)  # 旋转物体 1°，绕x、y、z轴旋转
        
        draw_cube()  # 绘制立方体
        
        glfw.swap_buffers(window)  # 交换缓冲区，显示渲染结果
        
    glfw.terminate()  # 退出程序

if __name__ == "__main__":
    main()
