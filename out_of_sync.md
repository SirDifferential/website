# The Network Connection Has Gone Out of Synch

Today we solved the dreaded Desynch Bug.

A bit over half a year ago we (Oldlaptop and I) discovered a new bug in the Shiver's Net Melee Balance Mod for Ur-Quan Masters. This was a particularly undesired occurrence since the bug was an Out of Synch error in net play and we had no idea on how the net code really worked in the core, and how to even begin debugging it. At a seemingly random point in an online match the two sides of the net connection would suddenly go out of synch and game would thus be terminated. This appeared without any discovered patterns and we were completely cluesless on where it originated from. Since we had no idea in what scenario it appeared and why it at times happened more often the debugging was gruesomely slow. We played a few games now and then and tried to record as much data as possible, but one can only do so much in a game where each test run lasts at least 30 minutes and may not produce any bugs for multiple games in row.

At a point we were somewhat certain, or possibly hopeful, that we had solved the issue. We had ended up playing about a ten games without the bug appearing after we had built the game using GCC 4.7.0. Proudly we released a patched version and organized a tournament.

About half of the games in the tournament ended with a desynch bug.

One of the culprits which we long suspected was the Pkunk respawn code. Pkunk Fury is a ship which always has a random chance of respawning, and the function by which this is done is somewhat complex. It was also one of the most uncertain changes which the mod does.

```
if (((TFB_Random () >> 10) % 100) < (INITIAL_RESPAWN_CHANCE - 1)
    - (StarShipPtr->static_counter * RESPAWN_CHANCE_DECREMENT))
        hPhoenix = AllocElement ();
```
   
What this says is:

If a random number shifted right by 10, and with the remainder to 100 is smaller than the initial respawn chance - 1 - the lifes the ship has already had multiplied by the respawn chance decrement, then respawn the ship. Or in simpler terms: Start with a high likelyhood of respawn, decrement by a set value each time the ship respawns.

Naturally since this was a huge eyesore we suspected there was obviously something fishy going on here. We spent a while debugging the random number generator (which is bundled in the source at src/libs/math/random.h) and investigated if it produced differing values: it did, after a desynch. To arrive to this conclusion we had to play a gruesome quantity of games just to get the bug appear. However, since the RNG uses the game's internal state for producing the seed it was not odd that the Out of Synch games would have differing RNG results. The tests finally showed us that the RNG was not at fault.

But then, what was?

SvdB of the UQM team originally wrote the net code for Ur-Quan Masters and offered some help to us. He told us how he had tested the checksum code when he first had written it:

1) Compile two versions of the game: One has a debug section enabled which artificially causes the game to run a bit behind in the net connection
2) Launch two instances, one running the laggy version
3) In the game that is running ahead, add a gdb breakpoint in the branch where the game announces that an OOS error has happened
4) Upon this breakpoint triggering, in the game that is running behind, add a breakpoint to the function which calculates the checksum
5) Now just step through the checksum code and see where a bit goes odd

We never saw the bug when testing.

Since we had never seen the bug in local network tests it was very hard to do these artificial delay tests over half the world (Finland -> Michigan). Oldlaptop did some artificial lag tests of his own, but never found the bug, so we arrived at the logical assumption that packet loss was somehow related to the issue. However, about a month ago I was testing something entirely different locally in two simultaneous game instances on localhost when I happened upon the bug. I was quite jubilant at this since it meant that debugging could be done without a slow connection that would cause the game to take hours to finish. Time went on, but I didn't find the bug again. Until one week ago I finally found a pattern.

One of the changes in Balance Mod is that Ilwrath, a ship with a cloaking generator, remains visible for the player who controls the ship while the other player sees nothing. In the original game the battle is designed to be played on hot-seat, so the cloaked Ilwrath is naturally invisible for even the controlling player. This is just silly over network, so Shiver changed this in the Balance Mod.

Now, what would happen if a, say, cloaked Ilwrath vessel was fired upon, and it was destroyed in this blast? It would then move on to the destruction function, reset some values, prepare the arena for a new ship, that sort of stuff... and play a death animation.

The Ilwrath's cloak is implemented as follows:

1) If the ship is visible, do nothing with the ship's overlay mask.
2) If the ship is cloaked, change the mask's colour to blue to the controlling player, and to black to the other player. Also change transparency for the mask to 0.
3) When the ship decloaks, turn the mask's transparency to 1.

The mask is a primitive shape called STAMPFILL_PRIM. This filled stamp primitive then has a colour. In this case, two colours are involved:

```
BUILD_COLOR (MAKE_RGB15 (0x00, 0x03, 0x1B), 0x00)   // INVIS_COLOR
BUILD_COLOR (MAKE_RGB15 (0x00, 0x00, 0x00), 0x00)   // BLACK_COLOR
```

After finally noticing this pattern I slapped my face hard at the massive lack of insight which we had had! It was obvious now that one side had differing values on his ship than the other: One side sees INVIS_COLOR while the other sees BLACK_COLOR. Why didn't we notice this earlier? Surely we had tested the multiplayer cloak a lot when it was first implemented, so it sounds odd that an error like this would make it to the release. Well, there were two reasons:

1) Originally in the first version of the mod this worked. The mod was later ported to UQM 0.7.0 which possibly chaged something in the animation, graphics or checksum code.
2) The bug does not appear in this match, but the following.

Point 2 here is the main issue. Every time the OOS happened, it usually was right at the start of the match. We had noticed earlier that the it occurred when a player pressed one of his movement keys. Of course we immediately started ruthless debugging for the ships that were involved in that match, not the one that occurred earlier. The thing is that while the Ilwrath's death animation is playing the two sides aren't sending any RNG based data to each other. But when new ships spawn the game is already in different states. As the bug manifested in the match that FOLLOWED Ilwrath we never quite figured out why seemingly random pairs of ships always produced the issue.

It didn't help that Star Control 2 code is C from the early 90s. The fix was [this](https://github.com/Roisack/Shiver-Balance-Mod/commit/c80bfe7544f53c662d88a33ed7b9b4b497eff78d).

