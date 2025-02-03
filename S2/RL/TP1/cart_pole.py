import gymnasium as gym

env = gym.make('CartPole-v1', render_mode="human")

# Affiche les informations sur l'espace d'état
print("\nEspace d'état:")
print(env.observation_space)
print("Valeurs maximales:", env.observation_space.high)
print("Valeurs minimales:", env.observation_space.low)

# Affiche les informations sur l'espace d'actions
print("\nEspace d'actions:")
print(env.action_space)

# Réinitialise l'environnement et obtient l'état initial
initial_state, _ = env.reset() 
print("\nÉtat initial:", initial_state)

# Définit le nombre d'épisodes et de pas de temps par épisode
num_episodes = 100
num_timesteps = 50

print("\nEntraînement de l'agent avec politique aléatoire:")

# Boucle sur chaque épisode
for episode in range(num_episodes):
    # Réinitialise l'environnement pour chaque épisode
    state, _ = env.reset()
    total_reward = 0
    
    # Boucle sur chaque pas de temps dans l'épisode
    for t in range(num_timesteps):
        # Sélectionne une action aléatoire
        action = env.action_space.sample()
        
        # Applique l'action et obtient le nouvel état et la récompense
        state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        
        # Vérifie si l'épisode est terminé ou tronqué
        if terminated or truncated: 
            break
    
    # Affiche le retour total tous les 10 épisodes
    if episode % 10 == 0:
        print(f"Episode: {episode}, Return: {total_reward}")

# Ferme l'environnement
env.close()