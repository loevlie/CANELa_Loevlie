Usage
=====

.. _installation:

Installation
------------

To use *cp2k_helper*, first install it using pip:

.. code-block:: console

   (venv) $ pip install cp2k_helper

You should also be able to instal *ce_expansion* using the following code:

.. code-block:: console

   (venv) $ pip install git+https://github.com/mpourmpakis/ce_expansion.git

Finally, you can install my package from Demystifying the Chemical Ordering of Polymetallic Nanoparticles.
It's a wrapper around ce_expansion with some extra functionality.

.. code-block:: console

   (venv) $ git clone https://github.com/mpourmpakis/CANELa_NP.git
   (venv) $ cd CANELA_NP
   (venv) $ pip install -e .


Other dependencies include:

* ASE
* Pandas
* Numpy 
* Matplotlib
* Lxml (for web scraping)
* molgif



Package Overviews
----------------


CANELa_NP
^^^^^^^^^^


Importing packages:

.. code-block:: python

   from CANELa_NP.Nanotools import Nanoparticle
   import ase.cluster as ac

Creating a bimetallic ase atoms object:

.. code-block:: python

   atoms = ac.Icosahedron('Au', 5)
   atoms.symbols[100:] = 'Pd'

Creating a nanoparticle object:

.. code-block:: python

   NP = Nanoparticle(atoms)

Visualizing the non-optimized chemical ordering:

.. code-block:: python

   NP.core_shell_plot()

.. image:: ../../README_Notebook_10_0.png
   :align: center

Optimizing the chemical ordering with a genetic algorithm:

.. code-block:: python

   NP.run_ga(max_gens=-1,max_nochange=1_000)

.. code-block:: console

   --------------------------------------------------
   GA Sim for Au100Pd209 - none:
   Min: -3.66177 eV/atom -- Gen: 02840
   Form: Au100Pd209
   nAtom: 309
   nGens: 2840
   Start: -3.44202 eV/atom
   Best: -3.66177 eV/atom
   Diff: -0.21974 eV/atom (6.38%)
   Mute: 80.0%
   Pop: 50
   Time: 0:00:28
   --------------------------------------------------
   Saving optimized structure...
   Done!

Visualizing the optimized chemical ordering (full NP):

.. code-block:: python

   NP.core_shell_plot()

.. image:: ../../README_Notebook_14_0.png
   :align: center

.. tab-set::

   .. tab-item:: Molgif 
            
            .. code-block:: python
      
                  NP.view(rotate=True,path="full_np.gif")
      
            .. image:: ../../Au100Pd209.gif
               :align: center

   .. tab-item:: ASE GUI
         
         .. code-block:: python
   
            NP.view()
   
         .. image:: ../../full_np.png 
            :align: center


Visualizing the optimized chemical ordering (X-Cut NP):

.. tab-set::

   .. tab-item:: Molgif 
            
            .. code-block:: python

                  NP.view(cut=True,rotate=True,path="half_np.gif")
      
            .. image:: ../../half_np.gif
               :align: center

   .. tab-item:: ASE GUI
         
         .. code-block:: python
   
            NP.view(cut=True)
   
         .. image:: ../../half_np.png 
            :align: center

   


Working with your own structure files

.. code-block:: python

   xyz_file = "Example_data/AuPdPt.xyz"
   NP = Nanoparticle(xyz_file)
   NP.core_shell_plot()


.. image:: ../../README_Notebook_23_0.png

#########################################
Calculating New Gamma Values
######################################### 


If you would like to generate gamma values for metal combinations that have not been done yet please follow the following steps from the publication Demystifying the Chemical Ordering of Multimetallic Nanoparticles by Dennis Loevlie, Brenno Ferreira, and Giannis Mpourmpakis.

