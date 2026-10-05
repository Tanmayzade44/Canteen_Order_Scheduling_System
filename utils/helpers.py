def validate_orders(orders):
    seen=set()
    for o in orders:
        if not {"id","name","prep_time","priority"}.issubset(o): raise ValueError("Invalid order")
        if o["id"] in seen: raise ValueError("Duplicate order ID")
        seen.add(o["id"])
        if o["prep_time"]<=0 or o["priority"]<1: raise ValueError("Invalid preparation time or priority")

def print_schedule(title,result,metrics):
    print("\n"+"="*62); print(title); print("="*62)
    print(f'{"Order":<8}{"Item":<18}{"Start":<8}{"Finish":<8}{"Wait":<8}')
    print("-"*62)
    for o in result: print(f'{o["id"]:<8}{o["name"]:<18}{o["start"]:<8}{o["completion"]:<8}{o["waiting"]:<8}')
    print("-"*62); print(f'Total preparation time : {metrics["total_time"]} min'); print(f'Average waiting time   : {metrics["average_waiting_time"]:.2f} min'); print(f'Average turnaround time : {metrics["average_turnaround_time"]:.2f} min')
