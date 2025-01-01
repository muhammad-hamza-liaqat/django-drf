from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


# def get_tokens_for_user(user):

#     refresh = RefreshToken.for_user(user)
#     refresh['userName'] = user.userName  
#     refresh['email'] = user.email

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

def get_tokens_for_user(user):
    signing_key = getattr(settings, 'SIMPLE_JWT', {}).get('SIGNING_KEY', settings.SECRET_KEY)
    print(f"JWT Signing Key: {signing_key}") 

    refresh = RefreshToken.for_user(user)
    refresh['userName'] = user.userName
    refresh['email'] = user.email  

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

