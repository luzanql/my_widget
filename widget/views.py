from Crypto.Cipher import AES
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from base64 import b64encode, b64decode, binascii
from Crypto.Util.Padding import pad, unpad
import json



def index(request):
    return render(request, 'widget/index.html')

def nonce(request):
    # Shared Key between servers!
    key = b'A3ildelkRxNqzmjzA3ildelkRxNqzmjz'
    id = request.POST.get('n')
    encrypted = json.loads(b64decode(id).decode())

    # Get the initialization vector we used to encrypt
    iv = b64decode(encrypted['iv'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(b64decode(encrypted['data']))
    clean = unpad(data, 16).decode().rstrip()
    # our message is a json to decode!
    decoded_json = json.loads(b64decode(clean).decode())

    return JsonResponse(decoded_json)
