import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as gt


crv01_pt_list=rs.DivideCurve(crv01,n)
crv02_pt_list=rs.DivideCurve(crv02,n)

new_pt_list=[]
edges=[]

crv01_pl=[]
crv02_pl=[]

for i in range(n):
    if i % 2==0:
        new_pt_list.append(crv01_pt_list[i])
        crv01_pl.append(crv01_pt_list[i])
    else:
        new_pt_list.append(crv02_pt_list[i])
        crv02_pl.append(crv02_pt_list[i])


for i in range(n):
    new_edge=[]
    new_srf=[]
    if i < n-3:
        pt_a=new_pt_list[i]
        pt_b=new_pt_list[i+1]
        pt_c=new_pt_list[i+2]
    tri_edge=[pt_a,pt_b,pt_c,pt_a]
    new_edge=rs.AddPolyline(tri_edge)
    edges.append(new_edge)