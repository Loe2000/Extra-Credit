import sentence

class TestSentenceReversePytest:
    def test_1(self):
        assert "world hello" == sentence.reverse("hello world")
    
    def test_2(self):
        assert  "cool and nice very wow" == sentence.reverse("wow very nice and cool")
