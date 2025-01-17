# Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the NVIDIA Source Code License [see LICENSE for details].

"""
Slight variant of pick place task.
"""
import numpy as np
from robosuite.environments.manipulation.pick_place import PickPlace

class BinPicking_D0(PickPlace):
    """
    Slightly easier task where we have only one object
    """
    def __init__(self, **kwargs):
        assert "z_rotation" not in kwargs
        super().__init__(
            z_rotation=(0., np.pi / 2.),
            **kwargs,
        )
        self.object_names = ["target"]
        self.object_id = {"target": 0}