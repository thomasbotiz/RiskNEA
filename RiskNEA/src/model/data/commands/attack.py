from dataclasses import dataclass
from ....utils import Command, ExplicitEvent
from __future__ import annotations

class Territory():
    pass

class Game():
    pass

class AttackCommand(Command):
    """
    The family of classes only allowed to execute during the Attack phase.
    """ 
    pass

class FocusOffensiveCommand(AttackCommand):
    def __init__(self, territory_from : Territory, territory_to: Territory):
        """
        A command to set the focus of attack between two territories

        Parameters
        ----------
        territory_from : Territory
            The territory the attack is commenced from
        territory_to : Territory
            The defending territory being captured 
            
        Attributes
        ----------
        territory_from : Territory
            The territory the attack is commenced from
        territory_to : Territory
            The defending territory being captured 
        """
        pass
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to create a front between the desired territories 

        Parameters
        ----------
        game : Game 
            The instance of Game being executed on

        Returns
        -------
        str 
            The accompanying error message(None assumes valid)

        Notes
        -----
        FocusOffensiveCommand should validate if:

        territory_from is owned by the current turn player and has more
        than one unit

            AND

        territory_to is owned by an opponent player and is contiguous to 
        territory_from
        """
        
    def execute(self, game: Game) -> FocusOffensiveEvent:
        """
        Sets the active attack of State between the desired territories

        Attributes
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        FocusOffensiveEvent
            Data on what was changed in `Game`  

        Notes
        -----
        When creating OffensiveFront object, should set the attacking dice
        and defending dice to max possible, set loss_threshold
        to 0. Do not emit a separate event to relay this. 
        """
        pass

@dataclass
class FocusOffensiveEvent(ExplicitEvent):
    """
    An event emitted when the player focuses on a front 

    Attributes
    ----------
    success : bool
        True if the offensive was successfully changed
    error : str
        The accompanying error message from _validate()
    player_from : Player
        The player commencing the attack
    player_to : PlayerName
        The defending player's name 
    territory_from : Territory
        The territory the attack is commenced from
    territory_to : Territory
        The territory under attack 
    attacker_dice : int
        The number of dice the attacker is using
    defender_dice : int 
        The number of dice the defender is using     
        """

class CancelFocusOffensiveCommand(AttackCommand):
    def __init__(self):
        """
        A command to forget the front being focused on
        Attributes
        ----------
        success : bool
            True if front was successfully set to None
        error : str
            The accompanying error message from _validate()
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to cancel the front in State 

        Parameters
        ----------
        game : Game 
            The instance of Game being executed on

        Returns
        -------
        str 
            The accompanying error message(None assumes valid)

        Notes
        -----
        CancelFocusOffensiveCommand should validate if:

        front is defined as anything except None 
        """
    
    def execute(self, game: Game) -> CancelFocusOffensiveEvent:
        """
        Sets front in State to None 

        Attributes
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        CancelFocusOffensiveEvent
            Data on what was changed in `Game`  

        Notes
        -----
        Modifies State's front by interacting with the interface, overwriting 
        if necessary 
        """
        pass

@dataclass
class CancelFocusOffensiveEvent(ExplicitEvent):
    """
    An event emitted when a player cancels a front 

    Attributes
    ----------
    success : bool
        True if the offensive was successfully changed
    error : str
        The accompanying error message from _validate()
    """

class AttackManualCommand(AttackCommand):
    def __init__(self):
        """
        A command to simulate one round of combat in front
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Attributes
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        AttackManualCommand should validate if: 

        front is defined in state

        Note that all validation occurs when selecting the front
        in the first place.
        """

    def execute(self, game: Game) -> AttackManualEvent:
        """
        Simulates a round of battle between the territories
        if valid 

        Parameters
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        AttackManualEvent
            Data on what was changed in `Game`  

        Notes
        -----
        Modifies State's front by interacting with the interface, overwriting 
        if necessary.
        """
        pass

@dataclass
class AttackManualEvent(ExplicitEvent):
    """
    An event emitted after a manual battle command is executed

    Attributes
    ----------
    success : bool
        True if the battle successfully occured
    error : str
            The accompanying error message from _validate()
        player_from : Player
            The player commencing the attack
        player_to : Player
            The player defending
        territory_from : Territory
            The territory the attack is commenced from
        territory_to : Territory
            The territory under attack 
        attacker_dice_rolled : List[int]
            The values of the attacker's dice sorted in descending order
        defender_dice_rolled : List[int]
            The values of the defender's dice sorted in descending order
        attacker_units_lost : int 
            The number of units removed from the attacking territory
        defender_units_lost : int 
            The number of units removed from the defending territory 
    """
    pass

class AttackSimulateCommand(AttackCommand):
    def __init__(self):
        """
        A command to simulate battle in the front 
        until the attack is successful, repelled
        or meets the loss threshold 
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Attributes
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        AttackSimulateCommand should validate if: 

        front is defined in state

        Note that all validation occurs when selecting the front
        in the first place.
        """

    def execute(self, game: Game) -> AttackSimulateEvent:
        """
        Simulates battle between the territories
        if valid until the attack is repelled,
        successful or meets the loss threshold

        Attributes
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        AttackManualEvent
            Data on what was changed in `Game`  

        Notes
        -----
        Should stop when front's loss threshold is met, 
        the defending territory has zero units left, the attacking
        territory has 1 unit left, or the attacking territory
        has less than or equal to the loss threshold 

        Should calculate the winner of the battle immediately,
        not create a list of arrays. Could be changed in the 
        future. 
        """
        pass

@dataclass
class AttackSimulateEvent(ExplicitEvent):
    """
    An event emitted after a manual battle command is executed

    Attributes
    ----------
    success : bool
        True if the battle successfully simulated
    error : str
        The accompanying error message from _validate()
    player_from : Player
        The player commencing the attack
    player_to : Player
        The player defending
    territory_from : Territory
        The territory the attack is commenced from
    territory_to : Territory
        The territory under attack 
    attacker_units_lost : int
        The number of units removed from the attacking territory
    defender_units_lost : int 
        The number of units removed from the defending territory 

    Notes
    -----
    Information about which player won is already
    handled by an Implicit Event.
    """
    pass

class AttackChangeAttackerDiceCommand(AttackCommand):
    def __init__(self, count: int):
        """
        A command to change the number
        of dice the attacker uses in the front
        
        Attributes
        ----------
        count : int
            The new number of dice for the attacker
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Parameters
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        AttackChangeAttackerDice should validate if: 

        front is defined in state

            AND

        count is within a valid range

        Notes
        -----
        The valid range of count should factor in how many 
        units the attacking player has.

        Should also display the maximum number of dice allowed
        in the error message if applicable
        """
    
    def execute(self, game: Game) -> AttackChangeAttackerDiceEvent:
        """
        Changes the number of dice the attacking player is using

        Parameters
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        AttackChangeAttackerDiceEvent
            Data on what was changed in `Game`
        """

@dataclass
class AttackChangeAttackerDiceEvent(ExplicitEvent): 
    """
    An event emitted after the attacker changes their dice count
    
    Attributes
    ----------
    success : bool
        True if the dice successfully changed
    error : str
            The accompanying error message from _validate()
    player : Player
        The player changing their dice
    new_count : int
        The new number of dice being used 
    """

class AttackChangeDefenderDiceCommand(AttackCommand):
    def __init__(self, count: int):
        """
        A command to change the number
        of dice thed defender uses in the front
        
        Attributes
        ----------
        count : int
            The new number of dice for the defender
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Parameters
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        AttackChangeDefenderDiceCommand should validate if: 

        front is defined in state

            AND

        count is within a valid range

        Notes
        -----
        The valid range of count should factor in how many 
        units the attacking player has.

        Should also display the maximum number of dice allowed
        in the error message if applicable
        """
    
    def execute(self, game: Game) -> AttackChangeDefenderDiceEvent:
        """
        Changes the number of dice the defending player is using

        Parameters
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        AttackChangeAttackerDiceEvent
            Data on what was changed in `Game`
        """

@dataclass
class AttackChangeDefenderDiceEvent(ExplicitEvent): 
    """
    An event emitted after the defender changes their dice count
    
    Attributes
    ----------
    success : bool
        True if the dice successfully changed
    error : str
            The accompanying error message from _validate()
    player : Player
        The player changing their dice
    new_count : int
        The new number of dice being used 
    """

class AttackChangeLossThresholdCommand(AttackCommand):
    def __init__(self, new_threshold: int):
        """
        A command to change the loss threshold of the attacker
        
        Attributes
        ----------
        The new attack threshold before stopping simulation
        """
    
    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Attributes
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        AttackChangeLossThresholdCommand should validate if: 

        front is defined in state

            AND
        
        loss_threshold is less than or equal to the number of 
        attacking units
        """
    
    def execute(self, game: Game) -> AttackChangeLossThresholdEvent:
        """
        Simulates battle between the territories
        if valid until the attack is repelled,
        successful or meets the loss threshold

        Attributes
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        AttackChangeLossThresholdEvent 
            Data on what was changed in `Game`  

        Notes
        -----
        Should stop when front's loss threshold is met, 
        the defending territory has zero units left, the attacking
        territory has 1 unit left, or the attacking territory
        has less than or equal to the loss threshold 

        Should calculate the winner of the battle immediately,
        not create a list of arrays. Could be changed in the 
        future. 
        """
        pass

