from ase.data import covalent_radii, atomic_numbers, atomic_masses
from ase.geometry.geometry import _row_col_from_pdist
from ase.geometry import find_mic
from ase.formula import Formula
from itertools import product, permutations, combinations
from collections import abc
import networkx as nx
import numpy as np
import scipy
import math


def neighbor_shell_list(atoms, dx=0.3, neighbor_number=1, 
                        different_species=False, mic=False,
                        radius=None, span=False):
    """Make dict of neighboring shell atoms for both periodic and 
    non-periodic systems. Possible to return neighbors from defined 
    neighbor shell e.g. 1st, 2nd, 3rd by changing the neighbor number.

    Parameters
    ----------
    atoms : ase.Atoms object
        Accept any ase.Atoms object. No need to be built-in.

    dx : float, default 0.3
        Buffer to calculate nearest neighbor pairs.

    neighbor_number : int, default 1
        Neighbor shell number.

    different_species : boolean, default False
        Whether each neighbor pair are different species.

    mic : boolean, default False
        Whether to apply minimum image convention. Remember to set 
        mic=True for periodic systems.

    radius : float, default None 
        The radius of each shell. Works exactly as a conventional 
        neighbor list when specified. If not specified, use covalent 
        radii instead.

    span : boolean, default False
        Whether to include all neighbors spanned within the shell.

    """

    natoms = len(atoms)
    if natoms == 1:
        return {0: []}
    cell = atoms.cell
    positions = atoms.positions
    
    nums = set(atoms.numbers)
    pairs = product(nums, nums)
    res = np.asarray(list(permutations(np.asarray(range(natoms)),2)))    
    indices1, indices2 = res[:,0], res[:,1]
    p1, p2 = positions[indices1], positions[indices2]

    if mic:
        _, distances = find_mic(p2 - p1, cell, pbc=True)
    else:
        distances = np.linalg.norm(p2 - p1, axis=1)
    ds = np.insert(distances, np.arange(0, distances.size, natoms), 0.)

    if not radius:
        cr_dict = {(i, j): (covalent_radii[i]+covalent_radii[j]) for i, j in pairs}
    
    conn = {k: [] for k in range(natoms)}
    for atomi in atoms:
        for atomj in atoms:
            i, j = atomi.index, atomj.index
            if i != j:
                if not (different_species & (atomi.symbol == atomj.symbol)):
                    d = ds[i*natoms:(i+1)*natoms][j]
                    crij = 2 * radius if radius else cr_dict[(atomi.number, atomj.number)] 

                    if neighbor_number == 1 or span:
                        d_max1 = 0.
                    else:
                        d_max1 = (neighbor_number - 1) * crij + dx

                    d_max2 = neighbor_number * crij + dx

                    if d > d_max1 and d < d_max2:
                        conn[atomi.index].append(atomj.index)

    return conn


def get_connectivity_matrix(neighborlist):
    """Returns a connectivity matrix from a neighborlist object.

    Parameters
    ----------
    neighborlist : dict
        A neighborlist (dictionary) that contains keys of each 
        atom index and values of their neighbor atom indices.

    """ 

    conn_mat = []
    index = range(len(neighborlist.keys()))
    # Create binary matrix denoting connections.
    for index1 in index:
        conn_x = []
        for index2 in index:
            if index2 in neighborlist[index1]:
                conn_x.append(1)
            else:
                conn_x.append(0)
        conn_mat.append(conn_x)

    return np.asarray(conn_mat)


