import codecs


def save_roles():
    """
    主要是为了人名.txt文件中的name 后面加上 词性nr
    :return:
    """
    name_path = r"./jinyong_novels_library/人名.txt"
    with codecs.open(name_path, 'r', 'utf-8') as f:
        name_list = f.readlines()
    names = ["{} nr".format(name.split("\r")[0]) for name in name_list]
    role_path = r"./jinyong_novels_library/roles.txt"
    with codecs.open(role_path, 'a+', 'utf-8') as f:
        for name in names:
            f.write(name + "\r\n")


if __name__ == '__main__':
    save_roles()