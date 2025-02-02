import gymnasium as gym

env = gym.make('CartPole-v1', render_mode="human")

print("\nEspace d'état:")
print(env.observation_space)
print("Valeurs maximales:", env.observation_space.high)
print("Valeurs minimales:", env.observation_space.low)


print("\nEspace d'actions:")
print(env.action_space)

initial_state, _ = env.reset() 
print("\nÉtat initial:", initial_state)

num_episodes = 100
num_timesteps = 50

print("\nEntraînement de l'agent avec politique aléatoire:")

for episode in range(num_episodes):
    state, _ = env.reset()
    total_reward = 0
    
    for t in range(num_timesteps):
        action = env.action_space.sample()
        
        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        
        if terminated or truncated: 
            break
    
    if episode % 10 == 0:
        print(f"Episode: {episode}, Return: {total_reward}")

env.close()