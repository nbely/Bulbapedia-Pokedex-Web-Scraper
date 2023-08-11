#Packages
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
from urllib.request import urlopen

#Set-up
url = "https://bulbapedia.bulbagarden.net/"
img_url_base = 'https://archives.bulbagarden.net/media/upload/'
pageurl = url + "wiki/List_of_Pokémon_by_National_Pokédex_number"
response = requests.get(pageurl)

pokeList = []
page = response.text
soup = BeautifulSoup(page, 'html.parser')

# Start of Script
no = []
name = []
forme = []
classification = []
generation = []
primary = []
secondary = []
abil1 = []
abil2 = []
habil = []
otherAbil = []
gender = []
genderM = []
genderF = []
catchRate = []
eggGroup1 = []
eggGroup2 = []
hatchTime = []
heightIn = []
heightM = []
weightLbs = []
weightKg = []
megaStone1 = []
megaStone2 = []
expYield_I = []
expYield_II = []
expYield_III = []
expYield_IV = []
expYield_VPlus = []
levelRate = []
evYieldHP = []
evYieldAtk = []
evYieldDef = []
evYieldSpAtk = []
evYieldSpDef = []
evYieldSpd = []
shape = []
footprint = []
baseFriendship = []
hp = []
atk = []
defense = []
spatk = []
spdef = []
spd = []
bst = []
color = []

# Scrape Pokemon List from Bulbapedia
all_matches = soup.find_all('table', class_='roundy').pop()
for i in all_matches:
    urlExtensions = ([a.attrs.get('href') for a in soup.select('table.roundy td a[title*="Pok"]')])
    for extension in urlExtensions:
        pokeList.append(url + extension)

