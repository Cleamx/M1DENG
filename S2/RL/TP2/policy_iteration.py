import numpy as np
import gymnasium as gym

def compute_value_function(env, policy, num_iterations=1000, threshold=1e-20, gamma=1):
    """
    Calculer la fonction de valeur pour une politique donnée.
    Cette fonction diffère de la Value Iteration car elle utilise la politique donnée
    au lieu de rechercher les Q-valeurs maximales.
    """
    # Initialiser la table de valeurs à zéro
    value_table = np.zeros(env.observation_space.n)
    
    # Boucle principale
    for i in range(num_iterations):
        old_value_table = value_table.copy()
        
        # Pour chaque état
        for state in range(env.observation_space.n):
            # Utiliser l'action donnée par la politique au lieu de rechercher le maximum
            action = policy[state]
            next_states_rewards = env.unwrapped.P[state][action]
            
            # Calculer la valeur en utilisant la formule V^π(s) = Σ P^a_ss'[R^a_ss' + γV^π(s')]
            value_table[state] = sum(
                prob * (reward + gamma * old_value_table[next_state])
                for prob, next_state, reward, _ in next_states_rewards
            )
        
        # Vérifier la convergence
        if np.all(np.abs(value_table - old_value_table) <= threshold):
            break
            
    return value_table

def extract_policy(env, value_table, gamma=1):
    """
    Extraire la politique à partir de la fonction de valeur.
    Cette fonction est identique à celle de la partie 1.2
    """
    policy = np.zeros(env.observation_space.n)
    
    for state in range(env.observation_space.n):
        q_values = []
        for action in range(env.action_space.n):
            next_states_rewards = env.unwrapped.P[state][action]
            q_value = sum(
                prob * (reward + gamma * value_table[next_state])
                for prob, next_state, reward, _ in next_states_rewards
            )
            q_values.append(q_value)
            
        policy[state] = np.argmax(q_values)
        
    return policy

def policy_iteration(env):
    """
    Intégration des deux étapes précédentes.
    Cette partie est nouvelle par rapport à la Value Iteration.
    """
    # Initialisation avec une politique aléatoire
    policy = np.zeros(env.observation_space.n)
    max_iterations = 1000
    
    for i in range(max_iterations):
        # Mémoriser l'ancienne politique pour vérifier la convergence
        old_policy = policy.copy()

        value_function = compute_value_function(env, policy)
        policy = extract_policy(env, value_function)

        # Vérifier si la politique a convergé
        if np.all(policy == old_policy):
            print(f"Politique convergée après {i+1} itérations")
            break
            
    return policy

# Test sur l'environnement Frozen Lake
def solve_frozen_lake_policy_iteration():
    env = gym.make('FrozenLake-v1')
    optimal_policy = policy_iteration(env)
    print("\nPolitique optimale trouvée (Policy Iteration):")
    print(optimal_policy.reshape(4, 4))
    return optimal_policy

if __name__ == "__main__":
    solve_frozen_lake_policy_iteration()