import numpy as np
import gymnasium as gym

# Crée un environnement FrozenLake avec une carte 4x4 
env = gym.make('FrozenLake-v1', map_name="4x4", render_mode="human")

print(env.action_space)

# Affiche les probabilités de transition pour l'état 3 et l'action 1
print(env.unwrapped.P[3][1])
optimal_policy = np.array([[0, 3, 3, 3], [0, 0, 0, 0], [3, 1, 0, 0], [0, 2, 1, 0]]).flatten()
observation, info = env.reset()

num_timesteps = 100

def generate_episode_with_policy():
    state, _ = env.reset()
    total_reward = 0
    terminated = False
    truncated = False
    path = [state]  # Pour garder une trace du chemin
    
    number_of_steps = 100
    for t in range(number_of_steps):
        # Au lieu d'une action aléatoire, on utilise notre politique optimale
        action = int(optimal_policy[state])
        
        # Effectuer l'action
        next_state, reward, terminated, truncated, _ = env.step(action)
        total_reward += reward
        
        # Afficher l'état actuel et l'action prise
        print(f"\nÉtape {t + 1}:")
        print(f"État: {state} (position: {state//4},{state%4})")
        print(f"Action: {['GAUCHE', 'BAS', 'DROITE', 'HAUT'][action]}")
        print(f"Récompense: {reward}")
        
        if terminated or truncated:
            if reward == 1:
                print("\nBravo ! L'objectif est atteint ! 🎉")
            else:
                print("\nOups ! Tombé dans un trou ! 💦")
            break
            
        state = next_state
        path.append(state)
    
    return total_reward, path

# Tester la politique plusieurs fois
num_episodes = 5
print("\nTest de la politique optimale:")
for episode in range(num_episodes):
    print(f"\n=== Épisode {episode + 1} ===")
    total_reward, path = generate_episode_with_policy()
    print(f"Récompense totale: {total_reward}")
    print(f"Chemin parcouru: {path}")

# Fermer l'environnement
env.close()