from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션이라는걸 만든다.
# 이 모델에 맞는 테이블을 만듭니다.
# 질문 : 여름에 놀러간다면 어디에 갈래? 
# 산, 강, 바다, 도심 호캉스

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True) # 처음 생길 때
    # 질문, 질문 생성 날짜 
    
    # score = models.FloatField(default=0)
    # is_somthing = models.BooleanField(default=False)
    # json_field = models.JSONField(default=dict)
    # average_score = models.FloatField(default=0.0)
    # 모델의 변경사항 -> 테이블에 반영하기 위해 마이그레이션을 만들어야함 

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 어제보다 최근에 만들어졌으면 !

    # 제목이 목록으로 되게끔 ! 
    def __str__(self): # 모델의 문자열 표현 방식 
        if self.was_published_recently():
            new_badge = 'NEW!!!'
        else:
            new_badge = ''
        return f'{new_badge} 제목: {self.question_text}, 날짜 : {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 초이스가 퀘스쳔에 속해있음 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.question.question_text}]{self.choice_text}'