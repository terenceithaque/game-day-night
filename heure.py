# Metttre à jour le temps en temps réel
import time


def update_time(queue):
    "Mettre à jour l'heure du jeu"
    global heures
    heures = 0  # Heure actuelle dans le jeu

    while heures < 24:
        print("Heures :", heures)
        temps = time.time()
        time.sleep(1)
        temps += 1.0
        print(temps)
        delai = time.time() - temps
        print("Délai :", delai)

        if delai <= 5.0:
            heures += 1
            # print("Heures :", heures)
            temps = 0.0

        if heures == 24:
            print("Il est minuit ! Une nouvelle journée commence.")
            heures = 0

            continue

    queue.put(heures)
