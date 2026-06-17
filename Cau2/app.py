import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow  # Khớp với file ui/caesar.py trong thư mục của Phú
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        
        payload = {
            "message": self.ui.txtInput.toPlainText(),
            "key": self.ui.spinKey.value()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                
                self.ui.txtOutput.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: Status code", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error: Connection failed")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        
        payload = {
            "ciphertext": self.ui.txtInput.toPlainText(),
            "key": self.ui.spinKey.value()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                
                # 5. Trả kết quả văn bản gốc hiển thị về ô txtOutput
                self.ui.txtOutput.setText(data["decrypted_message"])

                # Hiển thị thông báo thành công
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: Status code", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error: Connection failed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())