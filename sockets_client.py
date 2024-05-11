# -*- coding: utf-8 -*-🚀
import matplotlib
matplotlib.use('QtAgg')
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QMenu, QWidget, QDialog
from PySide6.QtCore import QTimer, QThread, Signal, QObject, Qt
from PySide6.QtGui import QImage, QPixmap, QColor, QCursor

from util.Ui_MainWindow import Ui_MainWindow
from util.CustomMessageBox import MessageBox
from util.line_chart import RealTimePlot
from util.UIFunctions import *
from util.rtsp_win import RTSP_Window
from pathlib import Path
from PySide6.QtCore import Slot

import os
import cv2
import sys
import time
import json
import socket
import struct
import threading
import numpy as np
import supervision as sv

camera_detecting = None
rtsp_detecting = None

class RTSPClient(QObject):
    
    video_frame_received = Signal(np.ndarray)
    cap_frame_received = Signal(np.ndarray)
    yolo_fps = Signal(str)
    yolo_status_msg = Signal(str)
    reconnect_signal = Signal(str, int)

    def __init__(self, server_host, server_port):
        super(RTSPClient, self).__init__()
        self.server_host = server_host
        self.server_port = server_port

        self.server_address = (server_host, server_port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)


    def reconnect_to_server(self, host, port):
        # 关闭之前的连接
        self.client_socket.close()

        # 重新连接服务器
        self.server_address = (host, port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)
        # self.yolo_results_receiver = YoloResultsReceiver(self.client_socket)  
        self.reconnect_signal.emit(host, port)

    def send_message(self, message):
        try:
            if isinstance(message, str):
                message = message.encode('utf-8')

            msg_len = struct.pack("I", len(message))
            self.client_socket.sendall(msg_len)  
            self.client_socket.sendall(message)  
        
        except BrokenPipeError:
            print("Error: Server closed the connection.")
            # 在这里执行你希望的处理方式，例如重新连接服务器
            self.reconnect_to_server(self.server_host, self.server_port)

        except Exception as e:
            print(f"Error sending message to host: {e}")

    def close_connection(self):
        try:
            if self.client_socket:
                self.client_socket.close()
        except Exception as e:
            print(f"Error closing connection: {e}")
    
class YoloResultsReceiver(QObject):

    receive_numbers_results = Signal(list, list)
    receive_finished = Signal(str)
    video_frame_received = Signal(np.ndarray)
    cap_frame_received = Signal(np.ndarray)
    progress_updated = Signal(int, int)
    class_num_received = Signal(int)
    yolo_fps = Signal(int)
    model = Signal(str) 

    def __init__(self, server_socket):
        super(YoloResultsReceiver, self).__init__()
        self.server_socket = server_socket
        self.results_thread = threading.Thread(target=self.process_results)
        self.results_thread.start()

    def extract_frame_from_data(self, frame_data):
        frame = None
        frame = cv2.imdecode(np.frombuffer(frame_data, dtype=np.uint8), 1)
        return frame
        
    def receive_yolo_results(self):
        try:
            # 接收结果数据长度和帧数据长度
            model_len, counts_len, results_len, frame_len, yolo_fps_len = struct.unpack('IIIII', self.server_socket.recv(20))

            model_data = b''
            while len(model_data) < model_len:
                model_data += self.server_socket.recv(model_len - len(model_data))

            counts_data = b''
            while len(counts_data) < counts_len:
                counts_data += self.server_socket.recv(counts_len - len(counts_data))

            # 接收结果数据
            results_data = b''
            while len(results_data) < results_len:
                results_data += self.server_socket.recv(results_len - len(results_data))

            # 接收帧数据
            frame_data = b''
            while len(frame_data) < frame_len:
                frame_data += self.server_socket.recv(frame_len - len(frame_data))

            # 接收FPS数据
            fps_data = b''
            while len(fps_data) < yolo_fps_len:
                fps_data += self.server_socket.recv(yolo_fps_len - len(fps_data))

            return results_data, frame_data, fps_data, model_data, counts_data

        except Exception as e:
            print(f"Error receiving frame and results from server: {e}")

    def process_results(self):
        try:
            frams = []
            num_list = []
            natural_num = 0
            while True:
                results_data, frame_data, fps_data, model_data, counts_data = self.receive_yolo_results()
                total_frames = counts_data.decode("utf-8")
                total_frames = int(total_frames)
                model_name = model_data.decode("utf-8")[1:-1]
                json_results_data = results_data.decode('utf-8')
                json_fps_data = fps_data.decode('utf-8')
                yolo_results = json.loads(json_results_data)
                raw_fps_data =json.loads(json_fps_data)
                fps_data = int(raw_fps_data)
                data_rows = yolo_results.split(';')
                i = 0
                print("reserve raw data:", results_data)
                print("reserve fps data", raw_fps_data)
                frame = self.extract_frame_from_data(frame_data)
                if frame is not None:
                    self.video_frame_received.emit(frame)
                    self.cap_frame_received.emit(frame)
                    num_people_list = sum(1 for val in data_rows[i].split(',') if val == '0')
                    class_num = 1 if num_people_list else 0 
                    i += 1
                    natural_num += 1
                    frams = [natural_num]
                    num_list = [num_people_list]
                    print("x-axis:", frams)
                    print("y-axis:", num_list)
                    self.receive_numbers_results.emit(frams, num_list)
                    self.class_num_received.emit(class_num)
                    self.yolo_fps.emit(fps_data)
                    self.model.emit(model_name)
                    self.progress_updated.emit(natural_num, total_frames)  
                    time.sleep(1 / 15)
                if natural_num == total_frames or natural_num == 1:
                    self.receive_finished.emit('接收到服务器的响应')
        except Exception as e:
            print(f"Error receiving yolo_results from server: {e}")

