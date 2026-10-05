# Canteen Order Scheduling System

DAA Mini Project — Python 3

## Introduction
This project demonstrates algorithmic scheduling for a canteen preparation counter. It compares FCFS, Shortest Processing Time (SPT), and Priority Scheduling.

## Problem Statement
Several food orders may require different preparation times and priorities. A poor service order can increase customer waiting time. The system schedules orders and compares measurable performance.

## Objectives
- Model canteen orders with preparation time and priority.
- Implement FCFS, SPT and Priority Scheduling.
- Calculate waiting and turnaround times.
- Compare algorithm performance.
- Demonstrate correctness and complexity.

## Algorithm Design
**FCFS:** processes orders in input/arrival order.

**SPT:** sorts by ascending preparation time. Under the standard single-machine assumption with all jobs available initially, SPT minimizes average waiting time.

**Priority:** sorts by descending priority; ties use shorter preparation time and then order ID.

## Complexity
| Algorithm | Time | Extra Space |
|---|---|---|
| FCFS | O(n) | O(n) |
| SPT | O(n log n) | O(n) |
| Priority | O(n log n) | O(n) |

## Run
```bash
python canteen_scheduler.py
```
Tests:
```bash
python -m unittest discover -s tests -v
```

## Sample Data
O1 Thali 12 min priority 2; O2 Sandwich 5 min priority 1; O3 Dosa 8 min priority 3; O4 Tea 3 min priority 1.

## Repository Structure
```text
Canteen-Order-Scheduling-System/
├── canteen_scheduler.py
├── README.md
├── requirements.txt
├── algorithms/
│   ├── fcfs.py
│   ├── spt.py
│   └── priority.py
├── utils/helpers.py
├── tests/test_scheduling.py
├── docs/sample_output.txt
└── screenshots/
```

## GitHub
Suggested repository name: `Canteen-Order-Scheduling-System`.
```bash
git init
git add .
git commit -m "Add canteen order scheduling DAA mini project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Canteen-Order-Scheduling-System.git
git push -u origin main
```
