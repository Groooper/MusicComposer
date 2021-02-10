def init(layers, inputcount, outputcount, epochs, check_from_examples):
    """
    Инициализация начальных переменных и создание по ним нейронной сети
    :param layers: кол-во скрытых слоёв
    :param inputcount: кол-во клеток во входном слое
    :param outputcount: кол-во клеток в выходном слое
    :param epochs: эпох обучения
    :param check_from_examples: между 0 и 1 - процент контрольных примеров
    :return: Nothing
    """
    pass


def chooseExamples(path):
    """
    Выбор папки с примерами - MIDI-файлами
    :param path: путь до папки с обучающими примерами
    """
    pass


def readExamples():
    """
    #какие ещё параметры читает?
    читает примеры из указанной раннее папки и возвращает словарь examples
    :return: словарь examples, содержащий ноты, длительности, громкость
    """
    pass


layers, inputcount, outputcount, epochs, check_from_examples = 0
path = ""
examples = {}

init(layers, inputcount, outputcount, epochs, check_from_examples)
chooseExamples(path)
examples = readExamples()
