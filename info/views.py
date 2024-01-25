from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model as user_model
from info import forms
from info.models import Info
from django.views import View


def info(request):
    context = dict()
    context['user'] = User.objects.all()

    return render(request, 'index/sharjewallet.html', context=context)


@login_required
@require_http_methods(request_method_list=['POST'])
def update_info(request):
    mobile = request.user.mobile
    User = user_model()
    user = User.objects.filter(mobile=mobile).first()
    form = forms.InfoUserForm(request.POST, request.FILES)
    if form.is_valid():
        information = form.save(commit=False)
        information.user = request.user
        information.is_active = False
        information.save()

        return HttpResponseRedirect(reverse_lazy('index'))

    messages.error(request, "اطلاعات ارسال شده توسط شما مطابق انتظار ما نبود! لطفا مجددا تلاش نمائید")
    return HttpResponseRedirect(reverse_lazy('index'))


class Profile(View):
    template_name = 'web/profile/index.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        user_info = request.user
        context['user_info'] = user_info
        information = Info.objects.filter(user=request.user).first()
        if information:
            context['info'] = information
            if information.image == "":
                context['image'] = "https://rebo.ir/static/web/assets/img/profile/profile2.jpg"
            else:
                context['image'] = information.image.url

            if information.image_codemeli == "":
                context['image_codemeli'] = "https://rebo.ir/static/web/assets/images/cardmeli.jpg"
                context['okmeli'] = False
            else:
                context['image_codemeli'] = information.image_codemeli.url
                context['okmeli'] = information.okmeli
            if information.image_shaba == "":
                context['image_shaba'] = "https://rebo.ir/static/web/assets/images/cardbanki.jpg"
                context['okbank'] = False
            else:
                context['image_shaba'] = information.image_shaba.url
                context['okbank'] = information.okbank
        else:
            context['image'] = "https://rebo.ir/static/web/assets/img/profile/profile2.jpg"
            context['image_codemeli'] = "https://rebo.ir/static/web/assets/images/cardmeli.jpg"
            context['image_shaba'] = "https://rebo.ir/static/web/assets/images/cardbanki.jpg"

        return render(request, template_name=self.template_name, context=context,
                      content_type=None, status=None, using=None)


@login_required
@require_http_methods(request_method_list=['POST'])
def update_info(request):
    mobile = request.user.mobile
    User = user_model()
    user = User.objects.filter(mobile=mobile).first()
    checkoneuser = request.user
    infoexist = Info.objects.filter(user_id=checkoneuser.pk).first()
    if infoexist:
        form = forms.InfoUserForm(request.POST, request.FILES, instance=infoexist)
    else:
        form = forms.InfoUserForm(request.POST, request.FILES)

    if form.is_valid():
        information = form.save(commit=False)
        if infoexist:
            print("info-valid-form")
            information.save()
        else:
            print("else-form")
            information.user = request.user
            information.is_active = False
            information.save()
        messages.info(request, "اطلاعات با موفقیت ارسال شد، بعد از تایید اطلاعات می توانید از این سامانه استفاده کنید")
        return HttpResponseRedirect(reverse_lazy('profile'))
    else:

        if not testmeli(request.POST.get('codemeli'))[1]:
            messages.error(request, testmeli(request.POST.get('codemeli'))[0])
            return HttpResponseRedirect(reverse_lazy('profile'))

        if request.POST.get('shaba') is not None:
            if not testshaba(request.POST.get('shaba'))[1]:
                messages.error(request, testshaba(request.POST.get('shaba'))[0])
                return HttpResponseRedirect(reverse_lazy('profile'))
    messages.error(request, "اطلاعات ارسال شده توسط شما مطابق انتظار ما نبود! لطفا مجددا تلاش نمائید")
    return HttpResponseRedirect(reverse_lazy('profile'))


def testshaba(shaba):
    res = True
    message_error = "در حال بررسی شبای بانکی ..."
    if shaba == "None":
        message_error = None
        res = False
        return message_error, res
    if len(shaba) != 24:
        message_error = "شماره شبا وارد شده معتبر نیست"
        res = False
        return message_error, res
    existshaba = Info.objects.filter(shaba=shaba).first()
    if existshaba:
        message_error = "شماره شبا وارد شده قبلا ثبت شده است"
        res = False
    return message_error, res


def testmeli(codemeli):
    res_meli = True
    message_error_meli = "در حال بررسی کد ملی ..."
    if len(codemeli) != 10:
        message_error_meli = "کد ملی وارد شده معتبر نیست"
        res_meli = False
        return message_error_meli, res_meli
    existmelli = Info.objects.filter(codemeli=codemeli).first()
    if existmelli:
        message_error_meli = "کد ملی وارد شده قبلا ثبت شده است"
        res_meli = False
    return message_error_meli, res_meli


@login_required
@require_http_methods(request_method_list=['POST'])
def update_info_image(request):
    checkoneuser = request.user
    infoexist = Info.objects.filter(user_id=checkoneuser.pk).first()
    if infoexist:

        form = forms.InfoImageForm(request.POST, request.FILES, instance=infoexist)
    else:

        form = forms.InfoImageForm(request.POST, request.FILES)
    if form.is_valid():
        information = form.save(commit=False)
        information.image = request.FILES.get('image_info')
        information.save()
    return HttpResponseRedirect(reverse_lazy('profile'))


