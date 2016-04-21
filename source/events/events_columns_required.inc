* ``EVENT_ID`` type: int
    * Event identification number at the DL3 level (lower data levels could be different, see note below).
    * Required: The pair (``OBS_ID``, ```EVENT_ID``) must be globally unique for all events from a given instrument. (to be discussed ... it's not clear if CTA will have 'runs' ``OBS_ID``).
    * Required: ``EVENT_ID`` should increase monotonically with ``TIME``. (to be discussed if this should be changed to a recommendation only)
    * Required: event lists should be sorted by ``EVENT_ID`` and ``TIME``. (to be discussed if this should be changed to a recommendation only)