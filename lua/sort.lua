local tb = {}
table.insert(tb, {k="a",v=1})
table.insert(tb, {k="b",v=1})
table.insert(tb, {k="c",v=3})
table.insert(tb, {k="d",v=3})
table.insert(tb, {k="e",v=5})

function sorttb(obja, objb)
	return obja.v < objb.v
end

table.sort( tb, sorttb )

for i=1,#tb do
	print(tb[i].v,tb[i].k)
end