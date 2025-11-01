from ....utils import Command, ExplicitEvent
from dataclasses import dataclass
from __future__ import annotations

class Game:
    pass

class Territory:
    pass

class SaveCommand(Command):
    def __init__(self, filename: str):
        """
        A command to save the game to /saves

        Parameters
        ----------
        filename : str
            The name of the file being saved.

        Attributes
        ----------
        filename : str
            The name of the file being saved.
        
        Notes
        -----
        Should overwrite the file if present
        """

    def _validate(self):
        """
        Checks if the command is valid to call or not

        Notes
        -----
        Normal Commands are handled by State, rather than
        Command. SaveCommand should validate in any State 
        at any time EXCEPT in the attack phase where the 
        game is expecting a transfer of units or a trade in
        of a set. 
        """
    
    def execute(self):
        """
        No logic for meta commands

        Notes
        -----
        State itself should act on meta-level commands. 
        """

@dataclass
class SaveEvent(ExplicitEvent):
    """
    Event emitted when a player saves the game

    Attributes
    -------
    success : bool
        True if the offensive was successfully changed
    error : str
        The accompanying error message from _validate()
    filename : str
        The name of the file that was just saved
    """

class LoadCommand(Command):
    def __init__(self, filename: str):
        """
        A command to load a game from /saves with filename

        Parameters
        ----------
        filename : str
            The name of the file being saved.

        Attributes
        ----------
        filename : str
            The name of the file being saved.
        
        Notes
        -----
        Should overwrite the file if present
        """

    def _validate(self):
        """
        Checks if the command is valid to call or not

        Notes
        -----
        Always valid to call. 
        """
    
    def execute(self):
        """
        No logic for meta commands

        Notes
        -----
        State itself should act on meta-level commands. 
        """

class LoadEvent(ExplicitEvent):
    """
    Event emitted when a player saves the game

    Attributes
    -------
    success : bool
        True if the offensive was successfully changed
    error : str
        The accompanying error message from _validate()
    filename : str
        The name of the file that was just saved
    """

class NextTurnCommand(Command):
    def __init__(self):
        """
        A command to load a game from /saves with filename
        """

    def _validate(self):
        """
        Checks if the command is valid to call or not

        Notes
        -----
        See each accompanying state for when the command
        is valid. 
        """
    
    def execute(self):
        """
        No logic for meta commands

        Notes
        -----
        State itself should act on meta-level commands. 
        """

class NextTurnEvent(ExplicitEvent):
    """
    Event emitted when a player saves the game

    Attributes
    -------
    success : bool
        True if the offensive was successfully changed
    error : str
        The accompanying error message from _validate()
    """

@dataclass
class RecruitUnitCommand(Command):
    def __init__(self, territory_placed_on : Territory, count: int):
        """
        A command to recruit a unit to a territory
        
        Attributes
        ----------
        territory_placed_on : Territory
            The territory being placed on
        count : int
            The number of units being placed

        Notes
        -----
        Always valid in the recruitment phase. 

        Valid in the attack phase when units_left is greater
        than 0
        """
        pass

    def execute(self, game: Game) -> RecruitUnitEvent:
        """
        Places units on the desired territory

        Attributes
        ----------
        game : Game
            The instance of Game being placed on
        
        Returns
        -------
        PlaceUnitAttackEvent
            Data on what was changed in `Game` 
        
        success : bool
            True if the units were placed successfully
        error : str
            The accompanying error message from _validate()
        player : Player
            The player who issued the command 
        units_placed : int
            The number of units placed
        """
        pass
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to place the units 
        on the territory
        
        Returns
        -------
        str
            The accompanying error message from all failed checks
        
        Notes
        -----
        `territory_placed_on` must be owned by the current turn player 

            AND 
        
        `count` is bigger than zero and results in `units_placed` being zero or greater
        """
        pass

@dataclass
class RecruitUnitEvent(ExplicitEvent):
    """
    Event emitted when the player place unit to a territory
    in their attack phase

    Attributes
    ----------
    success : bool
        Whether the command successfully executed
    error : str
        The error message that came with the failed command(None assumes success)
    player : Player
        The player who issued the recruitment command
    territory_placed_on : Territory
        The territory that a unit was recruited on
    units_placed : int
        The number of units placed on the territory
    """

class TradeSetCommand(Command):
    def __init__(self):
        """
        A command to trade in a set of cards
        
        Attributes
        ----------
        Cards : List[Card]
            The cards being traded in by the player
        """
        pass

    def execute(self, game: Game) -> TradeSetEvent:
        """
        Add the corresponding number of units to a player's
        `unplaced_units` if the cards are valid 

        Returns
        -------
        AttackTradeSetEvent
            Data representing the change made to `Game`
        
        success : bool
            True if cards were validated else false
        error : str
            Accompanying error message if success is False
        player : Player
            The player who issued the command to trade in the set
        set_traded_in : list[Card]
            The set that was just traded in 
        
        Notes
        -----
        Should use `Games` interface to calculate how many units
        the set is worth 
        """
        pass

    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to trade in the set of cards
        
        Returns
        -------
        str
            The accompanying error message(None assumes command is valid)

        Notes
        -----
        TradeSetAttackCommand would fully validate if: 

        There are three cards in `Cards`.

            AND 

        The current player owns all three of those cards.

            AND 

        The cards combine to form a valid set.
        """
        pass

@dataclass
class TradeSetEvent(ExplicitEvent):
    """
    An event emitted after AttackTradeSetCommand is called
    
    Attributes
    ----------
    success : bool
        Whether the command successfully executed
    error : str
        The error message that came with the failed command(None assumes success)
    player : Player
        The player who issued the recruitment command
    set_traded_in : list[Card]
        The cards that were traded in
    units_received : int
        The units received at the start of the turn/from trading in the set
    """
    pass