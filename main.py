

def find_activated(receptor_map, molecule):
    activated = []
    for ind, activated_by in enumerate(receptor_map):
        if molecule in activated_by:
            activated.append(ind)
    return activated
ALL_MOLECULE_NAMES = ("Benzyl Acetate", "Alpha-Ionone", "Ethyl maltol")
ALL_RECEPTOR_NAMES = ("OR", "V1R", "V2R", "TAAR", "FPR", "GC-D")
molecule_names = ALL_MOLECULE_NAMES
receptor_names = ALL_RECEPTOR_NAMES
mappings = [[] for i in range(len(molecule_names))]
for receptor in range(4):
    print(find_activated(mappings, receptor))
def activate(receptor_ind, *molecule_inds):
    currently_activated_by = mappings[receptor]
    for molecule_ind in molecule_inds:
        if molecule_ind in currently_activated_by:
            print(molecule_names[molecule_ind], "already activates", receptor_names[receptor_ind])

        