from enum import IntEnum

class QurtionType(IntEnum):
    PRIVATE = 1
    PUBLIC = 2



QUESTION_TYPE = (
        (QurtionType.PRIVATE.value, 'Private'),
        (QurtionType.PUBLIC.value, 'Public'),
    )