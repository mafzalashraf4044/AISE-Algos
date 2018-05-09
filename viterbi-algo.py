import pprint

states = ('Healthy', 'Fever')
end_state = 'E'
 
observations = ('normal', 'cold', 'dizzy')
 
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
 
transition_probability = {
   'Healthy' : {'Healthy': 0.69, 'Fever': 0.3, 'E': 0.01},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.59, 'E': 0.01},
   }
 
emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }

def forward(observations, states, initial_prob, transition_prob, emission_prob):

  viterbi = []
  backpointers = []
  viterbi_cur = {}
  viterbi_prev = {}
  final_prob = 0

  for i, state in enumerate(states):
    viterbi_cur[state] = initial_prob[state] * emission_prob[state][observations[0]]

  v = [viterbi_cur[curr_state] for curr_state in viterbi_cur]
  k = [curr_state for curr_state in viterbi_cur]
  backpointers.append(k[v.index(max(v))])

  viterbi.append(viterbi_cur)
  viterbi_prev = viterbi_cur
  viterbi_cur = {}

  for i, obs in enumerate(observations):
    if i >= 1:
      viterbi_cur = {}
      for i, state in enumerate(states):
        viterbi_cur[state] = max(viterbi_prev[prev_state] * transition_prob[prev_state][state] * emission_prob[state][obs] for prev_state in viterbi_prev)
        
      v = [viterbi_cur[curr_state] for curr_state in viterbi_cur]
      k = [curr_state for curr_state in viterbi_cur]
      backpointers.append(k[v.index(max(v))])

      viterbi.append(viterbi_cur)
      viterbi_prev = viterbi_cur

  final_prob = max(viterbi_prev[prev_state] * transition_prob[prev_state][end_state] for prev_state in viterbi_prev)

  return viterbi, final_prob, backpointers

viterbi, final_prob, backpointers = forward(observations, states, initial_prob, transition_prob, emission_prob)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(viterbi)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(backpointers)

print "Probability of given sequence: ", final_prob