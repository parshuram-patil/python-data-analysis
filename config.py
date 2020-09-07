import os


def get_value(var_name, default_value):
    if var_name in os.environ:
        env_value = os.environ.get(var_name)
        env_value = env_value.strip()
        if len(env_value) == 2 and env_value[0] is "\"" and env_value[1] is "\"":
            return None
        elif len(env_value) == 2 and env_value[0] is "'" and env_value[1] is "'":
            return None
        return env_value
    if default_value:
        return default_value
    return None


class Config:

    __ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    # Data files path
    __TITANIC_DATA_PATH = get_value('TITANIC_DATA_PATH', __ROOT_PATH + '/datasets/titanic/')
    TITANIC_CSV_DATA_FILE = __TITANIC_DATA_PATH + 'titanic.csv'
    TITANIC_XLSX_DATA_FILE = __TITANIC_DATA_PATH + 'titanic.xlsx'

    OUTPUT_PATH = get_value('OUTPUT_PATH', __ROOT_PATH + '/outputs/')

