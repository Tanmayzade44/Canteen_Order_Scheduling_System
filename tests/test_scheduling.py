import unittest
from algorithms.fcfs import schedule as fcfs
from algorithms.spt import schedule as spt
from algorithms.priority import schedule as priority
ORDERS=[{"id":"O1","name":"Thali","prep_time":12,"priority":2},{"id":"O2","name":"Sandwich","prep_time":5,"priority":1},{"id":"O3","name":"Dosa","prep_time":8,"priority":3},{"id":"O4","name":"Tea","prep_time":3,"priority":1}]
class TestScheduling(unittest.TestCase):
    def test_fcfs_order(self): self.assertEqual([x["id"] for x in fcfs(ORDERS)[0]],["O1","O2","O3","O4"])
    def test_spt_order_and_wait(self): self.assertEqual([x["id"] for x in spt(ORDERS)[0]],["O4","O2","O3","O1"]); self.assertAlmostEqual(spt(ORDERS)[1]["average_waiting_time"],6.75)
    def test_priority_order(self): self.assertEqual([x["id"] for x in priority(ORDERS)[0]],["O3","O1","O4","O2"])
if __name__=="__main__": unittest.main()
