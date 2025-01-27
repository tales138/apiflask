from .token_creator import TokenCreator

token_creator = TokenCreator(
    token_key='1234',
    exp_time__min=30,
    refresh_time__min=15
)