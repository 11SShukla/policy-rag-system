chat_history = []


def add_to_memory(user, assistant):

    chat_history.append({
        "user": user,
        "assistant": assistant
    })

    if len(chat_history) > 5:
        chat_history.pop(0)


def get_memory():

    history_text = ""

    for turn in chat_history:
        history_text += f"""
User: {turn['user']}
Assistant: {turn['assistant']}
"""

    return history_text