# Dynamic Host Blocking System (SDN)

This project uses SDN and POX controller to dynamically block malicious hosts.

## Files
- topology/topo.py → Network topology
- dynamic_block_pox.py → Controller logic
- topology.pdf → Network diagram

## How to run
1. Run POX:
   ./pox.py misc.dynamic_block_pox

2. Run Mininet:
   sudo python topology/topo.py
