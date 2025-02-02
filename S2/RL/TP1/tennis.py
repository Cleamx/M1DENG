import gymnasium as gym
from gymnasium.wrappers import RecordEpisodeStatistics, RecordVideo
import ale_py

gym.register_envs(ale_py)

num_episodes  = 100
num_timesteps = 50

env = gym.make('ALE/Tennis-v5', render_mode="rgb_array", obs_type="rgb")

env = RecordVideo(env, video_folder="./recordings", name_prefix="eval", episode_trigger=lambda x: True)
env = RecordEpisodeStatistics(env, buffer_length=num_episodes)

for episode_num in range(num_episodes):
    obs, info = env.reset()

    episode_over = False
    while not episode_over:
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)

        episode_over = terminated or truncated

env.close()

print(f'Episode time taken: {env.time_queue}')
print(f'Episode total rewards: {env.return_queue}')
print(f'Episode lengths: {env.length_queue}')