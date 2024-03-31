from django.shortcuts import render
from django.views import View
# from .models import ...
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count

class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        self.answer2 = {'username': Author.objects.annotate(number_of_entries=Count('entries')).values('username').order_by('-number_of_entries').first()}# TODO Какой автор имеет наибольшее количество опубликованных статей?
        self.answer3 = Entry.objects.filter(Q(tags__name='Кино')|Q(tags__name='Музыка')).annotate(en_count=Count('id')).values('text')  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer4 = Author.objects.filter(gender='ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer5 = f'{Author.objects.filter(status_rule=1).count()/Author.objects.all().count()*100:.2f}%'  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer6 =  Author.objects.filter(Q(authorprofile__stage__gte=1) & Q(authorprofile__stage__lte=5))  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        # max_age =

        self.answer7 = Author.objects.aggregate(Max_age=Max('age'))['Max_age']  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lte=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 = Author.objects.annotate(count=Count('entries')).values('username', 'count')  # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
# class TrainView(View):
#     def get(self, request):
#         context = {}  # Создайте здесь запросы к БД
#         return render(request, 'train_db/training_db.html', context=context)

