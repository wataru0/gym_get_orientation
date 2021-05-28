import os
import numpy as np

import gym
from gym import wrappers
from gym import utils
from gym.envs.mujoco import mujoco_env
import mujoco_py

class GetOrientationEnv(gym.Wrapper):
    def __init__(self, env, body_name: str = 'torso'):
        super().__init__(env)
        self.world_quat = np.array([1.0, 0.0, 0.0, 0.0])
        self.base_vec = np.array([0.0, 0.0, 1.0])
        self.body_name = body_name

    def reset(self, **kwargs):
        return self.env.reset(**kwargs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        body_orientation = self._get_body_orientation(body_name=self.body_name)
        info['body_orientation'] = body_orientation
        return obs, reward, done, info
    
    def _get_body_orientation(self, body_name: str):
        now_quat = self.data.get_body_xquat(body_name)

        res = np.zeros(4)
        mujoco_py.functions.mju_mulQuat(res, self.world_quat, now_quat)
        if res[0] < 0:
            res = res * -1

        world_vec = np.zeros(3)
        mujoco_py.functions.mju_rotVecQuat(world_vec, self.base_vec, now_quat)
        
        self.world_quat = res
        return world_vec