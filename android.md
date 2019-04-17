# [Android](https://www.reddit.com/r/androiddev/comments/3ka9j0/what_to_know_for_a_mobile_developer_interview/)

![](http://i.imgur.com/2q7uebE.jpg)

> "Imagine being a phone. At launch, everyone loves you and is in line to get you. You amaze every review website or youtube channel out there. You're beautiful, sturdy, incredibly fast and affordable. People flash new roms on you on the daily. Over thirty THOUSAND people discuss you on a dedicated subreddit. There's millions of apps promoting themselves using you for their screenshots. Your owner takes you everywhere. You're with your owner through the best and worst times, always ready to rock. Your owner promotes you to their friends often. Over time, your power button starts getting funky, new phones come out and then one day, your owner is ordering a new phone through your screen. You try stopping them by randomly rebooting one more time, but this only seems to encourage the owner more. One day, you hear the doorbell. Your owner takes their new phone out of the box, with the same excitement they felt back when you were unboxed 2 years ago. They pick you up one last time to post a photo of the new phone, turn you off, take out your SIM and put you in a drawer never to be picked up again. You wonder where you went wrong. Was it the battery life? The camera? The power button? You lay there, waiting for your battery to completely run out, and when it does, you know you've had a good life." - [/u/alectprasad](https://www.reddit.com/r/Android/comments/721w8x/you_just_got_a_new_smartphone_what_is_the_first/dnfmdp4/)

## [Android Guides](https://github.com/codepath/android_guides/wiki)

1. If you don't have a phone app (say you adb disabled it) and someone calls you, the device will still ring, but you will have no way to answer.
1. Assuming a reasonable goal of owning a phone for $0.50 per day, and you aim to use it for 2 years, the maximum cost (before tax) of such a phone is ~$323, or, if you plan to keep it for 3 whole years, then ~$484. In contrast, your phone (~$700) needs ~3.5 years to pay itself off, and the earliest you can get a new phone is: *February 2021*. **Repair your devices.**
1. Use [`monkey -p com.packagename 1`](https://stackoverflow.com/a/25398877/1558430) to launch an app without input.
1. Your particular device's fstab file is located at `/system/vendor/etc/fstab.qcom`. You can change your zram size there (if you enabled it).
1. If your device is *not* encrypted, and you encounter "incorrect password/pin" after restoring from a NANDroid backup, [try this](https://android.gadgethacks.com/how-to/fix-wrong-pin-errors-after-restoring-nandroid-backup-0176446/) or just delete `/data/system/locksettings.db`, which says you should have a PIN.
1. To automate scrolling up a long list, use `while true; do input swipe 300 300 300 1500 100; done`.
1. During the Pixel 3 announcement, [Google did not mention "Android" a single time](https://bgr.com/2018/10/12/android-vs-fuchsia-pixel-3-event-no-android-mention/).
1. [Throwing a file into the "intent firewall" directory](https://android.stackexchange.com/questions/128053/removing-a-contact-from-direct-share-panel/160350#160350) instantly disables direct share, without the need for an xposed module.
1. To get how healthy your battery thinks it is, use `adb shell 'su -c cat /sys/class/power_supply/battery/charge_full_design'` from your laptop.
1. [Android 9 Pie is a whole load of crap](https://www.reddit.com/r/Android/comments/9dprkc/if_you_could_what_changes_would_you_make_to/): left clock can't be moved, circular status bar thing can't be themed away (because substratum theming doesn't work), can't record calls, horizontal recents doesn't scroll well...
1. Samsung earns far more in its semiconductor business than its smartphone business, because smartphones are now a commodity, and have low profit margins. [It does not innovate in the smartphone business unless it has to.](https://www.youtube.com/watch?v=k05Q1k4A5ls) Sony had made a similar pivot to playstation and image sensors.
1. [Xiaomi's "we'll make only 5%" slogan is a PR campaign](https://www.youtube.com/watch?v=esUOQpKNLsE), because firstly, the 5% only applies to their hardware business, where they don't earn money anyway, and secondly, investors do know the difference, so they will realise that lower hardware prices means higher profits from MIUI, their software division.
1. Any app with "storage" access can [modify another app's update files](http://blog.checkpoint.com/2018/08/12/man-in-the-disk-a-new-attack-surface-for-android-apps/) to run malicious executable updates.
1. LineageOS devs clearly and explicitly outline [hardware and software requirements for a device to qualify for an official build](https://github.com/LineageOS/charter/blob/master/device-support-requirements.md).
1. `adb install -r` installs the apk without failing when it already exists.
1. If you have both exactly one device and exactly one emulator running, [`adb -e`](http://stackoverflow.com/a/20163013/1558430) chooses the emulator, and `adb -d` chooses the only connected device.
1. To remove Google Play Services from the whitelist that lets them do whatever they want without battery optimisation, [edit the `/system/etc/sysconfig/google.xml` file](https://android.stackexchange.com/questions/143247/how-to-make-google-play-services-and-other-default-white-listed-system-apps-doze) and comment out the appropriate sections.
1. [`.dex` files are VM caches in an APK](https://www.addictivetips.com/mobile/what-is-odex-and-deodex-in-android-complete-guide/), and `.odex` files are optimised VM caches outside an APK. "De-odexed" ROMs put the odex files inside the APK, so you can mod the APK or something without odex files conflicting with it.
1. As of 2018-05-04, a package called `com.google.android.quicksearchbox` contained an [offline podcast](https://www.androidpolice.com/2018/05/04/can-now-download-podcasts-listen-offline-google-app/) function.
1. "Some apps will use OpenSL ES for Android to record audio, an example is WhatsApp. Xposed cannot hook into native code, so this cannot be prevented." - XPrivacyLua
1. To "verify udev rules", [do this](https://gist.github.com/smac89/251368c8df2ccd645baedc3e1238fdb4): enter `SUBSYSTEM=="usb", ATTR{idVendor}=="05c6", MODE="0666", GROUP="plugdev"` into `/etc/udev/rules.d/51-android.rules`, `chmod a+r` that file, and then `sudo udevadm control --reload-rules && sudo udevadm trigger`.
1. There is [no straightforward way](https://stackoverflow.com/questions/16650765/get-application-name-label-via-adb-shell-or-terminal) to find a package's application label by ID. At minimum, you need to first find the path to your APK (`pm list packages -f com.example.package`), then somehow transfer that to `aapt dump badging /path/to/installed.apk`.
1. [More people downloaded Subway Surfers than Google Calendar.](https://en.wikipedia.org/wiki/List_of_most_downloaded_Google_Play_applications)
1. From GCMod5's point of view (called `GCam5.1.014-Arnova8G2-v11.1-N.apk`), your particular device is closer to Nexus 6 than it is to Nexus 6P.
1. The Facebook Android app has [2.2 billion monthly active users](https://growthbug.com/google-play-store-data-3-7mn-36331f2c8b26), only a small percentage of which would be bots given the collection method.
1. You can `pm disable` apps or components (with root), [`pm hide` only apps](https://android.stackexchange.com/questions/128949/pm-hide-vs-pm-disable-the-identity-crisis#comment160333_128949) (no root), or `pm uninstall -k --user 0 ...` (also no root).
1. Using OpenKeychain [requires](https://www.openkeychain.org/faq/#are-my-secret-keys-safe-on-my-mobile-device) your secret key to be on your mobile device. The project knows that this is inherently less secure than if your key were stored offline in a remote bank vault.
1. 2018-04-01 LineageOS builds have [an Easter egg that a) got pushed to devices late, and b) will not disappear after April Fools day](https://www.lineageos.org/An-April-Apology/).
1. Qualcomm Quickboot is just putting the phone in a [special kind of airplane mode](https://forum.xda-developers.com/android/software/universal-quickboot-cyanogenmod-12-0-12-t3082041).
1. OnePlus 2 and 3 had the lamest codenames in the series: bacon (1), onyx (X), *oneplus2* (2), *oneplus3* (3/3T), cheeseburger (5), dumpling (5T), enchilada (6), fajita (6T).
1. [Samsung phones (article: Galaxy S8) lose 20% battery capacity when rooted](https://www.xda-developers.com/sampwnd-root-galaxy-s8-snapdragon/) because Samsung really hates you, your life choices, and making money off you.
1. Inputs can be emulated with [`input tap x y` and `input swipe x1 y1 x2 y2`](https://forum.xda-developers.com/u/tasker-tips-tricks/best-run-shell-commands-tasker-t3419204)
1. Screen off gestures not working might be MinMinGuard's fault. To fix, wipe your Dalvik/ART cache, and not ironically.
1. `pkill -l19 com.xiaomi.hm.health  # SIGSTOP that damn background process`
1. `pkill -l18 com.xiaomi.hm.health  # SIGCONT that app so it works again`
1. You can stop mpdecision by simply typing [`stop mpdecision`](https://stackoverflow.com/questions/20221680/android-how-to-force-cpu-core-offlineshut-down-cores).
1. When your phone says it accepts a max of 5 fingerprints, [you can put multiple fingers on the sensor in a single run, fun fact...](https://www.reddit.com/r/GalaxyS7/comments/4bd8s9/more_than_four_fingerprints/d188r2j/)
1. Doze parameters can be found [here](https://forum.xda-developers.com/android/apps-games/root-doze-settings-editor-android-t3235130). A flowchart of doze's events can be found [here](https://forum.xda-developers.com/android/apps-games/root-doze-settings-editor-android-t3235130/post63962529#post63962529).
1. Remember, the next time they stop updating their devices, put "🅵🆄🅲🅺🅾🅽🅴🅿🅻🆄🆂" up as your reddit flair.
1. `adb logcat *:W` to filter at least WARN.
1. [Lots of `build.prop` entries don't do anything.](https://forum.xda-developers.com/showthread.php?t=2544330)
1. `dumpsys batterystats --reset  # resets battery graph`
1. [`pm grant com.uzumapps.wakelockdetector.noroot android.permission.BATTERY_STATS`](https://forums.androidcentral.com/moto-g-2016/700464-wakelock-detector-no-root-required.html): [`cmd appops set com.android.application WAKE_LOCK ignore`](https://www.xda-developers.com/stop-wakelocks-android-without-root/)
1. On the opposite (coincidentally, the same) side of the planet, [two Internet giants do mentally special things to each other on their users' phones in other to share shopping links over a chat service](https://www.reddit.com/r/oneplus/comments/7prvrj/i_looked_into_what_actually_is_being_sent_and/dsk9ykl/)
1. LG G3, G4, [*AND* G5](https://www.reddit.com/r/Android/comments/7mmz3s/htc_and_motorola_say_they_dont_slow_old_phones/drvh082/) bootloop.
1. ShareIt, CM browser, DU battery saver, and ES file explorer are among the apps that [China uses to spy on other countries](https://www.reddit.com/r/Android/comments/7godzf/china_is_spying_through_42_apps_delete_them/dqlb3yh/).
1. The battery stats is reset when it reaches [MAX_HISTORY_BUFFER](https://github.com/aosp-mirror/platform_frameworks_base/blob/master/core/java/com/android/internal/os/BatteryStatsImpl.java), which is 256kB.
1. If the [camera mods](https://www.celsoazevedo.com/files/android/google-camera/) don't work, you need to [enable the Camera2 API](https://forum.xda-developers.com/apps/magisk/module-camera2api-enabler-t3656651) (`persist.camera.HAL3.enabled=1`) first.
1. Cyanogen was [Steve Kondik's nickname](https://github.com/cyanogen). He created CyanogenMod.
1. `adb shell dumpsys batterystats --reset` resets the battery graph.
1. The Moto E(2) is [a bitch to fix](https://www.ifixit.com/Guide/Motorola+Moto+E+2nd+Generation+Battery+Replacement/56502).
1. Not being on a stock rom while relocking your bootloader will brick the device, says [this guy](https://forum.xda-developers.com/showpost.php?p=69267541&postcount=9).
1. If your friendly local LineageOS installation complains about [having no `TERM` variable](https://jira.lineageos.org/browse/BUGBASH-556?attachmentViewMode=list), then see if adding `export TERM=xterm` to `/etc/mkshrc` helps. The message you get is: `Error opening terminal: unknown.`
1. The Pixel has [Snapdragon 821-AB](https://www.xda-developers.com/dissecting-speed-how-oneplus-leveraged-excellent-real-world-performance/), whereas the Oneplus 3T has Snapdragon 821-AC, with a slightly higher boost frequency.
1. Face Unlock is less popular in countries like Saudi Arabia and UAE.
1. Download the SDK before attempting to compile anything.
1. Daydream is triggered only if the device is allowed to sleep from screen timeout while charging. Pressing the power button at any time will cancel the timeout.
1. Use the ["debug GPU overdraw"](https://www.youtube.com/watch?v=I4MhEx-nck4) thing in developer options to check where your app is drawing over a pixel twice or more (which is wasteful), including re-computing the colour over transparent areas.
1. Google Play Services keeps track of your boot count in a `shared_prefs/bootCount.xml`.
1. The Nexus 5x has a fake bottom speaker grille.
1. September 2017--a month which will live in infamy--both [BroadPwn](https://blog.exodusintel.com/2017/07/26/broadpwn/) and [Blueborne](https://www.armis.com/blueBorne/) vulnerabilities were released into the wild. In the same month, Google released Android O[nion], rendering all N-based ROMs vulnerable to these attacks.
1. CAF (Code Aurora Forums) is not the project; "Android for MSM" is the project. When dudes say they are based on CAF, they actually mean they are based on Android for MSM by CAF.
1. In a very glitchy way, one-handed mode is shipped with Android 6.0 using the [`wm overscan`](https://forum.xda-developers.com/u/tasker-tips-tricks/guide-hold-swipe-home-button-to-enable-t3330353) command.
1. Android devices can be rooted with the [row hammer effect](https://en.wikipedia.org/wiki/Row_hammer). "Repeatedly accessing data stored in memory chips could flip certain bits," say [Arstechnica](https://arstechnica.com/information-technology/2016/10/using-rowhammer-bitflips-to-root-android-phones-is-now-a-thing/).
1. Stop (my particular android) device from charging using `echo 0 > /sys/class/power_supply/battery/charging_enabled`. (Use 1 to re-enable, or 2 to blow the phone up.) Note the power manager wakelock will be active even if you aren't charging, so the device never goes to sleep when plugged in.
1. Samsung is not an Android manufacturer for Google; [Samsung is a conglomerate that wants to take Android off Google](https://www.youtube.com/watch?v=2_L9j6mDJBg). No other series of devices have both Samsung and Google Apps suites.
1. Tapping "Cached data" in System>Storage on Android clears caches for all apps. Beware, it also clears Google offline maps and gReader article data.
1. If a Oneplus One boot loops because of a [corrupt `persist` partition](http://www.androidpolice.com/2014/10/13/heres-easy-fix-oneplus-one-sudden-death-bug-results-neverending-boot-loops/), run `make_ext4fs /dev/block/mmcblk0p15`
1. As of ~~Android L~~CyanogenMod 12, the shell now comes with [htop](http://en.wikipedia.org/wiki/Htop) (or its busybox).
1. However much Google results decide to decay, the way to check (your particular android) device's battery percentage is `cat /sys/class/power_supply/battery/capacity`.
1. [The last three digits of a Google Play Services package](https://www.reddit.com/r/Android/comments/3mh7vt/new_google_play_services_8118_438/cvf1ni5) defines the compatible android version, CPU architecture, and PPI, respectively. The most common combination is "030", package for Pre-5 devices.
1. MediaTek is "not that much worse" than Qualcomm *iff* [you don't use custom ROMs](https://www.reddit.com/r/Android/comments/6p8nio/is_mediatek_really_that_worse/).
1. Do not give internet access to Android System WebView. Granting network to this component gives all apps that use this component internet access, even if they aren't themselves whitelisted.
1. "userdebug" seen in Android's build string apparently means something. ["No root because it's a 'user' build, which is what manufacturers ship. 'userdebug' builds which contain root also contain debugging tools and other things that some users might consider to be bugs."](https://www.reddit.com/r/oneplus/comments/3sre4p/exodus_511_nightlies_vs_60_sultans_rom/cx07d0u)
1. ["You may already know that every app/process in Android is assigned an oom_adj value, which indicates the likelihood of it being killed when an out of memory (OOM) situation occurs. More higher it's value, the higher likelihood of it getting killed. Valid range is -17 to +15. (if in the -17 range means it won't get killed)."](http://forum.xda-developers.com/showthread.php?t=2751559)
1. [Android N will have *two* system partitions](https://en.wikipedia.org/wiki/Android_Nougat#Development_platform), one online and one offline. The online one will push updates to the offline one, and they switch once the offline one is updated.
1. Mounting android's system as rw: `mount -o remount,rw /system`
1. Mounting android's system as ro: `mount -o remount,ro /system` (I know right)
1. The file `batterystats.bin` is used to display the battery graph, and [has no impact on battery capacity](https://androidcentral.com/wiping-battery-stats-doesnt-improve-battery-life-says-google-engineer) or battery life.
1. CyanogenMod supports [9 out of however many](https://wiki.lineageos.org/devices/athene/#special-boot-modes) Moto G4s out there.
1. In Tasker, "top priority" is 50, not 1.
1. The Samsung Galaxy Note II (Note 2) had a 5.5 inch screen, the size everyone has today. Nexus 6p, which was never sold as a phablet, share the same screen size with the Note 3, 4, 5, and 7.
1. [Accelerometer readings can be used to reverse engineer what you were typing](https://www.youtube.com/watch?v=metkEeZvHTg), including passwords. Video was from 2011.
1. People can totally downgrade your APK while preserving data with the 'adb -r -d' options.
