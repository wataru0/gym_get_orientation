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
env = go.GetOrientationEnv(env, body_name='torso')

done = False
env.reset()
while True:
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    print(info['body_orientation'])
    if done:
        env.reset()
        break
```
