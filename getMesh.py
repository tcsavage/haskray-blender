import bpy

# bpy.context.active_object.data.polygons[0].vertices[0]
# bpy.context.active_object.data.vertices[0].co
mesh = bpy.context.active_object.data

def joinit(iterable, delimiter):
	it = iter(iterable)
	yield next(it)
	for x in it:
		yield delimiter
		yield x

def makeVec3(vector):
	return "(Vector3 {x3 = %f, y3 = %f, z3 = %f})" % (vector.x, vector.y, vector.z)

def makeVec2(vector):
	return "(Vector2 {x2 = %f, y2 = %f})" % (vector.x, vector.y)

def makeVertex(n, data):
	pos = makeVec3(data.vertices[n].co)
	norm = makeVec3(data.vertices[n].normal)
	uv = makeVec2(data.uv_layers[0].data[n].uv)
	vstr = "(Vertex %s %s %s)" % (pos, norm, uv)
	return vstr

tstrs = []

for p in mesh.polygons:
	if len(p.vertices) != 3:
		raise Exception("Not triangle enough: %d" % (len(p.vertices)))
	vstrs = []
	for v in p.vertices:
		vstrs.append(makeVertex(v, mesh))
	tstr = "Triangle " + " ".join(vstrs)
	tstrs.append(tstr)

meshstr = '(ShapeRep "Mesh" "Mesh (Vector3 {x3 = 0.0, y3 = 0.0, z3 = 0.0}) [%s]")' % (", ".join(tstrs))
print(meshstr)
