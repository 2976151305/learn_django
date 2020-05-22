import logging
import json
import re
import hashlib

from django.shortcuts import render

from api.models import UserModel
from django.http import JsonResponse
from api.HTTP_STATUS import STATUS

logger = logging.getLogger('django')

class User():
  ''' 获取用户信息 '''
  def getUserInfo(request):
    id = request.GET.get('id', '')
    if not id:
      res = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '没有id传入'
      }
      return JsonResponse(data = res)
    user = UserModel.objects.filter(id = id, is_del = 0, status = 1).first()
    if not user:
      res = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '用户不存在'
      }
      return JsonResponse(data = res)
    res = {
      'code': STATUS.SUCCESS,
      'data': user.to_json()
    }
    return JsonResponse(data = res)

  ''' 注册 '''
  def register(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data['username']
    password = data['password']
    if not (username and password):
      data = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '账号密码不能为空'
      }
      return JsonResponse(data = data)
    if len(username) < 6:
      data = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '用户名不能少于6个字符'
      }
      return JsonResponse(data = data)
    if len(password) < 6:
      data = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '密码不能少于6个字符'
      }
    if UserModel.objects.filter(username = username).exists():
      data = {
        'code': STATUS.PARAMETER_ERROR,
        'msg': '账号已存在'
      }
      return JsonResponse(data)
    UserModel.objects.create(
      username = username,
      password = hashlib.md5().update(password.encode(encoding = 'utf-8'))
    )
    return JsonResponse(data = {
      'code': STATUS.SUCCESS,
      'data': ''
    })

  ''' 更新用户数据 '''
  def updateUserInfo(request):
    data = json.loads(request.body.decode('utf-8'))
    UserModel.objects.filter(id = data['id']).update(**data)
    