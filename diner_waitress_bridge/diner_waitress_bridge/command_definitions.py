# diner_waitress_bridge/command_definitions.py

"""
Definisi command dan response standar untuk komunikasi antara Jetson dan Arduino.
"""

# === Komando standar ke Arduino ===
COMMANDS = {
    'MOVE_FORWARD': 'MOVE_FORWARD',
    'MOVE_BACKWARD': 'MOVE_BACKWARD',
    'TURN_LEFT': 'TURN_LEFT',
    'TURN_RIGHT': 'TURN_RIGHT',
    'STOP': 'STOP',
    'BEEP': 'BEEP',
    'LED_ON': 'LED_ON',
    'LED_OFF': 'LED_OFF',
    'STATUS': 'STATUS'
}

# === Respon standar dari Arduino ===
RESPONSES = {
    'ACK': 'ACK',
    'OK': 'OK',
    'ERR': 'ERR',
    'DONE': 'DONE',
    'BUSY': 'BUSY'
}

def make_command(cmd: str, **kwargs) -> str:
    """
    Format command dengan argumen tambahan.
    Example: make_command("MOVE_FORWARD", SPD=100)
    Output: "CMD:MOVE_FORWARD;SPD:100"
    """
    base = f"CMD:{cmd}"
    for k, v in kwargs.items():
        base += f";{k}:{v}"
    return base

def is_acknowledged(response_dict: dict) -> bool:
    return response_dict.get('ACK', '') != ''

def is_error(response_dict: dict) -> bool:
    return response_dict.get('RESP', '') == 'ERR'
