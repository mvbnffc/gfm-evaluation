import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio import features
from rasterio.enums import MergeAlg
from rasterio.plot import show
from functions import label_fema_floodzones
import numpy as np

# Read in data
# FEMA vector flood file
vector = gpd.read_file(r"D:\GFM_Uncertainty\Ohio\Validation_Data\nfhl_ohio.shp")
# blank reference raster
raster = rasterio.open(r"D:\GFM_Uncertainty\Ohio\Blank_Rasters\blank_1as.tif")

# Get list of geometries for all features in vector file
geom = [shapes for shapes in vector.geometry]

# Convert all string FEMA FLD_ZN labels to integer for raster conversion
vector['FLD_ZONE_INT'] = vector.apply(lambda row: label_fema_floodzones(row), axis=1)

# Create tuples of vector geometry and FLD_ZONE_INT for raster conversion
geom_value = ((geom,value) for geom, value in zip(vector.geometry, vector['FLD_ZONE_INT']))

# Rasterize vector using the shape and transform of the raster
rasterized = features.rasterize(geom_value,
                                out_shape = raster.shape,
                                transform = raster.transform,
                                all_touched = False,
                                fill = 0,   # background value
                                merge_alg = MergeAlg.replace,
                                dtype = np.int16)

profile = raster.profile
profile.update(
    dtype=rasterio.int16,
    count=1,
    compress='lzw'
)

# Write new raster
with rasterio.open(r'D:\GFM_Uncertainty\Ohio\Validation_Data\nfhl_ohio_1as.tif', 'w', **profile) as dst:
    dst.write(rasterized.astype(rasterio.int16), 1)

# # Plot raster
# fig, ax = plt.subplots(1, figsize = (10, 10))
# show(rasterized, ax = ax)
# plt.gca().invert_yaxis()
#
# plt.show()
