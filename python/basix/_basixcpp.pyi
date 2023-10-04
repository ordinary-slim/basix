from typing import Any, ClassVar, List, Tuple, overload

import numpy
import numpy.typing as npt

__version__: str = ...

class CellType:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    hexahedron: ClassVar[CellType] = ...
    interval: ClassVar[CellType] = ...
    point: ClassVar[CellType] = ...
    prism: ClassVar[CellType] = ...
    pyramid: ClassVar[CellType] = ...
    quadrilateral: ClassVar[CellType] = ...
    tetrahedron: ClassVar[CellType] = ...
    triangle: ClassVar[CellType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class DPCVariant:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    diagonal_equispaced: ClassVar[DPCVariant] = ...
    diagonal_gll: ClassVar[DPCVariant] = ...
    horizontal_equispaced: ClassVar[DPCVariant] = ...
    horizontal_gll: ClassVar[DPCVariant] = ...
    legendre: ClassVar[DPCVariant] = ...
    simplex_equispaced: ClassVar[DPCVariant] = ...
    simplex_gll: ClassVar[DPCVariant] = ...
    unset: ClassVar[DPCVariant] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class ElementFamily:
    __members__: ClassVar[dict] = ...  # read-only
    BDM: ClassVar[ElementFamily] = ...
    CR: ClassVar[ElementFamily] = ...
    DPC: ClassVar[ElementFamily] = ...
    HHJ: ClassVar[ElementFamily] = ...
    Hermite: ClassVar[ElementFamily] = ...
    iso: ClassVar[ElementFamily] = ...
    N1E: ClassVar[ElementFamily] = ...
    N2E: ClassVar[ElementFamily] = ...
    P: ClassVar[ElementFamily] = ...
    RT: ClassVar[ElementFamily] = ...
    Regge: ClassVar[ElementFamily] = ...
    __entries: ClassVar[dict] = ...
    bubble: ClassVar[ElementFamily] = ...
    custom: ClassVar[ElementFamily] = ...
    serendipity: ClassVar[ElementFamily] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PolysetType:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    standard: ClassVar[PolysetType] = ...
    macroedge: ClassVar[PolysetType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class FiniteElement:
    def __hash__(self, object, int): ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def apply_dof_transformation(self, arg0: npt.NDArray[numpy.float64], arg1: int, arg2: int) -> npt.NDArray[numpy.float64]: ...
    def apply_dof_transformation_to_transpose(self, arg0: npt.NDArray[numpy.float64], arg1: int, arg2: int) -> npt.NDArray[numpy.float64]: ...
    def apply_inverse_transpose_dof_transformation(self, arg0: npt.NDArray[numpy.float64], arg1: int, arg2: int) -> npt.NDArray[numpy.float64]: ...
    def base_transformations(self) -> npt.NDArray[numpy.float64]: ...
    def entity_transformations(self) -> dict: ...
    def get_tensor_product_representation(self) -> List[Tuple[List[FiniteElement],List[int]]]: ...
    def pull_back(self, arg0: npt.NDArray[numpy.float64], arg1: npt.NDArray[numpy.float64], arg2: npt.NDArray[numpy.float64], arg3: npt.NDArray[numpy.float64]) -> npt.NDArray[numpy.float64]: ...
    def push_forward(self, arg0: npt.NDArray[numpy.float64], arg1: npt.NDArray[numpy.float64], arg2: npt.NDArray[numpy.float64], arg3: npt.NDArray[numpy.float64]) -> npt.NDArray[numpy.float64]: ...
    def tabulate(self, arg0: int, arg1: npt.NDArray[numpy.float64]) -> npt.NDArray[numpy.float64]: ...
    def __eq__(self, arg0: object) -> bool: ...
    @property
    def M(self) -> List[List[npt.NDArray[numpy.float64]]]: ...
    @property
    def cell_type(self) -> CellType: ...
    @property
    def polyset_type(self) -> PolysetType: ...
    @property
    def coefficient_matrix(self) -> npt.NDArray[numpy.float64]: ...
    @property
    def degree(self) -> int: ...
    @property
    def dim(self) -> int: ...
    @property
    def discontinuous(self) -> bool: ...
    @property
    def dof_transformations_are_identity(self) -> bool: ...
    @property
    def dof_transformations_are_permutations(self) -> bool: ...
    @property
    def dpc_variant(self) -> Any: ...
    @property
    def dual_matrix(self) -> npt.NDArray[numpy.float64]: ...
    @property
    def entity_closure_dofs(self) -> List[List[List[int]]]: ...
    @property
    def entity_dofs(self) -> List[List[List[int]]]: ...
    @property
    def family(self) -> ElementFamily: ...
    @property
    def has_tensor_product_factorisation(self) -> bool: ...
    @property
    def highest_complete_degree(self) -> int: ...
    @property
    def highest_degree(self) -> int: ...
    @property
    def interpolation_is_identity(self) -> bool: ...
    @property
    def interpolation_matrix(self) -> npt.NDArray[numpy.float64]: ...
    @property
    def interpolation_nderivs(self) -> int: ...
    @property
    def lagrange_variant(self) -> Any: ...
    @property
    def map_type(self) -> MapType: ...
    @property
    def sobolev_space(self) -> SobolevSpace: ...
    @property
    def num_entity_closure_dofs(self) -> List[List[int]]: ...
    @property
    def num_entity_dofs(self) -> List[List[int]]: ...
    @property
    def points(self) -> npt.NDArray[numpy.float64]: ...
    @property
    def value_shape(self) -> List[int]: ...
    @property
    def value_size(self) -> int: ...
    @property
    def wcoeffs(self) -> npt.NDArray[numpy.float64]: ...
    @property
    def x(self) -> List[List[npt.NDArray[numpy.float64]]]: ...

class LagrangeVariant:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    chebyshev_centroid: ClassVar[LagrangeVariant] = ...
    chebyshev_isaac: ClassVar[LagrangeVariant] = ...
    chebyshev_warped: ClassVar[LagrangeVariant] = ...
    equispaced: ClassVar[LagrangeVariant] = ...
    gl_centroid: ClassVar[LagrangeVariant] = ...
    gl_isaac: ClassVar[LagrangeVariant] = ...
    gl_warped: ClassVar[LagrangeVariant] = ...
    gll_centroid: ClassVar[LagrangeVariant] = ...
    gll_isaac: ClassVar[LagrangeVariant] = ...
    gll_warped: ClassVar[LagrangeVariant] = ...
    legendre: ClassVar[LagrangeVariant] = ...
    unset: ClassVar[LagrangeVariant] = ...
    vtk: ClassVar[LagrangeVariant] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LatticeSimplexMethod:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    centroid: ClassVar[LatticeSimplexMethod] = ...
    isaac: ClassVar[LatticeSimplexMethod] = ...
    none: ClassVar[LatticeSimplexMethod] = ...
    warp: ClassVar[LatticeSimplexMethod] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class LatticeType:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    chebyshev: ClassVar[LatticeType] = ...
    equispaced: ClassVar[LatticeType] = ...
    gl: ClassVar[LatticeType] = ...
    gll: ClassVar[LatticeType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class MapType:
    __members__: ClassVar[dict] = ...  # read-only
    L2Piola: ClassVar[MapType] = ...
    __entries: ClassVar[dict] = ...
    contravariantPiola: ClassVar[MapType] = ...
    covariantPiola: ClassVar[MapType] = ...
    doubleContravariantPiola: ClassVar[MapType] = ...
    doubleCovariantPiola: ClassVar[MapType] = ...
    identity: ClassVar[MapType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SobolevSpace:
    __members__: ClassVar[dict] = ...  # read-only
    L2: ClassVar[SobolevSpace] = ...
    H1: ClassVar[SobolevSpace] = ...
    H2: ClassVar[SobolevSpace] = ...
    H3: ClassVar[SobolevSpace] = ...
    HInf: ClassVar[SobolevSpace] = ...
    HDiv: ClassVar[SobolevSpace] = ...
    HCurl: ClassVar[SobolevSpace] = ...
    HEin: ClassVar[SobolevSpace] = ...
    HDivDiv: ClassVar[SobolevSpace] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PolynomialType:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    legendre: ClassVar[PolynomialType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class QuadratureType:
    __members__: ClassVar[dict] = ...  # read-only
    Default: ClassVar[QuadratureType] = ...
    __entries: ClassVar[dict] = ...
    gauss_jacobi: ClassVar[QuadratureType] = ...
    gll: ClassVar[QuadratureType] = ...
    xiao_gimbutas: ClassVar[QuadratureType] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def cell_facet_jacobians(arg0: CellType) -> npt.NDArray[numpy.float64]: ...
def cell_facet_normals(arg0: CellType) -> npt.NDArray[numpy.float64]: ...
def cell_facet_orientations(arg0: CellType) -> List[bool]: ...
def cell_facet_outward_normals(arg0: CellType) -> npt.NDArray[numpy.float64]: ...
def cell_facet_reference_volumes(arg0: CellType) -> npt.NDArray[numpy.float64]: ...
def cell_volume(arg0: CellType) -> float: ...
def sobolev_space_intersection(arg0: SobolevSpace, arg1: SobolevSpace) -> SobolevSpace: ...
def compute_interpolation_operator(arg0: FiniteElement, arg1: FiniteElement) -> npt.NDArray[numpy.float64]: ...
def create_custom_element(arg0: CellType, arg1: List[int], arg2: npt.NDArray[numpy.float64], arg3: List[List[npt.NDArray[numpy.float64]]], arg4: List[List[npt.NDArray[numpy.float64]]], arg5: int, arg6: MapType, arg7: SobolevSpace, arg8: bool, arg9: int, arg10: int, arg11: PolysetType) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: bool) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: LagrangeVariant, arg4: bool) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: DPCVariant, arg4: bool) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: LagrangeVariant, arg4: DPCVariant, arg5: bool) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: LagrangeVariant) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: DPCVariant) -> FiniteElement: ...
@overload
def create_element(arg0: ElementFamily, arg1: CellType, arg2: int, arg3: LagrangeVariant, arg4: DPCVariant) -> FiniteElement: ...
@overload
def create_lattice(arg0, arg1: int, arg2: LatticeType, arg3: bool) -> npt.NDArray[numpy.float64]: ...
@overload
def create_lattice(arg0, arg1: int, arg2: LatticeType, arg3: bool, arg4: LatticeSimplexMethod) -> npt.NDArray[numpy.float64]: ...
def geometry(arg0) -> npt.NDArray[numpy.float64]: ...
@overload
def index(arg0: int) -> int: ...
@overload
def index(arg0: int, arg1: int) -> int: ...
@overload
def index(arg0: int, arg1: int, arg2: int) -> int: ...
def make_quadrature(arg0: QuadratureType, arg1: CellType, arg2: PolysetType, arg3: int) -> Tuple[npt.NDArray[numpy.float64],npt.NDArray[numpy.float64]]: ...
def sub_entity_connectivity(arg0) -> List[List[List[List[int]]]]: ...
def sub_entity_geometry(arg0, arg1: int, arg2: int) -> npt.NDArray[numpy.float64]: ...
def tabulate_polynomial_set(arg0: CellType, arg1: int, arg2: int, arg3: npt.NDArray[numpy.float64]) -> npt.NDArray[numpy.float64]: ...
def tabulate_polynomials(arg0: PolynomialType, arg1: CellType, arg2: int, arg3: npt.NDArray[numpy.float64]) -> npt.NDArray[numpy.float64]: ...
def polynomials_dim(arg0: PolynomialType, arg1: CellType, arg2: int) -> int: ...
@overload
def topology(arg0) -> List[List[List[int]]]: ...
@overload
def topology(vertexindices) -> Any: ...
def superset(arg0: CellType, arg1: PolysetType, arg2: PolysetType) -> PolysetType: ...
def restriction(arg0: PolysetType, arg1: CellType, arg2: CellType) -> PolysetType: ...
