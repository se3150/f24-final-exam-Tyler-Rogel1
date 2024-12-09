import pytest #type: ignore
from brute import Brute
from unittest.mock import Mock
todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        # write your test cases here
        def it_returns_true_on_match():
            cracker = Brute("TEST")
            assert cracker.bruteOnce("TEST")

        def it_returns_false_on_mismatch():
            cracker = Brute("TEST")
            assert not cracker.bruteOnce("WRONG")
        
        def it_returns_false_on_empty_string():
            cracker = Brute("TEST")
            assert not cracker.bruteOnce("")


    def describe_bruteMany():
        # write your test cases here
        def it_returns_positive_time_on_match():
            cracker = Brute("TEST")
            mock_guess = Mock()
            mock_guess.return_value = "TEST"
            cracker.randomGuess = mock_guess
            assert cracker.bruteMany() > 0
        
        def it_returns_negative_one_on_mismatch():
            cracker = Brute("TEST")
            mock_guess = Mock()
            mock_guess.return_value = "WRONG"
            cracker.randomGuess = mock_guess
            assert cracker.bruteMany(100) == -1
        
        def it_returns_negative_one_on_empty_string():
            cracker = Brute("TEST")
            mock_guess = Mock()
            mock_guess.return_value = ""
            cracker.randomGuess = mock_guess
            assert cracker.bruteMany(100) == -1