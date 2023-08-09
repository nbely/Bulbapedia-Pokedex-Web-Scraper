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

**About the Data**

The .csv file includes the following:
1. Dex No.
2. Name
3. Forme Name
4. Classification
3. Generation
4. Primary Typing
5. Secondary Typing (Blank if none)
6. Ability 1
7. Ability 2 (Blank if none)
8. Hidden Ability (Blank if none)
9. Gender Assignment (Blank if always true)
10. Gender Male Ratio
11. Gender Female Ratio
12. Catch Rate
13. Egg Group 1 (Blank if none)
14. Egg Group 2 (Blank if none)
15. Hatching Time in Cycles
16. Height in Inches
17. Height in Meters
18. Weight in Pounds
19. Weght in Kilograms
20. Mega Stone 1 (Blank if none)
21. Mega Stone 2 (Blank if none)
22. EXP Yield (Gen I) (Blank if none)
23. EXP Yield (Gen II) (Blank if none)
24. EXP Yield (Gen III) (Blank if none)
25. EXP Yield (Gen IV) (Blank if none)
26. EXP Yield (Gen V+)
27. Leveling Rate
28. EV Yield for HP
29. EV Yield for Attack
30. EV Yield for Defense
31. EV Yield for Special Attack
32. EV Yield for Special Defense
33. EV Yield for Speed
34. Shape Image URL
35. Footprint Image URL ('?' Image if not from Gen I-V)
36. Base Friendship
37. Base HP Stats (Pipe-Separated by Generation)
38. Base Attack Stat (Pipe-Separated by Generation)
39. Base Defense Stat (Pipe-Separated by Generation)
40. Base Special Attack Stat (Pipe-Separated by Generation)
41. Base Special Defense Stat (Pipe-Separated by Generation)
42. Base Speed Stat (Pipe-Separated by Generation)
43. Base Total Stats (Pipe-Separated by Generation)
44. Color