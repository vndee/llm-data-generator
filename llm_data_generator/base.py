import abc


class LLMDataGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self, num_samples: int):
        pass
