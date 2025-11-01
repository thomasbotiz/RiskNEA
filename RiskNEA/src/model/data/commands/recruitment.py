from dataclasses import dataclass
from ....utils import Command, ExplicitEvent
from __future__ import annotations


class RecruitmentCommand(Command):
    """
    The family of classes only allowed to execute during the Recruitment phase.
    """
    pass

"""
Note that all recruitment commands (trade set, recruit units) is also shared
by AttackState, so these commands must be made agnostic. 

"""
