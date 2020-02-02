# WolfBot
I'm a discord bot that runs Mathematica/Wolfram code and sends you the result quickly!

> Currently, we are not releasing the bot invitation here yet while we are still in development, but to learn more or use WolfBot, head over to our server: [WolfBot Discord Server](https://discord.gg/eyd376A)

My four current discord commands are

|Command|Description|
|--------|-----------------------------------------------------|
|- bark  | ***Takes in Wolfram code from you to be evaluated***|
|- alpha | ***Command that queries WolframAlpha.***| 
|- help  | ***Sends a message regarding the bot info, and the commands listed here with their syntax***|
|- docs  | ***Searches the Wolfram Language Documentation for you***|


## Using WolfBot
***Bark Command***
- Plot the graph of `E^x` from 0 to 5:
```
.bark Plot[E^x, {x, 0, 5}]
```
- Define a function `Sin[t]`, then graph the function from -π to π:
 ```
 .bark f[t_] = Sin[t]; 
Plot[f[x], {x, -Pi, Pi}]
```
***Alpha Command***
- Query Wolfram|Alpha
 ```
 .alpha Hello, how are you?
 ```

### Download our manual:
[Download](https://github.com/trevortrusty/WolfBot/raw/master/docs/man.pdf)
