List of marks I am ownership for:
=================================

Files:
------

* zimp.engine.gamestate
* zimp.ui.cligame
* zimp.ui.cmd_ui
* zimp.unittests.engine.gamestate

Features:
---------

__Shared:__
* Can deal with directories and file locations
* Provide doctests
* Provide unittests
* Provides object-persistence / object serialization using either pickle or shelve

__My own code:__
* Raises exceptions and provides exception handling<br/>
    This would be considered shared in terms of raises exceptions.<br/>
    However provides exception handling wasn't really.
* Has a line-oriented command interpreter based on cmd