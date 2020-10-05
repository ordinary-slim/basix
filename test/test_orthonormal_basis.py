# Copyright (c) 2020 Chris Richardson
# FEniCS Project
# SPDX-License-Identifier: MIT

import sympy
import fiatx
import pytest
import numpy as np


@pytest.mark.parametrize("order", [1, 2, 3])
def test_quad(order):
    pts = fiatx.create_lattice(fiatx.CellType.interval, 1, True)
    Lpts, Lwts = fiatx.make_quadrature(pts, order + 2)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            Qpts.append([p[0], q[0]])
            Qwts.append(u*v)
    basis = fiatx.tabulate_polynomial_set(fiatx.CellType.quadrilateral,
                                          order, Qpts)
    ndofs = basis.shape[1]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[:, i] * basis[:, j] * Qwts)

    np.set_printoptions(suppress=True)
    print(mat, np.eye(mat.shape[0]))
    assert(np.isclose(mat * 4.0, np.eye(mat.shape[0])).all())


@pytest.mark.parametrize("order", [1, 2, 3, 4])
def test_pyramid(order):
    pts = fiatx.create_lattice(fiatx.CellType.interval, 1, True)
    Lpts, Lwts = fiatx.make_quadrature(pts, order + 4)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            for r, w in zip(Lpts, Lwts):
                sc = (1.0 - r[0])
                Qpts.append([p[0]*sc, q[0]*sc, r[0]])
                Qwts.append(u*v*sc*sc*w)
    basis = fiatx.tabulate_polynomial_set(fiatx.CellType.pyramid,
                                          order, Qpts)
    ndofs = basis.shape[1]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[:, i] * basis[:, j] * Qwts)

    np.set_printoptions(suppress=True, linewidth=220)
    print(mat)
    assert(np.isclose(mat * 8.0, np.eye(mat.shape[0])).all())


@pytest.mark.parametrize("order", [1, 2, 3])
def test_hex(order):
    pts = fiatx.create_lattice(fiatx.CellType.interval, 1, True)
    Lpts, Lwts = fiatx.make_quadrature(pts, order + 2)
    Qwts = []
    Qpts = []
    for p, u in zip(Lpts, Lwts):
        for q, v in zip(Lpts, Lwts):
            for r, w in zip(Lpts, Lwts):
                Qpts.append([p[0], q[0], r[0]])
                Qwts.append(u*v*w)
    basis = fiatx.tabulate_polynomial_set(fiatx.CellType.hexahedron,
                                          order, Qpts)
    ndofs = basis.shape[1]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[:, i] * basis[:, j] * Qwts)

    np.set_printoptions(suppress=True)
    print(mat)
    assert(np.isclose(mat * 8.0, np.eye(mat.shape[0])).all())


@pytest.mark.parametrize("order", [1, 2, 3])
def test_prism(order):
    pts = fiatx.create_lattice(fiatx.CellType.triangle, 1, True)
    Tpts, Twts = fiatx.make_quadrature(pts, order + 2)
    pts = fiatx.create_lattice(fiatx.CellType.interval, 1, True)
    Lpts, Lwts = fiatx.make_quadrature(pts, order + 2)
    Qwts = []
    Qpts = []
    for p, u in zip(Tpts, Twts):
        for q, v in zip(Lpts, Lwts):
            Qpts.append([p[0], p[1], q[0]])
            Qwts.append(u*v)
    basis = fiatx.tabulate_polynomial_set(fiatx.CellType.prism, order, Qpts)
    ndofs = basis.shape[1]

    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[:, i] * basis[:, j] * Qwts)

    np.set_printoptions(suppress=True)
    print(mat)
    assert(np.isclose(mat * 8.0, np.eye(mat.shape[0])).all())


@pytest.mark.parametrize("cell_type", [fiatx.CellType.interval,
                                       fiatx.CellType.triangle,
                                       fiatx.CellType.tetrahedron])
@pytest.mark.parametrize("order", [1, 2, 3, 4])
def test_cell(cell_type, order):

    pts = fiatx.create_lattice(cell_type, 1, True)
    Qpts, Qwts = fiatx.make_quadrature(pts, order + 2)
    basis = fiatx.tabulate_polynomial_set(cell_type, order, Qpts)
    ndofs = basis.shape[1]
    mat = np.zeros((ndofs, ndofs))
    for i in range(ndofs):
        for j in range(ndofs):
            mat[i, j] = sum(basis[:, i] * basis[:, j] * Qwts)

    np.set_printoptions(suppress=True)
    print(mat)
    fac = 2 ** pts.shape[0] / 2
    assert(np.isclose(mat * fac, np.eye(mat.shape[0])).all())


def test_derivs_triangle():
    cell = fiatx.CellType.triangle
    pts0 = fiatx.create_lattice(cell, 5, True)
    eps = np.array([1e-6, 0.0])
    pts1 = pts0 - eps
    pts2 = pts0 + eps
    n = 3
    nderiv = 1
    w = fiatx.tabulate_polynomial_set_deriv(cell, n, nderiv, pts0)
    w1 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts1)[0]
    w2 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts2)[0]
    v = (w2 - w1)/2/eps[0]
    assert(np.isclose(w[1], v).all())
    eps = np.array([0.0, 1e-6])
    pts1 = pts0 - eps
    pts2 = pts0 + eps
    w1 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts1)[0]
    w2 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts2)[0]
    v = (w2 - w1)/2/eps[1]
    assert(np.isclose(w[2], v).all())


