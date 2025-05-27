# diner_waitress_bridge/parser.py

"""
Parser pesan string ke dictionary dan sebaliknya untuk komunikasi UART.
"""

def parse_message(message: str) -> dict:
    """
    Ubah string seperti "CMD:MOVE_FORWARD;SPD:100" menjadi dict.
    Output: {'CMD': 'MOVE_FORWARD', 'SPD': '100'}
    """
    data = {}
    try:
        for pair in message.strip().split(';'):
            if ':' in pair:
                key, val = pair.split(':', 1)
                data[key.strip()] = val.strip()
    except Exception as e:
        print(f"[Parser] Error parsing message: {e}")
    return data

def format_command(command: dict) -> str:
    """
    Ubah dict menjadi string format command.
    Input: {'CMD': 'MOVE_FORWARD', 'SPD': 100}
    Output: "CMD:MOVE_FORWARD;SPD:100"
    """
    try:
        return ';'.join(f"{k}:{v}" for k, v in command.items())
    except Exception as e:
        print(f"[Formatter] Error formatting command: {e}")
        return ""

def is_valid_command(data: dict, required_keys: list = ["CMD"]) -> bool:
    return all(k in data for k in required_keys)
