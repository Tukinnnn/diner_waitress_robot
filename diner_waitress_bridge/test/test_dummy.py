# test/test_dummy.py

import unittest
from diner_waitress_bridge.parser import parse_message, format_command, is_valid_command

class TestParser(unittest.TestCase):
    def test_parse_message(self):
        msg = "CMD:MOVE_FORWARD;SPD:100"
        parsed = parse_message(msg)
        self.assertEqual(parsed['CMD'], 'MOVE_FORWARD')
        self.assertEqual(parsed['SPD'], '100')

    def test_format_command(self):
        cmd = {'CMD': 'MOVE_FORWARD', 'SPD': 100}
        result = format_command(cmd)
        self.assertIn('CMD:MOVE_FORWARD', result)
        self.assertIn('SPD:100', result)

    def test_valid_command(self):
        cmd = {'CMD': 'STOP'}
        self.assertTrue(is_valid_command(cmd))

if __name__ == '__main__':
    unittest.main()
