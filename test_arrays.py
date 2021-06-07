import arrays


class TestSentenceReversePytest:
    def test_1(self):
        assert [2, 7] == arrays.sumFinder([2,7,11,15], 9)
    
    def test_2(self):
        assert [-3, 13] == arrays.sumFinder([-3, 0, 8, 9, 12, 13], 10)

    def test_3(self):
        assert [8, 9] == arrays.sumFinder([-3, 0, 8, 9, 12, 13], 17)
