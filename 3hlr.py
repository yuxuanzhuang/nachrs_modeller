# Comparative modeling by the AutoModel class
#
# Demonstrates how to build multi-chain models, and symmetry restraints
#
from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()

class MyModel(AutoModel):
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B', 'C', 'D', 'E'],
                             renumber_residues=[1, 1, 1, 1, 1])
env = Environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# be sure to change to MyModel
a = MyModel(env,
            alnfile  = 'fivechain.ali' ,     # alignment filename
            knowns   = '6pv7_cleaned',              # codes of the templates
            sequence = '3hlr')              # code of the target

a.starting_model= 1                # index of the first model
a.ending_model  = 1                # index of the last model
                                   # (determines how many models to calculate)
a.make()                           # do comparative modeling
