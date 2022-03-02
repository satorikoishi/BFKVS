"""BF(r7525) Nodes Connected

Instructions:
Param n: # of nodes
Param l: # of links between nodes
Param i: Disk image
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "n", "Number of nodes", portal.ParameterType.INTEGER, 2)
portal.context.defineParameter( "l", "Number of links between nodes", portal.ParameterType.INTEGER, 3)
portal.context.defineParameter( "i", "Disk image", portal.ParameterType.IMAGE, "urn:publicid:IDN+clemson.cloudlab.us+image+bfkvs-PG0:BFNodes.node0")

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

# Check parameter validity.
if params.n < 1 or params.n > 8:
    portal.context.reportError( portal.ParameterError( "You must choose at least 1 and no more than 8 nodes.", ["n"] ) )
if params.l < 1 or params.l > 4:
    portal.context.reportError( portal.ParameterError( "You must choose at least 1 and no more than 4 links.", ["l"] ) )

# Abort execution if there are any errors, and report them.
portal.context.verifyParameters()

nodes = []
interfaces = []
# Create n raw "PC" nodes
for i in range(0, params.n):
    nodes.append(request.RawPC("node" + str(i)))
    nodes[i].hardware_type = "r7525"
    nodes[i].disk_image = params.i
    node_if = []
    
    for l in range(0, params.l):
        node_if.append(nodes[i].addInterface('node' + str(i) + 'interface' + str(l)))
    interfaces.append(node_if)

# Create link between them
link_idx = 0
for i in range(0, params.n):
    for j in range(i + 1, params.n):
        for l in range(0, params.l):
            link = request.Link('link' + str(link_idx))
            link_idx = link_idx + 1
            
            link.addInterface(interfaces[i][l])
            link.addInterface(interfaces[j][l])

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
