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
