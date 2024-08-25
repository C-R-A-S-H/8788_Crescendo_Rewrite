import phoenix6.hardware
import rev
from wpimath.geometry import Rotation2d
from wpimath.kinematics import SwerveModuleState, SwerveModulePosition

import constants


class SwerveModule:
   def __init__(self,drive_motor_can,turn_motor_can,encoder_can):
      self.drive_can = drive_motor_can
      self.turn_can = turn_motor_can
      self.encoder_can = encoder_can

      self.turn_pid = constants.swivel_pid
      self.drive_pid = constants.drive_pid

      self.drive_motor = rev.CANSparkMax(self.drive_can,rev.CANSparkMax.MotorType.kBrushless)
      self.turn_motor = rev.CANSparkMax(self.turn_can, rev.CANSparkMax.MotorType.kBrushless)

      self.drive_enc = self.drive_motor.getEncoder()

      self.absolute_encoder = phoenix6.hardware.CANcoder(encoder_can,"rio")

   def set(self, desired_state: SwerveModuleState):
      self.state = desired_state
      current_angle = Rotation2d().fromDegrees(self.absolute_encoder.get_position().value_as_double)
      self.state = SwerveModuleState.optimize(self.state, current_angle)

      target_angle = self.state.angle.degrees()

      self.set_drive_velocity(self.state.speed)

   def set_drive_velocity(self,velocity):
      """
      Sigma sigma on the wall who is the skibidiest of them all??????
      :param velocity:
      :return:
      """
      return

   def set_spinny_angle(self,angle):
      return

   def get_position(self) -> SwerveModulePosition:
      return SwerveModulePosition(self.drive_enc.getPosition(), Rotation2d().fromDegrees(self.absolute_encoder.get_position().value_as_double))

   def get(self) -> SwerveModuleState:
      return SwerveModuleState(self.drive_enc.getVelocity(), Rotation2d().fromDegrees(self.absolute_encoder.get_position().value_as_double))
