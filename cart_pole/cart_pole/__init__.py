from gym.envs.registration import register

register(
    id='custom-cart-pole-v0',
    entry_point='cart_pole.envs:CartPoleEnv',
)