from __future__ import annotations

import requests

HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'


async def oobabooga(prompt):
    request = {
        'prompt': f'<|user|>\n<|user-message|>\n{prompt}\n\n'
                  f'<|bot|>\n<|bot-message|>\n',
        'max_new_tokens': 250,
        'do_sample': True,
        'temperature': 1.3,
        'top_p': 0.1,
        'typical_p': 1,
        'repetition_penalty': 1.18,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': [],
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        return result
