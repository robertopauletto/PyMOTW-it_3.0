# abc_abc_base.py
import abc


class PluginBase(abc.ABC):

    @abc.abstractmethod
    def load(self, input):
        """Ottiene i dati dalla sorgente in pinput
        e ritona un oggetto
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Salva l'oggetto dati verso l'output."""


class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Sottoclasse:', issubclass(SubclassImplementation,
                                  PluginBase))
    print('Istanza:', isinstance(SubclassImplementation(),
                                  PluginBase))
