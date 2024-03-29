import rdkit
# Making a list of atoms
atom_type_lst = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

# Making a list of all bonds supported bu rdkit
bond_types_lst = [rdkit.Chem.rdchem.BondType.SINGLE, rdkit.Chem.rdchem.BondType.DOUBLE,
                    rdkit.Chem.rdchem.BondType.TRIPLE, rdkit.Chem.rdchem.BondType.AROMATIC]

def chemis(mol_lst, atom_type_lst = atom_type_lst, bond_types_lst = bond_types_lst, method = 1):
  from copy import deepcopy
  import rdkit
  from rdkit import Chem


  final_lst, all_lst = [], [] # Declaring variables which will store the data generated inside the for-loop to be used outside the for-loop
  for mol in mol_lst: # The bigining of the for-loop

    # Collecting the data for each molecule
    Main_Atom_Index, End_Atom_Index, Bond_Type, Atom_Valence, Symbol = [],[],[],[],[]

    for bond in mol.GetBonds():
      Main_Atom_Index.append(bond.GetBeginAtomIdx()) # Main_Atom_Index: returns the index of the current atom. e.g: [0, 1, 2]
      End_Atom_Index.append(bond.GetEndAtomIdx()) # End_Atom_Index: returns the index of the atom connected to the current atom. e.g: [1, 2, 3]
      Bond_Type.append(bond.GetBondType()) # Bond_Type: returns the bond type. e.g: [rdkit.Chem.rdchem.BondType.SINGLE, rdkit.Chem.rdchem.BondType.SINGLE, rdkit.Chem.rdchem.BondType.SINGLE]

    for atom in mol.GetAtoms():
      Symbol.append(atom.GetSymbol()) # Symbol: returns the symbol of the current atom. e.g: ['C', 'C', 'C', 'C']
      Atom_Valence.append(atom.GetTotalValence()) # Atom_Valence: returns number of bonds an element can have. e.g: [4, 4, 4, 4]
    #_______________________________________________________
    # It makes a list for the each connection between the atoms. e.g: [[0, 1], [1, 2], [2, 3]]
    Conn_lst = []
    for i in range(len(Main_Atom_Index)):
      Temp_var = [Main_Atom_Index[i], End_Atom_Index[i]]
      Conn_lst.append(Temp_var)
    Conn_lst.sort()
    #_______________________________________________________
    # This basicaly makes a nested list where the index is the main atom and the what is inside the list is what is connected to the main atom. e.g: [[1], [2, 0], [3, 1], [2]]
    Basic_conn = []
    for i in range(len(Conn_lst)):
      temp_lst = []
      if i < len(Conn_lst)-1:
        Temp_var = i
        while Main_Atom_Index[Temp_var] == Main_Atom_Index[Temp_var+1]:
          if End_Atom_Index[Temp_var] not in temp_lst:
            temp_lst.append(End_Atom_Index[Temp_var])
            temp_lst.append(End_Atom_Index[Temp_var+1])
            Temp_var+=1
          else:
            if Main_Atom_Index[Temp_var] not in temp_lst:
              temp_lst.append(End_Atom_Index[Temp_var+1])
            Temp_var+=1
          Basic_conn.append(temp_lst)

        else:
          if len(Basic_conn) == 0:
            temp_lst.append(End_Atom_Index[Temp_var])
            Basic_conn.append(temp_lst)
          if End_Atom_Index[Temp_var] not in Basic_conn[-1]:
            temp_lst.append(End_Atom_Index[Temp_var])
            Basic_conn.append(temp_lst)

      if i == len(Conn_lst)-1:
        if End_Atom_Index[i] not in Basic_conn[-1]:
          Basic_conn.append([End_Atom_Index[i]])

    All_conn = deepcopy(Basic_conn)

    for index in range(len(Basic_conn)):
      for val in range(len(Basic_conn)):
        if index in Basic_conn[val]:
          All_conn[index].append(val)

    for i in range(len(End_Atom_Index)):
      if End_Atom_Index[i] not in Main_Atom_Index:
        All_conn.append([Main_Atom_Index[i]])
    #_______________________________________________________
    #This code makes a list of each connection and the type of bond they have.
    udata= []
    for i in range(len(Main_Atom_Index)):
      Temp_lst = [Main_Atom_Index[i] ,End_Atom_Index[i], Bond_Type[i]]
      udata.append(Temp_lst)
      if i == len(Main_Atom_Index)-1:
        Temp_lst = [End_Atom_Index[i] ,Main_Atom_Index[i], Bond_Type[i]]
        udata.append(Temp_lst)
    #the above part makes this [[0, 1, rdkit.Chem.rdchem.BondType.SINGLE], [1, 2, rdkit.Chem.rdchem.BondType.SINGLE], [2, 1, rdkit.Chem.rdchem.BondType.SINGLE]]
    #but it still does not have all the connections. So
    udata.sort()
    udata_copy = deepcopy(udata)
    for i in range(len(All_conn)):
      for o in All_conn[i]:
        Temp_var, Temp_lst1 = 0, []
        for p in range(len(udata_copy)):
          if i == udata[p][0]:
            Temp_var+=1
            Temp_lst1.append(udata_copy[p][1])
        if Temp_var != len(All_conn[i]):
          if o not in Temp_lst1:
            for p in range(len(udata_copy)):
              if o == udata_copy[p][0]:
                if i == udata_copy[p][1]:
                  Temp_lst2 = [i ,o, udata_copy[p][2]]
                  udata.append(Temp_lst2)
    udata.sort()
    #The above part adds those connections from All_conn list Ex:[[1], [2, 0], [1]] and does some magic and produces this
    #[[0, 1, rdkit.Chem.rdchem.BondType.SINGLE], [1, 0, rdkit.Chem.rdchem.BondType(1)], [1, 2, rdkit.Chem.rdchem.BondType.SINGLE], [2, 1, rdkit.Chem.rdchem.BondType.SINGLE]]
    #______________________________________________________
    #making a list that contains the atoms that are connected to the main atom (which is the index of the list) and what type of bond they are conneted in.
    #[[[1], [], [], []], [[0, 2], [], [], []], [[1], [], [], []]]
    #the 0 index in index 0 from the whole list is Single bond, 1 is Double bond, 2 is Triple bond, 3 is Aromatic.
    #You are the one that chooses what types of bonds are available and at what order by customising the (bond_types_lst) list present at the very top. :)
    bnd_lst_ = []
    for i in range(len(All_conn)):
      bnd_lst = []
      for o in range(len(bond_types_lst)):
        Temp_lst = []
        for p in range(len(udata)):
          if udata[p][0] == i:
            if udata[p][2] == bond_types_lst[o]:
              Temp_lst.append(udata[p][1])
        bnd_lst.append(Temp_lst)
      bnd_lst_.append(bnd_lst)
    #______________________________________________________
    #this code converts the connected atom into their symbol in the molecule. [[['C'], [], [], []], [['C', 'C'], [], [], []], [['C', 'C'],
    sym_lst = deepcopy(bnd_lst_)
    for i in range(len(bnd_lst_)):
      for o in range(len(bnd_lst_[i])):
        Temp_lst = []
        if bnd_lst_[i][o] != []:
          for p in range(len(bnd_lst_[i][o])):
            Temp_lst.append(Symbol[bnd_lst_[i][o][p]])
          sym_lst[i][o] = Temp_lst
    #______________________________________________________
    #this code the symbols into their index list, were we add all the atoms indexes for atoms connected in the same bond type, and make a index list of 0's
    #indicating that no atoms are connected in this type of bond.
    for i in range(len(bnd_lst_)):
      for o in range(len(bnd_lst_[i])):
        Temp_lst = []
        if bnd_lst_[i][o] != []:
          Temp_lst = (sin_mol(sym_lst[i][o], atom_type_lst))
          if len(Temp_lst) == 1:
            sym_lst[i][o] = Temp_lst[0]
          else:
            Temp_var1 = []
            for p in range(len(Temp_lst[0])):
              Temp_var2 = 0
              for l in Temp_lst:
                Temp_var2+= l[p]
              Temp_var1.append(Temp_var2)
            sym_lst[i][o] = Temp_var1
        else:
          Temp_lst = []
          for m in range(len(atom_type_lst)):
            Temp_lst.append(0)
          sym_lst[i][o] = Temp_lst
    #______________________________________________________
    #Adding each main atom with the connected atoms in their respective bond placement in a list.
    all_lst_sublst = []
    M_atom = sin_mol(Symbol, atom_type_lst)
    for i in range(len(M_atom)):
      Temp_lst1, Temp_lst2 = [], []
      for o in range(len(sym_lst[i])):
        Temp_lst1.append(sym_lst[i][o])
      for p in Temp_lst1:
        for l in p:
          Temp_lst2.append(l)
      all_lst_sublst.append(M_atom[i] + Temp_lst2)
    all_lst.append(all_lst_sublst)
  #_______________________________________________________
  # Making a list of all unique indexs. e.g: [[3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0]]
  unique_lst = []
  for o in range(len(all_lst)):
    for i in all_lst[o]:
      if i not in unique_lst:
        unique_lst.append(i)
  #_______________________________________________________
  # Making a list that has the unique index in the form of its index+1 e.g:[[1, 2, 1, 0, 0, 0], [3, 4, 5, 6, 7, 0], [8, 9, 1, 0, 0, 0], [10, 10, 10, 10, 10, 10]]
  # For every item in all_lst. This is done so that the sequance of the atoms in a molecule is not changes which is done in the second method.
  if method == 1:
    for i in all_lst:
      final_sublst = []
      for z in i:
        Temp_var = 0
        for p in unique_lst:
          Temp_var+=1

          if p == z:
            final_sublst.append(Temp_var)
            break
      final_lst.append(final_sublst)
    Temp_lst = []
    for i in final_lst:
      Temp_lst.append(len(i))
    Temp_var = max(Temp_lst)

    for i in range(len(final_lst)):
      while len(final_lst[i]) < Temp_var:
        final_lst[i].append(0)
  # The seocond method makes a list and just shows you how many atom and its connetions are present in a sertine format. [[2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
  # The inxed of the list represents they type of atom and its connetions which has the same index in unique_lst.
  else:
    for i in all_lst:
      final_sublst = []
      for z in unique_lst:
        Temp_var = 0
        if z in i:
          for o in i:
            if o == z:
              Temp_var+=1
          final_sublst.append(Temp_var)
        else:
          final_sublst.append(0)
      final_lst.append(final_sublst)
  return final_lst
