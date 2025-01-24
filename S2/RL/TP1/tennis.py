import gymnasium as gym
import ale_py
import time 

gym.register_envs(ale_py)

env = gym.make('ALE/Tennis-v5', render_mode="human", obs_type="rgb")
obs, info = env.reset()

episode = 0
total_reward = 0

for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    
    time.sleep(0.02)
    
    if terminated or truncated:
        print(f"Episode {episode} terminé avec score: {total_reward}")
        episode += 1
        total_reward = 0
        obs, info = env.reset()

env.close()