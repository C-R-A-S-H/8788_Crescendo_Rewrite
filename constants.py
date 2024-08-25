#can
from wpimath._controls._controls.controller import PIDController

front_left_drive = 1
front_right_drive = 2
back_left_drive = 3
back_right_drive = 4

front_left_turn = 5
front_right_turn = 6
back_left_turn = 7
back_right_turn = 8

front_left_enc = 9
front_right_enc = 10
back_left_enc = 11
back_right_enc = 12

#pid
swivel_pid = PIDController(0.001,0,0)
drive_pid = PIDController(0.001,0,0)