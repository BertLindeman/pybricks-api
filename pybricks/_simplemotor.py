"""Shortened and simplified motor docs, by hiding optional methods and args."""

from .builtins import Motor
from .parameters import Direction, Stop


class Motor(Motor):
    """Generic class to control motors with built-in rotation sensors."""

    def __init__(self, port, positive_direction=Direction.CLOCKWISE):
        """Motor(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port):
                Port to which the motor is connected.
            positive_direction (Direction): Which direction the motor should
                turn when you give a positive speed value or
                angle (*Default*: ``Direction.CLOCKWISE``).
        """
        pass

    def angle(self):
        """Get the rotation angle of the motor.

        Returns:
            :ref:`angle`: Motor angle.

        """
        pass

    def reset_angle(self, angle):
        """Reset the accumulated rotation angle of the motor.

        Arguments:
            angle (:ref:`angle`): Value to which the angle should be reset.
        """
        pass

    def speed(self):
        """Get the speed of the motor.

        Returns:
            :ref:`speed`: Motor speed.

        """
        pass

    def stop(self, stop_type=Stop.COAST):
        """stop()

        Stop the motor.
        """
        pass

    def run(self, speed):
        """Keep the motor running at a constant speed.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
        """
        pass

    def run_time(self, speed, time, stop_type=Stop.COAST, wait=True):
        """run_time(speed, time)

        Run the motor at a constant speed for a given amount of time.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            time (:ref:`time`): Duration of the maneuver.
        """
        pass

    def run_angle(self, speed, rotation_angle,
                  stop_type=Stop.COAST, wait=True):
        """run_angle(speed, rotation_angle)

        Rotate the motor at a constant speed by a given angle.

        Arguments:
            speed (:ref:`speed`): Speed of the motor.
            rotation_angle (:ref:`angle`): Angle by which the motor should
                                           rotate.
        """
        pass

    def run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True):
        """run_target(speed, target_angle)

        Run the motor at a constant speed towards a given target angle. The
        direction of rotation is automatically selected based on the target
        angle.

        Arguments:
            speed (:ref:`speed`): Absolute speed of the motor. The direction
                                  will be automatically selected based on the
                                  target angle: it makes no difference if you
                                  specify a positive or negative speed.
            target_angle (:ref:`angle`): Target angle that the motor should
                                         rotate to, regardless of its current
                                         angle.
        """
        pass