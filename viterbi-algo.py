import pprint

states = ('A+', 'A', 'B', 'C', 'D', 'E', 'F')

end_state = 'END'
 
observations = ('<2', '<4', '>=6')
# observations = ('>=6', '>=6', '>=6')
 
initial_prob = {'A+': 0.12, 'A': 0.24, 'B': 0.28, 'C': 0.2, 'D': 0.04, 'E': 0.04, 'F': 0.08}
 
transition_prob = {
  'A+' : {'A+': 0.38, 'A': 0.26, 'B': 0.18, 'C': 0.08, 'D': 0.04, 'E': 0.03, 'F': 0.02, 'END': 0.01},
  'A' : {'A+': 0.15, 'A': 0.3, 'B': 0.2, 'C': 0.15, 'D': 0.1, 'E': 0.05, 'F': 0.03, 'END': 0.02},
  'B' : {'A+': 0.11, 'A': 0.17, 'B': 0.32, 'C': 0.2, 'D': 0.12, 'E': 0.03, 'F': 0.03, 'END': 0.02},
  'C' : {'A+': 0.08, 'A': 0.11, 'B': 0.2, 'C': 0.28, 'D': 0.15, 'E': 0.1, 'F': 0.04, 'END': 0.04},
  'D' : {'A+': 0.06, 'A': 0.1, 'B': 0.12, 'C': 0.2, 'D': 0.24, 'E': 0.14, 'F': 0.1, 'END': 0.04},
  'E' : {'A+': 0.02, 'A': 0.04, 'B': 0.06, 'C': 0.12, 'D': 0.18, 'E': 0.28, 'F': 0.22, 'END': 0.08},
  'F' : {'A+': 0.01, 'A': 0.02, 'B': 0.04, 'C': 0.1, 'D': 0.15, 'E': 0.28, 'F': 0.32, 'END': 0.08},
}
 
emission_prob = {
  'A+' : {'<1': 0.02, '<2': 0.06, '<4': 0.18, '<6': 0.32, '>=6': 0.42},
  'A' : {'<1': 0.02, '<2': 0.06, '<4': 0.2, '<6': 0.34, '>=6': 0.36},
  'B' : {'<1': 0.02, '<2': 0.07, '<4': 0.25, '<6': 0.34, '>=6': 0.32},
  'C' : {'<1': 0.04, '<2': 0.06, '<4': 0.38, '<6': 0.3, '>=6': 0.22},
  'D' : {'<1': 0.24, '<2': 0.3, '<4': 0.28, '<6': 0.1, '>=6': 0.08},
  'E' : {'<1': 0.28, '<2': 0.36, '<4': 0.22, '<6': 0.08, '>=6': 0.06},
  'F' : {'<1': 0.36, '<2': 0.26, '<4': 0.22, '<6': 0.04, '>=6': 0.02},
}

def max_key_of_dic(dictionary):
  v = [dictionary[key] for key in dictionary]
  k = [key for key in dictionary]
  return k[v.index(max(v))]

def forward(observations, states, initial_prob, transition_prob, emission_prob):

  viterbi = []
  backpointers = []
  viterbi_cur = {}
  viterbi_prev = {}
  final_prob = 0

  for i, state in enumerate(states):
    viterbi_cur[state] = initial_prob[state] * emission_prob[state][observations[0]]

  backpointers.append(max_key_of_dic(viterbi_cur))
  viterbi.append(viterbi_cur)
  viterbi_prev = viterbi_cur
  viterbi_cur = {}

  for i, obs in enumerate(observations):
    if i >= 1:
      viterbi_cur = {}
      for i, state in enumerate(states):
        viterbi_cur[state] = max(viterbi_prev[prev_state] * transition_prob[prev_state][state] * emission_prob[state][obs] for prev_state in viterbi_prev)
        
      backpointers.append(max_key_of_dic(viterbi_cur))
      viterbi.append(viterbi_cur)
      viterbi_prev = viterbi_cur

  final_prob = max(viterbi_prev[prev_state] * transition_prob[prev_state][end_state] for prev_state in viterbi_prev)

  return viterbi, final_prob, backpointers

viterbi, final_prob, backpointers = forward(observations, states, initial_prob, transition_prob, emission_prob)

print "Trellis: "

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(viterbi)

print "Backpointers: "

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(backpointers)

print "Max probability of given sequence: ", final_prob