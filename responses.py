import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'oi':
        return 'Eae, lazarento!'
    
    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`Essa é uma mensagem de ajuda!`'

    return 'Não entendi o que você disse, seu burro!'