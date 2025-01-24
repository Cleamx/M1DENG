import gymnasium as gym

# Création de l'environnement
env = gym.make('FrozenLake-v1', map_name="4x4", render_mode="human")
print(env.action_space)
print(env.unwrapped.P[3][1])

# Actions possibles :
# 0: GAUCHE
# 1: BAS
# 2: DROITE
# 3: HAUT

# Réinitialisation de l'environnement
observation, info = env.reset()
num_timesteps = 20

for _ in range(num_timesteps):
    # Faire une action aléatoire
    random_action = env.action_space.sample()
    print("Action: ", random_action)
    
    # Effectuer l'action aléatoire
    observation, reward, terminated, truncated, info = env.step(random_action)
    print("Observation: ", observation)
    print("Reward: ", reward)
    print("Terminated: ", terminated)
    print("Truncated: ", truncated)
    print("Probability: ", info)
    print("\n")

    env.render()
    
    # Si l'épisode est terminé (trou ou objectif atteint)
    if terminated or truncated:
        observation, info = env.reset()
        print("Episode terminé")

env.close()