class InferenceThread_Video(QThread):
    
    frame_received = Signal(np.ndarray)
    inference_finished = Signal()

    def __init__(self, file_path, client_socket=None):  
        super(InferenceThread_Video, self).__init__()
        self.file_path = file_path
        self.client_socket = client_socket 
        self.is_running = True

    def run(self):
        cap = cv2.VideoCapture(self.file_path)
        while cap.isOpened() and self.is_running:
            ret, frame = cap.read()
            if not ret:
                break
            # 发送帧到主线程显示
            self.frame_received.emit(frame)
            self.msleep(30)
        cap.release()
        self.inference_finished.emit()
    def stop(self):
        self.is_running = False

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, server_address, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # sudo lsof -i:8888
        # kill -9 port  
        self.server_host = server_address
        self.server_port = 8888
        self.inference_thread = None  
        self.rtsp_client = RTSPClient(self.server_host, self.server_port)  
        # self.rtsp_client = None
        self.yolo_results_receiver = YoloResultsReceiver(self.rtsp_client.client_socket)  

        # 创建实时折线图部件
        self.realtime_plot = RealTimePlot()
        self.yolo_video_predict = InferenceThread_Video(None)
        # 设置延时间隔
        self.delay_interval = 5  
        self.delay_counter = 0
        self.Class_num.setText('--')
        self.Target_num.setText('--')
        self.fps_label.setText('--')
        self.Model_name.setText('--')
        
        # 将实时折线图部件添加到左侧框中
        layout = QVBoxLayout()
        layout.addWidget(self.realtime_plot)
        self.line_chart.setLayout(layout)        

        UIFuncitons.uiDefinitions(self)
        UIFuncitons.shadow_style(self, self.Class_QF, QColor(0, 0, 255).lighter(150))  
        UIFuncitons.shadow_style(self, self.Target_QF, QColor(255, 165, 0).lighter(150))  
        UIFuncitons.shadow_style(self, self.Fps_QF, QColor(0, 0, 255).lighter(150))  
        UIFuncitons.shadow_style(self, self.Model_QF, QColor(0, 255, 127).lighter(150))  

        
        self.stop_button.clicked.connect(self.stop_inference)
        self.src_cam_button.clicked.connect(self.camera_infrence)
        self.src_file_button.clicked.connect(self.open_src_file)
        self.src_rtsp_button.clicked.connect(self.rtsp_seletction)
        self.ToggleBotton.clicked.connect(lambda: UIFuncitons.toggleMenu(self, True)) 
        self.yolo_results_receiver.yolo_fps.connect(self.update_fps)
        self.yolo_results_receiver.model.connect(self.update_model) 
        self.yolo_results_receiver.progress_updated.connect(self.update_progress_bar)
        self.yolo_results_receiver.receive_numbers_results.connect(self.update_with_plot)
        self.yolo_results_receiver.class_num_received.connect(self.update_class_num_slot)    
        self.yolo_results_receiver.receive_numbers_results.connect(self.update_target_number)     
        self.yolo_results_receiver.video_frame_received.connect(self.show_camera_frame)  
        self.rtsp_client.reconnect_signal.connect(self.handle_reconnect_server)
        self.yolo_results_receiver.receive_finished.connect(self.show_status)
               

    def handle_reconnect_server(self, host, port):
        self.server_host = host
        self.server_port = port
        self.yolo_results_receiver = YoloResultsReceiver(self.rtsp_client.client_socket)  
        self.reconnect_signals()

    def reconnect_signals(self):
        # 重新连接信号与槽
        self.src_cam_button.clicked.connect(self.camera_infrence)
        self.yolo_results_receiver.yolo_fps.connect(self.update_fps)
        self.yolo_results_receiver.model.connect(self.update_model)
        self.yolo_results_receiver.receive_finished.connect(self.show_status)
        self.yolo_results_receiver.progress_updated.connect(self.update_progress_bar)  
        self.yolo_results_receiver.video_frame_received.connect(self.show_camera_frame)
        self.yolo_results_receiver.receive_numbers_results.connect(self.update_with_plot)
        self.yolo_results_receiver.class_num_received.connect(self.update_class_num_slot)
        self.yolo_results_receiver.receive_numbers_results.connect(self.update_target_number)
        
    #获取鼠标位置（用于按住标题栏拖动窗口）
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

    #拖动窗口大小时优化调整
    def resizeEvent(self, event):
        UIFuncitons.resize_grips(self)

    # 更新总人数
    def update_target_number(self, frams, num_list):
        if frams and num_list:
            latest_frame = frams[-1]
            latest_target_num = num_list[-1]
            self.Target_num.setText(str(latest_target_num))

    @Slot(int, int)
    def update_progress_bar(self, progress, total_frames):
        # 更新进度条
        if camera_detecting == False and rtsp_detecting == False:
            progress = int((progress / total_frames) * 1000) 
            self.progress_bar.setValue(progress)

    def update_fps(self, raw_fps_data):
        self.fps_label.setText(str(raw_fps_data))

    def update_class_num_slot(self, class_num):
        # 更新UI中的Class_num框
        self.Class_num.setText(str(class_num))
    
    def update_model(self, model_data):
        self.Model_name.setText(model_data)

    # 线程处理操作
    def start_inference_thread(self):
        self.inference_thread = InferenceThread_Video(self.name)
        self.inference_thread.inference_finished.connect(self.handle_inference_finished)  
        self.inference_thread.start()

    def stop_inference_thread(self):
        # 停止推理线程
        if self.inference_thread is not None and self.inference_thread.isRunning():
            self.inference_thread.stop()
            self.inference_thread.wait()  
            self.inference_thread = None  

    def toggle_inference_thread(self):
        # 切换推理线程状态
        if self.inference_thread is None or not self.inference_thread.isRunning():
            self.start_inference_thread()
        else:
            self.stop_inference_thread()

    def handle_inference_finished(self):
        # 接收到推理完成信号时执行的操作，例如停止线程、关闭进程等
        self.stop_inference_thread()

    def show_status(self, msg):
        self.status_bar.setText(msg)
        if msg == '重新连接服务器':
            self.progress_bar.setValue(0)
            self.res_video.clear()          
            self.Class_num.setText('--')
            self.Target_num.setText('--')
            self.fps_label.setText('--')
            self.Model_name.setText('--')

    # UI界面打开文件夹
    def open_src_file(self):
        global camera_detecting
        global rtsp_detecting
        camera_detecting = False
        rtsp_detecting = False
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        self.name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold, "Pic File(*.mp4 *.mkv *.avi *.flv *.jpg *.png)")
        if self.name:
            self.source = self.name
            self.show_status('加载文件：{}'.format(os.path.basename(self.name)))
            config['open_fold'] = os.path.dirname(self.name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            self.rtsp_client.video_frame_received.connect(self.show_camera_frame) 

            # 显示原视频
            if hasattr(self, 'inference_thread') and self.inference_thread is not None:
                self.inference_thread.stop()
                self.inference_thread.wait()
            # 创建新的推理线程并启动它
            inference_thread = InferenceThread_Video(file_path=self.name)
            inference_thread.frame_received.connect(self.show_camera_frame)
            inference_thread.inference_finished.connect(self.handle_inference_finished)
            inference_thread.start()
            # 存储推理线程的引用以确保正确管理
            self.inference_thread = inference_thread

            # 调用新方法将文件路径发送到主机并重新连接            
            self.send_file_path_to_host(self.name)

    def send_file_path_to_host(self, file_path):
        try:
            # 获取当前工作目录
            current_dir = os.getcwd()
            # 将文件路径转换为相对路径
            relative_path = os.path.relpath(file_path, current_dir)
            # 发送相对路径给主机端
            file_path_msg = f"{relative_path}"
            self.rtsp_client.send_message(file_path_msg.encode('utf-8'))
        except Exception as e:
            print(f"Error sending file path to host: {e}")

    # RTSP
    def rtsp_seletction(self):
        global rtsp_detecting
        rtsp_detecting = True
        self.rtsp_window = RTSP_Window()
        config_file = 'config/ip.json'
        if not os.path.exists(config_file):
            ip = "rtsp://gentle:8888@192.168.43.107:8554/live"
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            ip = config['ip']
        self.rtsp_window.rtspEdit.setText(ip)
        self.rtsp_window.show()
        self.rtsp_window.rtspButton.clicked.connect(lambda: self.load_rtsp(self.rtsp_window.rtspEdit.text()))
    
    #加载RTSP
    def load_rtsp(self, ip):
        MessageBox(self.close_button, 
                    title='提示', 
                    text='加载 rtsp...', 
                    time=1000, 
                    auto=True).exec()
        
        new_config = {"ip": ip}
        new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
        with open('config/ip.json', 'w', encoding='utf-8') as f:
            f.write(new_json)
        self.show_status('加载rtsp地址:{}'.format(ip))
        self.rtsp_window.close()
        self.rtsp_client.send_message(ip)

    def camera_infrence(self):
        global camera_detecting
        camera_detecting = True
        self.rtsp_client.cap_frame_received.connect(self.show_camera_frame) 
        # 发送 "stop_video_inference" 给服务器
        start_cap = "stop_video_inference"
        self.rtsp_client.send_message(start_cap.encode('utf-8'))

    @Slot(np.ndarray)
    def show_camera_frame(self, frame):
        self.show_image(frame, self.res_video)

    @Slot(list, list)
    def update_with_plot(self, frams, num_people):
        # 更新实时折线图的数据
        self.realtime_plot.update_plot(frams, num_people)
                
    # 重新连接服务器
    def stop_inference(self):
        self.res_video.clear()
        if self.rtsp_client.client_socket is not None:
            self.show_status("重新连接服务器") 
            self.rtsp_client.reconnect_to_server(self.server_host, self.server_port) 

    @staticmethod
    def show_image(img_src, label):
        try:
            if len(img_src.shape) == 3:
                ih, iw, _ = img_src.shape
            if len(img_src.shape) == 2:
                ih, iw = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))
            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))
            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))
        except Exception as e:
            print(repr(e))           

    def closeEvent(self, event):
        if hasattr(self, 'rtsp_client'):
            del self.rtsp_client
        super().closeEvent(event)

class StartupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Server Address Input")
        self.setWindowModality(Qt.ApplicationModal)

        self.label = QLabel("Enter Server Address:")
        self.server_edit = QLineEdit()
        self.server_edit.setPlaceholderText("Enter server address here")
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.server_edit)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def on_start_clicked(self):
        server_address = self.server_edit.text()
        if server_address:
            self.close()
            main_window = MainWindow(server_address)
            main_window.show()
        else:
            app.quit()
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    startup_window = StartupWindow()
    startup_window.show()
    sys.exit(app.exec())
