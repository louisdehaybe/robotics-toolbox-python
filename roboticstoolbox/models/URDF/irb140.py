#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.ERobot import ERobot


class irb140(ERobot):
    """
    Class that imports a irb120 URDF model

    ``irb120()`` is a class which imports a irb120 robot
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
        	"abb_irb140/urdf/irb140.urdf"
        )

        super().__init__(
            links,
            name=name.upper(),
            manufacturer="ABB",
            # gripper_links=links[7],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )

        # self.addconfiguration("qz", np.array([0, 0, 0, 0, 0, 0]))
        # self.addconfiguration("qr", np.array([np.pi, 0, 0, 0, np.pi / 2, 0]))

        # sol=robot.ikine_LM(SE3(0.5, -0.2, 0.2)@SE3.OA([1,0,0],[0,0,-1]))
        # self.addconfiguration(
        #     "qn",
        #     np.array(
        #         [
        #             -7.052413e-01,
        #             3.604328e-01,
        #             -1.494176e00,
        #             1.133744e00,
        #             -7.052413e-01,
        #             0,
        #         ]
        #     ),
        # )


if __name__ == "__main__":  # pragma nocover

    robot = irb120()
    print(robot)
    print(robot.ets())
