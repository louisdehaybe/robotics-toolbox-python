#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ERobot import ERobot


class irb120(ERobot):
    """
    Class that imports a irb120 URDF model

    ``irb120()`` is a class which imports a abb irb120 robot
    definition from a URDF file.  The model describes its kinematic and
    graphical characteristics.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.irb120()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration

    .. codeauthor:: Jesse Haviland
    .. sectionauthor:: Peter Corke
    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "abb_irb120_support/urdf/irb120.urdf"
        )

        super().__init__(
            links,
            name=name.upper(),
            manufacturer="ABB",
            # gripper_links=links[7],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        self.addconfiguration("home", np.array([0, 0, 0, 0, 0, 0]))


if __name__ == "__main__":  # pragma nocover

    robot = irb120()
    print(robot)
    print(robot.ets())
