from itertools import permutations

engineers = ['Amit', 'Bhavna', 'Charan', 'Deepa', 'Ekta']
departments = ['AI', 'Backend', 'Cloud', 'Data', 'Embedded']
rooms = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']
topics = ['Security', 'Performance', 'Reliability', 'Scalability', 'Usability']
times = ['10am', '11am', '12pm', '1pm', '2pm']

def satisfies_constraints(schedule):
    eng_index = {e[0]: i for i, e in enumerate(schedule)}
    dept_index = {e[1]: i for i, e in enumerate(schedule)}
    room_index = {e[2]: i for i, e in enumerate(schedule)}
    topic_index = {e[3]: i for i, e in enumerate(schedule)}

    if not (0 <= eng_index['Charan'] < 4 and eng_index['Charan'] + 1 == topic_index['Scalability']):
        return False
    if schedule[dept_index['Backend']][2] != 'Gamma':
        return False
    if schedule[dept_index['AI']][4] != '11am':
        return False
    if schedule[eng_index['Deepa']][3] != 'Performance':
        return False
    if schedule[eng_index['Deepa']][2] == 'Alpha':
        return False
    if schedule[eng_index['Deepa']][4] == '10am':
        return False
    if schedule[room_index['Delta']][3] != 'Usability':
        return False
    if eng_index['Ekta'] >= room_index['Delta']:
        return False
    if schedule[eng_index['Bhavna']][2] != 'Alpha':
        return False
    if not (0 <= eng_index['Amit'] < 4 and dept_index['Data'] == eng_index['Amit'] + 1):
        return False
    if schedule[dept_index['Embedded']][4] != '10am':
        return False
    if not (0 <= topic_index['Security'] < 4 and topic_index['Security'] + 1 == dept_index['Cloud']):
        return False
    if schedule[room_index['Epsilon']][4] != '1pm':
        return False
    return True

for engs in permutations(engineers):
    for depts in permutations(departments):
        for rms in permutations(rooms):
            for tpcs in permutations(topics):
                for tms in permutations(times):
                    schedule = list(zip(engs, depts, rms, tpcs, tms))
                    if satisfies_constraints(schedule):
                        for entry in schedule:
                            print(entry)
                        exit()
