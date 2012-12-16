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
        leftHost1 = 1
        leftSwitch = 2
	leftHost2 = 3
	rightHost1 = 4
        rightSwitch = 5
        rightHost2 = 6

        # Add nodes
        self.add_node( leftSwitch, Node( is_switch=True ) )
        self.add_node( rightSwitch, Node( is_switch=True ) )
        self.add_node( leftHost1, Node( is_switch=False ) )
        self.add_node( rightHost1, Node( is_switch=False ) )
	self.add_node( leftHost2, Node( is_switch=False ) )
        self.add_node( rightHost2, Node( is_switch=False ) )

        # Add edges
        self.add_edge( leftHost1, leftSwitch )
	self.add_edge( leftHost2, leftSwitch )
        self.add_edge( leftSwitch, rightSwitch )
        self.add_edge( rightSwitch, rightHost1 )
	self.add_edge( rightSwitch, rightHost2 )

        # Consider all switches and hosts 'on'
        self.enable_all()

topos = { 'mytopo': ( lambda: MyTopo() ) } 
