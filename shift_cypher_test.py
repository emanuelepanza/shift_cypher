def test_encode():
  assert encode("He llo", 1) == "If mmp"
  assert encode("He llo, 20!", 7) == "Ol ssv, 20!"
  assert encode("emaNuElE", 26) == "emaNuElE"
  print("All tests passed!")

def test_decode():
  assert decode(encode("He llo", 1), 1) == "He llo"
  assert decode(encode("He llo, 20!", 7), 7) == "He llo, 20!"
  assert decode(encode("emaNuElE", 26), 26) == "emaNuElE"
  print("All tests passed!")

def run_tests():
  test_encode()
  test_decode()

run_tests()