@dataclass
class AttackChangeLossThresholdEvent(ExplicitEvent):
    """
    An event emitted after the loss threshold is changed

    Attributes
    ----------
    success : bool
        True if the battle successfully simulated
    error : str
        The accompanying error message from _validate()
    player_from : Player
        The player commencing the attack
    loss_threshold : int
        The new loss threshold 
    """

class PlaceUnitAttackCommand(AttackCommand):
    def __init__(self, territory_placed_on : Territory, count: int):
        """
        A command to recruit a unit to a territory
        
        Attributes
        ----------
        territory_placed_on : Territory
            The territory being placed on
        count : int
            The number of units being placed
        """
        pass

    def execute(self, game: Game) -> PlaceUnitAttackEvent:
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
class PlaceUnitAttackEvent(ExplicitEvent):
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

class AttackTradeSetCommand(AttackCommand):
    def __init__(self):
        """
        A command to trade in a set of cards
        
        Attributes
        ----------
        Cards : List[Card]
            The cards being traded in by the player
        """
        pass

    def execute(self, game: Game) -> AttackTradeSetEvent:
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
class AttackTradeSetEvent(ExplicitEvent):
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

class FortifyCapturedTerritoryCommand(AttackCommand):
    def __init__(self, units_transferred: int):
        """
        A command to transfer units from an attacking
        territory to a defending territory once captured

        units_transferred : int
            The number of units transferred from the attacking
            territory to the captured territory
        """
        pass

    def _validate(self, game: Game) -> str:
        """
        Checks if it is legal to call the command
        
        Attributes
        ----------
        game : Game
            The instance of Game being executed on
        
        Returns
        -------
        str
            The accompanying error message(None assumes valid)

        Notes
        -----
        FortifyCapturedTerritoryCommand should validate if: 

        front is defined in state and expecting_transfer is true

            AND
        
        units_transferred is greater than or equal to the number
        of attacking dice used and results in the transferring
        territory having one or more units left 
        """
    
    def execute(self, game: Game) -> FortifyCapturedTerritoryEvent:
        """
        Transfers units from the defending territory
        to the attacking territory

        Attributes
        ----------
        game : Game
            The instance of Game being executed on 
        
        Returns
        -------
        FortifyCapturedTerritoryEvent
            Data on what was changed in `Game`  

        Notes
        -----
        Should set front in State to None after transferring.
        """
        pass

@dataclass
class FortifyCapturedTerritoryEvent(ExplicitEvent):
    """
    An event emitted after a captured territory is reinforced
    
    Attributes
    ----------
    success : bool
        True if the battle successfully simulated
    error : str
        The accompanying error message from _validate()
    player_from : Player
        The player commencing the attack
    territory_from : Territory
        The territory the attack was commenced from
    territory_from_units : int
        The new number of units on the transferring territory
    territory_to_units : int
        The new number of units on the captured territory
    territory_to: Territory
        The territory that was captured
    units_transferred : int
        The number of units transferred from territory_from
    """

    