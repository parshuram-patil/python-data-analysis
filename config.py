import os


def get_value(var_name, default_value):
    if var_name in os.environ:
        env_value = os.environ.get(var_name)
        env_value = env_value.strip()
        if len(env_value) == 2 and env_value[0] == "\"" and env_value[1] == "\"":
            return None
        elif len(env_value) == 2 and env_value[0] == "'" and env_value[1] == "'":
            return None
        return env_value
    if default_value:
        return default_value
    return None


class Config:

    __ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    # Data files path
    IS_RUNNING_ON_CLOUD = True if (get_value('IS_RUNNING_ON_CLOUD', False) == 'True') else False
    if IS_RUNNING_ON_CLOUD:
        TITANIC_DATA_PATH = get_value('TITANIC_DATA_PATH', None)
        TITANIC_CSV_DATA_FILE = get_value('TITANIC_CSV_DATA_FILE', None)
        TITANIC_XLSX_DATA_FILE = get_value('TITANIC_XLSX_DATA_FILE', None)
        OUTPUT_PATH = get_value('OUTPUT_PATH', None)
    else:
        TITANIC_DATA_PATH = __ROOT_PATH + '/datasets/titanic/'
        TITANIC_CSV_DATA_FILE = TITANIC_DATA_PATH + 'titanic.csv'
        TITANIC_XLSX_DATA_FILE = TITANIC_DATA_PATH + 'titanic.xlsx'
        OUTPUT_PATH = __ROOT_PATH + '/outputs/'

