
class LogMessage(object):

    @classmethod
    def get_ParamValue(self, _param):
        value = _param

        if _param is None:
            value = "None"

        return value

    @classmethod
    def set_Level(self, _pre_message, _level):
        prefix = ""

        for n in range(int(_level)):
            prefix += "..."

        if isinstance(_level, float):
            level_str = str(_level)
            level_part = level_str.split('.')[1]

            if int(level_part) > 2:
                raise ValueError("Decimal part is greates than 2")

            for n in range(int(level_part)):
                prefix += "."

        message = f"{prefix}{_pre_message}"

        return message

    @classmethod
    def get_Start(self, _args, _message, _level):
        qty = 0
        params_str = ""

        for param in _args:
            qty += 1

            value = self.get_ParamValue(param)

            if qty == len(_args):
                params_str += f"{value}"
            else:
                params_str += f"{value}, "

        pre_message = f"{_message} Params: ({params_str})"
        message = self.set_Level(pre_message, _level)

        return message

    @classmethod
    def get_End(self, _message, _level, _result):
        pre_message = f"{_message} {_result}"

        return self.set_Level(pre_message, _level)
