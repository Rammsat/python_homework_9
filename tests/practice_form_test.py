from demoqa_tests.model.data.user import User
from demoqa_tests.model.pages.practice_form import PractiseFromUserSteps


def test_student_registration_form():
    user = User(first_name='World',
                last_name='Peace',
                email='qwe@mail.com',
                gender='Male',
                phone='9998887755',
                birthday_year='1999',
                birthday_month='May',
                birthday_day=11,
                subject='English',
                hobby='Sports',
                image='resources/image.PNG',
                address='Some address',
                state='NCR',
                city='Delhi')

    practice_form.given_opened()
    practice_form.fill_data(user)
    practice_form.submit()

    practice_form.assert_fields(user)


practice_form = PractiseFromUserSteps()
