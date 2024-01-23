import json

with open('result.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

text = ''
for message in data['messages']:
    if 'text' in message:
        if isinstance(message['text'], str):
            text += f'{message["text"]}\n'
        elif isinstance(message['text'], list):
            for msg in message['text']:
                if isinstance(msg, str):
                    text += f'{msg}\n'

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(text)