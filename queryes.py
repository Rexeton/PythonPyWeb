import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train.models import  Author, AuthorProfile, Entry,Tag #,Blog

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    """<QuerySet [<Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Новые гаджеты и устройства: обзор рынка>]>"""

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)

    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # """<QuerySet [<Entry: Знакомство с Парижем>,
    # <Entry: Инновации в области виртуальной реальности>]>"""
    #
    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))  # Аналогично exact
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))
    #
    #
    # print(Entry.objects.filter(headline__contains='мод'))

    # all_obj = Blog.objects.all()
    # obj_first = all_obj.first()
    # print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
    #        f"Все значения = {all_obj}")
    from django.db.models import Count, Max,Q

    # entries_with_tags_count = Entry.objects.annotate(
    #     en_count=Count('Entry__author_id')).values('author_id', 'en_count')
    # # entries_max_count = Entry.objects.select_related('author','entry').get(id=1)
    # print(entries_with_tags_count)

    entry =  Author.objects.annotate(number_of_entries=Count('entries')).values('username').order_by('-number_of_entries').first()['username']
    # max_age = Author.objects.aggregate(Max_age=Max('age'))
    # max_ages = max_age['Max_age']
    print(entry)
