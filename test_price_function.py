import unittest

def calc_price_by_country(country, price_gbp, eur_rate):
  if country == "DE" or country == "ES":
    postage = 15
  elif country == "FR" or country == "IT":
    postage = 10
  new_price = (price_gbp + postage) * eur_rate
  if new_price > 149.00 and new_price < 200:
  new_price = 149.99

  return new_price



class Testcalcprice(unittest.TestCase):
    def test_blanks(self):
        self.assertEqual(calc_price_by_country("DE","99.99","1.3"), 149.49)
        self.assertEqual(calc_price_by_country("DE","99.99",1.3), 149.49)
        self.assertEqual(calc_price_by_country("DE",99.99,1.3), 149.49)
        self.assertEqual(calc_price_by_country("ES",99.99,1.3), 149.49)
        self.assertEqual(calc_price_by_country("ES","99.99",1.3), 149.49)
        self.assertEqual(calc_price_by_country("ES","99.99","1.3"), 149.49)
                
    def test_floats(self):
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5, 4.5]), 3)
        self.assertAlmostEqual(mean([1.1, 2.1, 3.1, 4.1]), 2.5, places=1)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5, places=1)

    def test_empty_list(self):
        self.assertRaises(ZeroDivisionError, mean, [])

    def test_one_element_list(self):
        self.assertEqual(mean([10]), 10)
        self.assertEqual(mean([-10]), -10)
        self.assertEqual(mean([0]), 0)

    def test_list_with_none_elements(self):
        self.assertRaises(TypeError, mean, [1, 2, None, 4, 5])
        self.assertRaises(TypeError, mean, [1, 2, 3, 4, None])
        self.assertRaises(TypeError, mean, [None, None, None])

    def test_with_alpha_chars(self):
        self.assertRaises(TypeError, mean, ["A", 1,0,5,6])
