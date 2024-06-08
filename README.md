# deploy-lanparty

Lightweight script that deploys LAN compatible games to a Linux host.

## Games

This script will install the following freely available games:

- [Sonic Robo Blast 2 Kart](https://www.wiki.srb2.org/wiki/SRB2Kart)

This script can also install the following titles **if** you provide your own game data:

- [Counter-Strike 1.6](https://store.steampowered.com/app/10/CounterStrike)
- [ioquake3](https://ioquake3.org)
- [OpenRA](https://www.openra.net)
- [OpenRCT2](https://openrct2.org)
- [StarCraft: Brood War Classic](https://en.wikipedia.org/wiki/StarCraft:_Brood_War)

## Providing Game Data

This script is capable of installing games that require you to provide your own game data.

To provide your own game data place a zip file for each game in a folder and provide the folder's path to the script.
Example:

```none
$ ls ~/my_game_data
counterstrike-16.zip  quake3.zip  openra.zip
```

```bash
./src/main.py ~/my_game_data
```

#### Counter-Strike 1.6

1. Purchase [Counter-Strike 1.6](https://store.steampowered.com/app/10/CounterStrike) from Steam
2. Install the Windows version of Counter-Strike 1.6 using Steam,
   if you are on Linux you will need to force usage of Proton to download the Windows version of the game
3. Locate Counter-Strike 1.6 in your Steam library, right click on it, click Manage, and then click Browse local files
4. You should now see the contents of the `Half-Life` game folder which should also contain a `cstrike` folder
5. Browse up one level so that you can see the `Half-Life` game folder and folders for any other Steam games
6. Compress the `Half-Life` game folder into a zip file called `counterstrike-16.zip`
7. Place the `counterstrike-16.zip` zip file in your game data folder

#### ioquake3

1. Purchase Quake 3 from [Steam](https://store.steampowered.com/app/2200/Quake_III_Arena)
   or [GOG](https://www.gog.com/game/quake_iii_arena)
2. Install Quake 3
3. Browse to the Quake 3 game files and locate the `baseq3` and `missionpack` folders within
4. Compress the `baseq3` and `missionpack` folders into a zip file called `quake3.zip`
5. Place the `quake3.zip` zip file in your game data folder

#### OpenRA

OpenRA can install its own game data but if you want to provide your own follow these steps:

1. Install [OpenRA](https://www.openra.net)
2. Launch an OpenRA game such as 'OpenRA - Red Alert'
3. Follow the in game wizard to import game data, you can provide data from disks or download a lite version
4. Repeat steps 2 and 3 for each OpenRA game you want to configure
5. Browse to your OpenRA game data folder, this should contain a `Content` folder among other things
6. Compress the `Content` game folder into a zip file called `openra.zip`
7. Place the `openra.zip` zip file in your game data folder

#### OpenRCT2

1. Purchase [RollerCoaster Tycoon 2](https://www.gog.com/game/rollercoaster_tycoon_2) from GOG
2. Download the offline installer for RollerCoaster Tycoon 2 from GOG
3. Install [OpenRCT2](https://openrct2.org)
4. Launch OpenRCT2 and when prompted select the GOG installer file
5. Browse to your OpenRCT2 game data folder, this should contain an `rct2` folder among other things
6. Compress the `rct2` game folder into a zip file called `openrct2.zip`
7. Place the `openrct2.zip` zip file in your game data folder

#### StarCraft: Brood War

1. Install [StarCraft: Brood War](https://en.wikipedia.org/wiki/StarCraft:_Brood_War) Classic from CD, etc.
2. Install any patches that you want, see: https://archive.org/details/StarCraftPatches
3. Browse to your StarCraft game data folder
4. Browse up one level so that you can see the `StarCraft` game folder
5. Compress the `StarCraft` game folder into a zip file called `starcraft-bw.zip`
6. Place the `starcraft-bw.zip` zip file in your game data folder
