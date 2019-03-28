from pymatgen.io.vasp.inputs import Kpoints, Poscar, Potcar, Incar
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.structure_matcher import StructureMatcher
import sys
import os 
from shutil import copytree, copyfileobj, copy

sm = StructureMatcher()
dir_path = os.path.dirname(os.path.realpath(__file__))

user_directory = sys.argv[1]
user_structure = Structure.from_file(sys.argv[1] + "/POSCAR")
user_incar = Incar.from_file(sys.argv[1] + "/INCAR")
user_kpoints = Incar.from_file(sys.argv[1] + "/KPOINTS")

data_directory = "{}/fake_vasp_data".format(dir_path)

structure_matched = False
KPOINTS_matched = None
INCAR_matched = None

for path, dirs, files in os.walk(data_directory):
    for directory in dirs:
        INCAR = Incar.from_file(os.path.join(path, directory)+"/INCAR")
        structure = Structure.from_file(os.path.join(path, directory)+ "/POSCAR")
        KPOINTS = Incar.from_file(os.path.join(path, directory)+"/KPOINTS")
        s1 = SpacegroupAnalyzer(user_structure).get_primitive_standard_structure()
        s2 = SpacegroupAnalyzer(structure).get_primitive_standard_structure()
#         print(user_incar)
#         print(INCAR)
        if  sm.fit(s1, s2) :
            structure_matched = True
#             print("structures match")
            if user_kpoints == KPOINTS:
                KPOINTS_matched = True
#                 print("KPOINTS match")
                if user_incar == INCAR:
                    INCAR_matched = True
#                     print("INCAR match")
                    with open(os.path.join(path, directory)+"/output.txt", "r") as f:
                        copyfileobj(f, sys.stdout)
                    for subpath, subdirs, subfiles in os.walk(os.path.join(path, directory)):
                        for file in subfiles:
                            # Don't overwrite user's input files
                            if "INCAR" not in file and "POSCAR" not in file and "KPOINTS" not in file and "POTCAR" not in file:
                                copy(os.path.join(subpath, file), user_directory)
                    exit()
error_string = """
No matching pre-computed data for the input files in directory '{}' were found:
    Problem with POSCAR? {}
    Problem with INCAR? {}
    Problem with KPOINTS? {}
Please check your input files and try again.
""".format(user_directory, (not structure_matched if structure_matched is not None else "Unknown"), (not INCAR_matched if INCAR_matched is not None else "Unknown"), (not KPOINTS_matched if KPOINTS_matched is not None else "Unknown"))
print(error_string)

