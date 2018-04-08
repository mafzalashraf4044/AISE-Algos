states = ('Healthy', 'Fever')

end_state = 'E'
 
observations = ('normal', 'cold', 'dizzy')
 
initial_prob = {'Healthy': 0.6, 'Fever': 0.4}
 
transition_prob = {
   'Healthy' : {'Healthy': 0.69, 'Fever': 0.3, 'E': 0.01},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.59, 'E': 0.01},
   }
 
emission_prob = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }


def forward(observations, states, initial_prob, transition_prob, emission_prob):

  fwd = []
  fwd_cur = {}
  fwd_prev = {}

  for i, state in enumerate(states):
    fwd_cur[state] = initial_prob[state] * emission_prob[state]['normal']
  
  fwd.append(fwd_cur)
  fwd_prev = fwd_cur
  fwd_cur = {}

  return fwd

print forward(observations, states, initial_prob, transition_prob, emission_prob)