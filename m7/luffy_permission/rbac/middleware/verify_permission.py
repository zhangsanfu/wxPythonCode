from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from luffy_permission.settings import PERMISSION_LIST_SESSION_KEY,WHITE_LIST
import re

class VerifyPermission(MiddlewareMixin):

    def process_request(self, request):
        # 通过字典的get(key)方法获取value不会报错，得到的是一个列表，里面存放着每一个权限的字典，如[{权限1},{权限2},{权限3}]
        permission_list = request.session.get(PERMISSION_LIST_SESSION_KEY)

        # 循环白名单，如果匹配白名单中的路径成功，那么就在中间件中return，直接去执行视图函数
        for url in WHITE_LIST:
            url_ret = re.search(url, request.path_info)
            if not url_ret:
                continue
            else:
                return

        # 循环权限列表，用每一个权限字典中的url和当前请求的路径相匹配，判断其是否可以访问
        if permission_list:
            for permission in permission_list:
                per_ret = re.match('^'+permission['url']+'$', request.path_info)
                if not per_ret:
                    continue
                else:
                    return
            return HttpResponse('没有权限访问')
        else:
            # 如果登录的用户有角色，但是角色内没有分配权限，所以permission_list就会为空，没有访问任何页面的权限
            if request.user.is_authenticated:
                return HttpResponse('没有权限访问')

            # 如果用户访问的不是白名单的路径，访问的是需要权限的路径，让其先登录
            return HttpResponse('请先登录')
