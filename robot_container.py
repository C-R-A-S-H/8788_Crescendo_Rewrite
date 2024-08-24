import commands2
import wpilib
import wpimath

from constants import OIConstants
from subsystems.swerb.drivetrain import DriveSubsystem


class RobotContainer:
   def __init__(self):
      self.configure_bindings()

      self.robotDrive = DriveSubsystem()
      self.driver = wpilib.PS5Controller(1)

      # Configure default commands
      self.robotDrive.setDefaultCommand(
         # The left stick controls translation of the robot.
         # Turning is controlled by the X axis of the right stick.
         commands2.RunCommand(
            lambda: self.robotDrive.drive(
               -wpimath.applyDeadband(
                  self.driver.getLeftY(), OIConstants.kDriveDeadband
               ),
               -wpimath.applyDeadband(
                  self.driver.getLeftX(), OIConstants.kDriveDeadband
               ),
               -wpimath.applyDeadband(
                  self.driver.getRightX(), OIConstants.kDriveDeadband
               ),
               True,
               True,
            ),
            self.robotDrive,
         )
      )


   def configure_bindings(self):
      pass