def test_derivs_tetrahedron():
    cell = fiatx.CellType.tetrahedron
    pts0 = fiatx.create_lattice(cell, 5, True)
    eps = np.array([1e-7, 0.0, 0.0])
    pts1 = pts0 - eps
    pts2 = pts0 + eps
    n = 7
    nderiv = 1
    w = fiatx.tabulate_polynomial_set_deriv(cell, n, nderiv, pts0)
    w1 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts1)[0]
    w2 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts2)[0]
    v = (w2 - w1)/2/eps[0]
    assert(np.isclose(w[1], v).all())
    eps = np.array([0.0, 1e-6, 0.0])
    pts1 = pts0 - eps
    pts2 = pts0 + eps
    w1 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts1)[0]
    w2 = fiatx.tabulate_polynomial_set_deriv(cell, n, 0, pts2)[0]
    v = (w2 - w1)/2/eps[1]
    assert(np.isclose(w[2], v).all())


def test_symbolic_interval():
    n = 7
    nderiv = 4

    x = sympy.Symbol("x")
    x0 = x * sympy.S(2) - sympy.S(1)
    r = [sympy.S(1) for i in range(n + 1)]

    for p in range(1, n + 1):
        a = sympy.S(1) - sympy.Rational(1, p)
        r[p] = x0 * r[p - 1] * (a + sympy.S(1))
        if p > 1:
            r[p] = r[p] - r[p - 2] * a
    for p in range(n + 1):
        r[p] *= sympy.sqrt(p + sympy.Rational(1, 2))

    cell = fiatx.CellType.interval
    pts0 = fiatx.create_lattice(cell, 10, True)
    w = fiatx.tabulate_polynomial_set_deriv(cell, n, nderiv, pts0)

    wsym = np.zeros_like(w[0])

    for i in range(n + 1):
        for j, p in enumerate(pts0):
            wsym[j, i] = r[i].subs(x, p[0])

    assert(np.isclose(w[0], wsym).all())

    for k in range(1, 5):
        for i in range(n+1):
            r[i] = sympy.diff(r[i], x)

        wsym = np.zeros_like(w[0])
        for i in range(n + 1):
            for j, p in enumerate(pts0):
                wsym[j, i] = r[i].subs(x, p[0])

        assert(np.isclose(w[k], wsym).all())


def test_symbolic_triangle():
    n = 5
    nderiv = 4

    def idx(p, q):
        return (p + q + 1) * (p + q) // 2 + q

    def jrc(a, n):
        an = sympy.Rational((a + 2 * n + 1) * (a + 2 * n + 2),
                            2 * (n + 1) * (a + n + 1))
        bn = sympy.Rational(a * a * (a + 2 * n + 1),
                            2 * (n + 1) * (a + n + 1) * (a + 2 * n))
        cn = sympy.Rational(n * (a + n) * (a + 2 * n + 2),
                            (n + 1) * (a + n + 1) * (a + 2 * n))
        return (an, bn, cn)

    m = (n + 1) * (n + 2) // 2
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    x0 = x * sympy.S(2) - sympy.S(1)
    y0 = y * sympy.S(2) - sympy.S(1)
    f3 = (sympy.S(1) - y0)**2 / sympy.S(4)
    r = [sympy.S(1) for i in range(m)]

    np.set_printoptions(linewidth=200)
    for p in range(1, n + 1):
        a = sympy.Rational(2 * p - 1, p)
        r[idx(p, 0)] = (x0 + (y0 + sympy.S(1))/sympy.S(2)) \
            * r[idx(p - 1, 0)] * a
        if p > 1:
            r[idx(p, 0)] -= f3 * r[idx(p - 2, 0)] * (a - sympy.S(1))

    for p in range(n):
        r[idx(p, 1)] = r[idx(p, 0)] * (y0 * sympy.Rational(3 + 2 * p, 2)
                                       + sympy.Rational(1 + 2 * p, 2))
        for q in range(1, n - p):
            a1, a2, a3 = jrc(2 * p + 1, q)
            r[idx(p, q + 1)] = r[idx(p, q)] * (y0 * a1 + a2) \
                - r[idx(p, q - 1)] * a3

    for p in range(n + 1):
        for q in range(n - p + 1):
            r[idx(p, q)] *= sympy.sqrt(sympy.Rational(2*p + 1, 2)
                                       * sympy.S(p + q + 1))

    cell = fiatx.CellType.triangle
    pts0 = fiatx.create_lattice(cell, 3, True)
    w = fiatx.tabulate_polynomial_set_deriv(cell, n, nderiv, pts0)

    wsym = np.zeros_like(w[0])

    for i in range(m):
        for j, p in enumerate(pts0):
            wsym[j, i] = r[i].subs([(x, p[0]), (y, p[1])])

    assert(np.isclose(w[0], wsym).all())

    rd = r.copy()
    for kx in range(nderiv):
        for ky in range(0, nderiv - kx):
            for i in range(m):
                rd[i] = sympy.diff(r[i], x, kx, y, ky)

            wsym = np.zeros_like(w[0])
            for i in range(m):
                for j, p in enumerate(pts0):
                    wsym[j, i] = rd[i].subs([(x, p[0]), (y, p[1])])

            assert(np.isclose(w[idx(kx, ky)], wsym).all())