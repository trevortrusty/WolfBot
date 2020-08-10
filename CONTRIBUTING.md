# Contributing Guidelines
---
## Want to contribute to WolfBot's development?
You can go into the repository and propose changes if you feel that there's something that you can add or make better!

## Feel free to report issues or propose ideas for my dev team to implement in the Issues tab
### Join [WolfBot's discord server](https://discord.gg/eyd376A) to get help with using the bot or with the wolfram language, or if you would like to make suggestions


To clone this repo, follow these instructions from terminal:
 - ```git clone https://github.com/trevortrusty/WolfBot/```
 - create a file in the root directory called paths.py, and set the following python variables:
  ```py
  file = 'path/to/WolfBot'


  img_path = 'path/to/WolfBot/output/output.png'
  gif_path = 'path/to/WolfBot/output/output.gif'
  kernel_path = 'path/to/Wolfram Research/Wolfram Engine/12.0/WolframKernel.exe'
  cogs_path = './cogs'  # if this doesn't work, set it to the absolute path to the cogs folder instead
  wl_path = 'path/to/WolfBot/cogs/whitelist.csv'
  bl_path = 'path/WolfBot/cogs/blacklist.csv'
  ```
  
  - Next create a python script in the root directory called `BotToken.py`, 
    and set a variable `token_str` to a string containing your bot token.
 
 Use this set-up to test the bot in your own environment. Make sure the .gitignore file contains the namse of the BotToken.py and paths.py files before pushing any changes to your own branch
