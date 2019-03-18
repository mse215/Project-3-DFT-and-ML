from pymatgen.io.vasp.inputs import Kpoints, Poscar, Potcar, Incar
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import sys
import os 
from shutil import copytree, copyfileobj, copy

dir_path = os.path.dirname(os.path.realpath(__file__))

user_directory = sys.argv[1]
user_structure = Structure.from_file(sys.argv[1] + "/POSCAR")
user_incar = Incar.from_file(sys.argv[1] + "/INCAR")
user_kpoints = Incar.from_file(sys.argv[1] + "/KPOINTS")

data_directory = "{}/fake_vasp_data".format(dir_path)

for path, dirs, files in os.walk(data_directory):
    for directory in dirs:
        INCAR = Incar.from_file(os.path.join(path, directory)+"/INCAR")
        structure = Structure.from_file(os.path.join(path, directory)+ "/POSCAR")
        KPOINTS = Incar.from_file(os.path.join(path, directory)+"/KPOINTS")
        
        if SpacegroupAnalyzer(user_structure).get_primitive_standard_structure() == SpacegroupAnalyzer(structure).get_primitive_standard_structure() and user_kpoints == KPOINTS and user_incar == INCAR:
            with open(os.path.join(path, directory)+"/output.txt", "r") as f:
                copyfileobj(f, sys.stdout)
            for subpath, subdirs, subfiles in os.walk(data_directory):
                for file in subfiles:
                    # Don't overwrite user's input files
                    if "INCAR" not in file and "POSCAR" not in file and "KPOINTS" not in file and "POTCAR" not in file:
                        copy(os.path.join(subpath, file), user_directory)
            exit()

print("No matching pre-computed data for the input files in specified directory were found. Please check your input files and try again.")
