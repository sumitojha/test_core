from django.conf.urls import url
import views

urlpatterns =[
    url(
        regex=r'^$',
        view=views.index,
        name="dashboard"
    ),

    url(
        regex=r'^qa/$',
        view=views.QuestionAnswerView.as_view(),
        name="question-answer"
    )
]