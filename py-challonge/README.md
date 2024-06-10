# Challonge Match Parser

This Python program reads a tourney page from Challonge and parses all matches from it. Currently compatible with Double Elimination and Swiss brackets.

## General info

- Make sure you get the `.svg` URL for the bracket without the language locale.
    - Format: `https://challonge.com/{bracket-id}.svg`
- The match output might break if there's no score in one of the matches of the event.

## Formatting options

- **Option 0.** Outputs the matches as `Match N ~ Player 1 | ScoreP1 : ScoreP2 | Player 2`
- **Option 1.** Outputs the matches as `MatchNumber | Player1 | SeedP1 | Player1 | ScoreP1 | Player2 | SeedP2 | Player2 | ScoreP2`
- **Option 2.** Outputs the matches as `SeedP1 | Player1 | ScoreP1 | ScoreP2 | Player2 | SeedP2 | MatchNumber`