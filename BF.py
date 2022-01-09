"""BF(r7525) Nodes Connected

Instructions:
Param n: # of nodes
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "n", "Number of nodes", portal.ParameterType.INTEGER, 2)

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

# Check parameter validity.
if params.n < 1 or params.n > 8:
    portal.context.reportError( portal.ParameterError( "You must choose at least 1 and no more than 8 VMs.", ["n"] ) )

# Abort execution if there are any errors, and report them.
portal.context.verifyParameters()

nodes = []
# Create n raw "PC" nodes
for i in range(0, params.n):
    nodes.append(request.RawPC("node" + str(i)))
    nodes[i].hardware_type = "r7525"
    nodes[i].disk_image = "urn:publicid:IDN+clemson.cloudlab.us+image+bfkvs-PG0:BF"
    
# links = []
# for i in range(0, params.n):
#     links.append(request.Link(members = [x for x in nodes]))

# Create link between them
link = request.Link(members = [x for x in nodes])

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
