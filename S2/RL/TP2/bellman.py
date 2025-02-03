import numpy as np
import gymnasium as gym


def Value_iteration(env, nbr_iteration=1000, nbr_threshold=1e-20, gamma=1):
    value_table = np.zeros(env.observation_space.n)
    
    for i in range(nbr_iteration):
        updated_value_table = np.copy(value_table)
        
        for state in range(env.observation_space.n):
            Q_values = []
            for action in range(env.action_space.n):
                q_value = 0
                for prob, next_state, reward, done in env.unwrapped.P[state][action]:
                    q_value += prob * (reward + gamma * value_table[next_state])
                Q_values.append(q_value)
            updated_value_table[state] = max(Q_values)
        
        if np.max(np.abs(updated_value_table - value_table)) <= nbr_threshold:
            print(f"Convergence achieved after {i+1} iterations.")
            break
        
        value_table = updated_value_table
    
    return value_table


# Extraction de la politique optimale
def extract_policy(env, value_table, gamma=1):
    policy = np.zeros(env.observation_space.n, dtype=int)
    
    for state in range(env.observation_space.n):
        Q_values = np.zeros(env.action_space.n)
        for action in range(env.action_space.n):
            for prob, next_state, reward, done in env.unwrapped.P[state][action]:
                Q_values[action] += prob * (reward + gamma * value_table[next_state])
        policy[state] = np.argmax(Q_values)
    
    return policy



# Crée un environnement FrozenLake avec une carte 4x4
env = gym.make('FrozenLake-v1', is_slippery=False)

# Appel de la fonction Value_iteration
optimal_value_table = Value_iteration(env)

print("Optimal Value Table:")
print(optimal_value_table)

optimal_policy = extract_policy(env, optimal_value_table)

print("Optimal Policy:")
print(optimal_policy)