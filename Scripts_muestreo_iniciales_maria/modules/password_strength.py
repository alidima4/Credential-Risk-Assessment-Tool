import zxcvbn
def password_strength(password):
    result = zxcvbn.zxcvbn(password)
    filtered_result = {
        'password': password,
        #'guesses': result['guesses'],
        'guesses_log10': result['guesses_log10'],
        'sequence': [
            {'token': seq['token'], 'pattern': seq['pattern']}
            for seq in result['sequence']
        ],
        'online_no_throttling_10_per_second_display': result['crack_times_display']['online_no_throttling_10_per_second'],
        'online_no_throttling_10_per_second_seconds': result['crack_times_seconds']['online_no_throttling_10_per_second'],
        'score': result['score']
    }
    
    return filtered_result

