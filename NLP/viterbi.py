states = ("N", "V", "Adj")

# observations
obs = ("coffee", "takes", "free")

# start_probability
sp = {
    "N": 0.33, "V": 0.33, "Adj": 0.33
}

# transition_probability
tp = {
    "N" : {"N": 0.4, "V": 0.5, "Adj": 0.1},
    "V" : {"N": 0.4, "V": 0.1, "Adj": 0.2},
    "Adj" : {"N": 0.5, "V": 0.2, "Adj": 0.3}
}
# emission_probability
ep = {
    "N" : {"coffee": 0.3, "takes": 0.3, "free": 0.4},
    "V" : {"coffee": 0.2, "takes": 0.4, "free": 0.4},
    "Adj" : {"coffee": 0.5, "takes": 0.1, "free": 0.4}
}

def viterbi(obs, states, sp, tp, ep):
    # T = {path to current position, probability up to the current path}
    # at position t
    T = {}
    for output in obs:
        if output == "coffee":
            for state in states:
                T[state] = ([state], sp[state]*ep[state]["coffee"])
            continue
        # U = {path to current position, probability up to the current path}
        # at position t+1
        U = {}
        for next_state in states:
            # argmax = record of the local best path
            argmax = None
            # valmax = the highest probability to the simbol
            valmax = 0
            # source_state is current state
            for source_state in states:
                (v_path, v_prob) = T[source_state]
                p = ep[next_state][output] * tp[source_state][next_state]
                v_prob *= p
                # if v_prob > valmax, update record
                if v_prob > valmax:
                    argmax = v_path + [next_state]
                    valmax = v_prob
            U[next_state] = (argmax, valmax)
        T = U

    highest_prob = 0
    order = None
    for state in states:
        if T[state][1] > highest_prob:
            highest_prob = T[state][1]
            order = T[state][0]
    return highest_prob, order

a, b = viterbi(obs, states, sp, tp, ep)
print(a, b)