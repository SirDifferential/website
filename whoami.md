# Portfolio

My name is Jesse Kaukonen. I'm a programmer and computer enthusiast located in Espoo, Finland. I've been interested in computers and video games since my early childhood when I had an Amiga 500, which I still have in working order on my desk. My interests lay mainly in parallel computing, code optimization, hardware programming, 3D and graphics programming, video games, and procedural generation. I'm not interested in web development if I can avoid it. I prefer programming in C for its simplicity and understandable ecosystem, and overall believe in strongly typed languages with a compiler spotting errors before they occur in runtime.

## Professional

### Nexi Digital Finland
#### Senior software developer in payment terminals (2021 - present)

At Nexi Digital Finland my work involves credit & debit card payment terminals. My role specifically is focused on the business logic inside the physical device into which the customer inserts their credit card.

This company was previously called Nets Denmark / Poplatek.

Assorted technologies I work with: C, LUA, Kotlin, Java, Javascript, Nodejs, Linux, Android, EMV, APDU, Ghidra

### Delicode Ltd
#### Lead software developer (2014 - 2021)

<iframe width="500" height="300" src="https://www.youtube.com/embed/A-6XqqYWzU8" frameborder="0" allowfullscreen></iframe>

I was employed at [Delicode](https://www.delicode.com/) as a software developer. My work focused around infrared depth cameras, embedded devices, USB devices, computer vision, servers and customer service.

[Delicode Signals](https://signals.delicode.com) is a people counting & analytics solution using infrared depth cameras.

[NI mate](https://ni-mate.com) is a program that communicates with USB depth sensors and processes their depth images into usable data. Examples of data that NI mate computes are skeleton joints from detected users, user location information, and floor planes. NI mate is used for interactive adverts, motion capture, education, and art installations.

[Z-Vector](https://z-vector.com) is a real-time VJ visualization tool that creates a 3D point-cloud based visualizations out of the captured depth + color feed using an infrared camera. Z-Vector has been used for several music videos, such as [Kebu - Deep Blue](https://www.youtube.com/watch?v=A-6XqqYWzU8) and [Phantom - Scars](https://www.youtube.com/watch?v=HFpou6izBQg).

Assorted technologies I worked with: C, C++, Assembly, ARM NEON & x86 SIMD, OpenGL, Python, Golang, Rust, Javascript, Nodejs, Qt, USB, UEFI / BIOS, Blender, Cinema 4D, Maya, 3ds Max

### Tmi Jesse Kaukonen
#### Entrepreneur (2010-2017)

I ran my own software / 3D modeling business for several years, doing a few odd jobs here and there. This was mostly for some secondary income.

### Renderfarm.fi
#### Distributed volunteer rendering (2010-2014)

<iframe width="500" height="300" src="https://www.youtube.com/embed/4VUWrZRCtI8" frameborder="0" allowfullscreen></iframe>

During / after my intership at Turku Polytechnic I worked at a project called renderfarm.fi that utilized [BURP](http://burp.renderfarming.net/development/v2_files/) (Big and Ugly Rendering Project) for distributed volunteer rendering with [Blender](https://www.blender.org/) and [BOINC](https://boinc.berkeley.edu/) (Berkeley Open Infrastructure for Network Computing). This was my first real programming job and I learned a ton. Unfortunately the project wasn't viable as a business and ultimately went defunct.

At renderfarm.fi I did coding, design, testing, customer support and server & database maintenance.

## Personal

### Farstrider Oy
#### Novelist

[![farstrider](pics/farstrider-web.png 'farstrider')](https://farstrider.fi)

I write novels and publish them via my own [book publication business](https://farstrider.fi). My work is mostly fantasy of various types. Currently all my weekends and vacations are spent on this activity.

* [Company website](https://farstrider.fi)

### Art portfolio

[![art portfolio](pics/artportfolio.png 'Art portfolio')](https://art.plantmonster.net)

I started learning art in 2023 and wanted some place to share my progress, mainly so I could illustrate my own novels. I wanted a static website that was in my own control where I had to do minimal amount of work to publish the pieces.

The solution I went with is simply parsing art piece filenames for the piece number and date, and reading an optional JSON file with description and licensing information.

* [Live site](https://art.plantmonster.net)
* [Github link](https://github.com/SirDifferential/art-portfolio)

### Loathsome Bäsk Drinker
#### Live gaming session turn timer

[![baskdrinker](pics/baskdrinker.png 'Loathsome Bäsk Drinker')](https://github.com/SirDifferential/baskdrinker)

We occasionally gather to play Souls-like games in a form of couch gaming. As we got too good in the games and no longer died (which was the turn control system earlier), we decided to start using a timer so people don't have to wait too long for their own turn. This called for an engineering solution.

We wrote a software in Qt to define custom timers and warning sounds. Another software, the [Loathsome Pad Swapper](https://github.com/Sonicus/loathsome-pad-swapper), communicates with this software over a websocket API, toggling the currently active gamepad via [ViGemBus](https://github.com/nefarius/ViGEmBus) driver.

This way two gamepads can be used on the couch, and upon hearing a warning sound, all that is needed is for people to pick up the currently inactive gamepad. Once the timer expires, control over the game is switched between the two controllers and the previously active gamepad is calmly and orderly passed to the new player waiting for their turn without anyone having to panic or toss the gamepads around.

Honestly, we're kind of amazed this actually works.

* [Github link](https://github.com/SirDifferential/baskdrinker)

### Derpling Uploader
#### Starcraft 2 replay uploader

[![derpling](pics/sc2replaystats.png 'Derpling Uploader')](https://github.com/SirDifferential/derpling_uploader)

This is a tool I wrote to automatically upload Starcraft 2 replay files to sc2replaystats.com. They offer their own tool to perform the same task, but it's a closed source executable binary that requires admin privileges. I didn't feel like installing it on my computer, so I wrote my own auditable version instead.

* [Github link](https://github.com/SirDifferential/derpling_uploader)

### Sonic 1 romhack
#### Romhack for bachelor party

[![romhack](pics/romhack_kekkonen2.png 'romhack')](https://github.com/pts-demos/s1disasm)

We created a Sonic 1 romhack for a friend's bachelor party. You can read about it in [this](https://jessekaukonen.net/blog_romhack.html) blog entry.

* [Github link](https://github.com/pts-demos/s1disasm)

### PTSD
#### Sega Megadrive demo

[![ptsd](pics/ptsd_ukk.png 'ptsd')](https://bitbucket.org/ptsdemos/segademo)

Our demo group, [PTS](http://www.pouet.net/groups.php?which=13815), released our first demo for the [Simulaatio 2018](http://www.pouet.net/party.php?which=1099&when=2018) demo party. This demo was the first time any of us worked with this hardware. Our expectations were largely limited to getting anything at all done and released, a goal we achieved after some party coding to wrap things up. As someone else put it, "It's not quite [Titan](http://www.pouet.net/prod.php?which=61724) yet, but that's the next one, right?"

* [Pouet link](http://www.pouet.net/prod.php?which=76304)
* [Source code](https://bitbucket.org/ptsdemos/segademo)
* [Detailed blog entry](https://jessekaukonen.net/blog_ptsd.html)

### Proceduralis
#### OpenCL based procedural world generator

[![proceduralis](pics/proceduralis.png 'proceduralis')](https://github.com/SirDifferential/proceduralis)

Ever since I first played Dwarf Fortress, I've been fascinated by procedural world generation. While I had studied the basic tools used by such games, I never truly implemented them in practise. As I got into studying some OpenCL, I suddenly figured it would be fun to create a world using the GPU's immense computational power. You can read more about this project in the relevant [blog entry](./blog_proceduralis.html).

* [Github link](https://github.com/SirDifferential/proceduralis)

### Shiver's Balance Mod
#### Star Control 2 online play improvement

[![balance mod](pics/balancemod.png 'balance-mod')](https://github.com/uqm-arena/balance-mod)

Originally and mainly created by the fellow going by the username Shiver, the Balance Mod balances the very broken multiplayer supermelee of Star Control 2. The mod has been a work of love by Shiver, and to lesser part by myself and a few other people. I was mostly involved in testing early on, but performed some development and maintaining tasks later on.

* [Github link](https://github.com/uqm-arena/balance-mod)

### Global Tech
#### Europa Univeralis 4 modification

[![global tech](pics/gtech.jpg 'global tech')](https://steamcommunity.com/sharedfiles/filedetails/?id=258318354&searchtext=global+tech)

A product of one day during which I wondered how EU4 would work if every nation in the game used western tech. After a spell of scripting the results were so fun I decided to publish the mod.

[Steam workshop link](https://steamcommunity.com/sharedfiles/filedetails/?id=258318354&searchtext=global+tech)

### Python MIDI
#### Synthesizer-to-python Star Control 2

<iframe width="500" height="300" src="https://www.youtube.com/embed/aRz1xe9Kff8" frameborder="0" allowfullscreen></iframe>

A software that reads data from a MIDI keyboard and converts that into keyboard events, allowing playing video games via MIDI input.

* [Github link](https://github.com/SirDifferential/instrument_controller)

### batchrender.py
#### Sequential rendering plugin for Blender

[![batchrender](pics/batchrender.png 'batchrender')](https://github.com/SirDifferential/batch_render)

Someone on IRC complained that Blender didn't have a tool for setting up sequential render tasks that the computer would automatically execute in a queue. As the Blender's Python API is pretty clear it didn't take long for me to write such a tool.

* [Github link](https://github.com/SirDifferential/batch_render)

### Website
#### You're reading it

My website is made entirely out of markdown turned into HTML with minimal amounts of extra junk, always served as static files, using the Github markdown style. The pages are created using a bash script and some Python. To this day I haven't found any problems with this system. It's minimal and works, no need for bloated frameworks or vulnerable dependencies.

* [Github link](https://github.com/sirdifferential/website)

### Story of a Lost Sky
#### Touhou fangame RPG

I ran into a Touhou fan game project I liked, found a couple of bugs and ended up doing dedicated testing for a while. Unfortunately the website for this game is no longer around.

### Free software contributions

Here's some projects for which I've made contributions:

* [libfreenect2](https://github.com/openkinect/libfreenect2)
* [Now defunct Orbbec Astra SDK](https://github.com/orbbec/astra), replaced by the [new SDK](https://github.com/orbbec/OrbbecSDK)

### KAAL
#### Short film

<iframe width="500" height="300" src="https://www.youtube.com/embed/uqbVLlJjku8" frameborder="0" allowfullscreen></iframe>

We created a short film for the Kill All Audio and Lights competition at Assembly 2009. The idea was to make a very loud and visual film that would be shown on the screen when the audience was to shut their audio systems and displays. The project included three graphics artists and one musician, with me mostly responsible for the landscape and props, as well as animation.

### Haba-ipa
#### Beer brewing documentary

<iframe width="500" height="300" src="https://www.youtube.com/embed/kvvKGE30-6k" frameborder="0" allowfullscreen></iframe>

Olutkulttuuriseura, a beer association in Finland, organized a beer brewing competition for the annual party in 2017. The members in the Helsinki region got together to brew a beer together. As part of this I filmed a documentary about how the beer was made. This video was targeted mainly at people interested in beer while also serving as a publicity stunt to broaden the understanding about beer culture.

The filming was done using one Sony handheld camcorder that had a really low quality mic and some exposure problems. The audio had some noise in it that I didn't bother fixing.

Special thanks to the brewing meister for allowing to film this as well as offering critique on the footage. The assorted members of Olutkulttuuriseura also assisted. Kristian Kristola, Mika Saari and RantingHuman offered me critique.

[Detailed blog entry](https://jessekaukonen.net/blog_habaipa.html)

