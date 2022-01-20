from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


KV = """
FloatLayout:
    BoxLayout:
        id: chess_board
        orientation: "vertical"
"""
# Создание игровой доски, где "." - белая клетка, "*" - черная клетка.
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Словарь с фигурами и их положением на доске
figures = {'ph1': ['2a', '7a'], 'ph2': ['2b', '7b'], 'ph3': ['2c', '7c'], 'ph4': ['2d', '7d'], 'ph5': ['2e', '7e'],
           'ph6': ['2f', '7f'], 'ph7': ['2g', '7g'], 'ph8': ['2h', '7h'], 'K': ['1d', '8d'], 'Q': ['1e', '8e'],
           'RL': ['1a', '8a'], 'RR': ['1h', '8h'], 'HL': ['1b', '8b'], 'HR': ['1g', '8g'], 'EL': ['1c', '8c'],
           'ER': ['1f', '8f']}
log_game = []
game = True
print('Начнем игру!')

