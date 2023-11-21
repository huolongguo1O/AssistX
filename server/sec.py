def check(history):
    for data in history[1:]:
        if data['role'] == 'system':
            return False
    return True