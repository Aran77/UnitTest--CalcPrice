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
        self.assertEqual(calc_price_by_country("IT",99.99,1.3), 149.49)
        self.assertEqual(calc_price_by_country("IT","99.99",1.3), 149.49)
        self.assertEqual(calc_price_by_country("IT","99.99","1.3"), 149.49)
        self.assertEqual(calc_price_by_country("",99.99,1.3), 149.49)
        self.assertEqual(calc_price_by_country("","99.99",1.3), 149.49)
        self.assertEqual(calc_price_by_country("","99.99","1.3"), 149.49)
            
          
    
