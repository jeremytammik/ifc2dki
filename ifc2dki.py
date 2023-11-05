#!python3
#
# ifc2dki.py
#
# Generate DK-Integral data from IFC BIM file
#
# Copyright (C) 2023 Jeremy Tammik
#
# 2023-10-31 initial code
#
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.placement
import ifcopenshell.util.shape

angle_to_north = 21 # degrees
path = '/Users/jta/j/doc/house/huenerberg/waldrain/html/waldrain.github.io/doc/kuri/2023-09-27_kuechenmeister'
filename = '0_3d_modell.ifc'

print('pydki.py loading', filename)

model = ifcopenshell.open(path + '/' + filename)

walls = model.by_type('IfcWall')

print(len(walls), 'walls in', filename)

#for w in walls:
#  print(w.Name)

i = 0
wall = walls[i]

print(len(wall), 'data items in wall', i)

#for p in wall: print(' ', p)

print(wall.get_info())

wall_type = ifcopenshell.util.element.get_type(wall)
if wall_type: print(f"The wall type of {wall.Name} is {wall_type.Name}")
else: print(f"The wall type of {wall.Name} is {wall_type}")

container = ifcopenshell.util.element.get_container(wall)
print(f"The wall is located on {container.Name}")

matrix = ifcopenshell.util.placement.get_local_placement(wall.ObjectPlacement)
print('local placement\n', matrix)

# all elements which are referencing our wall
#print(model.get_inverse(wall))

#location = ifcopenshell.util.element.get_location(wall)
#print(location)

# AllPlan property sets
#print(ifcopenshell.util.element.get_psets(wall, qtos_only=False))
# You can use ifcopenshell.util.element.get_psets(wall, qtos_only=True)
# if you are using the high level ifcopenshell python api

# Quantities (and property sets) are not guaranteed to populated in a model
# (or generated consistently for that matter). Luckily ifcopenshell provides
# the tooling to generate a lot of quantities from the geometry:

elem = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), wall)
geo = elem.geometry
x = ifcopenshell.util.shape.get_x(geo)
y = ifcopenshell.util.shape.get_y(geo)
z = ifcopenshell.util.shape.get_z(geo)
print('X', x, 'Y', y, 'Z', z, 'X*Z', x*z)
print('area', ifcopenshell.util.shape.get_area(geo))
print('volume', ifcopenshell.util.shape.get_volume(geo))
#print('matrix', ifcopenshell.util.shape.get_shape_matrix(geo))