# Scrape Individual Bulbapedia Pokemon Pages
p_index = 0
f_index = 0
startIndex = 0
endIndex = 1161
for x in pokeList[startIndex:endIndex]: #Pokemon total 1161 (up to Pokedex #1010)
  # Skip if the pokemon is duplicated
  if p_index > 0:
    if pokeList[startIndex + p_index] == pokeList[startIndex + p_index - 1]:
      p_index = p_index + 1
      continue
  p_url = x
  response = requests.get(p_url)
  p_page = response.text
  p_soup = BeautifulSoup(p_page, 'html.parser')
  p_table = p_soup.find('table', class_='roundy')
  
  # Manually set number of formes for Pokemon formes in Bulbapedia that can't be initially identified 
  f_a = p_table.select('tbody tr td table.roundy tbody tr td table.roundy tbody tr td a[title*=""]')
  num_formes = len(f_a)-1
  manual_added_formes = []
  if (
    f_a[0]['title'] == "Shellos"
    or f_a[0]['title'] == "Gastrodon"
    or f_a[0]['title'] == "Meowstic"
    or f_a[0]['title'] == "Indeedee"
    or f_a[0]['title'] == "Basculegion"
    or f_a[0]['title'] == "Oinkologne"
  ):
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 2
  elif f_a[0]['title'] == "Greninja":
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 3
  elif f_a[0]['title'] == "Pumpkaboo" or f_a[0]['title'] == "Gourgeist":
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 4
  elif f_a[0]['title'] == "50% Forme": # Zygarde
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 5
  elif f_a[0]['title'] == "Meteor Form": # Minior
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 8
  elif f_a[0]['title'] == "Alcremie":
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 10
  elif f_a[0]['title'] == "Vivillon":
    manual_added_formes.append(f_a[0]['title'])
    num_formes = 20

  for f_num in range(num_formes):
    # Skip if the forme is duplicated (not including manually entered formes)
    if f_num > 0:
      if (f_a[0]['title'] not in manual_added_formes):
        if f_a[f_num]['title'] == f_a[f_num - 1]['title']:
          continue
    # p_tables[0] includes name, classification, pokedex no
    # p_tables[1] includes images and forme names
    # p_tables[2] includes types
    # p_tables[3] includes abilities
    # p_tables[4] includes gender ratio
    # p_tables[5] includes catch rate
    # p_tables[6] includes egg groups
    # p_tables[7] includes hatch time
    # p_tables[8] includes height
    # p_tables[9] includes weight
    # p_Tables[10] includes Mega Stone
    # p_tables[11] includes base experience yield
    # p_tables[12] includes leveling rate
    # p_tables[13] includes EV yield
    # p_tables[14] includes shape
    # p_tables[15] includes footprint
    # p_tables[16] includes color
    # p_tables[17] includes base friendship
    # p_tables[18] includes generation info
    p_tables = p_table.select('table.roundy')

    #Find Dex Number
    no.append(int(p_tables[0].th.big.a.span.text.split('#')[1]))
    print("Pokedex No: #" + str(no[f_index]) + " (pokeIndex: " + str(p_index) + ") (formeIndex: " + str(f_index) + ")")

    #Find Name
    name.append(p_tables[0].select('td.roundy td big b')[0].text)
    print("Name: " + name[f_index])

    # Find Forme
    # Set manully entered formes first
    if (
      name[f_index] == "Shellos"
      or name[f_index] == "Gastrodon"
    ):
      if f_num == 0:
        forme.append("West Sea " + name[f_index])
      elif f_num == 1:
        forme.append("East Sea" + name[f_index])
    elif name[f_index] == 'Greninja':
      if f_num == 0:
        forme.append('')
      elif f_num == 1:
        forme.append('Battle Bond Greninja')
      elif f_num == 2:
        forme.append('Ash-Greninja')
    elif name[f_index] == 'Vivillon':
      if f_num == 0:
        forme.append('Meadow Pattern')
      elif f_num == 1:
        forme.append('Icy Snow Pattern')
      elif f_num == 2:
        forme.append('Polar Pattern')
      elif f_num == 3:
        forme.append('Tundra Pattern')
      elif f_num == 4:
        forme.append('Continental Pattern')
      elif f_num == 5:
        forme.append('Garden Pattern')
      elif f_num == 6:
        forme.append('Elegant Pattern')
      elif f_num == 7:
        forme.append('Modern Pattern')
      elif f_num == 8:
        forme.append('Marine Pattern')
      elif f_num == 9:
        forme.append('Archipelago Pattern')
      elif f_num == 10:
        forme.append('High Plains Pattern')
      elif f_num == 11:
        forme.append('Sandstorm Pattern')
      elif f_num == 12:
        forme.append('River Pattern')
      elif f_num == 13:
        forme.append('Monsoon Pattern')
      elif f_num == 14:
        forme.append('Savanna Pattern')
      elif f_num == 15:
        forme.append('Sun Pattern')
      elif f_num == 16:
        forme.append('Ocean Pattern')
      elif f_num == 17:
        forme.append('Jungle Pattern')
      elif f_num == 18:
        forme.append('Fancy Pattern')
      elif f_num == 19:
        forme.append('Poké Ball Pattern')
    elif (
      name[f_index] == "Meowstic"
      or name[f_index] == "Indeedee"
      or name[f_index] == "Basculegion"
      or name[f_index] == "Oinkologne"
    ):
      if f_num == 0:
        forme.append("Male " + name[f_index])
      elif f_num == 1:
        forme.append("Female " + name[f_index])
    elif (
      name[f_index] == "Pumpkaboo"
      or name[f_index] == "Gourgeist"
    ):
      if f_num == 0:
        forme.append("Small Size")
      elif f_num == 1:
        forme.append("Average Size")
      elif f_num == 2:
        forme.append("Large Size")
      elif f_num == 3:
        forme.append("Super Size")
    elif (name[f_index] == "Zygarde"):
      if f_num == 0:
        forme.append("50% Forme")
      elif f_num == 1:
        forme.append("10% Forme")
      elif f_num == 2:
        forme.append("Complete Forme")
      elif f_num == 3:
        forme.append("Power Construct 50% Forme")
      elif f_num == 4:
        forme.append("Power Construct 10% Forme")
    elif (name[f_index] == "Minior"):
      if f_num == 0:
        forme.append("Meteor Form")
      elif f_num > 0 and f_num < 8:
        forme.append("Core")
    elif (name[f_index] == "Alcremie"):
      if f_num == 0:
        forme.append("Vanilla Cream")
      elif f_num == 1:
        forme.append("Ruby Cream")
      elif f_num == 2:
        forme.append("Matcha Cream")
      elif f_num == 3:
        forme.append("Mint Cream")
      elif f_num == 4:
        forme.append("Lemon Cream")
      elif f_num == 5:
        forme.append("Salted Cream")
      elif f_num == 6:
        forme.append("Ruby Swirl")
      elif f_num == 7:
        forme.append("Caramel Swirl")
      elif f_num == 8:
        forme.append("Rainbow Swirl")
      elif f_num == 9:
        forme.append("Gigantamax Alcremie")
    # Set no forme if the base Pokémon name is matched
    elif f_a[f_num]['title'] == name[f_index]:
      forme.append('')
    # Set the forme otherwise
    else:
      forme.append(f_a[f_num]['title'].replace('\u00A0', ' '))
    print("Forme: " + forme[f_index])

    #Find Classification
    classif = p_table.select('td.roundy td a[title*="Pokémon category"] span')[0].text
    classifs = classif.split(" Pokémon")
    classifs.pop()
    # Separate 1-to-1 classification assignments for formes
    if num_formes == len(classifs):
      classif = classifs[f_num].strip()
    # Handle exceptions for classification count and forme count not matching up
    else:
      if name[f_index] == 'Basculin':
        if f_num < 2:
          classif = 'Hostile'
        else:
          classif = 'Mellow'
      elif name[f_index] == 'Darmanitan':
        if f_num % 2 == 0:
          classif = 'Blazing'
        else:
          classif = 'Zen Charm'
      elif name[f_index] == 'Calyrex':
        if f_num == 0:
          classif = 'King'
        else:
          classif = 'High King'
    if "Pokémon" in classif:
      classif = classif.replace('Pokémon', '').strip()
    classification.append(classif)
    print("Classification: " + classification[f_index])
    
    #Find Generation
    g = p_tables[18].select('ul li span a[class*="external text"]')
    g = BeautifulSoup(str(g), "html.parser").get_text()
    g = g[:-1][1:]
    g = g.split(",")
    if (g[0].strip() == 'Generation I'):
      generation.append(1)
    elif (g[0].strip() == 'Generation II'):
      generation.append(2)
    elif (g[0].strip()  == 'Generation III'):
      generation.append(3)
    elif (g[0].strip()  == 'Generation IV'):
      generation.append(4)
    elif (g[0].strip()  == 'Generation V'):
      generation.append(5)
    elif (g[0].strip()  == 'Generation VI'):
      generation.append(6)
    elif (g[0].strip()  == 'Generation VII'):
      generation.append(7)
    elif (g[0].strip()  == 'Generation VIII'):
      generation.append(8)
    elif (g[0].strip()  == 'On Smogon Pokédex'): # FUTURE: Remove 'On Smogon Pokédex one Gen IX is updated in Bulbapedia):
      generation.append(9)
    # Override Generation for Regional and Gimmick Formes
    if 'Mega' in forme[f_index]:
      generation[f_index] = 6
    if 'Alolan' in forme[f_index]:
      generation[f_index] = 7
    if (
      'Galarian' in forme[f_index]
      or 'Gigantamax' in forme[f_index]
      or 'Hisuian' in forme[f_index]
    ):
      generation[f_index] = 8
    if 'Paldean' in forme[f_index]:
      generation[f_index] = 9
    print("Generation: " + str(generation[f_index]))

    #Find Types
    t_found = False
    t_tds = p_tables[2].select('tbody tr td')
    for t_td in t_tds:
      if len(t_td.select('table')) == 0:
        continue
      if len(t_td.select('small')) != 0:
        if forme[f_index] == '':
          if t_td.select('small')[0].text != name[f_index]:
            continue
        else:
          parsed_form = forme[f_index].split('(')
          if (len(parsed_form) > 1):
            parsed_form = parsed_form[1].split(')')[0] # Parsed form for Urshifu
          if (
            t_td.select('small')[0].text.replace('(', ' (').replace('\u00A0', ' ')!= forme[f_index]
            and t_td.select('small')[0].text.replace('\u00A0', ' ') != parsed_form
          ):
            continue
      t = t_td.select('a[href*="(type)"] span b')
      if (len(t) == 0):
        continue
      if (t[0].text == 'Unknown'):
        continue
      primary.append(t[0].text)
      if (len(t) > 1):
        if (t[1].text == 'Unknown'):
          secondary.append('')
        else:
          secondary.append(t[1].text)
      else:
        secondary.append('')
      t_found = True
      break
    if (t_found == False):
      t = p_tables[2].select('td a[title*="(type)"] span b')
      primary.append(t[0].text)
      if (len(t) > 1):
        if (t[1].text == 'Unknown'):
          secondary.append('')
        else:
          secondary.append(t[1].text)
      else:
        secondary.append('')
    print("Type 1: " + primary[f_index])
    print("Type 2: " + secondary[f_index])

    #TODO: Fix Abilities for various Pokemon with formes
    #Find Abilities
    a_found = False
    ha_found = False
    base_ha_index = -1
    a_tds = p_tables[3].select('tbody tr td')
    for a_i in range(len(a_tds)):
      ability_type = "Ability"
      if len(a_tds[a_i].select('small')) != 0:
        td_small = a_tds[a_i].select('small')[0].text.replace('\u00A0', ' ').strip()
        td_small_matched = False
        fnames = []
        if (forme[f_index] != ''):
          if f_num == 0:
            fnames.append(name[f_index])
          fnames.append(forme[f_index])
        else:
          fnames.append(name[f_index])
        if ("Hidden Ability" in td_small):
          ability_type = "Hidden Ability"
          base_ha_index = a_i
        td_small_fnames = td_small.split(' & ')
        if len(td_small_fnames) < 2:
          td_small_fnames = td_small.split(' and ')
          if len(td_small_fnames) < 2:
            td_small_fnames = td_small.split('/')
            if len(td_small_fnames) > 1:
              td_small_fnames[0] = td_small_fnames[0] + " " + name[f_index]
        if "50%, 10% & Complete Formes" in td_small:  # Exception for Zygarde
          td_small_fnames = ["Power Construct 50% Forme", "Power Construct 10% Forme", "Complete Forme"]
        for fname in fnames:
          a_matches = [
            fname,
            "Ability",
            fname + " Ability",
          ]
          ha_matches = [
            "Hidden Ability",
            fname + " Hidden Ability",
            fname.split(' (')[0] + " Hidden Ability",  # Exception for Paldean Tauros/Ushifu
            "Gen VIII+ Hidden Ability",
            "Gen VI+ " + fname + " Hidden Ability",
            "Gen VIII+ " + fname + " Hidden Ability",
          ]
          matches = set(td_small_fnames).intersection(a_matches + ha_matches)
          if len(matches) > 0:
            td_small_matched = True
        if td_small_matched == False:
          continue
      else:
        if f_num > 0:
          continue
      a = a_tds[a_i].select('a[title*="(Ability)"] span')
      if len(a) == 0:
        continue
      if a[0].text == 'Cacophony':
        continue
      if (ability_type == "Ability"):
        if a[0].text == 'As One':  # Exception for Calyrex
          if forme[f_index] == 'Ice Rider Calyrex':
            abil1.append('As One (Glastrier)')
          else:
            abil1.append('As One (Spectrier)')
        else:
          abil1.append(a[0].text)
        if len(a) > 1:
          if a[1].text == 'Cacophony':
            abil2.append('')
          else:
            abil2.append(a[1].text)
        else:
          abil2.append('')
        if len(habil) == f_index + 1:
          habil[f_index] = ''
        a_found = True
      elif (ability_type == "Hidden Ability"):
        if "Zen Mode" in forme[f_index]:  # Exception for Darmanitan Zen Mode
          abil1.append('Zen Mode')
          abil2.append('')
          habil.append('')
          a_found = True
        elif len(habil) == f_index:
          habil.append(a[0].text)
        else:
          habil[f_index] = a[0].text
        ha_found = True
      if (a_found and ha_found):
        break
    if a_found == False:
      a = p_tables[3].select('td a[title*="(Ability)"] span')
      abil1.append(a[0].text)
      if len(a) > 1:
        if a[1].text == 'Cacophony':
          abil2.append('')
        else:
          abil2.append(a[1].text)
      else:
          abil2.append('')
    if ha_found == False:
      a = p_tables[3].select('td a[title*="(Ability)"] span')

      if base_ha_index > 0:
        ha = a_tds[base_ha_index-1].select('a[title*="(Ability)"] span')
        if abil1[f_index] != a[0].text:
          habil.append('')
        else:
          if (ha[0].text == 'Cacophony'):
            habil.append('')
          else:
            habil.append(ha[0].text)
      else:
        habil.append('')
    print("Ability 1: " + abil1[f_index])
    print("Ability 2: " + abil2[f_index])
    print("Hidden Ability: " + habil[f_index])

    #Find Gender Ratio
    g_unk = p_tables[4].select('a[title*="unknown"] span')
    if (len(g_unk) > 0):
      gender.append('N')
      genderM.append('')
      genderF.append('')
    else:
      g_mf = p_tables[4].select('a[title*="Category"] span')
      if len(g_mf) > 2:
        gender.append('')
        genderM.append(float(g_mf[0].text.split('%')[0])/100)
        genderF.append(float(g_mf[2].text.split('%')[0])/100)
      else:
        if g_mf[0].text == '100% female':
          gender.append('F')
          genderM.append(0)
          genderF.append(1)
        else:
          gender.append('M')
          genderM.append(1)
          genderF.append(0)
    if 'Female' in forme[f_index]:
      gender[f_index] = 'F'
      genderM[f_index] = 0
      genderF[f_index] = 1
    elif 'Male' in forme[f_index]:
      gender[f_index] = 'M'
      genderM[f_index] = 1
      genderF[f_index] = 0
    print("Gender: " + gender[f_index])
    print("Gender Male Ratio: " + str(genderM[f_index]))
    print("Gender Female Ratio: " + str(genderF[f_index]))

    #Find Catch Rate
    cr = p_tables[5].select('td')
    if len(cr) > 0:
      catchRate.append(int(cr[0].text.split(' (')[0]))
    print("Catch Rate: " + str(catchRate[f_index]))

    #Find Egg Groups
    eg = p_tables[6].select('td a[title*="(Egg Group)"] span')
    if len(eg) == 1:
      if (eg[0].text == 'No Eggs Discovered'):
        eggGroup1.append('')
      else:
        eggGroup1.append(eg[0].text)
      eggGroup2.append('')
    if len(eg) > 1:
      eggGroup1.append(eg[0].text)
      if (eg[1].text == 'No Eggs Discovered'):
        eggGroup2.append('')
      else:
        eggGroup2.append(eg[1].text)
    eg_override = p_tables[6].select('sup a')
    if len(eg_override) > 0 :
      for override in eg_override:
        override_span = override.select('span')
        override_text = []
        if len(override_span) > 0:
          override_text = override_span[0].text.split(' & ')
        if (
          override['title'] == forme[f_index]
          or forme[f_index] in override_text
        ):
          if (eg[len(eg)-1].text == 'No Eggs Discovered'):
            eggGroup1[f_index] = ''
            eggGroup2[f_index] = ''
          else:
            eggGroup1[f_index] = eg[len(eg)-1].text
            eggGroup2[f_index] = ''
    if 'Parter' in forme[f_index]:
      eggGroup1[f_index] = ''
      eggGroup2[f_index] = ''

    print("Egg Group 1: " + eggGroup1[f_index])
    print("Egg Group 2: " + eggGroup2[f_index])

    #Find Hatch Time
    ht = p_tables[7].select('td')
    if len(ht) > 0:
      hatchTime.append(int(ht[0].text.split('\xa0cycles')[0]))
    print("Hatch Time (Cycles): " + str(hatchTime[f_index]))

    #Find Height
    heightSet = False
    h_tds = p_tables[8].select('td')
    if len(h_tds) > 0:
      for h in range(int(len(h_tds)/3)):
        if forme[f_index] == '':
          if h_tds[h*3+2].find('small').text != name[f_index]:
            continue
        else:
          if h_tds[h*3+2].find('small').text.replace('\u00A0', ' ').replace('(', ' (') != forme[f_index].replace('Power Construct ', ''): # Replace for PC Zygarde formes
            continue
        heightUS = h_tds[h*3].text.replace("′", "'").replace('″', '"').split("'")
        if (len(heightUS) < 2 and heightUS[0] == '\n'):
          heightUS = ['0', '0"']
        if (heightUS[0] == '0') and heightUS[1].split('"')[0] == '0':
          heightUS = h_tds[0].text.replace("′", "'").replace('″', '"').split("'")
        heightIn.append(int(heightUS[0])*12 + int(heightUS[1].split('"')[0]))
        heightMeters = h_tds[h*3+1].text.split(' m')[0]
        if (heightMeters == '0' or heightMeters == 'm\n'):
          heightMeters = h_tds[1].text.split(' m')[0]
        if "+" in heightMeters:
          heightMeters = heightMeters[:len(heightMeters)-1]
        heightM.append(float(heightMeters))
        heightSet = True
    if heightSet == False:
      heightUS = h_tds[0].text.replace("′", "'").replace('″', '"').split("'")
      heightIn.append(int(heightUS[0])*12 + int(heightUS[1].split('"')[0]))
      heightMeters = h_tds[1].text.split(' m')[0]
      if "+" in heightMeters:
        heightMeters = heightMeters[:len(heightMeters)-1]
      heightM.append(float(heightMeters))
    print("Height (In): " + str(heightIn[f_index]))
    print("Height (M): " + str(heightM[f_index]))

    #Find Weight
    weightSet = False
    w_tds = p_tables[9].select('td')
    if len(w_tds) > 0:
      for w in range(int(len(w_tds)/3)):
        if forme[f_index] == '':
          if w_tds[w*3+2].find('small').text != name[f_index]:
            continue
        else:
          if w_tds[w*3+2].find('small').text.replace('\u00A0', ' ').replace('(', ' (') != forme[f_index].replace('Power Construct ', ''): # Replace for PC Zygarde formes
            continue
        weightPounds = w_tds[w*3].text.replace(',', '').split(" lbs.")[0]
        if (
          weightPounds == '0'
          or weightPounds == '???'
          or weightPounds == 'lbs.\n'
          or forme[f_index] == 'Gigantamax Butterfree'
        ):
          weightPounds = w_tds[0].text.replace(',', '').split(" lbs.")[0]
        weightLbs.append(float(weightPounds))
        weightKilos = w_tds[w*3+1].text.replace(',', '').split(' kg')[0]
        if (
          weightKilos == '0'
          or weightKilos == '???'
          or weightKilos == 'kg\n'
          or forme[f_index] == 'Gigantamax Butterfree'
        ):
          weightKilos = w_tds[1].text.replace(',', '').split(' kg')[0]
        weightKg.append(float(weightKilos))
        weightSet = True
    if weightSet == False:
      weightPounds = w_tds[0].text.replace(',', '').split(" lbs.")[0]
      weightLbs.append(float(weightPounds))
      weightKilos = w_tds[1].text.replace(',', '').split(' kg')[0]
      weightKg.append(float(weightKilos))
    print("Weight (Lbs): " + str(weightLbs[f_index]))
    print("Weight (Kg): " + str(weightKg[f_index]))

    #Find Mega Stone(s)
    megaStonesSet = False
    ms = p_tables[10].select('td a[title*="ite"] span')
    if len(ms) == 1:
      megaStone1.append(ms[0].text.replace('\u200e', '').strip())
      megaStone2.append('')
      megaStonesSet = True
    elif len(ms) > 1:
      if (forme[f_index] == ''):
        megaStone1.append(ms[0].text.replace('\u200e', '').strip())
        megaStone2.append(ms[1].text.replace('\u200e', '').strip())
        megaStonesSet = True
      else:
        for m in ms:
          if (m.text.split('ite')[0].strip() in forme[f_index] and (m.text.split('ite')[1] != '' and m.text.split('ite')[1].strip() in forme[f_index])):
            megaStone1.append(m.text.replace('\u200e', '').strip())
            megaStone2.append('')
            megaStonesSet = True
            break
    if megaStonesSet == False:
      if 'Gigantamax' in forme[f_index]:
        megaStone1.append('')
        megaStone2.append('')
      else:
        if len(ms) == 1:
          megaStone1.append(ms[0].text.strip())
          megaStone2.append('')
        elif len(ms) > 1:
          megaStone1.append(ms[0].text.strip())
          megaStone2.append(ms[1].text.strip())
        else:
          megaStone1.append('')
          megaStone2.append('')
    print("Mega Stone 1: " + megaStone1[f_index])
    print("Mega Stone 2: " + megaStone2[f_index])

    #Find EXP Yield
    ey_tds = p_tables[11].select('td')
    for ey_td in ey_tds:
      if len(ey_td.select('small')) != 0:
        if ey_td.find('small').text == 'Gen. I-III':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_I.append(int(ey_td.text.split('Gen')[0]))
            expYield_II.append(int(ey_td.text.split('Gen')[0]))
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_I.append('')
            expYield_II.append('')
            expYield_III.append('')
        elif ey_td.find('small').text == 'Gen. I-IV':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_I.append(int(ey_td.text.split('Gen')[0]))
            expYield_II.append(int(ey_td.text.split('Gen')[0]))
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
            expYield_IV.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_I.append('')
            expYield_II.append('')
            expYield_III.append('')
            expYield_IV.append('')
        elif ey_td.find('small').text == 'Gen. II-III':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_II.append(int(ey_td.text.split('Gen')[0]))
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_II.append('')
            expYield_III.append('')
          expYield_I.append('')
        elif ey_td.find('small').text == 'Gen. II-IV':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_II.append(int(ey_td.text.split('Gen')[0]))
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
            expYield_IV.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_II.append('')
            expYield_III.append('')
            expYield_IV.append('')
          expYield_I.append('')
        elif ey_td.find('small').text == 'Gen. III':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_III.append('')
          expYield_I.append('')
          expYield_II.append('')
        elif ey_td.find('small').text == 'Gen. III-IV':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_III.append(int(ey_td.text.split('Gen')[0]))
            expYield_IV.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_III.append('')
            expYield_IV.append('')
          expYield_I.append('')
          expYield_II.append('')
        elif ey_td.find('small').text == 'Gen. IV':
          if ey_td.text.split('Gen')[0] != 'Unknown':
            expYield_IV.append(int(ey_td.text.split('Gen')[0]))
          else:
            expYield_IV.append('')
          expYield_I.append('')
          expYield_II.append('')
          expYield_III.append('')
        elif ey_td.find('small').text == 'IV':
          if ey_td.text.split('I')[0] != 'Unknown':
            expYield_IV.append(int(ey_td.text.split('I')[0]))
        elif ey_td.find('small').text == 'V+':
          if ey_td.text.split('V')[0] != 'Unknown':
            expYield_VPlus.append(int(ey_td.text.split('V')[0]))
          else:
            expYield_VPlus.append('')
      else:
        expYield_VPlus.append(int(ey_td.text.strip()))
    print("EXP Yield (Gen I): " + str(expYield_I[f_index]))
    print("EXP Yield (Gen II): " + str(expYield_II[f_index]))
    print("EXP Yield (Gen III): " + str(expYield_III[f_index]))
    print("EXP Yield (Gen IV): " + str(expYield_IV[f_index]))
    print("EXP Yield (Gen V+): " + str(expYield_VPlus[f_index]))

    #Find Leveling Rate
    lr = p_tables[12].select('td')
    if len(lr) > 0:
      levelRate.append(lr[0].text.strip())
    else:
      levelRate.append('')
    print("Leveling Rate: " + levelRate[f_index])

    #Find EV Yields
    evYieldsSet = False
    ev_tds = p_tables[13].select('td')
    ev_tds.pop(0)
    for ev in range(int(len(ev_tds)/7)):
      if forme[f_index] != '' and forme[f_index] == ev_tds[ev*7].text.strip().replace('(', ' ('):
        if '*' in ev_tds[ev*7+1].text:
          evYieldHP.append(int(ev_tds[ev*7+1].text.split('*')[0].strip()))
        else:
          evYieldHP.append(int(ev_tds[ev*7+1].text.split('HP')[0].strip()))
        if '*' in ev_tds[ev*7+2].text:
          evYieldAtk.append(int(ev_tds[ev*7+2].text.split('*')[0].strip()))
        else:
          evYieldAtk.append(int(ev_tds[ev*7+2].text.split('Atk')[0].strip()))
        if '*' in ev_tds[ev*7+3].text:
          evYieldDef.append(int(ev_tds[ev*7+3].text.split('*')[0].strip()))
        else:
          evYieldDef.append(int(ev_tds[ev*7+3].text.split('Def')[0].strip()))
        if '*' in ev_tds[ev*7+4].text:
          evYieldSpAtk.append(int(ev_tds[ev*7+4].text.split('*')[0].strip()))
        else:
          evYieldSpAtk.append(int(ev_tds[ev*7+4].text.split('Sp.Atk')[0].strip()))
        if '*' in ev_tds[ev*7+5].text:
          evYieldSpDef.append(int(ev_tds[ev*7+5].text.split('*')[0].strip()))
        else:
          evYieldSpDef.append(int(ev_tds[ev*7+5].text.split('Sp.Def')[0].strip()))
        if '*' in ev_tds[ev*7+6].text:
          evYieldSpd.append(int(ev_tds[ev*7+6].text.split('*')[0].strip()))
        else:
          evYieldSpd.append(int(ev_tds[ev*7+6].text.split('Speed')[0].strip()))
        if (
          evYieldHP[f_index] == 0 and evYieldAtk[f_index] == 0
          and evYieldDef[f_index] == 0 and evYieldSpAtk[f_index] == 0
          and evYieldSpDef[f_index] == 0 and evYieldSpd[f_index] == 0
        ):
          evYieldHP.pop()
          evYieldAtk.pop()
          evYieldDef.pop()
          evYieldSpAtk.pop()
          evYieldSpDef.pop()
          evYieldSpd.pop()
        else:
          evYieldsSet = True
    if evYieldsSet == False:
      if '*' in ev_tds[1].text:
        evYieldHP.append(int(ev_tds[1].text.split('*')[0].strip()))
      else:
        evYieldHP.append(int(ev_tds[1].text.split('HP')[0].strip()))
      if '*' in ev_tds[2].text:
        evYieldAtk.append(int(ev_tds[2].text.split('*')[0].strip()))
      else:
        evYieldAtk.append(int(ev_tds[2].text.split('Atk')[0].strip()))
      if '*' in ev_tds[3].text:
        evYieldDef.append(int(ev_tds[3].text.split('*')[0].strip()))
      else:
        evYieldDef.append(int(ev_tds[3].text.split('Def')[0].strip()))
      if '*' in ev_tds[4].text:
        evYieldSpAtk.append(int(ev_tds[4].text.split('*')[0].strip()))
      else:
        evYieldSpAtk.append(int(ev_tds[4].text.split('Sp.Atk')[0].strip()))
      if '*' in ev_tds[5].text:
        evYieldSpDef.append(int(ev_tds[5].text.split('*')[0].strip()))
      else:
        evYieldSpDef.append(int(ev_tds[5].text.split('Sp.Def')[0].strip()))
      if '*' in ev_tds[6].text:
        evYieldSpd.append(int(ev_tds[6].text.split('*')[0].strip()))
      else:
        evYieldSpd.append(int(ev_tds[6].text.split('Speed')[0].strip()))
    print("EV Yield (HP): " + str(evYieldHP[f_index]))
    print("EV Yield (Atk): " + str(evYieldAtk[f_index]))
    print("EV Yield (Def): " + str(evYieldDef[f_index]))
    print("EV Yield (SpAtk): " + str(evYieldSpAtk[f_index]))
    print("EV Yield (SpDef): " + str(evYieldSpDef[f_index]))
    print("EV Yield (Spd): " + str(evYieldSpd[f_index]))

    #Find Shape
    #Exceptions sourced from: https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_shape
    sh = p_tables[14].select('td a img')
    if len(sh) > 0:
      url_ext = sh[0]['src'].split('/32px')[0].split('thumb/')[1]
      shape.append(img_url_base + url_ext)
    if forme[f_index] != '':
      if (
        name[f_index] == 'Giratina' and forme[f_index] == 'Origin Forme'
        or forme[f_index] == 'Eternamax Eternatus'
      ):
        shape[f_index] = img_url_base + '7/7a/Body02.png'
      elif (forme[f_index] == 'Mega Slowbro'):
        shape[f_index] = img_url_base + '2/2c/Body04.png'
      elif (
        forme[f_index] == 'Galarian Meowth'
        or name[f_index] == 'Thundurus' and forme[f_index] == 'Therian Forme'
        or name[f_index] == 'Zygarde' and forme[f_index] == 'Complete Forme'
        or forme[f_index] == 'Hoopa Unbound'
        or name[f_index] == 'Lycanroc' and forme[f_index] == 'Midnight Form'
      ):
        shape[f_index] = img_url_base + '8/88/Body06.png'
      elif (
        name[f_index] == 'Palkia' and forme[f_index] == 'Origin Forme'
        or name[f_index] == 'Landorus' and forme[f_index] == 'Therian Forme'
        or name[f_index] == 'Zygarde' and forme[f_index].replace('Power Construct ', '') == '10% Forme'
        or forme[f_index] == 'Dusk Mane Necrozma'
        or forme[f_index] == 'Ice Rider Calyrex'
        or forme[f_index] == 'Shadow Rider Calyrex'
        or name[f_index] == 'Enamorus' and forme[f_index] == 'Therian Forme'
      ):
        shape[f_index] = img_url_base + 'c/cc/Body08.png'
      elif (
        name[f_index] == 'Tornadus' and forme[f_index] == 'Therian Forme'
        or forme[f_index] == 'Dawn Wings Necrozma'
      ):
        shape[f_index] = img_url_base + '9/98/Body09.png'
      elif (name[f_index] == 'Wishiwashi' and forme[f_index] == 'School Form'):
        shape[f_index] = img_url_base + '3/36/Body11.png'
      elif (
        forme[f_index] == 'Hisuian Lilligant'
        or name[f_index] == 'Gimmighoul' and forme[f_index] == 'Roaming Form'
      ):
        shape[f_index] = img_url_base + '4/45/Body12.png'
      elif (
        forme[f_index] == 'Mega Pinsir'
        or forme[f_index] == 'Ultra Necrozma'
      ):
        shape[f_index] = img_url_base + '0/09/Body13.png'
    print("Shape: " + shape[f_index])

    #Find Footprint
    fp = p_tables[15].select('td a img')
    footprint.append('https:'+fp[0]['src'])
    if name[f_index] == 'Giratina' and forme[f_index] == 'Origin Forme':
      footprint[f_index] = img_url_base + '4/40/F0487O.png'
    print("Footprint: " + footprint[f_index])

    #Find Base Friendship
    fr = p_tables[17].select('td')
    bfr = fr[0].text.strip()
    if bfr == 'Unknown':
      baseFriendship.append(0)
    else:
      baseFriendship.append(int(bfr))
    print("Base Friendship: " + str(baseFriendship[f_index]))

    #Find Base Stats
    st_tables = p_soup.select('table[style*="white-space:nowrap"]')
    st_indices = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    forme_indices_set = False
    for st in range(len(st_tables)):
      htag_loc = 3
      found_loc = htag_loc
      header_located = False
      st_header = ''
      for loc in range(4):
        temp_header = st_tables[st].find_previous('h'+str(htag_loc))
        if temp_header == None:
          htag_loc = htag_loc + 1
          continue
        temp_header = temp_header.text.strip()
        if (temp_header == 'Base Stats' or temp_header == 'Base stats'):
          found_loc = htag_loc
          st_header = temp_header
          header_located = True
        elif (
          temp_header == name[f_index]
          or temp_header == forme[f_index].replace('Power Construct ', '')  # Replace exception for PC Zygarde Formes
          or temp_header == forme[f_index].split(' (')[0]  # Exception For Paldean Tauros
          or name[f_index] == "Rotom" and forme[f_index].split(' ')[0] in temp_header  # Exception for Rotom Formes
        ):
          st_header = temp_header
          found_loc = htag_loc
          header_located = True
        htag_loc = htag_loc + 1
      if header_located == False:
        continue
      else:
        if (
          st_header == forme[f_index].replace('Power Construct ', '')  # Replace exception for PC Zygarde Formes
          or st_header == forme[f_index].split(' (')[0]  # Exception For Paldean Tauros
          or name[f_index] == "Rotom" and forme[f_index].split(' ')[0] in st_header  # Exception for Rotom Formes
          and forme_indices_set == False
        ):
          st_indices = [st, st, st, st, st, st, st, st, st]
          forme_indices_set = True
        gen_header = ''
        sub_header = st_tables[st].find_previous('h'+str(found_loc+1))
        super_header = st_tables[st].find_previous('h'+str(found_loc-1)).text.strip()
        if sub_header != None:
          gen_header = sub_header.text.strip()
        elif 'Generation' in super_header:
          gen_header = super_header
        if gen_header != '':
          if gen_header == 'Generations I-V' or gen_header == 'Generations I to V':
            st_indices[0] = st
            st_indices[1] = st
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
          elif gen_header == 'Generations I-VI':
            st_indices[0] = st
            st_indices[1] = st
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
            st_indices[5] = st
          elif gen_header == 'Generations II-V':
            st_indices[1] = st
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
          elif gen_header == 'Generations II-VI':
            st_indices[1] = st
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
            st_indices[5] = st
          elif gen_header == 'Generations III-V':
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
          elif gen_header == 'Generations III-VI':
            st_indices[2] = st
            st_indices[3] = st
            st_indices[4] = st
            st_indices[5] = st
          elif gen_header == 'Generations IV-V':
            st_indices[3] = st
            st_indices[4] = st
          elif gen_header == 'Generations IV-VI':
            st_indices[3] = st
            st_indices[4] = st
            st_indices[5] = st
          elif gen_header == 'Generation IV to VIII':
            st_indices[3] = st
            st_indices[4] = st
            st_indices[5] = st
            st_indices[6] = st
            st_indices[7] = st
          elif gen_header == 'Generation V':
            st_indices[4] = st
          elif gen_header == 'Generations V-VI' or gen_header == 'Generations V & VI':
            st_indices[4] = st
            st_indices[5] = st
          elif gen_header == 'Generation VI':
            st_indices[5] = st
          elif gen_header == 'Generations VI-VII':
            st_indices[5] = st
            st_indices[6] = st
          elif 'Generation VI onward' in gen_header:
            st_indices[5] = st
            st_indices[6] = st
            st_indices[7] = st
            st_indices[8] = st
          elif 'Generation VII onward' in gen_header or gen_header == 'Generation VII':
            st_indices[6] = st
            st_indices[7] = st
            st_indices[8] = st
          elif 'Generation VIII onward' in gen_header:
            st_indices[7] = st
            st_indices[8] = st
          elif gen_header == 'Generation IX':
            st_indices[8] = st
          elif "Version" in gen_header:
            if st == len(st_tables) - 1:
              st_indices = [st, st, st, st, st, st, st, st, st]
    if generation[f_index] != 1:
      st_indices[0] = -1
      if generation[f_index] != 2:
        st_indices[1] = -1
        if generation[f_index] != 3:
          st_indices[2] = -1
          if generation[f_index] != 4:
            st_indices[3] = -1
            if generation[f_index] != 5:
              st_indices[4] = -1
              if generation[f_index] != 6:
                st_indices[5] = -1
                if generation[f_index] != 7:
                  st_indices[6] = -1
                  if generation[f_index] != 8:
                    st_indices[7] = -1
    hp_stats = []
    atk_stats = []
    def_stats = []
    spatk_stats = []
    spdef_stats = []
    spd_stats = []
    bst_stats = []
    for st_index in st_indices:
      if st_index == -1:
        hp_stats.append('')
        atk_stats.append('')
        def_stats.append('')
        spatk_stats.append('')
        spdef_stats.append('')
        spd_stats.append('')
        bst_stats.append('')
        continue
      stats = st_tables[st_index].find_all('th', attrs = {'style':['width:85px; padding-left:0.5em; padding-right:0.5em']})
      if stats == []:
        stats = st_tables[st_index].find_all('th', attrs = {'style':['width:85px;padding-left:0.5em;padding-right:0.5em']})
      stats = ([x.text for x in stats])
      #Keep only the stats numbers and store into a list
      store = []
      for x in stats:
        store.append(re.findall(r'[0-9]?[0-9]?[0-9]?[0-9]', x))
      #Removing brackets and converting stats into integer
      holder = []
      for x in store:
        x = (str(x))[:-2][2:]
        holder.append(x)
      #Store stats into appropriate list
      hp_stats.append(holder[0])
      atk_stats.append(holder[1])
      def_stats.append(holder[2])
      spatk_stats.append(holder[3])
      spdef_stats.append(holder[4])
      spd_stats.append(holder[5])
      bst_stats.append(holder[6])
    hp.append(str(hp_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    atk.append(str(atk_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    defense.append(str(def_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    spatk.append(str(spatk_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    spdef.append(str(spdef_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    spd.append(str(spd_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    bst.append(str(bst_stats).replace(']', '').replace('[', '').replace("'", '').replace(' ', '').replace(',', '|'))
    print("HP Stats: " + hp[f_index])
    print("Attack Stats: " + atk[f_index])
    print("Defense Stat: " + defense[f_index])
    print("Sp.Atk Stat: " + spatk[f_index])
    print("Sp.Def Stat: " + spdef[f_index])
    print("Speed Stat: " + spd[f_index])
    print("Base Stat Total: " + bst[f_index])
    
    #Adjust Minior Forme Names for Color Identification
    if name[f_index] == 'Minior' and forme[f_index] == 'Core':
      if f_num == 1:
        forme[f_index] = 'Red Core'
      elif f_num == 2:
        forme[f_index] = 'Orange Core'
      elif f_num == 3:
        forme[f_index] = 'Yellow Core'
      elif f_num == 4:
        forme[f_index] = 'Green Core'
      elif f_num == 5:
        forme[f_index] = 'Blue Core'
      elif f_num == 6:
        forme[f_index] = 'Indigo Core'
      elif f_num == 7:
        forme[f_index] = 'Violet Core'

    #Find Color
    col = p_tables[16].select('td')
    color.append(col[0].text.split(' ')[1].split('Other')[0].strip())
    if (
      forme[f_index] == 'Galarian Moltres'
      or name[f_index] == 'Castform' and forme[f_index] == 'Sunny Form'
      or name[f_index] == 'Burmy' and forme[f_index] == 'Trash Cloak'
      or name[f_index] == 'Wormadam' and forme[f_index] == 'Trash Cloak'
      or name[f_index] == 'Deerling' and forme[f_index] == 'Autumn Form'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Modern Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Sun Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Ocean Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Poké Ball Pattern'
      or name[f_index] == 'Lycanroc' and forme[f_index] == 'Midnight Form'
      or name[f_index] == 'Minior' and forme[f_index] == 'Red Core'
      or name[f_index] == 'Minior' and forme[f_index] == 'Orange Core'
      or forme[f_index] == 'Original Color Magearna'
      or name[f_index] == 'Tatsugiri' and forme[f_index] == 'Droopy Form'
    ):
      color[f_index] = 'Red'
    elif (
      forme[f_index] == 'Alolan Sandslash'
      or forme[f_index] == 'Alolan Ninetales'
      or forme[f_index] == 'Alolan Meowth'
      or forme[f_index] == 'Alolan Persian'
      or name[f_index] == 'Castform' and forme[f_index] == 'Rainy Form'
      or forme[f_index] == 'East Sea Shellos'
      or forme[f_index] == 'East Sea Gastrodon'
      or name[f_index] == 'Darmanitan' and forme[f_index] == 'Zen Mode'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Polar Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Tundra Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Marine Pattern'
      or name[f_index] == 'Minior' and forme[f_index] == 'Blue Core'
      or name[f_index] == 'Minior' and forme[f_index] == 'Indigo Core'
      or forme[f_index] == 'Dawn Wings Necrozma'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Mint Cream'
      or name[f_index] == 'Squawkabilly' and forme[f_index] == 'Blue Plumage'
      or name[f_index] == 'Gimmighoul' and forme[f_index] == 'Roaming Form'
    ):
      color[f_index] = 'Blue'
    elif (
      name[f_index] == 'Vivillon' and forme[f_index] == 'Continental Pattern'
      or name[f_index] == 'Oricorio' and forme[f_index] == 'Pom-Pom Style'
      or name[f_index] == 'Minior' and forme[f_index] == 'Yellow Core'
      or forme[f_index] == 'Dusk Mane Necrozma'
      or forme[f_index] == 'Ultra Necrozma'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Lemon Cream'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Ruby Swirl'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Rainbow Swirl'
      or name[f_index] == 'Squawkabilly' and forme[f_index] == 'Yellow Plumage'
      or name[f_index] == 'Tatsugiri' and forme[f_index] == 'Stretchy Form'
    ):
      color[f_index] = 'Yellow'
    elif (
      forme[f_index] == 'Alolan Grimer'
      or forme[f_index] == 'Alolan Muk'
      or forme[f_index] == 'Galarian Stunfisk'
      or name[f_index] == 'Deerling' and forme[f_index] == 'Summer Form'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Garden Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Savanna Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Jungle Pattern'
      or name[f_index] == 'Minior' and forme[f_index] == 'Green Core'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Matcha Cream'
    ):
      color[f_index] = 'Green'
    elif (
      forme[f_index] == 'Mega Charizard X'
      or forme[f_index] == 'Alolan Rattata'
      or forme[f_index] == 'Alolan Raticate'
      or forme[f_index] == 'Paldean Tauros (Combat Breed)'
      or forme[f_index] == 'Paldean Tauros (Blaze Breed)'
      or forme[f_index] == 'Paldean Tauros (Aqua Breed)'
      or forme[f_index] == 'Hisuian Qwilfish'
      or name[f_index] == 'Zygarde' and forme[f_index].replace('Power Construct ', '') == '10% Forme'
      or name[f_index] == 'Zygarde' and forme[f_index] == 'Complete Forme'
      or forme[f_index] == 'Shadow Rider Calyrex'
    ):
      color[f_index] = 'Black'
    elif (
      forme[f_index] == 'Alolan Raichu'
      or forme[f_index] == 'Galarian Meowth'
      or forme[f_index] == 'Paldean Wooper'
      or name[f_index] == 'Burmy' and forme[f_index] == 'Sandy Cloak'
      or name[f_index] == 'Wormadam' and forme[f_index] == 'Sandy Cloak'
      or name[f_index] == 'Deerling' and forme[f_index] == 'Winter Form'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Archipelago Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'High Plains Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Sandstorm Pattern'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'River Pattern'
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Caramel Swirl'
      or forme[f_index] == 'Female Oinkologne'
    ):
      color[f_index] = 'Brown'
    elif (
      forme[f_index] == 'Alolan Marowak'
      or forme[f_index] == 'Galarian Articuno'
      or forme[f_index] == 'Mega Latias'
      or forme[f_index] == 'Mega Latios'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Elegant Pattern'
      or name[f_index] == 'Oricorio' and forme[f_index] == 'Sensu Style'
      or name[f_index] == 'Minior' and forme[f_index] == 'Violet Core'
      or name[f_index] == 'Morpeko' and forme[f_index] == 'Hangry Mode'
    ):
      color[f_index] = 'Purple'
    elif (
      forme[f_index] == 'Alolan Geodude'
      or forme[f_index] == 'Alolan Graveler'
      or forme[f_index] == 'Alolan Golem'
      or forme[f_index] == 'Galarian Weezing'
      or forme[f_index] == 'Hisuian Sneasel'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Monsoon Pattern'
    ):
      color[f_index] = 'Gray'
    elif (
      forme[f_index] == 'Alolan Sandshrew'
      or forme[f_index] == 'Alolan Vulpix'
      or forme[f_index] == 'Galarian Ponyta'
      or forme[f_index] == 'Galarian Rapidash'
      or forme[f_index] == 'Galarian Mr. Mime'
      or forme[f_index] == 'Galarian Corsola'
      or forme[f_index] == 'Galarian Zigzagoon'
      or name[f_index] == 'Castform' and forme[f_index] == 'Snowy Form'
      or forme[f_index] == 'Mega Audino'
      or forme[f_index] == 'Galarian Darumaka'
      or name[f_index] == 'Darmanitan' and forme[f_index] == 'Galarian Standard Mode'
      or name[f_index] == 'Darmanitan' and forme[f_index] == 'Galarian Zen Mode'
      or name[f_index] == 'Vivillon' and forme[f_index] == 'Icy Snow Pattern'
      or forme[f_index] == 'Female Meowstic'
      or forme[f_index] == 'Ice Rider Calyrex'
      or forme[f_index] == 'Hisuian Braviary'
      or name[f_index] == 'Squawkabilly' and forme[f_index] == 'White Plumage'
    ):
      color[f_index] = 'White'
    elif (
      name[f_index] == 'Cherrim' and forme[f_index] == 'Sunshine Form'
      or name[f_index] == 'Oricorio' and forme[f_index] == "Pa'u Style"
      or name[f_index] == 'Alcremie' and forme[f_index] == 'Ruby Cream'
    ):
      color[f_index] = 'Pink'
    print("Color: " + color[f_index])

    print(" ")
    f_index = f_index + 1
    # print(len(abil1))
    # print(abil1)
    # print(len(abil2))
    # print(abil2)
    # print(len(habil))
    # print(habil)
  p_index = p_index + 1

pokemon = {
  'Dex No.': no,
  'Name': name,
  'Forme': forme,
  'Classification': classification,
  'Generation':generation,
  'Primary Type': primary,
  'Secondary Type': secondary,
  'Ability 1': abil1,
  'Ability 2': abil2,
  'Hidden Ability': habil,
  'Gender': gender,
  'Male Gender Ratio': genderM,
  'Female Gender Ratio': genderF,
  'Catch Rate': catchRate,
  'Egg Group 1': eggGroup1,
  'Egg Group 2': eggGroup2,
  'Hatch Time Cycles': hatchTime,
  'Height (In)': heightIn,
  'Height (M)': heightM,
  'Weight (Lbs)': weightLbs,
  'Weight (Kg)': weightKg,
  'Mega Stone 1': megaStone1,
  'Mega Stone 2': megaStone2,
  'EXP Yield (Gen I)': expYield_I,
  'EXP Yield (Gen II)': expYield_II,
  'EXP Yield (Gen III)': expYield_III,
  'EXP Yield (Gen IV)': expYield_IV,
  'EXP Yield (Gen V+)': expYield_VPlus,
  'Leveling Rate': levelRate,
  'EV Yield (HP)': evYieldHP,
  'EV Yield (Attack)': evYieldAtk,
  'EV Yield (Defense)': evYieldDef,
  'EV Yield (Sp.Atk)': evYieldSpAtk,
  'EV Yield (Sp.Def)': evYieldSpDef,
  'EV Yield (Speed)': evYieldSpd,
  'Shape Img URL': shape,
  'Footprint Img Url': footprint,
  'Base Friendship': baseFriendship,
  'Base HP': hp,
  'Base Attack': atk,
  'Base Defense': defense,
  'Base Special Attack': spatk,
  'Base Special Defense': spdef,
  'Base Speed': spd,
  'Base Stat Total': bst,
  'Color': color,
}

#Create Dataframe
df = pd.DataFrame.from_dict(pokemon)

#Data Cleaning
df.drop_duplicates()

#Write Csv
df.to_csv('bulbapedia_data.csv', index = None, header = True) 
