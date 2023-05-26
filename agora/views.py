import json
import os
import time

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from agora_token_builder import RtcTokenBuilder, RtmTokenBuilder

ROLE_RTM_USER = 1
ROLE_PUBLISHER = 1


@login_required(login_url='/admin/')
def index(request):
    users = User.objects.all()
    all_users = [{'username': user.username, 'id': user.id} for user in users]
    return render(request, 'agora/index.html', {'allUsers': all_users, 'agoraAppID': os.environ.get('AGORA_APP_ID')})


def fetch_users(request):
    users = User.objects.all()
    all_users = [{'username': user.username, 'id': user.id} for user in users]
    return JsonResponse(all_users, safe=False)


@csrf_exempt
def generate_agora_token(request):
    app_id = os.environ.get('AGORA_APP_ID')
    print(app_id)
    app_certificate = os.environ.get('AGORA_APP_CERTIFICATE')
    print(app_certificate)
    body = json.loads(request.body.decode('utf-8'))
    channel_name = body.get('channelName')
    print(channel_name)
    user_account = request.user.username
    print(user_account)
    expire_time_in_seconds = 3600
    print(expire_time_in_seconds)
    current_timestamp = int(time.time())
    print(current_timestamp)
    privilege_expired_ts = current_timestamp + expire_time_in_seconds
    print(privilege_expired_ts)
    token = RtcTokenBuilder.buildTokenWithAccount(
        app_id, app_certificate, channel_name, user_account, ROLE_PUBLISHER, privilege_expired_ts)

    rtm_token = RtmTokenBuilder.buildToken(
        app_id, app_certificate, user_account, ROLE_RTM_USER, privilege_expired_ts)
    return JsonResponse({'token': token, 'rtm_token': rtm_token, 'appID': app_id})



