class student:
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year


        def introduce_name(self):
            print("이름은 %s이다." % self.name)

        def introduce_grade(self):
            print("학년은 %s학년이다." % self.grade)

        def introduce_student_number(self):
            print("학번은 %s 이다." % self.student_number)

        def introduce_sex(self):
            if( sex == '모른다'):
                sex = 'None'
            print("성별은 %s 이다." % self.sex)

        def introduce_address(self):
            print("성별은 %s 이다." % self.address)

        def introduce_phone_number(self):
            if( phone_number == '모른다'):
                phone_number = 'None'
            print(phone_number)

        def introduce_year(self):
            if( year == 1):
                print('멋사 1년차')
                print('우와 아기사자다!')
            else:
                print("멋사 %s년차" % self.year)


while True:
    class_name = str(input("객체 명을 입력하시오. (단, 영문으로): " ))
    name = str(input("이름을 입력하시오 (단, 한글로): " ))
    grade = int(input("학년을 입력하시오 (단, 숫자로): "))
    student_number = int(input("학번을 입력하시오 (단, 숫자로): "))
    sex = str(input("성별을 입력하시오(모를 때는 모른다 라고 입력.): " ))
    address = str(input("주소를 입력하시오(~시까지만): "))
    phone_number = str(input("전화번호를 입력하시오(모를 때는 모른다 라고 입력): "))
    year = int(input("멋사 몇년차인가요?(단, 숫자로): "))
    print()

    if( class_name == '종료'):
        break

    jiyun = student(name, grade, student_number, sex, address, phone_number, year)

    jiyun.introduce_name()
    jiyun.introduce_grade()
    jiyun.introduce_student_number()
    jiyun.introduce_sex()
    jiyun.introduce_address()
    jiyun.introduce_phone_number()
    jiyun.introduce_year()