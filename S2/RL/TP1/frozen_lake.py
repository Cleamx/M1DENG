import gymnasium as gym

# Crée un environnement FrozenLake avec une carte 4x4 
env = gym.make('FrozenLake-v1', map_name="4x4", render_mode="human")

print(env.action_space)

# Affiche les probabilités de transition pour l'état 3 et l'action 1
print(env.unwrapped.P[3][1])
observation, info = env.reset()

num_timesteps = 20

# Boucle pour exécuter des actions aléatoires dans l'environnement
for _ in range(num_timesteps):
    # Sélectionne une action aléatoire
    random_action = env.action_space.sample()
    print("Action: ", random_action)
    
    # Exécute l'action et obtient les résultats
    observation, reward, terminated, truncated, info = env.step(random_action)
    print("Observation: ", observation)
    print("Reward: ", reward)
    print("Terminated: ", terminated)
    print("Truncated: ", truncated)
    print("Probability: ", info)
    print("\n")

    # Affiche l'état actuel de l'environnement
    env.render()

    # Si l'épisode est terminé ou tronqué, réinitialise l'environnement
    if terminated or truncated:
        observation, info = env.reset()
        print("Episode terminé")

env.close()