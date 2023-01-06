
puzzle.process_polymer(4)
x=np.array(list(puzzle.polymer))
unique,frequency = np.unique(x, return_counts = True)
z=zip(unique,frequency)
# ~ print(z)
# ~ print(unique, frequency)
# ~ print(tuple(z))


#foo = {key: value for key, value in list(z)}
foo = {key: value for key, value in z}
print(f'+++DEBUG: foo: {foo}')



    # ~ def process_polymer(self, input_polymer=None):
        # ~ """ expands polymner using the insertion rules """

        # ~ if input_polymer is None:
            # ~ update_instance_polymer = True
            # ~ if self.polymer == '':
                # ~ p = self.polymer_template
            # ~ else:
                # ~ p = self.polymer
        # ~ else:
            # ~ p=input_polymer

        # ~ #--build the pairs to process in this step
        # ~ polymer_pairs = []
        # ~ for r in range(0,len(p)-1):
            # ~ polymer_pairs.append(f'{p[r]}{p[r+1]}')

        # ~ #--process the pairs
        # ~ new_p = ''
        # ~ for pair in polymer_pairs:
            # ~ new_p +=  f'{pair[0]}{self.insertion_rules[pair]}'
        # ~ #--add the last element back to the chain
        # ~ new_p += polymer_pairs[-1][1]

        # ~ #--update self.polymer if no input was given
        # ~ if update_instance_polymer:
            # ~ self.polymer = new_p
        # ~ return new_p
        
        # ~ def run_polymerization_chain (self,num_cycles=1):
        # ~ """ Calls the process_polymer function num_cycles times """

        # ~ for i in range(num_cycles):
            # ~ p = self.process_polymer()

