import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path = os.path.join(base_dir, "loginuidayat.ui")
        loadUi(ui_path, self)

        self.btnLogin.clicked.connect(self.handle_login)
        self.btnClear.clicked.connect(self.clear_form)

    def handle_login(self):
        username = self.txtUsername.text().strip()
        password = self.txtPassword.text()

        if username == "admin" and password == "123":
            QMessageBox.information(
                self, "Login Sukses", "Selamat datang Admin!"
            )
            self.labelStatus.setText("Login berhasil!")

        else:
            QMessageBox.warning(
                self, "Login Gagal", "Username atau password salah!"
            )
            self.labelStatus.setText("Login gagal!")

    def clear_form(self):
        self.txtUsername.clear()
        self.txtPassword.clear()
        self.labelStatus.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginApp()
    window.show()

    sys.exit(app.exec_())