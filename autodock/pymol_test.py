from ipymol import viewer as pymol
pymol.start()   # Start PyMOL RPC server
pymol.fetch('3odu') # Fetch PDB
pymol.show_as('cartoon') # Show as cartoon
pymol.bg_color('white') # Set background color to white
pymol.display() # Show current display