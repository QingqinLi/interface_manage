# coding=utf-8
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
import json
import requests
from interface.utils.get_result import GetResult
from interface.models import interfaceData
from django.core.paginator import Paginator, EmptyPage
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def index(request):
    pass


def msg_interface(request):
    response_info = {
        'code': 200,
        'msg': '添加成功',
        'result': 'success',
    }
    if request.method == 'GET':
        return render(request, "interface_add.html")
    elif request.method == 'POST':
        param_name = request.POST.get("interfaceName", None)
        param_describe = request.POST.get("interfaceDescribe", None)
        param_url = request.POST.get("interfaceUrl", None)
        param_method = request.POST.get("interfaceMethod", None)
        param_data = request.POST.get("interfaceData", None)
        param_except_desc = request.POST.get("interfaceExcept", None)
        param_except_content = request.POST.get("exceptContent", None)

        # 校验数据，存入数据库中
    else:
        response_info['code'] = 1001
        response_info['msg'] = '暂不支持此类型'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
    # 参数校验
    if 0 < len(param_name) < 50:
        name = param_name
    else:
        print("aaaaaaaa errorss")
        response_info['msg'] = '参数非法1'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, 'interface_add.html', {'response': response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if 0 < len(param_describe) < 100:
        describe = param_describe
    else:
        response_info['msg'] = '参数非法3'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if len(param_url) > 0:
        url = param_url
    else:
        response_info['msg'] = '参数非法5'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if param_method in ['get', 'post']:
        method = param_method.lower()
    else:
        response_info['msg'] = '参数非法7'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if method == 'get' and not param_data:
        request_data = None
    else:
        try:
            request_data = json.loads(param_data)
        except TypeError:
            response_info['msg'] = '参数非法9'
            response_info['code'] = 1002
            response_info['result'] = 'failed'
            return render(request, "interface_add.html", {"response": response_info})
            # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if param_except_desc in ['contains', 'equal', 'notcontains', 'notequal']:
        except_desc = param_except_desc
    else:
        response_info['msg'] = '参数非法0'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    if 0 < len(param_except_content):
        except_content = param_except_content
    else:
        response_info['msg'] = '参数非法11'
        response_info['code'] = 1002
        response_info['result'] = 'failed'
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))

    # 校验
    try:
        if method == 'get':
            if request_data:
                response = requests.get(url, request_data, timeout=5).text
                # print(response)
                if GetResult().get_result_except(response, except_desc, except_content):
                    data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "response_data": response,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                        "result": 'success',
                    }
                    db_data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                    }
                    response_info['data'] = data
                    return render(request, "interface_add.html", {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
                    # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
                else:
                    data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "response_data": response,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                        "result": 'failed',
                    }

                    db_data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                    }
                    response_info['data'] = data
                    return render(request, "interface_add.html", {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
            else:
                response = requests.get(url, timeout=5).text
                # print(response)
                if GetResult().get_result_except(response, except_desc, except_content):
                    data = {
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "interface_name": name,
                        "response_data": response,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                        "result": 'success',
                    }
                    db_data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                    }
                    response_info["data"] = data
                    print("data", response_info)
                    return render(request, 'interface_add.html', {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
                    # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
                else:
                    # print(response)
                    data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "response_data": response,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                        "result": 'failed',
                    }
                    db_data = {
                        "interface_name": name,
                        "describe": describe,
                        "url": url,
                        "request_data": request_data,
                        "request_method": method,
                        "except_desc": except_desc,
                        "except_content": except_content,
                    }
                    print("hello failed")
                    response_info['data'] = data
                    return render(request, "interface_add.html", {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
                    # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
        else:
            response = requests.post(url, json=request_data, timeout=5).text
            if GetResult().get_result_except(response, except_desc, except_content):
                data = {
                    "interface_name": name,
                    "describe": describe,
                    "url": url,
                    "request_data": request_data,
                    "response_data": response,
                    "request_method": method,
                    "except_desc": except_desc,
                    "except_content": except_content,
                    "result": 'success',
                }
                db_data = {
                    "interface_name": name,
                    "describe": describe,
                    "url": url,
                    "request_data": request_data,
                    "request_method": method,
                    "except_desc": except_desc,
                    "except_content": except_content,
                }
                response_info['data'] = data
                return render(request, "interface_add.html", {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
                # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
            else:
                data = {
                    "interface_name": name,
                    "describe": describe,
                    "url": url,
                    "request_data": request_data,
                    "response_data": response,
                    "request_method": method,
                    "except_desc": except_desc,
                    "except_content": except_content,
                    "result": 'failed',
                }
                db_data = {
                    "interface_name": name,
                    "describe": describe,
                    "url": url,
                    "request_data": request_data,
                    "request_method": method,
                    "except_desc": except_desc,
                    "except_content": except_content,
                }
                response_info['data'] = data
                return render(request, "interface_add.html", {"response": response_info, "db_data": json.dumps(db_data, ensure_ascii=False)})
                # return HttpResponse(json.dumps(response_info, ensure_ascii=False))
    except Exception as e:
        response_info['msg'] = "error"
        response_info['code'] = 1003
        response_info['result'] = 'failed'
        print("hello", e, response_info)
        return render(request, "interface_add.html", {"response": response_info})
        # return HttpResponse(json.dumps(response_info, ensure_ascii=False))


def add_interface(request):
    response_info = {
        'code': 200,
        'msg': '添加成功',
        'result': 'success',
    }
    if request.method == 'POST':
        interface = request.POST.get("dbData", None)
        if interface:
            interface = json.loads(interface, encoding='utf-8')
            name = interface.get('interface_name', None)
            describe = interface.get("describe", None)
            url = interface.get("url", None)
            request_data = interface.get("request_data", None)
            method = interface.get("request_method", None)
            except_desc = interface.get("except_desc", None)
            except_content = interface.get("except_content", None)

            # 判断是否有重复的数据，没有则存进数据库中
            obj = interfaceData.objects.filter(name=name, url=url, method=method,
                                               except_desc=except_desc, except_content=except_content)
            if len(obj) > 0:
                response_info['msg'] = '接口case已存在'
                response_info['code'] = 1001
                response_info['result'] = 'failed'
                return HttpResponseRedirect("/interface/show/1")
            else:
                interfaceData.objects.create(name=name, describe=describe, url=url,
                                             request_data=request_data, method=method,
                                             except_desc=except_desc, except_content=except_content)
                return HttpResponseRedirect("/interface/show/1")

        else:
            response_info['msg'] = 'case数据异常'
            response_info['code'] = 1002
            response_info['result'] = 'failed'
            return HttpResponse(response_info)

    else:
        response_info['msg'] = '暂不支持此类型请求'
        response_info['code'] = 1003
        response_info['result'] = 'failed'
        return HttpResponse(response_info)


def show_interface(request, page=None):
    response_info = {
        'code': 200,
        'msg': "搜索成功",
        'result': 'success',
    }
    print("page", page, type(page))
    if request.method == 'POST':
        page = request.POST.get("page", 1)
        try:
            page = int(page)
        except TypeError:
            response_info['code'] = 1002
            response_info['msg'] = '页码参数异常'
            response_info['result'] = 'failed'
            return HttpResponse(response_info)
    else:
        try:
            page = int(page)
        except TypeError:
            response_info['code'] = 1002
            response_info['msg'] = '页码参数异常'
            response_info['result'] = 'failed'
            return HttpResponse(response_info)
    page_num = 20
    objs = interfaceData.objects.filter(is_delete=False).order_by('-add_time')

    if len(objs) > 0:
        paging = Paginator(objs, page_num)
        try:
            showing = paging.page(page)
        except EmptyPage:
            showing = paging.page(paging.num_pages)
        show_list = []
        for item in showing:
            d = {

                'id': item.id,
                'name': item.name,
                'describe': item.describe,
                'url': item.url,
                'data': item.request_data,
                'method': item.method,
                'except_desc': item.except_desc,
                'except_content': item.except_content,
            }
            show_list.append(d)

        return render(request, 'interface_show.html', {'show_list': show_list, "page_all": range(paging.num_pages),
                                                       "current_page": page,
                                                       "max_page": paging.num_pages})
    else:
        response_info['code'] = 1001
        response_info['msg'] = '暂无数据'
        response_info['result'] = 'failed'
        return HttpResponse(response_info)

    # else:
    #     response_info['code'] = 1003
    #     response_info['msg'] = '暂不支持此类型'
    #     response_info['result'] = 'failed'
    #     return HttpResponse(response_info)


def del_interface(request, case_id=None):
    response_info = {
        'code': 200,
        'msg': '删除成功',
        'result': 'success',
    }
    try:
        case_id = int(case_id)
    except TypeError:
        response_info['code'] = 1001
        response_info['msg'] = '参数异常'
        response_info['result'] = 'failed'
        return HttpResponse(json.loads(response_info))
    obj = interfaceData.objects.filter(id=case_id)
    if obj:
        result = obj[0]
        result.is_delete = True
        result.save()
        return HttpResponseRedirect('/interface/show/1')
    else:
        response_info['code'] = 1001
        response_info['msg'] = '未找到该条数据'
        response_info['result'] = 'failed'
        return HttpResponse(json.loads(response_info))



