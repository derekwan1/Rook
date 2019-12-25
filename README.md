# Rook
Scrapers for common Berkeley queries

### Setup Instructions:  
For MacOS pre-Catalina and earlier:
1. Go to Settings -> Accessibility -> Dictation -> Dictation Commands -> `+`.  
2. Type your desired trigger phrase for a particular location (i.e., "what time is the stadium gym open today?")
3. For "Perform:" select Run workflow -> Other -> Path to the relevant Apple script in this repo.

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

I will likely expand functionality to other commonly queried locations.