1. Generate equally distributed NP xyz files using the script: `generate_nps <https://github.com/mpourmpakis/CANELa_NP/blob/main/CANELa_NP/Setup_NPs_for_DFT.py>`_
2. Geometrically optimize these structures to find the most stable energy.
3. Use this `script <https://github.com/mpourmpakis/CANELa_NP/blob/main/CANELa_NP/Gamma_Value_Calc.py>`_ with the optimized energy values and previously generated structures to calculate the new gamma values (they will be stored in "CANELa_NP/Data/np_gammas.json").  


Above I have provided code to calculate new gamma values for metal combinations we do not currently have already.  Please keep in mind that this was the code that worked for my system, I have not tested it on other systems.  I have attempted to make the code general but if you are testing other systems please update the code accordingly. 

.. list-table:: Metals that have NP gamma values calculated for them
   :widths: 35 35 35
   :header-rows: 1

   * - Metal Type
     - Validated with literature?
     - Functional
   * - Au
     - Yes
     - PBE + D3
   * - Pd
     - Yes
     - PBE + D3
   * - Pt
     - Yes
     - PBE + D3
   * - Ag
     - No 
     - PBE + D3
   * - Cu
     - No
     - PBE + D3


cp2k_helper
^^^^^^^^^^^^^

This package is a collection of functions that I use to parse and analyze CP2K output files. 

############################################################################################
Code Overview
############################################################################################

.. automodule:: cp2k_helper.cp2k_helper
   :members:
   :undoc-members:
   :show-inheritance:

############################################################################################
Example Usage
############################################################################################

**Uses**

* Retreive information from the output files generated after running a calculation using cp2k.

**Important Note**

* The class will retrieve all information under the given directory (with a max depth as an optional extra argument) and use the directory names to classify each calculation you ran. Therefore, you should not have two separate cp2k calculations with the same directory name.

**Example**

The output will be a dictionary of dictionaries (Containing the single point Energy calculations and Geometric optimization final energies found under the specified directory)

.. code-block:: python

   from cp2k_helper import output_parser
   # Depth automatically set to inf
   parser = output_parser(base_file_path='./cp2k') 
   # If all=False then only the final energies will be retrieved
   Energies = parser.get_energies(all=False) 
   print(Energies)

Output:

.. code-block:: console

   {'ENERGY': defaultdict(float,
             {'Folder_Name1': -1000.997638482306,
              'Folder_Name2': -1000.997638482306,
              'Folder_Name6': -1000.900349392778}),
   'GEO_OPT': defaultdict(None,
               {'Folder_Name5': -1000.900349392778,
               'Folder_Name7': -1000.997638482306,
               'Folder_Name3': -1000.900349392778,
               'Folder_Name4': -1000.900349392778})}

**Note:**

* The output example has fake folder names and energy values for proprietary reasons.

Command line tools

**restart**

cp2k_helper has a handy command line tool for restarting a calculation if it timed out. Just execute the command below in the directory that the calculation timed out and a new subdirectory will be created for the new job. You can then submit the new job to restart the calculation.

.. code-block:: console

   (venv) $ cp2k_helper --restart

**summ**

cp2k_helper can give you a quick summary of your output file. Just use the command below with your output filename:

.. code-block:: console

   (venv) $ cp2k_helper --summ OPT.out


**energy**

cp2k_helper can quickly get you the final energy values from all GEO_OPT or ENERGY DFT calculations under a specified directory. The values are converted from Ha to eV. They are saved as a csv (optionally you may name it whatever you want but the default is Energies.csv). An example of using this feature for all of the calculations under the current folder is below:

.. code-block:: console

   (venv) $ cp2k_helper --energy . My_Energy_Values 

The above command will save a csv file to your current directory with all of the final energy values along with the type of calculation run and the folder name of each. As of now the .csv file will look similar to below (if you had 4 DFT calculations in the given directory).


.. list-table:: Energies.csv
   :widths: 25 25 50
   :header-rows: 1

   * - Folder_Name
     - Type
     - Energy (eV)
   * - Folder_Name1
     - GEO_OPT
     - -10000.34324
   * - Folder_Name2
     - ENERGY
     - -10000.34324
   * - Folder_Name3
     - GEO_OPT
     - -10000.34324