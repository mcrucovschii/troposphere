# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import tags_or_list


def validate_tags_or_list(x):
    """
    Property: AppBlock.Tags
    Property: Application.Tags
    Property: Fleet.Tags
    Property: ImageBuilder.Tags
    Property: Stack.Tags
    """
    return tags_or_list(x)
