# Rook
Lightweight voice assistant that parses Berkeley facility websites to answer questions about open hours.

### Setup Instructions:  
Apple scripts unfortunately function only when given absolute paths. Hence, you will need to generate the appropriate scripts using `scrapers/generate_scripts.py`. Pass in the absolute path to the cloned `Rook` directory like so: `python3 generate_scripts.py /Users/YOUR_NAME_HERE/Desktop/Rook`. The program will automatically create a new directory called `scripts` in `Rook` and populate `scripts` with Apple scripts. You can set trigger words to run these scripts with the following steps.

For MacOS pre-Catalina and earlier:
1. Go to Settings -> Accessibility -> Dictation -> Dictation Commands -> `+`.  
2. Type your desired trigger phrase for a particular location (i.e., "what time is the stadium gym open today?")
3. For "Perform:" select Run workflow -> Other -> Path to the relevant Apple script generated by `generate_scripts.py`

For Catalina:
1. Go to Settings -> Accessibility -> Voice Control -> Commands -> `+`.  
2. Steps 2 and 3 are the same as above.

### Usage
For MacOS pre-Catalina and earlier:
To use Rook, tap the `fn` button twice and hold on the second time. The dictation box should pop up. Say the trigger phrase, and the system will parse the relevant web page and read the answer back to you.

For Catalina:
Unfortunately, Catalina no longer allows Dictation to run Apple Scripts. Instead, one must manually turn on Voice Control through Settings -> Accessibility -> Voice Control -> Check `Enable Voice Control`. Alternatively, one can turn on Siri and tell it "Turn on voice control"

Currently Rook supports:

1. Stadium gym hours
2. RSF hours
3. Anthropology library hours
4. VLSB library hours
5. Main stacks library hours
6. Moffitt library hours
7. Haas library hours
8. Kresge library hours
9. Chemistry library hours
10. East Asian library hours
11. Art history library hours
12. Doe library hours
13. Math library hours
14. Morrison library hours
15. Music library hours
16. Optometry library hours
17. Physics library hours
18. BAMPFA library hours
19. Bancroft library hours
20. Boalt library hours
21. Career Center library hours
22. Visual Resources Center hours
23. Earth Sciences library hours
24. Environmental Design library hours
25. Ethnic Studies library hours
26. Graduate Services hours
27. Theology library hours
28. Governmental Studies library hours
29. Transportation library hours
30. Interlibrary Services hours
31. Media library hours
32. Newspaper library hours
33. Northern Regional library hours
34. Privileges hours
35. Robbins library hours
36. Social Research library hours
