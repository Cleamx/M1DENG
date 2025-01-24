import gymnasium as gym

# Création de l'environnement CartPole
env = gym.make('CartPole-v1', render_mode="human")

# Afficher l'espace d'état
print("\nEspace d'état:")
print(env.observation_space)
print("Valeurs maximales:", env.observation_space.high)
print("Valeurs minimales:", env.observation_space.low)

# Afficher l'espace d'actions
print("\nEspace d'actions:")
print(env.action_space)

# Réinitialiser l'environnement et afficher l'état initial
initial_state, _ = env.reset()  # La nouvelle version retourne (state, info)
print("\nÉtat initial:", initial_state)

# 3.2 Équilibrage avec politique aléatoire
num_episodes = 100
num_timesteps = 50

print("\nEntraînement de l'agent avec politique aléatoire:")

for episode in range(num_episodes):
    state, _ = env.reset()
    total_reward = 0
    
    for t in range(num_timesteps):
        # Sélectionner une action aléatoire
        action = env.action_space.sample()
        
        # Effectuer l'action aléatoire
        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        
        if terminated or truncated: 
            break
    
    if episode % 10 == 0:
        print(f"Episode: {episode}, Return: {total_reward}")

env.close()