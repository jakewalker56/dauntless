# dauntless
sc2 bot

# Manifesto

1. Humans don't operate at the click level, they operate at the outcome level, and sucessful modeling of gameplay will first model desired outcomes, and then build models to achieve those outcomes.

2. Componentize everything, write manual modules for obvious things, and let RL learn things RL is good at

3. Game abstraction is part of feature engineering, and the most important part of how humans think about RTS games

4. Minimize end-to-end training.  Put networks in a situation to learn what you want them to learn, not to repeat the beginning of the game a million times (e.g. put a network in the position of having storm and a bunch of high templar agains all kinds of oponents)

5. Mechanics != micro

6. Training is a pipeline.  First we train our mechanics, then we train our ability to micro, then we train a macro engine to get us into situations our micro can win.  But also we can use replay data for a baseline of what is in the meta and just train toward that

7. You cannot win at starcraft without memory

8. There is no obvious structure for executing things in paralell with a sequential series of commands (e.g. do economy stuff in the background while also microing)

9. Embeddings are more important than outcomes
