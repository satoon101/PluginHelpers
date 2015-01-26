from configobj import ConfigObj

from common.constants import CONFIG_FILE


class InterfaceSettings(ConfigObj):

    """"""

    def __init__(self):
        """"""
        super(InterfaceSettings, self).__init__(CONFIG_FILE)

    def register_setting(self, name, comment=''):
        """"""
        if name in self:
            return
        self[name] = None
        self.comments[name] = comment
        self.save()

settings = InterfaceSettings()
