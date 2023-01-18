from ui_login import Ui_Widget as login_form
from ui_chat import Ui_Widget as chat_form
from PyQt5 import QtWidgets as qtw
import socket
import threading
from datetime import datetime
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class LoginWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = login_form()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)

    def login(self):
        self.username = self.ui.textEdit.toPlainText()
        self.hide()
        self.widget = ChatWidget(self.username)
        self.widget.show()
        self.connect()

    def connect(self):
        client.connect(('127.0.0.1',9999))
        msg = client.recv(1024).decode('utf-8')
        if(msg=="USERNAME"):
            client.send(self.username.encode('utf-8'))
            # Luodaan uusi thread
            thread = threading.Thread(target=self.widget.receive)
            # Käynnistetään thread
            thread.start()
  
class ChatWidget(qtw.QWidget):
    def __init__(self,username):
        super().__init__()
        self.ui = chat_form()
        self.ui.setupUi(self)
        self.ui.send_button.clicked.connect(self.send_message)
        self.username = username

        self.get_messages()

    def get_messages(self):
        try:
            with open('messages.json') as file:
                contents = json.load(file)
                for i in range(len(contents)):
                    time = contents[i]['time']
                    sender = contents[i]['name']
                    message = contents[i]['message']
                    msg = f"{time}---{sender}:{message}"
                    self.ui.listWidget.addItem(msg)

        except FileNotFoundError as e:
            print("File not found.")
            print(e)

    def receive(self):
        stopped = False
        while not stopped:
            msg = client.recv(1024).decode('utf-8')
            self.ui.listWidget.addItem(msg)

    def send_message(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        plainMessage = self.ui.textEdit.toPlainText()
        message = current_time+"---"+self.username+":"+plainMessage

        client.send(message.encode('utf-8'))
        self.ui.textEdit.setPlainText('')

        message = {"Time":current_time, "Name":self.username, "Message":plainMessage}
        try:
            with open('messages.json') as file:
                file_data = []
                file_data = json.load(file)
                file_data.append(message)
            with open ('messages.json', 'w') as file:
                json.dump(file_data, file, indent=4)

        except FileNotFoundError as fe:
            print("File not found.")
            print(fe)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = LoginWidget()
    widget.show()
    app.exec_()