import pyvista as pv
import numpy as np
pv.set_jupyter_backend("static")

# Sample data: points and vectors
n = 100
points = np.random.rand(n, 3) * 10         # Random positions
vectors = np.random.randn(n, 3)            # Random direction vectors
scales = np.linalg.norm(vectors, axis=1)   # Optional: scale by vector magnitude

# Create a point cloud with vector field
point_cloud = pv.PolyData(points)
point_cloud["vectors"] = vectors
point_cloud["scale"] = scales

# Glyphs (e.g., arrows)
glyphs = point_cloud.glyph(orient="vectors", scale="scale", factor=0.5)

# Plot
plotter = pv.Plotter()
plotter.add_mesh(glyphs, color="green")
plotter.show()
