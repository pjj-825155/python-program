from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import called
from pygame import mixer
import configparser
import time

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def host_login(request):
    return render(request, 'login/host_login.html')

@csrf_exempt
def player_login(request):
    return render(request, 'login/player_login.html')

@csrf_exempt
def host_logining(request):
    hostdata = called.read_ini("./configuration/host-login.ini", "hostInfo")
    server = called.read_ini("./configuration/server.ini", "ip")
    data = {}
    data['ip'] = server['ip']
    data['port'] = server['port']
    if hostdata['username'] == request.POST['user'] and hostdata['password'] == request.POST['pass']:
        data['score'] = called.read_ini("./configuration/score.ini", "score")
        return render(request, 'game/host.html', data)
    called.message(request, "用户名或密码错误")
    return render(request, 'login/host_login.html')

@csrf_exempt
def host(request):
    server = called.read_ini("./configuration/server.ini", "ip")
    data = {}
    data['ip'] = server['ip']
    data['port'] = server['port']
    data['score'] = called.read_ini("./configuration/score.ini", "score")
    Info = configparser.ConfigParser()
    Info['answer'] = {}
    with open("./configuration/answer.ini", "w") as configfile:
        Info.write(configfile)
    Info = configparser.ConfigParser()
    Info['state'] = {'state': 'true', 'answer': 'false'}
    with open("./configuration/state.ini", "w") as configfile:
        Info.write(configfile)
    return render(request, 'game/host.html', data)

@csrf_exempt
def player(request, param):
    server = called.read_ini("./configuration/server.ini", "ip")
    data = {}
    data['team'] = param
    data['ip'] = server['ip']
    data['port'] = server['port']
    return render(request, 'game/player.html', data)

@csrf_exempt
def change_score(request):
    score = called.read_ini("./configuration/score.ini", "score")
    for key in request.POST.keys():
        score[key] = request.POST[key]
    Info = configparser.ConfigParser()
    Info['score'] = score
    with open("./configuration/score.ini", "w", encoding='utf-8') as configfile:
        Info.write(configfile)
    server = called.read_ini("./configuration/server.ini", "ip")
    data = {}
    data['ip'] = server['ip']
    data['port'] = server['port']
    data['score'] = called.read_ini("./configuration/score.ini", "score")
    return render(request, 'game/host.html', data)

@csrf_exempt
def player_logining(request):
    server = called.read_ini("./configuration/server.ini", "ip")
    data = {}
    data['team'] = request.POST['team']
    data['ip'] = server['ip']
    data['port'] = server['port']
    return render(request, 'game/player.html', data)

def start(request):
    Info = configparser.ConfigParser()
    Info['state'] = {'state': 'false', 'answer': 'false'}
    with open("./configuration/state.ini", "w") as configfile:
        Info.write(configfile)
    try:
        mixer.init()
        mixer.music.load('./static/voices/1,2,3.mp3')
        mixer.music.play()
    except:
        pass
    return render(request, 'game/rockon.html')

def answer(request):
    Info = configparser.ConfigParser()
    Info['state'] = {'state': 'true', 'answer': 'true'}
    with open("./configuration/state.ini", "w") as configfile:
        Info.write(configfile)
    try:
        mixer.init()
        mixer.music.load('./static/voices/开始抢答.mp3')
        mixer.music.play()
    except:
        pass
    return render(request, 'game/answer.html')

def stop(request):
    data = {}
    server = called.read_ini("./configuration/server.ini", "ip")
    speed = called.read_ini("./configuration/time.ini", "time")
    answer = called.read_ini("./configuration/answer.ini", "answer")
    data['end'] = 'true'
    if not bool(answer):
        data['end'] = 'false'
    result = called.read_ini("./configuration/answer.ini", "answer")
    data['result'] = result
    for key,value in result.items():
        data['team'] = key
        data['time'] = value
        try:
            mixer.init()
            mixer.music.load(f"./static/voices/{data['team']}.mp3")
            mixer.music.play()
            time.sleep(1)
            mixer.music.load(f'./static/voices/抢答成功.mp3')
            mixer.music.play()
        except:
            pass
        break
    data['ip'] = server['ip']
    data['port'] = server['port']
    data['speed'] = speed['speed']
    return render(request, 'game/result.html', data)

def player_answer(request, param):
    server = called.read_ini("./configuration/server.ini", "ip")
    state = called.read_ini("./configuration/state.ini", "state")
    data = {}
    data['team'] = param
    data['ip'] = server['ip']
    data['port'] = server['port']
    if state['state'] == 'true' and state['answer'] == 'false':
        data['flag'] = 'defeat'
        return render(request, 'game/player-answer.html', data)
    if state['state'] == 'false' and state['answer'] == 'false':
        data['flag'] = 'timeout'
        try:
            mixer.init()
            time.sleep(1)
            mixer.music.load(f'./static/voices/{param}.mp3')
            mixer.music.play()
            time.sleep(1)
            mixer.music.load('./static/voices/抢答违规.mp3')
            mixer.music.play()
        except:
            pass
        return render(request, 'game/player-answer.html', data)
    if state['state'] == 'true' and state['answer'] == 'true':
        data['flag'] = 'success'
        answer = called.read_ini("./configuration/answer.ini", "answer")
        Info = configparser.ConfigParser()
        answer.update({param: time.asctime( time.localtime(time.time()))})
        Info['answer'] = answer
        with open("./configuration/answer.ini", "w", encoding='utf-8') as configfile:
            Info.write(configfile)
        return render(request, 'game/player-answer.html', data)
    return render(request, 'game/player.html', data)