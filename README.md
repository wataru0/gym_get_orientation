# gym_get_orientation
This package is enables OpenAI Gym's MuJoCo to easily get the orientation of the agent's body.

## Install
```sh
pip install git+https://github.com/wataru0/gym_get_orientation
``` 

## How to use
```python
import gym
import gym_get_orientation as go

env = gym.make('Ant-v2')

# body_name is the name of the body for which you want to get the orientation vector.
# The body_name is defined in the agent's xml file.
env = go.GetOrientationEnv(env, body_name='torso')

done = False
env.reset()
while True:
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)

    # You can get the orientation vector by accessing the info['body_orientation'].
    print(info['body_orientation'])
    if done:
        env.reset()
        break
```

The command line after execution.

![スクリーンショット 2021-05-10 19 00 18](https://user-images.githubusercontent.com/44032125/117642257-09231d00-b1c2-11eb-88e2-c25764648eff.png)

info['body_orientation'] contains an ndarray consisting of three elements.
Each of these elements corresponds to x, y, and z.
If you want to detect falls, you should pay attention to the value of z.

## Demo
Visualization of the change in torso's orientation vector.
![out-h](https://user-images.githubusercontent.com/44032125/117641471-25728a00-b1c1-11eb-9ddd-b5f96a64fff1.gif)

This software is released under the MIT License, see LICENSE.txt.