from django.shortcuts import render

'''
    GET /users/ — страница со списком всех пользователей
    GET /users/create/ — страница регистрации нового пользователя
    POST /users/create/ — создание пользователя
    GET /users/<int:pk>/update/ — страница редактирования пользователя
    POST /users/<int:pk>/update/ — обновление пользователя
    GET /users/<int:pk>/delete/ — страница удаления пользователя
    POST /users/<int:pk>/delete/ — удаление пользователя
    GET /login/ — страница входа
    POST /login/ — аутентификация (вход)
    POST /logout/ — завершение сессии (выход)
'''
def index(request):
    return render(
        request,
        'index.html',
    )
