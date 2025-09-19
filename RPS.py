import random

# Diese Funktion wählt den Zug des Spielers basierend auf dem letzten Zug (prev_play)
# und der Historie der Züge. Sie soll versuchen, den Gegner vorherzusagen.
def player(prev_play, opponent_history=[]):
    # Wenn es keinen vorherigen Zug gibt, wird ein zufälliger gewählt
    if prev_play:
        opponent_history.append(prev_play)

    # Standardmäßig wird "R" (Rock) gespielt, wenn keine Strategie erkennbar ist
    guess = "R"

    # Wenn die Historie mindestens 3 Züge enthält, versuchen wir Muster zu finden
    if len(opponent_history) > 3:
        # Wir nehmen die letzten drei Züge des Gegners
        last_three = opponent_history[-3:]
        
        # Wir erstellen ein Dictionary, das mögliche Folgen zählt
        possible = [
            opponent_history[i:i+3]
            for i in range(len(opponent_history)-3)
        ]

        # Wir schauen, wie oft die letzten drei Züge schon vorkamen
        occurrences = {}
        for i, seq in enumerate(possible):
            if seq == last_three:
                next_index = i + 3
                if next_index < len(opponent_history):
                    next_move = opponent_history[next_index]
                    occurrences[next_move] = occurrences.get(next_move, 0) + 1

        # Wenn wir Vorkommen gefunden haben, nehmen wir den häufigsten nächsten Zug an
        if occurrences:
            prediction = max(occurrences, key=occurrences.get)
            
            # Wir wählen den Zug, der den vorhergesagten Zug schlägt
            ideal_response = {"R": "P", "P": "S", "S": "R"}
            guess = ideal_response[prediction]

    return guess
