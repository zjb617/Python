db_file = 'student_data.db'


def validate_phone(num):#检验手机号的合法性
    if not num.isdigit():
        exit('手机号必须是数字。')
    elif len(num) != 11:
        exit('手机号必须达到11位。')


def register_api():
    stu_data = {}
    print("欢迎来到XXX".center(50, '-'))
    print('请完成学籍注册')
    name = input('姓名:').strip()
    age = input('年龄:').strip()
    phone = input('手机号:').strip()
    if phone in phone_list:
        exit('该手机已注册。')
    id_num = input('身份证号:').strip()
    if id_num in id_num_list:
        exit('该身份证号已注册 。')

    coure_list = ['Python', 'Linux', '网络安全', '前端', '数据分析']
    for index, course in enumerate(coure_list):
        print(f'{index}.{course}')

    selected_course = input('选择想学的课:')
    if selected_course.isdigit():
        selected_course = int(selected_course)
        if selected_course >= 0 and selected_course < len(coure_list):
            picked_course = coure_list[selected_course]
        else:
            exit('不合法的选项...')
    else:
        exit('非法输入...')

    stu_data['name'] = name
    stu_data['age'] = age
    stu_data['phone'] = phone
    stu_data['id_num'] = id_num
    stu_data['course'] = picked_course

    return stu_data


def commit_to_db(filename, stu_data):
    """
    把学员数据，存到文件里
    :param filename:学员数据库文件
    :param stu_data:单个学员数据的dict
    :return:
    """
    f = open(filename, 'a')
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}"
    f.write(row)
    f.close()


def load_validated_data(filename):
    f = open(filename)
    phone_list = []
    id_num_list = []
    for line in f:
        line = line.split(',')
        phone = line[2]
        id_num = line[3]
        phone_list.append(phone)
        id_num_list.append(id_num)

    return phone_list, id_num_list


phone_list, id_num_list = load_validated_data(db_file)


sudent_data = register_api()
print(sudent_data)
commit_to_db(db_file, sudent_data)