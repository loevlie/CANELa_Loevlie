Usage
=====

.. _installation:

Installation
------------

To use cp2k_helper, first install it using pip:

.. code-block:: console

   (.venv) $ pip install cp2k_helper

You should also be able to instal ce_expansion using the following code:

.. code-block:: console

   (.venv) $ pip install git+https://github.com/mpourmpakis/ce_expansion.git


Other dependencies include:

* ASE
* Click
* Pandas


Package Overviews
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

