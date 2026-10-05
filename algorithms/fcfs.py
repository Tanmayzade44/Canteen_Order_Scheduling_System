def schedule(orders):
    current=0; result=[]; wait=turn=0
    for o in orders:
        start=current; finish=start+o["prep_time"]
        result.append({**o,"start":start,"completion":finish,"waiting":start,"turnaround":finish})
        wait+=start; turn+=finish; current=finish
    n=len(orders)
    return result,{"total_time":current,"average_waiting_time":wait/n if n else 0,"average_turnaround_time":turn/n if n else 0}
