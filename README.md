# UNIDIE_API
## A Universal Dice Roller

I tried to find some good dice rollers out there and decided to make my own. I realize it's not perfect but with a little work, I think this little project can become the defacto RPG dice rolling kit for EVERYONE!!!

What's important to remember with this roller is that it doesn't just do all the work behind the scenes and hand you a result that you may have to work backwards from to figure out what happened.  The classes work together to provide you with a list datatype of all the die rolls and the order they happened along with modifiers and die types. The final Results() object is the presenter. It doesn't make any changes to the rolls, just gives you the tools to read the results.

## Class Results(tuple)
This baby is all the best parts of tuples, because I borrowed (inherited) from the builtin. I wanted to have an immutable list of values and sets are a little too prim, they only like unique values between their... brackets. 

there are no methods attached to Results, only @property's as we don't want to make changes, just give the user a couple new tools for presenting the results.

## Builder Classes:
### Unidie
Will roll any qty of die from d4 to d100 and give you all the rolls in a Result object.

### Savage(Unidie)
Same as Unidie but it changes the rolling mechanic by including EXPLODING DICE. Like kittens but less fur.
If at any time, your die rolls a MAX value (ie a 6 on d6), the roller keeps the MAX value and rolls again, adding the new value to the total. So even though you only have a d4 in shooting, you could potentially achieve a 25 or higher on your result before modifiers!!

### die_pool
Some systems don't care what your rolls are as long as they are either MAX or MIN values. Like Forbidden Lands. My necromancer has 5 in wits, that means I roll 5d6 and count all the 6's. If I 

### Forbidden
Forbidden Lands has a special die roll similar to the d100 or percentile die but they only use 2 d6's for both the 10's and 1's place so you get values like
11 - 16, 21 - 26 ... 61 - 66. Wierd, but ok. I made that work.


# Future
* Future: will include error raising for using d20's in Savage World's since that system doesn't use them.
* Future: Include stats logging of all die rolls... stats for nerds yo!
* Future: give the Results class the ability to PUSH as per Forbidden Lands protocols, which means to BANK the successes & failures and re-roll anything left over to try and get more successes. Kinda like Yahtzee. Maybe I'll have the Forbidden class stamp all it's results with a special boomarang method so results can call back to it!!  {:O


_Thanks for reading_
*** Friar Greg ***
