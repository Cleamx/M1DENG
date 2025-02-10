import numpy as np
import gymnasium as gym

def value_iteration(env, max_iterations=1000, threshold=1e-20, gamma=1):
    """
    1.1 Fonction Value_iteration
    Calcule la fonction de valeur optimale de manière itérative en prenant le maximum sur la fonction Q.
    
    Args:
        env: L'environnement Gym
        max_iterations: Nombre maximum d'itérations (défaut: 1000)
        threshold: Seuil de convergence (défaut: 1e-20)
        gamma: Facteur de réduction (défaut: 1)
    
    Returns:
        value_table: Table des valeurs optimales pour chaque état
    """

    value_table = np.zeros(env.observation_space.n)
    
    for i in range(max_iterations):
        # Sauvegarder l'ancienne table pour vérifier la convergence
        old_value_table = value_table.copy()
        
        for state in range(env.observation_space.n):
            # Calculer les Q-values pour toutes les actions possibles
            q_values = []
            for action in range(env.action_space.n):
                next_states_rewards = env.unwrapped.P[state][action]
                q_value = 0
                
                # Calculer la Q-value selon la formule: Q(s,a) = Σ P^a_ss'[R^a_ss' + γV(s')]
                for prob, next_state, reward, _ in next_states_rewards:
                    q_value += prob * (reward + gamma * old_value_table[next_state])
                q_values.append(q_value)
            
            # Mettre à jour la valeur de l'état avec le maximum des Q-values
            # V*(s) = max_a Q*(s,a)
            value_table[state] = max(q_values)
        
        # Vérifier la convergence
        if np.all(np.abs(value_table - old_value_table) <= threshold):
            break
            
    return value_table

def extract_policy(env, value_table, gamma=1):
    """
    1.2 Extraction de la politique optimale
    Extrait la politique optimale à partir de la fonction de valeur optimale.
    
    Args:
        env: L'environnement Gym
        value_table: Table des valeurs optimales
        gamma: Facteur de réduction (défaut: 1)
    
    Returns:
        policy: La politique optimale pour chaque état
    """

    policy = np.zeros(env.observation_space.n)
    
    # Pour chaque état
    for state in range(env.observation_space.n):
        # Calculer les Q-values pour toutes les actions possibles
        q_values = []
        for action in range(env.action_space.n):
            next_states_rewards = env.unwrapped.P[state][action]
            q_value = 0
            
            # Calculer la Q-value selon la formule donnée
            for prob, next_state, reward, _ in next_states_rewards:
                q_value += prob * (reward + gamma * value_table[next_state])
            q_values.append(q_value)
        
        # Sélectionner l'action avec la Q-value maximale
        # π*(s) = arg max_a Q(s,a)
        policy[state] = np.argmax(q_values)
        
    return policy

def solve_frozen_lake():
    """
    1.3 Résolution du Frozen Lake
    Résout l'environnement Frozen Lake en utilisant Value Iteration.
    
    Returns:
        optimal_policy: La politique optimale trouvée
    """

    env = gym.make('FrozenLake-v1')
    
    # Calculer la fonction de valeur optimale
    optimal_value_function = value_iteration(env)
    
    # Extraire la politique optimale
    optimal_policy = extract_policy(env, optimal_value_function)
    
    return optimal_policy


if __name__ == "__main__":
    optimal_policy = solve_frozen_lake()
    print("Politique optimale trouvée:")
    print(optimal_policy.reshape(4, 4)) 
