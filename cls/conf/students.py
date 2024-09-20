# 그냥 다른 파이썬 파일 '.py' 이게 모듈이다.
# 그렇게 만든 모듈들을 모아서 'package'라고 한다. 
# 즉, conf 폴더 -> 패키지다.

# 라이브러리 -> 패키지들을 모아놓은 것

# 다른 '모듈'에 있는 클래스 가져오기 
# 단, 명시성은 지켜주자.
from .base import Person 

# 학생 객체 -> 이름, 나이, 먹는다는 행위
# 상속
class Student(Person):  # 상속할 부모 클래스를 ()안에 작성한다.
    # def __init__(self, name, age):
    #     pass
    # 학생이 강의를 선택한다. 
    def app_for_courese(self, course):
        course.students.append(self)

s1 = Student('학생', 29)
print(s1.name)

