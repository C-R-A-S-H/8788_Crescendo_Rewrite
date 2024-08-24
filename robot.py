

import commands2
import wpilib

from robot_container import RobotContainer


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        # Instantiate our RobotContainer.  This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.container = RobotContainer()
        self.autonomousCommand = None


    def teleopInit(self) -> None:
        pass

    def testInit(self) -> None:
        commands2.CommandScheduler.getInstance().cancelAll()


if __name__ == "__main__":
    wpilib.run(MyRobot)