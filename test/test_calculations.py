# test/test_calculations.py
import sys
import os

# Agregar el directorio raíz al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

 # Importación desde main.py
from main import add, subtract

class TestCalculations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
