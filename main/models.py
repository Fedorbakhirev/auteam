from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class Tariff(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    speed = models.PositiveIntegerField(default=0, verbose_name='Скорость')
    cloud = models.PositiveIntegerField(default=0, verbose_name='Облако')
    desc = models.TextField(max_length=255, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    is_promotion = models.BooleanField(default=False, verbose_name='Акция')

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.title


class UserTariff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone_regex = RegexValidator(regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                                 message="Номер телефона должен быть в формате: +79992345679")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Номер телефона')  # validators should be a list
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тариф')
    is_paid = models.DateField(verbose_name='Оплачено до', null=True, blank=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Инженер"},
                                 related_name='Engineer', verbose_name='Активировал', null=True, blank=True)
    is_active = models.BooleanField(default=0, verbose_name='Активный')
    enabled_at = models.DateTimeField(auto_now=True, verbose_name='Дата активации')

    class Meta:
        verbose_name = 'Тариф пользователя'
        verbose_name_plural = 'Тариф пользователя'

    def __str__(self):
        return str(self.user)


class TariffHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тариф')
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Инженер"},
                                 related_name='Обработал', verbose_name='Отклонил', null=True, blank=True)
    is_declined = models.BooleanField(default=False, verbose_name='Отклонено')
    desc = models.TextField(max_length=255, verbose_name='Причина отклонения', blank=True)
    disabled_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отключения')

    class Meta:
        verbose_name = 'История тарифов'
        verbose_name_plural = 'История тарифов'

    def __str__(self):
        return str(self.user)


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    subject = models.CharField(max_length=50, verbose_name='Тема сообщения')
    desc = models.TextField(max_length=255, verbose_name='Сообщение')
    answer = models.TextField(max_length=255, verbose_name='Ответ', blank=True)
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Инженер"},
                                 related_name='Инженер', verbose_name='Инженер', null=True, blank=True)
    status = models.BooleanField(verbose_name='Ответ дан', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', null=True)
    desc = models.TextField(max_length=255, verbose_name='Сообщение')
    phone_regex = RegexValidator(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        message="Номер телефона должен быть в формате: +79992345679")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
                                    verbose_name='Номер телефона')  # validators should be a list
    status = models.BooleanField(verbose_name='Ответ дан', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return str(self.name)