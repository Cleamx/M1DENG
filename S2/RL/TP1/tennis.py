import gymnasium as gym
from gymnasium.wrappers import RecordEpisodeStatistics, RecordVideo
import ale_py

# Enregistre les environnements ALE
gym.register_envs(ale_py)

# Définition du nombre d'épisodes et du nombre de pas de temps par épisode
num_episodes  = 100

# Création de l'environnement de jeu Tennis 
env = gym.make('ALE/Tennis-v5', render_mode="rgb_array", obs_type="rgb")

# Enregistrement des vidéos des épisodes dans le dossier "./recordings" avec le préfixe "eval"
env = RecordVideo(env, video_folder="./recordings", name_prefix="eval", episode_trigger=lambda x: True)

# Enregistrement des statistiques des épisodes avec une longueur de buffer égale au nombre d'épisodes
env = RecordEpisodeStatistics(env, buffer_length=num_episodes)

# Boucle sur le nombre d'épisodes
for episode_num in range(num_episodes):
    # Réinitialisation de l'environnement pour un nouvel épisode
    obs, info = env.reset()

    episode_over = False
    # Boucle jusqu'à la fin de l'épisode
    while not episode_over:
        # Sélection d'une action aléatoire dans l'espace d'actions de l'environnement
        action = env.action_space.sample()
        # Exécution de l'action et récupération des résultats
        obs, reward, terminated, truncated, info = env.step(action)
        episode_over = terminated or truncated

# Fermeture de l'environnement
env.close()

# Affichage des statistiques des épisodes
print(f'Temps pris par épisode: {env.time_queue}')
print(f'Récompenses totales par épisode: {env.return_queue}')
print(f'Longueurs des épisodes: {env.length_queue}')