def schedule(orders):
    ordered=sorted(orders,key=lambda x:(x["prep_time"],x["id"]))
    current=0; result=[]; wait=turn=0
    for o in ordered:
        start=current; finish=start+o["prep_time"]
        result.append({**o,"start":start,"completion":finish,"waiting":start,"turnaround":finish})
        wait+=start; turn+=finish; current=finish
    n=len(ordered)
    return result,{"total_time":current,"average_waiting_time":wait/n if n else 0,"average_turnaround_time":turn/n if n else 0}
