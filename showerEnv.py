from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
from typing import Any


class ShowerEnv(Env):
    def __init__(self) -> None:
        super().__init__()
        self.action_space = Discrete(3)
        self.observation_space = Box(
            low=np.array([0], dtype=np.float32), high=np.array([100], dtype=np.float32)
        )
        self.state = 38 + random.randint(-3, 3)
        self.shower_length = 60

    def step(self, action: int) -> tuple:
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0 
        # 2 -1 = 1 temperature 
        self.state += action - 1

        # Reduce shower length by 1
        self.shower_length -= 1

        # Calculate reward
        if 37 <= self.state <= 39:
            reward = 1
        else:
            reward = -1

        # Check if shower is done
        done = self.shower_length <= 0

        # Set Placeholder for Info
        info = {Any: Any}

        return self.state, reward, done, info

    def reset(self) -> int:
        self.shower_length = 60
        self.state = 38 + random.randint(-3, 3)
        return self.state

    def render(self) -> None:
        pass
