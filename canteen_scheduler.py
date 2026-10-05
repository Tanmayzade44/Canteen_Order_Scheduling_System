from algorithms.fcfs import schedule as fcfs
from algorithms.spt import schedule as spt
from algorithms.priority import schedule as priority
from utils.helpers import validate_orders,print_schedule
ORDERS=[{"id":"O1","name":"Thali","prep_time":12,"priority":2},{"id":"O2","name":"Sandwich","prep_time":5,"priority":1},{"id":"O3","name":"Dosa","prep_time":8,"priority":3},{"id":"O4","name":"Tea","prep_time":3,"priority":1}]
def show():
 print("\nCurrent Orders"); print("-"*52); print(f'{"ID":<8}{"Item":<18}{"Prep":<10}{"Priority":<10}')
 for o in ORDERS: print(f'{o["id"]:<8}{o["name"]:<18}{o["prep_time"]:<10}{o["priority"]:<10}')
def compare():
 print("\n"+"="*72); print("ALGORITHM COMPARISON"); print("="*72); print(f'{"Algorithm":<16}{"Avg Waiting":<18}{"Avg Turnaround":<20}{"Total Time":<12}'); print("-"*72)
 for name,fn in [("FCFS",fcfs),("SPT",spt),("Priority",priority)]:
  m=fn(ORDERS)[1]; print(f'{name:<16}{m["average_waiting_time"]:<18.2f}{m["average_turnaround_time"]:<20.2f}{m["total_time"]:<12}')
 print("-"*72)
def main():
 validate_orders(ORDERS)
 while True:
  print("\n"+"="*62); print("       CANTEEN ORDER SCHEDULING SYSTEM"); print("="*62); print("1. Show Orders\n2. FCFS Scheduling\n3. Shortest Processing Time (SPT)\n4. Priority Scheduling\n5. Compare Algorithms\n6. Exit")
  c=input("Enter choice: ").strip()
  if c=="1": show()
  elif c=="2": r,m=fcfs(ORDERS); print_schedule("FCFS SCHEDULING RESULT",r,m)
  elif c=="3": r,m=spt(ORDERS); print_schedule("SPT SCHEDULING RESULT",r,m)
  elif c=="4": r,m=priority(ORDERS); print_schedule("PRIORITY SCHEDULING RESULT",r,m)
  elif c=="5": compare()
  elif c=="6": print("Thank you. Exiting..."); break
  else: print("Invalid choice. Please enter 1-6.")
if __name__=="__main__": main()
