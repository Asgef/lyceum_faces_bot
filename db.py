questions = {
    'question_1': 'Что было самое сложное в учебный период?',
    'question_2': 'Профиль класса, в котором учился?',
    'question_3': 'Как выбирал(а) ВУЗ?',
    'question_4': 'На какой факультет?',
    'question_5': 'Это был «ВУЗ мечты» или скорее «Реальный вариант»?',
    'question_6': 'Мама была рада твоему выбору ВУЗа и факультета?',
    'question_7': 'По каким предметам сдавал экзамены?',
    'question_8': 'Что было самым сложным на ЕГЭ?',
    'question_9': 'Была ли привилегия «БВИ»?',
    'question_10': 'Какие олимпиады взял(а)?',
    'question_11': 'Как готовился: курсы, кружки, репетиторы?',
    'question_12': 'Каким своим достижением, дипломом гордишься больше всего?',
    'question_13': 'Чтобы посоветовал сейчас себе в школьный период?',
    'question_14': 'Что посоветуешь будущим выпускникам?',
    'question_15': 'Кого из учителей нужно обнять от твоего имени?',
    'question_16': 'Рекомендуй выпускника, который по твоему мнению, должен попасть на сайт «Лицей в лицах»?'
}

question_order = [
    'question_1', 'question_2', 'question_3', 'question_4', 'question_5',
    'question_6', 'question_7', 'question_8', 'question_9', 'question_10',
    'question_11', 'question_12', 'question_13', 'question_14', 'question_15',
    'question_16'
]