def get_mic(p1, p2, cell, pbc=[1,1,0], 
            max_cell_multiples=1e5, 
            return_squared_distance=False): 
    """A highly efficient function for getting all vectors from p1
    to p2. Also able to calculate the squared distance using the 
    minimum image convention (mic). This function is useful when you 
    want to constantly calculate mic between two given positions. 
    Please use ase.geometry.find_mic if you want to calculate an 
    array of vectors all at a time (useful for e.g. neighborlist).  

    Parameters
    ----------
    p1 : numpy.array
        The 3D Cartesian coordinate of the position 1.

    p2 : numpy.array
        The 3D Cartesian coordinate of the position 2.

    cell : numpy.array
        The 3D parallel epipedal unit cell.

    pbc : numpy.array or list, default [1, 1, 0]
        Whether cell is periodic in each direction.

    max_cell_multiples : int, default 1e5
        A large number to account for the maximum repetitions of each 
        of the lattice vectors. The minimum number of repetitions is
        hence calculated by the algorithm using the intersection of a 
        sphere and the unit cell.

    return_squared_distance : bool, default False
        Whether to return the squared mic distance instead of the
        mic vector.
    
    """

    # Precompute some useful values
    a, b, c = cell[0], cell[1], cell[2]
    vol = np.abs(a @ np.cross(b, c))
    a_cross_b = np.cross(a, b)
    a_cross_b_len = np.linalg.norm(a_cross_b)
    a_cross_b_hat = a_cross_b / a_cross_b_len
    b_cross_c = np.cross(b, c)
    b_cross_c_len = np.linalg.norm(b_cross_c)
    b_cross_c_hat = b_cross_c / b_cross_c_len
    a_cross_c = np.cross(a, c)
    a_cross_c_len = np.linalg.norm(a_cross_c)
    a_cross_c_hat = a_cross_c / a_cross_c_len

    # TODO: Wrap p1, and p2 into the current unit cell
    dr = p2 - p1
    min_dr_sq = dr @ dr
    min_length = math.sqrt(min_dr_sq)
    a_max = math.ceil(min_length / vol * b_cross_c_len)
    a_max = min(a_max, max_cell_multiples)
    b_max = math.ceil(min_length / vol * a_cross_c_len)
    b_max = min(b_max, max_cell_multiples)
    if not pbc[2]:
        c_max = 0
    else:
        c_max = math.ceil(min_length / vol * a_cross_b_len)
        c_max = min(c_max, max_cell_multiples)

    min_dr = dr
    for i in range(-a_max, a_max + 1):
        ra = i * a
        for j in range(-b_max, b_max + 1):
            rab = ra + j * b
            for k in range(-c_max, c_max + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                out_vec = rab + k * c + dr
                len_sq = out_vec @ out_vec 
                if len_sq < min_dr_sq:
                    min_dr = out_vec
                    min_dr_sq = len_sq
    if not return_squared_distance:
        return min_dr

    else:
        return np.sum(min_dr**2)


def expand_cell(atoms, cutoff=None, padding=None):

    #Return Cartesian coordinates atoms within a supercell
    #which contains repetitions of the unit cell which contains
    #at least one neighboring atom. Borrowed from Catkit.
    cell = atoms.cell
    pbc = [1, 1, 0]
    pos = atoms.positions

    if padding is None and cutoff is None:
        diags = np.sqrt((([[1, 1, 1],
                           [-1, 1, 1],
                           [1, -1, 1],
                           [-1, -1, 1]]
                           @ cell)**2).sum(1))

        if pos.shape[0] == 1:
            cutoff = max(diags) / 2.
        else:
            dpos = (pos - pos[:, None]).reshape(-1, 3)
            Dr = dpos @ np.linalg.inv(cell)
            D = (Dr - np.round(Dr) * pbc) @ cell
            D_len = np.sqrt((D**2).sum(1))

            cutoff = min(max(D_len), max(diags) / 2.)

    latt_len = np.sqrt((cell**2).sum(1))
    V = abs(np.linalg.det(cell))
    padding = pbc * np.array(np.ceil(cutoff * np.prod(latt_len) /
                                     (V * latt_len)), dtype=int)

    offsets = np.mgrid[-padding[0]:padding[0] + 1,
                       -padding[1]:padding[1] + 1,
                       -padding[2]:padding[2] + 1].T
    tvecs = offsets @ cell
    coords = pos[None, None, None, :, :] + tvecs[:, :, :, None, :]

    ncell = np.prod(offsets.shape[:-1])
    index = np.arange(len(atoms))[None, :].repeat(ncell, axis=0).flatten()
    coords = coords.reshape(np.prod(coords.shape[:-1]), 3)
    offsets = offsets.reshape(ncell, 3)

    return index, coords, offsets


def get_close_atoms(atoms, cutoff=0.5, mic=False, delete=False):
    """Get a list of close atoms and delete one set of them if requested.
    Identify all atoms that lie within the cutoff radius of each other.

    Parameters
    ----------
    atoms : ase.Atoms object
        Accept any ase.Atoms object. No need to be built-in.

    cutoff : float, default 0.5
        The cutoff radius. Two atoms are too close if the distance between
        them is less than this cutoff

    mic : bool, default False
        Whether to apply minimum image convention. Remember to set 
        mic=True for periodic systems.

    delete : bool, default False
        Whether to delete one set of the close atoms.

    """

    res = np.asarray(list(combinations(np.asarray(range(len(atoms))),2)))
    indices1, indices2 = res[:, 0], res[:, 1]
    p1, p2 = atoms.positions[indices1], atoms.positions[indices2]                      
    if mic:
        _, dists = find_mic(p2 - p1, atoms.cell, pbc=True)
    else:
        dists = np.linalg.norm(p2 - p1, axis=1) 

    dup = np.nonzero(dists < cutoff)
    rem = np.array(_row_col_from_pdist(len(atoms), dup[0]))
    if delete:
        if rem.size != 0:
            del atoms[rem[:, 0]]
    else:
        return rem


def atoms_too_close(atoms, cutoff=0.5, mic=False):
    """Check if there are atoms that are too close to each other.

    Parameters
    ----------
    atoms : ase.Atoms object
        Accept any ase.Atoms object. No need to be built-in.

    cutoff : float, default 0.5
        The cutoff radius. Two atoms are too close if the distance between
        them is less than this cutoff

    mic : bool, default False
        Whether to apply minimum image convention. Remember to set 
        mic=True for periodic systems.

    """

    res = np.asarray(list(combinations(np.asarray(range(len(atoms))), 2)))
    indices1, indices2 = res[:, 0], res[:, 1]
    p1, p2 = atoms.positions[indices1], atoms.positions[indices2]
    if mic:
        _, dists = find_mic(p2 - p1, atoms.cell, pbc=True)
    else:
        dists = np.linalg.norm(p2 - p1, axis=1)

    return any(dists < cutoff)


def atoms_too_close_after_addition(atoms, n_added, cutoff=1.5, mic=False): 
    """Check if there are atoms that are too close to each other after 
    adding some new atoms.

    Parameters
    ----------
    atoms : ase.Atoms object
        Accept any ase.Atoms object. No need to be built-in.

    n_added : int
        Number of newly added atoms.

    cutoff : float, default 1.5
        The cutoff radius. Two atoms are too close if the distance between
        them is less than this cutoff

    mic : bool, default False
        Whether to apply minimum image convention. Remember to set 
        mic=True for periodic systems.

    """

    newp, oldp = atoms.positions[-n_added:], atoms.positions[:-n_added]
    newps = np.repeat(newp, len(oldp), axis=0)
    oldps = np.tile(oldp, (n_added, 1))
    if mic:
        _, dists = find_mic(newps - oldps, atoms.cell, pbc=True)
    else:
        dists = np.linalg.norm(newps - oldps, axis=1)

    return any(dists < cutoff)


def get_angle_between(v1, v2):
    """Returns the angle in radians between vectors 'v1' and 'v2'.

    Parameters
    ----------
    v1 : numpy.array
        Vector 1.
    v2 : numpy.array
        Vector 2.

    """

    v1_u = v1 / np.linalg.norm(v1)
    v2_u = v2 / np.linalg.norm(v2)

    return np.arccos(np.clip(v1_u @ v2_u, -1., 1.))


def get_rejection_between(v1, v2):
    """Calculate the vector rejection of vector 'v1' perpendicular 
    to vector 'v2'.

    Parameters
    ----------
    v1 : numpy.array
        Vector 1.
    v2 : numpy.array
        Vector 2.

    """

    return v1 - v2 * (v1 @ v2) / (v2 @ v2)


def get_rotation_matrix(v1, v2):
    """Return the rotation matrix R that rotates unit vector v1 onto 
    unit vector v2.
 
    Parameters
    ----------
    v1 : numpy.array
        Vector 1.
    v2 : numpy.array
        Vector 2.
 
    """
 
    ax, ay, az = v1[0], v1[1], v1[2]
    bx, by, bz = v2[0], v2[1], v2[2]
    au = v1 / (np.sqrt(ax * ax + ay * ay + az * az))
    bu = v2 / (np.sqrt(bx * bx + by * by + bz * bz))
 
    R = np.asarray([[bu[0] * au[0], bu[0] * au[1], bu[0] * au[2]], 
                    [bu[1] * au[0], bu[1] * au[1], bu[1] * au[2]], 
                    [bu[2] * au[0], bu[2] * au[1], bu[2] * au[2]]])
    return R


def get_rodrigues_rotation_matrix(axis, angle):
    """Return the Rodrigues rotation matrix associated with 
    counter-clockwise rotation about the given axis by an angle.
 
    Parameters
    ----------
    axis : numpy.array
        The axis (vector) to rotate around with.
    angle : numpy.array
        The angle (in radians) to rotate around.
 
    """

    return scipy.linalg.expm(np.cross(np.eye(3),
           axis / np.linalg.norm(axis) * angle))


def get_total_masses(symbol):
    """Get the total molar mass given the chemical symbol of a 
    molecule.

    Parameters
    ----------
    symbol : str
        Chemical symbol of the molecule.

    """

    return np.sum([atomic_masses[atomic_numbers[s]] 
                   for s in list(Formula(symbol))])


def is_list_or_tuple(obj):
    return (isinstance(obj, abc.Sequence)
            and not isinstance(obj, str))


def string_fragmentation(adsorbate):
    """A function for generating a fragment list (list of strings) 
    from a given adsorbate (string).

    Parameters
    ----------
    adsorbate : str
        The string of the adsorbate molecule.

    """
    if adsorbate == 'H2':
        return ['H', 'H']
    sym_list = list(Formula(adsorbate))
    nsyms = len(sym_list)
    frag_list = []
    for i, sym in enumerate(sym_list):
        if sym != 'H':
            j = i + 1
            if j < nsyms:
                hlen = 0
                while sym_list[j]  == 'H':
                    hlen += 1
                    j += 1
                    if j == nsyms:
                        break
                if hlen == 0:
                    frag = sym
                elif hlen == 1:
                    frag = sym + 'H'
                else:
                    frag = sym + 'H' + str(hlen)
                frag_list.append(frag)
            else:
                frag_list.append(sym)

    return frag_list        


def numbers_from_ratio(sum_numbers, ratio):
    """Return the number of atoms for each element from ratio.

    Parameters
    ----------
    sum_numbers : int
        The total number of atoms

    ratio : list
        A list of ratio for different elements
    """

    sum_ratio = sum(ratio)
    totals = [int((sum_numbers * r) // sum_ratio) for r in ratio]
    residues = [(sum_numbers * r) % sum_ratio for r in ratio]
    for i in sorted(range(len(ratio)), key=lambda i: residues[i] 
    * ratio[i], reverse=True)[:sum_numbers-sum(totals)]:
        totals[i] += 1

    return totals


def draw_graph(G, savefig='graph.png'):               
    """Draw the graph using matplotlib.pyplot.

    Parameters
    ----------
    G : networkx.Graph object
        The graph object

    savefig : str, default 'graph.png'
        The name of the figure to be saved.

    """

    import matplotlib.pyplot as plt
    labels = nx.get_node_attributes(G, 'symbol')
    
    # Get unique groups
    groups = sorted(set(labels.values()))
    mapping = {x: "C{}".format(i) for i, x in enumerate(groups)}
    nodes = G.nodes()
    colors = [mapping[G.nodes[n]['symbol']] for n in nodes]

    # Drawing nodes, edges and labels separately
    pos = nx.spring_layout(G)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_nodes(G, pos, 
                           nodelist=nodes, 
                           node_color=colors, 
                           node_size=500)
    nx.draw_networkx_labels(G, pos, labels, 
                            font_size=10, 
                            font_color='w')
    plt.axis('off')
    plt.savefig(savefig)
    plt.clf()
