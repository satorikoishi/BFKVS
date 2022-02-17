"""2 Specified Nodes Connected, Ubuntu-20

Instructions:
Param n: # of nodes
Param l: # of links between nodes
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "t", "Type of nodes", portal.ParameterType.NODETYPE, "c6525-25g")
portal.context.defineParameter( "l", "Number of links between nodes", portal.ParameterType.INTEGER, 2)

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

# Check parameter validity.
if params.l < 1 or params.l > 4:
    portal.context.reportError( portal.ParameterError( "You must choose at least 1 and no more than 4 links.", ["l"] ) )

# Abort execution if there are any errors, and report them.
portal.context.verifyParameters()

nodes = []
interfaces = []
# Create n raw "PC" nodes
for i in range(0, 2):
    nodes.append(request.RawPC("node" + str(i)))
    nodes[i].hardware_type = params.t
    nodes[i].disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD"
    node_if = []
    for j in range(0, 2):
        if j == i:
            if_dup = None
        else:
            if_dup = []
            for m in range(0, params.l):
                if_dup.append(nodes[i].addInterface('node' + str(i) + 'interface' + str(j) + 'dup' + str(m)))
        node_if.append(if_dup)
    interfaces.append(node_if)

# Create link between them
link_idx = 0
for i in range(0, 2):
    for j in range(i + 1, 2):
        for m in range(0, params.l):
            link = request.Link('link' + str(link_idx))
            link_idx = link_idx + 1
            
            link.addInterface(interfaces[i][j][m])
            link.addInterface(interfaces[j][i][m])

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
