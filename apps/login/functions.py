from apps.tokens.utils import set_token_cookies, get_token_pair


def login(response, user):
    payload = {
        'username': user.username,
        'password': user.password,
        'email': user.email
    }
    token_pair = get_token_pair(payload=payload)
    response = set_token_cookies(response, user, token_pair['access_token'], token_pair['refresh_token'])
    return response
