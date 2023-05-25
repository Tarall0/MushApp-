import random
import numpy as np



def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'ciao' or p_message == 'salve' or p_message == 'buonasera' or p_message == 'we' or p_message == 'hey':
        greetings = np.array(
            ["'Ciao 👋'", "Ehilà fattone!", "Hai già rollata il tuo joint prima di scrivere?", "Ciao ❤️",
             "01101001 ... Whoops scusate... "
             "Ciao!"])
        random_var = random.randint(0, 4)
        return greetings[random_var]



