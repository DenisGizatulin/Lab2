from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class Menu(QWidget): # Код для меню
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Меню - Змейка")
        self.setGeometry(800, 380, 300, 200)

        self.layout = QVBoxLayout()

        # Заголовок игры
        self.title_label = QLabel("Змейка", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        # Максимальный результат
        self.max_score = self.load_max_score()
        self.score_label = QLabel(f"Максимальный результат: {self.max_score}", self)
        self.layout.addWidget(self.score_label)

        # Кнопка "Запустить игру"
        self.start_button = QPushButton("Запустить игру", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        # Кнопка "Выход"
        self.exit_button = QPushButton("Выход", self)
        self.exit_button.clicked.connect(self.exit_game)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)