universities = {
    'vshe': {
        'name': 'НИУ ВШЭ',
        'photo': 'niy_vshe.jpg', # Фото университета
        'graduates': {
            'sofia': {
                'name': 'София',
                'photo': 'niy_vshe.jpg', # Фото выпускника
                'answers': {
                    'question_1': 'Самым сложным было все успевать',
                    'question_2': 'Маткласс',
                    'question_3': 'С выбором помогла классная руководитель, а также дни открытых дверей',
                    'question_4': 'Матфак, совместный бакалавриат НИУ ВШЭ и ЦПМ',
                    'question_5': 'Вуз мечты и реальный вариант одновременно',
                    'question_6': 'Да',
                    'question_7': 'Физика, математика и русский язык',
                    'question_8': 'Дождаться результатов',
                    'question_9': 'БВИ не было, ЕГЭ по математике 100 баллов',
                    'question_10': 'Олимпиада «РосАтом»',
                    'question_11': 'Кружки в школе и репетитор по русскому языку',
                    'question_12': 'Серебряная медаль',
                    'question_13': '«Держись, все закончится!»',
                    'question_14': '«Это все закончится!»',
                    'question_15': 'Светлану Владимировну Хащинину, Лидию Викторовну Бучневу и Елену Алексеевну Онучак',
                    'question_16': 'Зворыкин Илья'
                },
            },

            'artur': {
                'name': 'Артур',
                'photo': 'niy_vshe.jpg',
                'answers': {
                    'question_1': 'Сессии',
                    'question_2': 'ИТ',
                    'question_3': 'Рассматривал МГУ и ВШЭ',
                    'question_4': 'ФСН',
                    'question_5': 'ВУЗ мечты',
                    'question_6': 'Очень',
                    'question_7': 'Математика, физика, информатика и русский язык',
                    'question_8': 'Ждать результаты',
                    'question_9': 'БВИ не было',
                    'question_10': 'Не взял олимпиад',
                    'question_11': 'Школьные кружки и репетитор',
                    'question_12': 'Золотая медаль',
                    'question_13': '«Не переживать!»',
                    'question_14': '«Экзамены легче, чем кажется. Не нервничайте!»',
                    'question_15': 'Аннету Леонидовну, Зою Владимировну и всех учителей математики',
                    'question_16': 'Самвел Тарасов',
                },
            },

            'alsu': {
                'name': 'Алсу',
                'photo': 'niy_vshe.jpg',
                'answers': {
                    'question_1': 'Грамотно организовывать свое время',
                    'question_2': 'Математический',
                    'question_3': 'Популярность ВУЗа, успешность выпускников, величину учебной нагрузки.',
                    'question_4': 'ФКН',
                    'question_5': 'ВУЗ мечты',
                    'question_6': 'Да',
                    'question_7': 'Математика, физика, информатика и русский язык.',
                    'question_8': 'Сохранять концентрацию и внимательность, чтобы не допускать глупых ошибок',
                    'question_9': 'БВИ не было',
                    'question_10': 'РОСАТОМ, ФизТех, DANO',
                    'question_11': 'Кружки в школе, интенсивы в Школково, выездная школа к DANO, Сириус.Курсы',
                    'question_12': 'Диплом победителя ММО в 10 классе',
                    'question_13': 'Меньше времени тратить впустую, все время ботать',
                    'question_14': 'Участвовать в олимпиадах, много ботать',
                    'question_15': 'Светлану Владимировну, Лидию Викторовну, Наталью Исаевну, Аннету Леонидовну и Дарью Александровну',
                    'question_16': 'Поздеев Алексей',
                },
            },
            # Добавляем других выпускников...
        },
    },
    # Добавляем другие университеты...
    'bauman': {
        'name': 'МГТУ им. Н.Э. Баумана',
        'photo': 'mgty.jpeg',
        'graduates': {
                'asya': {
                'name': 'Ася',
                'photo': 'mgty.jpeg',
                'answers': {
                    'question_1': 'Режим дня',
                    'question_2': 'Маткласс',
                    'question_3': 'По своим интересам',
                    'question_4': 'СМ 1',
                    'question_5': 'ВУЗ мечты',
                    'question_6': 'Да',
                    'question_7': 'Математика, физика, информатика и русский язык',
                    'question_8': 'Ожидание результатов',
                    'question_9': 'БВИ',
                    'question_10': '«Шаг в будущее», «Газпром»',
                    'question_11': 'Кружки в школе',
                    'question_12': 'Золотая медаль и победа в олимпиаде «Шаг в будущее» в 10-м классе',
                    'question_13': 'Больше спать',
                    'question_14': '«Идти к своей цели»',
                    'question_15': 'Лидию Викторовну Бучневу и Светлану Владимировну Хащинину',
                    'question_16': 'Лебедева София'
                },
            },

            # Добавляем других выпускников...
        },
    },

    'mgu': {
        'name': 'МГУ',
        'photo': 'mgy.jpg',
        'graduates': {
                'denis': {
                'name': 'Денис',
                'photo': 'mgy.jpg',
                'answers': {
                    'question_1': 'Не выгореть',
                    'question_2': 'Физмат, в 11 классе перешел в маткласс.',
                    'question_3': 'Мне очень нравиться математика и информатика, поэтому искал Вуз, где их будет много',
                    'question_4': 'ВМК',
                    'question_5': 'ВУЗ мечты',
                    'question_6': 'Да',
                    'question_7': 'Математика, физика, информатика и русский язык, ДВИ в МГУ',
                    'question_8': 'Сдавать физику',
                    'question_9': 'БВИ не было',
                    'question_10': 'Дипломов по олимпиадам не было',
                    'question_11': '«Открытый курс»',
                    'question_12': 'Помогал с вариантами ЕГЭ по информатике одному из авторов на сайте kompege.ru',
                    'question_13': '«Лучше распределять время и не унывать!»',
                    'question_14': '«Больше спать и отдыхать! Учебы в ВУЗе будет еще больше и спать получится еще меньше.»',
                    'question_15': 'Наталью Ивановну Науменко',
                    'question_16': 'Гопкало Валерию'
                },
            },

            'matvey': {
                'name': 'Матвей',
                'photo': 'mgy.jpg',
                'answers': {
                    'question_1': 'Проснуться утром, а потом не заснуть на скучном уроке.',
                    'question_2': 'Физмат, с 10-го класса соцэконом',
                    'question_3': 'Выбирал по предмету. Математика нравиться больше других дисциплин.',
                    'question_4': 'Экономический',
                    'question_5': 'Совпало',
                    'question_6': 'Скорее да',
                    'question_7': 'Математика, физика, информатика и русский язык, ДВИ по математике (самый сложный).',
                    'question_8': 'Не проспать',
                    'question_9': 'БВИ не было',
                    'question_10': 'Олимпиады не писал',
                    'question_11': 'Репетиторы',
                    'question_12': 'Ничем не горжусь',
                    'question_13': 'Носить еду с собой в лицей.',
                    'question_14': 'Не париться по поводу ЕГЭ. Все сдадут и точно поступят.',
                    'question_15': 'Я не лицемер. С учителями у меня дистанция. Если это вопрос про уважение, то нескольким педагогам я бы от души пожал руку.',
                    'question_16': 'Без рекомендаций',
                },
            },

            # Добавляем других выпускников...
        },
    },

    'mfti': {
        'name': 'МФТИ',
        'photo': 'mfti.jpg',
        'graduates': {
            'ivan': {
                'name': 'Иван',
                'photo': 'mfti.jpg',
                'answers': {
                    'question_1': 'Много самостоятельно работать, просто пахать',
                    'question_2': 'Математический',
                    'question_3': 'После дня открытых дверей влюбился в этот ВУЗ',
                    'question_4': 'ФПМИ-ИвтСП',
                    'question_5': 'ВУЗ мечты',
                    'question_6': 'Да',
                    'question_7': 'Математика, физика, информатика и русский язык.',
                    'question_8': 'Ждать результаты',
                    'question_9': 'БВИ не было',
                    'question_10': 'Phystech/International по математике, Росатом (матем), ОРМО, ВОШ «Миссия выполнима. Твое призвание - финансист!» (матем), Межрегиональная олимпиада школьников имени И.Я. Верченко (комп. без.), ШвБ (физика, комп модел и графика)',
                    'question_11': 'Кружки в школе, курс по олимп математике «Поступашки»',
                    'question_12': 'Диплом победителя олимпиады Росатом по математике в 11 классе.',
                    'question_13': 'Вкладывать все время в учебу.',
                    'question_14': 'Не расстраиваться, когда кажется, что прогресса нет. Помни, ты становишься лучше с каждой решенной задачей.',
                    'question_15': 'Светлану Владимировну Хащинину, Лидию Викторовну Бучневу.',
                    'question_16': 'Каждый ученик 11 «Ж» класса, выпуск 2024. Наши ребята знают, что такое «Устал, но надо продолжать!»',
                },
            },
            # Добавляем других выпускников...

        },
    },
    # Добавляем другие университеты...

}
