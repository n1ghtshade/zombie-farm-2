README.md

The Payload/ folder contains the app binary (armv7 mach-O 32-bit) along with all of its resources that it needs to function. Once inside the Payload/ folder, there will be a single file with the “.app” extension. This file is actually just another folder, and you can open it like any other folder. On MacOS, right click it and press “Show Package Contents”.


## Brief overview of iOS app encryption mechanism

Basically every app you download has its binary executable (mach-O binary) encrypted (or codesigned, what you prefer) "on-the-fly" by Apple servers with public-key cryptography, and it's tied to a single apple id. 
When you try to run that .IPA on another device (not logged in with the apple id of the purchaser), that device won't have the key to decrypt the mach-o binary.

In this case, the .ipa has already been decrypted and is available on the releases page, however you will need to either sign the package yourself using XCode with a paid Apple developer account or use a public signing service.
Alternatively on a jailbroken device you can run unsigned apps with [AppSync Unified](https://github.com/akemin-dayo/AppSync) which can be installed inside Cydia after adding [Karen's repo](https://cydia.akemi.ai/?page/net.angelxwind.appsyncunified)

### About Zombie Farm 2

Zombie farm 2 is the highly anticipated sequel to Zombie Farm. It almost exactly like the original, but there are some minor differences, mentioned in the article linked below. 

[Differences from Original](https://zombie-farm.fandom.com/wiki/Zombie_Farm_2)

### Release Notes

New in v2.25:

    improved compatibility with iOS8 and most recent devices
    boosts, zombie, and farm management tools have been moved from "Options" to the main screen, to make them a lot easier to use
    the market has been completely reorganized to make it easier to browse among categories, and choose how to develop your farm
    resource packs (coins and brains) now give a lot more! and the bigger packs even give some extra resources!
    each pack now shows the exact percentage of free stuff granted to the player for the purchase
    many item prizes have been adjusted to better reflect their usefulness
    watch video ads to earn free brains
    various crash and bug fixes to improve the overall experience


### Version History:

May 23, 2012 Initial release
June 05, 2012 New version 2.02
June 14, 2012 New version 2.03
June 26, 2012 New version 2.04
July 12, 2012 New version 2.05
July 26, 2012 New version 2.06
August 14, 2012 New version 2.07
September 07, 2012 New version 2.08
September 25, 2012 New version 2.09
October 08, 2012 New version 2.10
October 24, 2012 New version 2.11
November 06, 2012 New version 2.12
November 22, 2012 New version 2.13
November 30, 2012 New version 2.14
January 15, 2013 New version 2.15
February 02, 2013 New version 2.16
February 22, 2013 New version 2.17
March 02, 2013 New version 2.18
March 15, 2013 New version 2.19
March 29, 2013 New version 2.20
April 12, 2013 New version 2.21
July 17, 2013 New version 2.22
August 20, 2013 New version 2.23
February 15, 2015 New version 2.25
