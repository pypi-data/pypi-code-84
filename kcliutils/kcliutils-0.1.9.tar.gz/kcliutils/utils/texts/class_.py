# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Local
from .core_texts import class_
from .utils import comment_line, multi_replace
from .file_key import FileKey
from .file_value import FileValue

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- Public methods -------------------------------------------------------- #

def new_class(
    class_name: str,
    tab_size: int,
    comment_line_len: int
) -> str:
    return multi_replace(
        class_,
        {
            FileKey.CLASS_NAME: class_name,
            FileKey.COMMENT_LINE_CLASS_NAME: comment_line(
                FileValue.COMMENT_LINE_CLASS_NAME.value.format(class_name),
                line_len=comment_line_len
            )
        },
        tab_size=tab_size,
        comment_line_len=comment_line_len
    )


# -------------------------------------------------------------------------------------------------------------------------------- #