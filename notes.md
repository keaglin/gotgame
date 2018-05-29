NEXT:  
django api user auth -- a mess 4/19
fix admin stuff; locked out at the moment -- DONE!
add api endpoint to add comments without admin access LOL -- fixed due to fix on line 3

User Auth

Login/out Signup Forms
  - create custom forms
  - style them

Model-related Forms
  - Posts: update, create, delete
  - Comments: update, create, delete
  - Games: update, create, delete (+ admin priv)

"Add" button for creating when on the "List" page; only admins can add new games

Comments: where are they displayed? and how? Maybe they drop down somehow? 

Additional indicators: platform, mic, style (hardcore, casual, mix?)

Styling the Game Detail: 
  - make that image smaller
  - add a blurb next to the game (include the title)
  - uhhh

Forums
  - there was some forum/community building software I REALLY wanted to use that I think started with an S but it seems I failed to bookmark it
  - maybe start with Discord? I like the quickness and efficiency of Discord and ppl can hop on voice chat even if they don't have a mic/headset for their game
  - still like forums for chronology but between posts looking for ppl to play with and Discord, is it actually even necessary?


Need to add more info to posts
  - platform
  - mic/no mic
  - lfg? lfm? 
And add corresponding filter buttons to the game_detail so ppl can get to what they want/need

Change up the urls (make the games the root and then branch off from there)
  - game list is root
  - each game should link to /games/<game title> (or maybe just <title>)
