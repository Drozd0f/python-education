"""Python - advanced: Iterables"""
import re
import typing as t
import unittest


class MultipleSentencesError(Exception):
    """This class describes the multiple sentences error"""
    def __init__(self, string: t.Optional[str] = None):
        self._string = string
        super().__init__()

    def __str__(self):
        if self._string is None:
            return 'String contains more than one sentence'
        return f'String \'{self._string}\' contains more than one sentence'


class SentenceIterator:
    """This class describes work sentence iterator"""
    def __init__(self, words):
        self._words = words

    def gen_words(self) -> str:
        """This method returns the next word in sentence"""
        return next(self._words)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        return self.gen_words()


class Sentence:
    """This class is a sentence container"""
    def __init__(self, string: str):
        if not isinstance(string, str):
            raise TypeError(f'{string} is not str')
        if len(re.findall(r'([.]{1,3}|[!?])', string)) > 1:
            raise MultipleSentencesError(string)
        if not re.match(r'^[\w+\s,-]+([.]|[.]{3}|[!?])$', string):
            raise ValueError(f'\'{string}\' does not end with . ... ! or ?')
        self._string = string

    def __repr__(self) -> str:
        return f'<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>'

    def __getitem__(self, index: t.Union[int, slice]):
        if isinstance(index, int):
            if index < 0 or index > len(self.words):
                raise IndexError
            return self.words[index]
        return ' '.join(self.words[index.start:index.stop:index.step])

    def __iter__(self):
        return SentenceIterator(self._words())

    def _words(self):
        return (word for word in re.findall(r'\w+', self._string))

    @property
    def words(self) -> list:
        """This method returns a list of words"""
        return list(self._words())

    @property
    def other_chars(self) -> list:
        """This method returns a list of not words"""
        return re.findall(r'\W', self._string)


class TestSentence(unittest.TestCase):
    """This class describes testing class Sentence"""
    text = 'Hello brave, new world!'
    sentence = Sentence(text)

    def test_invalid_end_text(self):
        """
        This test describes the behavior of a Sentence when one of
        the following characters (. ... ! ?) is missing at the end of a sentence
        """
        with self.assertRaises(ValueError):
            Sentence('Hello brave, new world')

        with self.assertRaises(ValueError):
            Sentence('Hello brave, new world..')

        with self.assertRaises(ValueError):
            Sentence('Hello brave, new world,')

    def test_multiple_sentences(self):
        """This test describes the behavior of a Sentence when there is more than one sentence"""
        with self.assertRaises(MultipleSentencesError):
            Sentence(self.text * 2)

    def test_type_error_string(self):
        """
        This test describes the behavior of the Sentence
        when the string data type is incorrect
        """
        not_str = (1, 1.5, {}, (), [], None)
        for text in not_str:
            with self.assertRaises(TypeError):
                Sentence(text)

    def test_success(self):
        """This test describes the behavior of a Sentence when a string is correctly entered."""
        sentence = Sentence(self.text[:-1] + '.')
        assert isinstance(sentence, Sentence)
        sentence = Sentence(self.text[:-1] + '...')
        assert isinstance(sentence, Sentence)
        sentence = Sentence(self.text)
        assert isinstance(sentence, Sentence)
        sentence = Sentence(self.text[:-1] + '?')
        assert isinstance(sentence, Sentence)

    def test_method_words(self):
        """This test checks the method words of a Sentence"""
        assert self.sentence.words == ['Hello', 'brave', 'new', 'world']

    def test_method_other_chars(self):
        """This test checks the method other_chars of a Sentence"""
        assert self.sentence.other_chars == [' ', ',', ' ', ' ', '!']

    def test_repr(self):
        """This test checks the method __repr__ of a Sentence"""
        assert repr(self.sentence) == '<Sentence(words=4, other_chars=5)>'

    def test_index(self):
        """This test checks the ability of a Sentence to return a word by index"""
        assert self.sentence[0] == 'Hello'
        assert self.sentence[1] == 'brave'
        assert self.sentence[2] == 'new'
        assert self.sentence[3] == 'world'

    def test_slice(self):
        """This test checks the ability of a Sentence to return a word by slice"""
        assert self.sentence[:] == 'Hello brave new world'
        assert self.sentence[2:] == 'new world'
        assert self.sentence[:2:] == 'Hello brave'
        assert self.sentence[::3] == 'Hello world'
        assert self.sentence[::-1] == 'world new brave Hello'
        assert self.sentence[1::-1] == 'brave Hello'
        assert self.sentence[4:] == ''
        assert self.sentence[-4::-1] == 'Hello'

    def test_loop_for(self):
        """This test checks if a class can be used in a loop"""
        test_words = ['Hello', 'brave', 'new', 'world']
        for idx, word in enumerate(self.sentence):
            assert word == test_words[idx]

    def test_iter(self):
        """
        This test checks if the iter() function will return a SentenceIterator
        when passed as an argument to it Sentence
        """
        assert isinstance(iter(self.sentence), SentenceIterator)


if __name__ == '__main__':
    unittest.main()
