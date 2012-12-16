"""Custom topology example

author: Brandon Heller (brandonh@stanford.edu)

Two directly connected switches plus a host for each switch:

host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined topology enables one to pass in '--topo=mytopo' from the command line. """

from mininet.topo import Topo, Node

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self, enable_all = True ):
        "Create custom topo."

        # Add default members to class.
        super( MyTopo, self ).__init__()

        # Set Node IDs for hosts and switches
	centerSwitch = 0
        Host1 = 1
	Host2 = 2
	Host3 = 3
        # Add nodes
        self.add_node( centerSwitch, Node( is_switch=True ) )
        self.add_node( Host1, Node( is_switch=False ) )
        self.add_node( Host2, Node( is_switch=False ) )
        self.add_node( Host3, Node( is_switch=False ) )

        # Add edges
        self.add_edge( Host1, centerSwitch )
	self.add_edge( centerSwitch, Host2 )
	self.add_edge( centerSwitch, Host3 )

        # Consider all switches and hosts 'on'
        self.enable_all()

topos = { 'mytopo': ( lambda: MyTopo() ) } 
