# Copyright 2023 The e3x Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import e3x
import jax.numpy as jnp


def test_rectangular_window() -> None:
  x = jnp.linspace(0.0, 2.0, 11)
  expected = jnp.asarray([
      [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ])
  assert jnp.allclose(
      e3x.nn.rectangular_window(x, num=8, limit=1.5), expected, atol=1e-5
  )


def test_triangular_window() -> None:
  x = jnp.linspace(0.0, 2.0, 11)
  expected = jnp.asarray([
      [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.93333334, 0.06666669, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.8666666, 0.13333337, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.7999999, 0.20000012, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.7333333, 0.26666674, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.6666667, 0.33333334, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5999997, 0.40000024],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5333335],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  ])
  assert jnp.allclose(
      e3x.nn.triangular_window(x, num=8, limit=1.5), expected, atol=1e-5
  )


def test_smooth_window() -> None:
  x = jnp.linspace(0.0, 2.0, 11)
  expected = jnp.asarray([
      [
          1.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          9.99994218e-01,
          5.77193669e-06,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          9.95913327e-01,
          4.08666627e-03,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          9.62586522e-01,
          3.74134891e-02,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          8.87619317e-01,
          1.12380676e-01,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          7.85673022e-01,
          2.14326918e-01,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          6.72978103e-01,
          3.27021778e-01,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          5.57734311e-01,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
      [
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
          0.00000000e00,
      ],
  ])
  assert jnp.allclose(
      e3x.nn.smooth_window(x, num=8, limit=1.5), expected, atol=1e-5
  )
