# Bulbapedia Web Scraper

Attached is a python script to web scrape [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page). The repository also includes the .csv file of the Pokemon's stats.

**Credits:**
- [Nick Bely](https://github.com/nbely)
- Original Author: [Ryan Luu](https://github.com/ryanluuwas) ([Original Repo](https://github.com/ryanluuwas/Bulbapedia-Web-Scraper))


**Issues:**
- While the Web Scraper is fully functional as of this commit, it's possible that functionality may break from changes to Bulbapedia's page layout or from the addition of new Pokemon mechanics and gimmicks.
- It is also possible that there are details the current implementation may have missed.
- If you come across any broken behavior or incorrect data, please feel free to [Create an Issue](https://github.com/nbely/Bulbapedia-Pokedex-Web-Scraper/issues) and I will address it at my earliest convenience.

___

**Objective**

The purpose of this repository is to collect the data of each pokemon and store it into a .csv file for any upcoming and potential trivial projects.

___

**Quick Start Guide**

1. Setup Python on your machine ([Windows Setup](https://docs.python.org/3/using/windows.html)) ([Mac Setup](https://docs.python.org/3/using/mac.html))
2. Clone this repository
3. Open a terminal and navigate to the 'Script' folder in this Repository
4. Enter the command: `python ws_bulbapedia.py` (or `python3 ws_bulbapedia.py` if `python` is not recognized)

___

**About the Data**

The .csv file includes the following:
1. Dex No.
2. Name
3. Forme Name (Blank if none)
4. Classification
5. Generation
6. Primary Typing
7. Secondary Typing (Blank if none)
8. Ability 1
9. Ability 2 (Blank if none)
10. Hidden Ability (Blank if none)
11. Gender Assignment (Blank if always true)
12. Gender Male Ratio (Blank if Gender Assignment is Unknown (N))
13. Gender Female Ratio (Blank if Gender Assignment is Unknown (N))
14. Catch Rate
15. Egg Group 1 (Blank if none)
16. Egg Group 2 (Blank if none)
17. Hatching Time in Cycles
18. Height in Inches
19. Height in Meters
20. Weight in Pounds
21. Weght in Kilograms
22. Mega Stone 1 (Blank if none)
23. Mega Stone 2 (Blank if none)
24. EXP Yield (Gen I) (Blank if none)
25. EXP Yield (Gen II) (Blank if none)
26. EXP Yield (Gen III) (Blank if none)
27. EXP Yield (Gen IV) (Blank if none)
28. EXP Yield (Gen V+)
29. Leveling Rate
30. EV Yield for HP
31. EV Yield for Attack
32. EV Yield for Defense
33. EV Yield for Special Attack
34. EV Yield for Special Defense
35. EV Yield for Speed
36. Shape Image URL
37. Footprint Image URL ('?' Image if not from Gen I-V)
38. Base Friendship
39. Base HP Stats (Pipe-Separated by Generation)
40. Base Attack Stat (Pipe-Separated by Generation)
41. Base Defense Stat (Pipe-Separated by Generation)
42. Base Special Attack Stat (Pipe-Separated by Generation)
43. Base Special Defense Stat (Pipe-Separated by Generation)
44. Base Speed Stat (Pipe-Separated by Generation)
45. Base Total Stats (Pipe-Separated by Generation)
46. Color
