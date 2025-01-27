from datetime import datetime, timedelta
import jwt
import time
from app.models.token_blocklist import TokenBlocklist
class TokenCreator:
    def __init__(self,token_key:str,exp_time__min:int,refresh_time__min:int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time__min
        self.__REFRESH_TIME_MIN = refresh_time__min

    def generate_token(self,uid:int):
        token = jwt.encode({
            'exp':datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN ),
            'uid':uid
        },key=self.__TOKEN_KEY,algorithm='HS256')
        return token
    
    def refresh(self,token:str):
        token_information = jwt.decode(token,key=self.__TOKEN_KEY,algorithms='HS256')
        token_uid = token_information['uid']
        exp_time = token_information['exp']
       
        if((exp_time -  time.time()) /60) < self.__REFRESH_TIME_MIN:
            blocked_token = TokenBlocklist(jwt=token)
            blocked_token.block_token()
            return self.generate_token(token_uid)
        
        return token