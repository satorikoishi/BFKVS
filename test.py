"""Two Nodes(m400) Connected

Instructions:
None
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

nodes = []
# Create two raw "PC" nodes
for i in range(0, 2):
    nodes.append(request.RawPC("node" + str(i)))
    nodes[i].hardware_type = "m400"
    # nodes[i].disk_image = "urn:publicid:IDN+utah.cloudlab.us+image+emulab-ops:UBUNTU18-64-A-OSCP-T"

# Create a link between them
link1 = request.Link(members = [x for x in nodes])

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
