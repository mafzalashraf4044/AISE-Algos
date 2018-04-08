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

  return None

print forward(observations, states, initial_prob, transition_prob, emission_prob)