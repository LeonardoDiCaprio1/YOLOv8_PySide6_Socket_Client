# -*- coding: utf-8 -*-🚀
import matplotlib
matplotlib.use('QtAgg')
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class RealTimePlot(QWidget):
    def __init__(self, parent=None):
        super(RealTimePlot, self).__init__(parent)
        self.figure = Figure(facecolor='none')
        self.canvas = FigureCanvas(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.ax = self.figure.add_subplot(111)
        self.line, = self.ax.plot([], [], 'b-', label='Number')
        self.ax.set_xlim(0, 50)  # 设置 x 轴范围
        self.ax.set_ylim(0, 50)  # 设置 y 轴范围
        self.xdata = []
        self.ydata = []
        self.current_x = 0
        # 设置绘图区域透明
        self.ax.set_facecolor('none')
        # 设置坐标轴可见性
        self.ax.spines['top'].set_visible(True)
        self.ax.spines['right'].set_visible(True)
        self.ax.spines['bottom'].set_visible(True)
        self.ax.spines['left'].set_visible(True)
        # 添加标题和标签
        self.ax.set_title('relationship between people and frames')
        self.ax.set_xlabel('frame')
        self.ax.set_ylabel('Number')
        # 添加网格线
        self.ax.grid(True)
        self.ax.legend()

    def update_plot(self, x, y):
        # 将 x 轴的当前值递增
        self.current_x += 1
        self.ydata.append(y)
        self.line.set_ydata(self.ydata)
        # 计时一天后数据清零
        if self.current_x >= 2160000:
            self.current_x = 0
            self.ydata = []
        self.line.set_xdata(list(range(1, self.current_x + 1)))
        # 设置 x 轴的范围，从当前值开始，一直到当前值减去 50
        self.ax.set_xlim(max(1, self.current_x - 50), max(50, self.current_x))
        self.canvas.draw()
        
    # def resize_plot(self, event):
    #     # 获取窗口大小
    #     width = self.layout.geometry().width()
    #     height = self.layout.geometry().height()

    #     # 调整折线图的大小
    #     self.figure.set_size_inches(width / self.figure.get_dpi(), height / self.figure.get_dpi())
    #     self.canvas.draw()
        
    # def update_plot(self, x, y):
    #     # 将 x 轴的当前值递增
    #     self.current_x += 1
    #     self.ydata.append(y)
    #     self.line.set_ydata(self.ydata)

    #     self.line.set_xdata(list(range(1, self.current_x + 1)))
    #     # 设置 x 轴的范围，从当前值开始，一直到当前值减去 50
    #     self.ax.set_xlim(max(1, self.current_x - 50), max(50, self.current_x))

    #     self.canvas.draw()
