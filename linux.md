![Dilbert][imgur]

1. On [`supervisorctl` commands](http://supervisord.org/running.html): `supervisorctl reread` reloads the configs, `supervisorctl reload` restarts the daemon (you might see a trend here), `supervisorctl restart` restarts without reloading the config, and `supervisorctl update` is said to do both `reread` and `restart`.
1. 64-bit implementations of the linux epoch allows [292 billion years](https://en.wikipedia.org/wiki/9,223,372,036,854,775,807) to be represented in an integer.
1. Linus' first rule of Linux development is "we don't break userspace". That means [never affect the user's applications negatively](https://stackoverflow.com/questions/25954270/what-does-it-mean-to-break-user-space).
1. If the KDE display configuration messes up, delete your `.local/share/kscreen/` folder or move it somewhere else.
1. Exclude a grep with `grep -v bad_word`.
1. HTTPS is considered necessary [even if PGP signing is verified correctly](https://www.reddit.com/r/linux/comments/ahkur8/vlc_refuses_to_update_from_http_to_https_https/): a "version freeze attack" that MITMs unverified traffic, making the user believe what's being seen is true; and weak signing key.
1. On multi-CPU systems, a load average less than or equal to the number of CPU cores (e.g. 3.7 < 4 CPUs) is [still considered healthy](http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages). Also, the load averages are listed with the last minute figure *first*.
1. KDE might require `im-config -n ibus` (and a logout) for ibus to start working.
1. [glogg](https://glogg.bonnefon.org/index.html) is a log file viewer UI, like somewhere between grep and less, maybe tail.
1. To extract a `.bz2` file that is *not* also a tarball, use `bzip2 -dk filename.bz2`.
1. `tar vf` does not have the 'origin ... destination ...' syntax. The first argument is still the archive file name, and the rest of the arguments are always what you want to compress/extract.
1. In 2004, [Ubuntu's boot image, among other things, were pictures of three people being naked](http://geekfeminism.wikia.com/wiki/Ubuntu_Warty_visual_theme/Image_archive).
1. If you add [`StrictHostKeyChecking no`](https://stackoverflow.com/questions/21383806/how-can-i-force-ssh-to-accept-a-new-host-fingerprint-from-the-command-line) to your `.ssh/config`, or run ssh as `ssh -o 'StrictHostKeyChecking no'`, then it will accept any host key without asking you (or your scripts) first.
1. Tarsnap is a portmanteau (which is a portable all-in-one closet, by the way) of `tar`, and "snapshot", which tarsnap does.
1. `inotify` watch limits appear to be put in to [limit memory use](https://stackoverflow.com/questions/535768/what-is-a-reasonable-amount-of-inotify-watches-with-linux), rather than to limit CPU use.
1. To make KDE not hiccup while moving files to the trash, [uncheck the "Limit to maximum size" option](https://forum.kde.org/viewtopic.php?f=224&t=140002). Observe that trash operations become instant.
1. Fix your everyday "WiFi keeps disconnecting on my (ubuntu wifi) laptop" problem by adding [`options iwlwifi 11n_disable=1`](https://appuals.com/ubuntu-16-04-to-17-10-wifi-and-ethernet-problem/) to the appropriate file in `/etc/modprobe.d`.
1. KDE's screenshot tool is called [`spectacle`](https://www.kde.org/applications/graphics/spectacle/).
1. The name `grep` came from the `ed` command pattern `g/re/p` (find global matches of "re" and print them). Also, [`ed` is pronounced "EE DEE", says man](https://www.youtube.com/watch?v=NTfOnGZUZDk).
1. `cat /path/to/{file1,file2,file3}` really lets you cat the three files without going there.
1. [`tail *`](https://stackoverflow.com/a/7816490/1558430) is a viable alternative to `cat *` if you want to see the file names as well.
1. There's [a script](https://github.com/Nyr/openvpn-install/blob/master/openvpn-install.sh) that installs openvpn for you.
1. You can [unset expiry dates you place on your pgp keys](https://riseup.net/en/security/message-security/openpgp/best-practices#use-an-expiration-date-less-than-two-years), says that page. The purpose of the expiration date is to be a dead man's switch to prevent further uses of the key after you die. Same page also says not to sign someone else's key with no expiration date.
1. [It is systemd's fault](https://askubuntu.com/a/723182) why your network interface is now called "wlp2s0" instead of "wlan0". "p2" is "PCI bus 2", and "s0" is "slot 0".
1. The `ServerAdmin` directive in apache2 [doesn't work](https://stackoverflow.com/q/21798272/1558430).
1. [`a2enssite` and `a2dissite`](https://manpages.debian.org/jessie/apache2/a2dissite.8.en.html) stand for "Apache2 enable site" and "Apache2 disable site", respectively.
1. Simply using [`sort -`](https://stackoverflow.com/a/2434719/1558430) will allow you to paste in any number of lines to be sorted. If too lazy to paste, you can also use `xclip -o | sort -`.
1. FUSE [probably](https://en.wikipedia.org/wiki/Filesystem_in_Userspace) stands for FilesysteminUserSpacE.
1. `Ctrl+U` in the shell deletes the entire command. `Ctrl+K` deletes anything right of the cursor.
1. The `PermitRootLogin without-password` directive actually means "disallow logging in as root with a password", not "allow root to log in without a password".
1. You are supposed to throw your personal binaries in `~/.local/bin/`.
1. If you change from a swap partition (linux default) to a swap file (windows default), then you can resize your swap without having to fuck [sic] with the partition scheme.
1. To show your swap files: `cat /proc/swaps`
1. There is `p7zip`; and then there is `7z`. You should probably use `7z` for simplicity: [`7z a outfile infile`](https://www.ibm.com/developerworks/community/blogs/6e6f6d1b-95c3-46df-8a26-b7efd8ee4b57/entry/how_to_use_7zip_on_linux_command_line144?lang=en) or [`7z a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on outfile infile`](https://askubuntu.com/questions/491223/7z-ultra-settings-for-zip-format)
1. `man 7z`: "DO NOT USE the 7-zip format for backup purpose on Linux/Unix because: 7-zip does not store the owner/group of the file."
1. [RMS eats stuff he grew himself (on his own feet).](https://www.youtube.com/watch?v=I25UeVXrEHQ) Probably licenced under GPLv3 too.
1. Pressing capital `H` in htop hides all user threads.
1. Pressing capital `P` in htop sorts by CPU.
1. Pressing capital `M` in htop sorts by memory usage.
1. In `gpg` (gnupg), `usage: S` means Signing, and `usage: E` means Encryption. [`C` is CERT and `A` is AUTH.](https://unix.stackexchange.com/a/32031) [The master key can never be used for encryption.](https://wiki.debian.org/Subkeys)
1. `dig` is "domain information groper". Tool names were more colourful back then.
1. The `rc` in `.foorc` meant [runcom](https://stackoverflow.com/a/11030607/1558430). It came from [CTSS](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System) (initial release 1961).
1. [`beep`](https://unix.stackexchange.com/questions/1974/how-do-i-make-my-pc-speaker-beep) hardly ever works if you have a laptop, or if you are logged in via ssh.
1. It used to be the case that [`finger`](https://en.wikipedia.org/?title=Finger_protocol) could read a user's `.plan(s)` file, which reveals the user's current activities. It was a form of blogging.
1. `freshclam` is the [command for updating ClamAV](https://help.ubuntu.com/community/ClamAV), not the scanning command.
1. [`Ctrl+z` stops a job.](https://www.howtogeek.com/111417/how-to-multitask-in-the-linux-terminal-3-ways-to-use-multiple-shells-at-once/) `jobs` lets you see your jobs. `fg %1` brings back up whichever one is the first job. `kill %1` then kills it. This concludes linux job control.
1. Use screen. While a little troublesome for ordinary things that tabs can do, `Ctrl+a, d` will detach a screen (and have its stuff run in the background, even after you exit ssh), and `screen -r` resumes that session.
1. Want a progress bar for `cp`? *NO YOU CAN'T!* (:D) But you can replace the command with [`rsync -ah --process src dest`](https://askubuntu.com/questions/17275/progress-and-speed-with-cp), if you are okay with a slightly slower transfer.
1. `ls -S` sorts files by size, *descending*.
1. [`/` is hardcoded to be forbidden in file names.](https://stackoverflow.com/a/9847573/1558430) You can still use any unicode slashes though.
1. `findmnt` is `mount` in tree form. See also: `lsblk`.
1. apt installing `git` installs the same things as `git-core`.
1. `git --amen` works!
1. The command for displaying `ls` like a tree is literally [`tree`](http://stackoverflow.com/a/3455675/1558430), as an optional install for some distros.
1. `yum` is managed by a list of repository configs in `/etc/yum.repos.d/`, each being an ini file.
1. EC2 has [Extra Packages for Enterprise Linux][amazon] (EPEL).
1. [Adding a new yum repository][cyberciti]
1. yum can be used in conjunction with [package priorities][serverfault] to determine which version of a package to install, if many repositories provide the same package.
1. Processing getting killed across SSH? [`nohup something &`][wikipedia]. This took way too long.
1. `-f` for `tail` autoscrolls it. Because `-f` is `--follow`. Because screw `-f` being `--file`.
1. Count instances of `foo`: `foo | grep -c .`
1. Log in as someone else: `(sudo) su - username`
1. `>` [redirects to (and overwrites) a file](http://linuxcommand.org/lts0060.php), while `<` redirects a file to a command. Both must appear after a command. So if you expect something like
    ```
    input_file.txt > command > output_file.txt      # You'd be bitterly disappointed
    command < input_file.txt > output_file.txt      # Instead, you live with this garbage
    cat input_file.txt | command > output_file.txt  # or win the useless cat award
    ```
1. `cat * > new_file` overwrites contents in `new_file` with everything else in the folder. However, [`cat anything`](http://porkmail.org/era/unix/award.html#backticks) (with the backticks) is dangerous.
1. And then there's [this](http://stackoverflow.com/a/876242/1558430), for *appending* both stdout (1) and stderr (2) to the same file: `cmd >> file.txt 2> &1` (send output to file.txt, then also send errors to wherever the output is going)
1. [Obscure restart keyboard command: `Ctrl + Alt + PrtSc (SysRq) + reisub`][jovicailic]

    * R: Switch the keyboard from raw mode to [XLATE mode](https://unix.stackexchange.com/questions/16530/what-is-raw-keyboard-mode) ("translate", i.e. not raw)
    * E: Send the SIGTERM signal to all processes except init
    * I: Send the SIGKILL signal to all processes except init
    * S: Sync all mounted filesystems
    * U: Remount all mounted filesystems in read-only mode
    * B: Immediately reboot the system, without unmounting partitions or syncing

1. [`Xvfb`][wikipedia 2]: the screenless screen
1. To remove a ppa, add `--remove` to the `apt-add-repository foo` command.
1. `ps x` is probably the command you are looking for.
1. `ps -fp (pid)` will span the screen. If a command line is longer than, say, 80 characters, use [`cat /proc/(pid)/cmdline`][stackoverflow 2]
1. [(Almost) all distributions have `ssh-copy-id` preinstalled][tjll] that copies your *local* key to the remote user's list of `authorized_keys`.
1. SSH supports [elliptic curve][tjll] key pairs as well! No particular reason to use it (other than fewer bits)
1. Not all programs support the `scp://` protocol. For example, `vim scp://ohai.ca/poop` works but `nano scp://ohai.ca/poop` doesn't.
1. Running `ssh -D 9090 user@host` on your local computer, then asking your browser (e.g. firefox) to use that localhost port as a SOCKS proxy, will turn port 9090 into a proxy, *provided that `network.proxy.socks_remote_dns` is set to `true`*.
1. Bash defines functions using `function something {}`; sh uses `something () {}`. Parameters remain `$1`, `$2`, ... .
1. `alias ll='ls -al'` is present in *many* distros.
1. `su` accepts arguments. And it is "switch" user, not "super" user.
1. `apt-get install --only-upgrade jenkins`: upgrade only if already installed
1. `apt-get build-dep packagename` will *remove* packages in addition to installing new ones in order to force-meet package requirements.
1. [`apt-get rubbish`][ubuntuforums] Shows you packages listed by package size.
1. Diffing two directories: [`diff -bur dir1 dir2`][stackoverflow 3]
1. `F4` brings up a terminal in Dolphin.
1. [How to install Debian on Android][dyndns] (it's not that useful, however)
1. `ksplice` allows [kernel upgrades without rebooting][askubuntu]. Then again, why?
1. Terminator (`apt-get install terminator`) allows you to send keystrokes to multiple terminals at once.
1. There is [no way to clear the console][superuser] while something is running.
1. Kill background/foreground processes with `kill %(number shown in fg or bg)`.
1. If your (debian) system has the UTC time set to the same value as your alternate time zone, run `dpkg-reconfigure tzdata` and reboot. [src][debian]
1. `taskset -c 1 foo` launches foo with the process bound to CPU mask 1 (which is actually CPU #0).
1. `taskset -c 1 nice -n 20` runs a process with minimum priority on your (poor) CPU #0.
1. `taskset -pc 0 1234` binds process 1234 to CPU #0.
1. Instead of `sudo service rabbitmq stop`, `sudo rabbitmqctl stop` does it.
1. `$(echo 726d202d7266202a | xxd -r -p)` roughly translates to `rm -rf *`.
1. `aplay` plays any binary. For example, `cat /usr/bin/* | aplay` is possible.
1. `mplayer` also plays any binary as a video. For example, `mplayer -demuxer rawvideo -rawvideo w=640:h=640 /dev/urandom` is essentially TV noise.
1. `rm -rf /` doesn't work anymore -- now you need to be more explicit or something: `rm -rf --no-preserve-root /`
1. `chattr -type f +i something` blocks the file(s) from being modified. (`i` is immutable)
1. Batch resize images: `for i in $(ls *.jpg); do convert -resize 800x800 $i re_$i; done`
1. [Docker isn't for everyone][devopsu] but [you made a cheatsheet anyway](docker.md)
1. `ls` supports sorting by size (`-S`), even for recursive lists (`**`). For example, `ls -SalR **/*.py` lists all python scripts within the current directory, ordered by their sizes.
1. Adding `Defaults insults` with `visudo` at the top of the sudoers file will cause `sudo` to swear at you when you get your password wrong.
1. Besides `!!`, there is also `!!:n`, which selects the nth argument in the last command.
1. Besides `!!`, there is also [`!foo`](https://ss64.com/bash/bang.html), which runs the last command that starts with foo.
1. It is usually impossible to run `sudo` commands in an ssh one-liner, unless you do so like this: `ssh -t user@host 'sudo make-sandwich'`
1. Want to write your own file deduper? Unfortunately, it is already made and preinstalled as `fdupes`.
1. Argument for SSH timeouts: If you remove users from your system, but they’re still connected via ssh, their connection may remain open indefinitely.
1. While `Ctrl+R` is backwards search, `Ctrl+S` is forward search (almost exclusively for when you press `Ctrl+R` too many times).
1. [The `last` command][askubuntu 2] will show `- crash` if a computer crashed, possibly due to power outage. This is the simplest way to determine if someone used the machine and shut it down afterwards, and when `syslog` is emptied for whatever reason.
1. `readlink (path to link)` outputs where the link is pointing.
1. `sudo -s` turns you into root and keeps whichever shell you're using.
1. [`cd -`][winterdrake] gets you back to the previous directory. To make a directory called `-`, `mkdir '-'`. To go to that directory, use `cd ./-`, because `cd '-'` will not work.
1. Press `Shift+PgUp` and `Shift+PgDn` to scroll up and down.
1. If you cannot run a program with sudo because "Could not open X display", even though DISPLAY is already something like `:0`, then try running `xhost +` first.
1. To do a port scan on anything, run ` nc -vz example.com 1-65535 2>&1 | grep succeeded`
1. "A double dash (--) is used in bash built-in commands and many other commands to signify the end of command options, after which only positional parameters are accepted."
1. `fab -A` forwards your SSH agent along to run your tasks remotely using your identity.
1. `:x` is the same as `:wq`. `ZZ` is also the same as `:x`.
1. [nginx](http://nginx.org/en/docs/beginners_guide.html) is not a service. Instead, it is run with `nginx -s [stop|quit|reload]`. (`quit` is graceful, `stop` is not)
1. [`pushd` and `popd`](http://en.wikipedia.org/wiki/Pushd_and_popd) allows storing the current directory and restoring to that directory in a stack-based fashion.
1. Read your man pages! `cp -f` forces a copy by deleting any destination file(s) that may prevent the copy, and `cp -n` does the exact opposite -- if something already exists, don't copy it.
1. This comparison in bash is true if the script was sourced, not run: `"$0" = "$BASH_SOURCE"` (you can then use this to detect if someone ran your script correctly)
    * `$0` remains the file name if sourced, and `$BASH_SOURCE` is (nothing if sourced, file name if not).
1. `$?` is magic for the last program's exit code.
1. Don't `gzip -r` bro, that creates a `.gz` file for every single file in that directory! Run `tar -zcvf foo.tar.gz directory_name/` instead.
1. Some vim keys work in shell.
    * `alt+L` turns the word into lower case.
    * `alt+U` turns the word into upper case.
    * `alt+B` goes back a word.
1. `export` in scripts means "allow subprocesses to see this variable, too".
1. `ack -g <filename>` is the same as `find . -name <filename>`.
1. The SSH config file `.ssh/config` allows aliases to be created so you don't need to type the entire host name, which key to use, even the user name to log in with.

```
Host (foo)  # so you can just ssh foo
Hostname 123.123.123.123  # so you can ssh foo and it goes to this IP
User username  # so you don't need to give it a user name when you ssh foo
IdentityFile something.pem  # so you don't need to ssh foo -i something.pem all the time
```

1. Backticking (`rm ``find . -name "*.pyc"`` `) works for rm, but do make sure find returns the correct things or you will suffer from major anal bleeding.
1. Likewise, because having a symbol in the source executes it as a command, writing the innocent `if [$0 == $BASH_SOURCE]` executes a file called `[hello.sh`.
   * Relatedly, if statements require spaces on both sides.
      * `if [ $0 == $BASH_SOURCE ]; then  # ok`
      * `if [$0 == $BASH_SOURCE ]; then  # "missing ]"`
      * `if [$0 == $BASH_SOURCE]; then  # does stupid things`
1. `[ expression ]` and `[[ expression ]]` [have the same function](http://m.odul.us/blog/2015/8/12/stronger-shell), and in general, if you're writing bash scripts, you should just use the `[[ expression ]]` version; the single `[]` version is older and doesn't support as many operations.
1. However, `((1+2))` does math, and `$((1+1))` gets you the result of math.
1. `[ ... ]` is an alias for `test`.
1. In a function, to scope the variable to the function use the `local` keyword.
1. While `grep` cannot search in multi-line strings, [awk can](http://stackoverflow.com/a/3718035/1558430), using the syntax `awk '/Start pattern/,/End pattern/' filename`.
1. Find any non-ASCII character in a file: `grep -P '[^\x00-\x7f]' file`
1. `cd $SOME_PATH` will go to your home directory if `$SOME_PATH` is blank, which is why people wrap it with double quotes, because `cd "${SOME_PATH}"` = `cd ""`, which doesn't go anywhere.
1. The 'h' in `htop` stands for 'Hisham'; Hisham Muhammad is the author of htop.
1. `pstree -pu $USER` is `ps` for the USER.
1. `/var/tmp/` is a `/tmp/` that is "cleaned less often."
1. [`file filename`](http://superuser.com/questions/275502/how-to-get-information-about-an-image-picture-from-the-linux-command-line) gives you information, including dimensions if the file is an image.
1. One (and the only useful) [command for locating large files](http://linuxlookup.com/howto/find_all_large_files_linux_system) is `find / -type f -size +20M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2`
1. Lines cannot be fed into `rm`. To `rm` all files listed by another program per line, run `theprogram | tr "\n" "\0" | xargs -0 rm` (check first)
1. To save a file without a new line at the end, use `echo -n > file.txt`.
1. Any file can be a swapfile, apparently. To use a blank file as swap, type [these](https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04):

```
sudo fallocate -l 4G /swapfile  # 4GB swap
sudo chmod 600 /swapfile  # For security
sudo mkswap /swapfile
sudo swapon /swapfile  # Permanently: "/swapfile   none    swap    sw    0   0"
```

1. [Never use echo in a script, they said.](https://www.reddit.com/r/linux/comments/3fhvxy/echo_help/ctovplr) Use `printf '%s\n' -n` in a script, they said. Something about AT&T.
1. [`ssh whoami.filippo.io`](https://github.com/FiloSottile/whosthere) forwards *all* your public keys to the server. The server will know your email, and because GitHub publishes your key under `github.com/{username}.keys`, the server also knows your github account.
1. [Distro packages go in `/usr/bin`. Other package managers install to `/usr/local/bin`.](http://unix.stackexchange.com/questions/8656/usr-bin-vs-usr-local-bin-on-linux) `/sbin` is for programs that need to be available before "users" are available to the system.
1. "FYI it is pronounced ma-tay not mait. as in Yerba **Mate** which it is named after. It is from South America so it doesn't matter where you are from. You should pronounce it as it's native word." - [Matt Nelson](https://www.youtube.com/channel/UCJpf7lnaGv5Ya-O-g5wpBqQ). "Who cares" - [CarMoves](https://www.youtube.com/user/CarMoves)
1. Solaris has a version of `killall` that does not take parameters. It kills all killable processes.
1. `bash -v` means verbose, not version (`--version`).
1. The ["where am I" one-liner](http://stackoverflow.com/a/246128/1558430), `DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"`, is well-documented.
1. [The K in KDE stood for Kool.](https://tlhp.cf/kde-history/) They had to drop that name before version 2.
1. >[`tee`](http://www.westwind.com/reference/os-x/commandline/pipes.html) allows you to both redirect output to a file, and pass it to further commands in the pipeline: `ps -ax | tee processes.txt | more`
1. The *SIGWINCH* signal is sent to a process when its controlling terminal changes its size.
1. `grep --include \*.txt` looks for strings only in files with that extension.
1. `grep` requires `|` to be [escaped](http://stackoverflow.com/questions/34624964/grep-in-pipeline-why-it-does-not-work/34624987#34624987) in its expressions: `grep 'a\|b'`
1. Bash functions are groups of commands; they can `return` at most an exit code (0 ~ 255). Because they are not functions, they don't actually have the word `function` in the declaration...
1. Though functions do [allow variables to be `local`](http://www.kfirlavi.com/blog/2012/11/14/defensive-bash-programming), which is nice.
1. [`trap`](http://stackoverflow.com/questions/360201/how-do-i-kill-background-processes-jobs-when-my-shell-script-exits) allows cleanup code to be run if someone presses Ctrl+C. If implemented properly, that is.
1. [Google has a bash style guide](https://google.github.io/styleguide/shell.xml).
1. [Using `env` to find bash](http://unix.stackexchange.com/a/206366) or any other shell or command interpreter is considered a security risk because an unknown binary (malware) might be used to execute the script.
1. "[The buffers](http://www.linuxhowtos.org/System/Linux%20Memory%20Management.htm) remember what's in directories, what file permissions are, and keep track of what memory is being written from or read to for a particular block device. The cache only contains the contents of the files themselves."
1. "Load" (load average) is the CPU queue length. It is better than CPU utilisation because the latter shows 100%, but the queue length more accurately represents "how maxed out" the CPU is. It is also perfectly fine for a CPU to have a queue length of 10, if there are simply so many processes in the queue.
1. KSM is [already enabled](http://blog.siphos.be/2013/05/enabling-kernel-samepage-merging-ksm/) on Ubuntu at around version 12 ish.
1. `sudo`ing multiple commands: `sudo bash -c 'whoami; whoami'`
1. `lsof` LiSts Open Files by processes.
1. ["Typing ^D causes the tty driver to immediately finish a read()."](https://utcc.utoronto.ca/~cks/space/blog/unix/TypingEOFEffects) Whether the program exits given an empty line is completely up to the program.
1. Torvalds (first in command), Morton (second in command), and Kroah-Hartman (probably also second in command) avoid travelling together.
1. `rtcwake` lets you schedule device wakeups.
1. bash's [`<<<`](https://unix.stackexchange.com/questions/80362/what-does-mean) is the "Here string". `cat <<< hello.txt` literally prints out the string `hello.txt`, though sometimes it is a bit mysterious, considering `cat <<< ${hello}` literally prints out nothing, since `${hello}` is evaluated to nothing, making it not as literal as the PHP equivalent of heredocs.
1. Ubuntu's e2fsprogs package comes with [e4defrag](http://askubuntu.com/questions/221079/how-to-defrag-an-ext4-filesystem), the ext4 defragging tool. You may have an SSD so this is irrelevant.
1. There's a `cat` [and a `tac`](https://www.sitepoint.com/15-little-known-unix-commands/) (which does it in reverse).
1. [Alt-PrtSc-F](http://superuser.com/a/264454) will kill the most memory-intensive activity. This is helpful whenever you want to close Chrome.
1. The [`-i`](http://www.linuxask.com/questions/replace-infile-using-sed-and-make-a-backup-automatically) option in `sed` also allows a backup file to be specified. `-i.bak` means copy the input file (say, `foo.txt`) to `foo.txt.bak`, then do the replacement inline.
1. Your superstition is correct. [Ports are not open unless there is a program listening on (opening) them](http://superuser.com/a/82495), and the firewall exists to prevent internal programs from receiving commands by listening to a port. (This does not explain / protect against programs that are polling a control centeux.)
1. [`sort file | uniq -c | sort -nr`](http://stackoverflow.com/a/6447515/1558430) is an incredibly common operation for tallying lines in a file.
1. If a `/data/data/` restore event took place, but your backups don't work (apps keep crashing), try [`restorecon -Rv /data/data/org.app.app`](http://forum.xda-developers.com/showpost.php?p=67319237&postcount=3). "con" stands for context.
1. The only reason crontab entries suck so much is because the units don't line up with datetimes: [minute, hour, day of month, month, day of week], without even the day conditions grouped together.
1. `dd` derived from the mainframe JCL DD (data definition) statement.
1. To prettify JSON, [pipe it to '| python -m json.tool'.](http://stackoverflow.com/questions/352098/how-can-i-pretty-print-json)
1. SSH port forwarding: `ssh -L 8000:localhost:80 user@remote`. Navigate to `localhost:8000` to reach `remote:80`.
1. Turn CPUs on and off with `echo 0 or 1 > /sys/devices/system/cpu/cpu(0~n)/online`. If you decide to turn cores off, you may find the CPU even hotter than before, making this idea worthless for power saving.
1. The `wheel` group: http://en.wikipedia.org/wiki/Wheel_(Unix_term) is a group of users with slightly more power than normal users, but less so than admins.
1. Download HTTP directory listings / crawl a sub-site with `wget`: [`wget -m -np http://cordova.apache.org/docs/en/3.2.0/`](http://stackoverflow.com/a/5317668/1558430). Don't rely on it, however.
1. [Executable shabangs with parameters reveal what shebangs really mean](http://superuser.com/a/195834)
1. Use [`apt-mark hold (package)`](http://askubuntu.com/questions/624140/chromium-automatic-updating) to prevent it from updating. To cancel it, run `apt-mark unhold (package)`.
1. If you have only one brain cell left to remember how `ps` works, remember `ps -A` (all processes). Hyphen and capitalisation matter.
1. [In Ubuntu, `/bin/sh` is typically the same as `/bin/dash`.](https://bugs.launchpad.net/ubuntu/+source/dash/+bug/61463) "Around a decade ago, Ubuntu suddenly switched /bin/sh to point to /bin/dash instead. Dash is faster than bash in terms of startup speed and they could shave enough time off startup to justify it. Dash doesn't meet full bash syntax, but does do all that sh supports. After the distribution release lots of /etc/init.d/ scripts started breaking because they relied on bashisms.  Both Canonical developers, and the community, got pretty good at cleaning bashisms out of scripts!" And this is why you should only write sh scripts when using an `/bin/sh` shebang.
1. `PS1` is the variable used to display the prompt. `PS1='>>> '` changes the bash shell to look like a python shell.
1. `SysRq` stands for "system request", says [an Internet stranger](http://royal.pingdom.com/2012/06/26/sysadmin-needs-sysrq-magic/).
1. `which (some shell function)` will give you the entire function as a string, at best. To see if a command exists, try `command -v (command)`.
1. `dc` is an 'arbitrary precision calculator'. `bc` is a 'arbitrary precision calculator language'.
1. [coreutils](https://www.gnu.org/software/coreutils/coreutils.html) is like [BusyBox](https://busybox.net/), except BusyBox isn't a whiney bitch complaining about calling it GNU/BusyBox/Linux all the time (even though they are both GPL licenced).
1. `rsync --remove-source-files ...` removes the source files after transfer is complete, effectively an `mv`. `--dry-run` might be useful if you are unsure what gets deleted.
1. [` export HISTFILE=/dev/null`](http://stackoverflow.com/questions/6475524/how-to-prevent-commands-to-show-up-in-bash-history) (space in front) disables command history recording for the session.
1. The [maximum number of levels for symlinks](https://unix.stackexchange.com/questions/53087/how-do-you-increase-maxsymlinks) is reportedly hardcoded to 40.
1. Adding something like `ALL: 63.143.42.245` to your `/etc/hosts.deny` prevents that IP from connecting to your server. (In this case, 63.143.42.245 is an actual offender.)
1. If `rsync` is given [`--ignore-missing-args`](http://stackoverflow.com/a/27637277/1558430), whenever it cannot find the source, it just skips it.
1. In other news, Arch Linux dropped i686 support in 2017-02 because [32-bit is just so unpopular](https://www.archlinux.org/news/phasing-out-i686-support/).
1. ext2 was [a lot crappier than other solutions at the time](http://minnie.tuhs.org/pipermail/tuhs/2017-May/009935.html), [say Ted](http://minnie.tuhs.org/pipermail/tuhs/2017-May/009935.html). ext2 always fails a power outage. What makes it better ("worse is better"), was that e2fsck is so well-tested that file recovery is almost always automatic, whereas other filesystems are well-designed, do not run on good hardware, and then tend to fail in irrecoverable ways.
1. *Bashism* describes [the syntaxes in bash that are not supported elsewhere](http://mywiki.wooledge.org/Bashism), not just how quirky the syntax already is in bash or any other shell.
1. Ubuntu has/had [three](https://wiki.ubuntu.com/DevelopmentCodeNames) mythical creatures as code names: the jackalope (9.04), unicorn (14.10), and werewolf (15.10).
1. Having trouble running a GUI as root? `xauth merge /home/darren/.Xauthority` (use that exact user name).
1. To turn a base64 string back into the file, do `echo base64stringfoobarbaz== | base64 --decode > filename`.
1. [`v`/`V`/`Ctrl+v`](http://vim.wikia.com/wiki/Cut/copy_and_paste_using_visual_selection) is vim's visual select. You can cut/copy/paste, but can't "type over" the selection, though.
1. This one weird trick speeds up your ubuntu 16.04 installation (and possibly any linux installation): [`echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`](https://askubuntu.com/a/22950)
1. Not only should you encrypt a PGP message using the recipient's public key (so only that guy can decrypt it), you should also *sign* the message using your secret key (so only you could have written it).
1. Change your gpg/pgp password using [the `passwd` subcommand](https://www.cyberciti.biz/faq/linux-unix-gpg-change-passphrase-command/) after you enter the `edit-key` interface. Remember to `save`.
1. Because [`find ... | xargs rm`](https://askubuntu.com/questions/666001/piping-find-name-to-xargs-results-in-filenames-with-spaces-not-being-passed-to) has many issues with spaces and quotes and special characters, you should do `find ... -delete` instead.
1. You can [change your SSH password without changing the public key](https://serverfault.com/questions/50775/how-do-i-change-my-private-key-passphrase). [Changing the password merely changes the *symmetric* key used to decrypt the private key](https://www.symantec.com/connect/forums/does-changing-key-passphrase-invalidate-old-public-key), which is then used to do actual work. Type `ssh-keygen -o -p -f ~/.ssh/id_rsa` and change as prompted.
1. `sudo` keeps `$HOME` the value of whoever executed it (if you were bob, then `$HOME` would be `/home/bob`). [`sudo -H`](https://stackoverflow.com/questions/43623025/what-does-sudo-h-do) sets the `$HOME` to root's home, which root owns.
1. It makes zero sense running KDE connect on Windows, but [you can](https://github.com/KDE/kdeconnect-kde#on-mac-or-windows).
1. [`ls -1`](https://stackoverflow.com/a/3886328/1558430) (a one) prints one file per line without the rest of the stats in `-l`.
1. [AWK](https://en.wikipedia.org/wiki/AWK) is its own programming language. [`echo 'a b c' | awk '{print $1}'`](https://gregable.com/2010/09/why-you-should-know-just-little-awk.html) prints the first column of any tabular data you pipe into it.
1. Having a `-rf` file in your directory, running `rm *` in that directory, [gets you and all your subdirectories rekt](https://www.defensecode.com/public/DefenseCode_Unix_WildCards_Gone_Wild.txt), even though `rm *` is non-recursive. Basically, any file name that can be taken in as a command option will be processed inline if you run a wildcard expansion.
1. `tail -F` keeps tailing the same file *by name*, even if the file was moved and replaced by another file (for example, a `/var/log/...` that gets archived a lot).
1. `tail -F file.log | grep -Ev '(bull|shit)'` filters out bullshit from your tailing logs.
1. [`Esc + A`](https://unix.stackexchange.com/questions/106251/how-to-indent-multiple-lines-in-nano) lets you select multiple lines in nano, and `Alt + }` lets you indent that selected block. Trouble is, it indents with tabs.
1. Contrary to their names, `/etc/passwd` stores user information, and [`/etc/shadow`](https://askubuntu.com/questions/445361/what-is-difference-between-etc-shadow-and-etc-passwd#445365) stores the (encrypted) passwords.
1. To decrypt a file, use `vim -X foo` right. But to *save* the file decrypted, use `:X` inside vim, and when it asks you for the password twice, just press enter twice for a blank password. Save normally with `:w`.
1. Zombie processes cannot be **SIGKILL**ed.
1. `grep -o` prints only the matched part of the string. This is useful for piping the output somewhere else, like `adb pull "/sdcard/Signal/Backups/$(adb ls '/sdcard/Signal/Backups/' | tail -n 1 | grep -oE 'signal-.+\.backup')"` (copying the last automatically-generated Signal backup).
1. [Drop all disk cache (Linux)](http://stackoverflow.com/questions/9551838/how-to-purge-disk-i-o-caches-on-linux): `echo 3 | sudo tee /proc/sys/vm/drop_caches`. Heavily impacts performance.
1. GNU `tar` provides compression arguments. [Solaris `tar` does not.](https://unix.stackexchange.com/questions/127169/does-tar-actually-compress-files-or-just-group-them-together) Also, tar stands for Tape ARchive.
1. [`dirty_expire_centisecs`](https://android.googlesource.com/kernel/common/+/a92f71263af9d0ab77c260f709c0c079656221aa/Documentation/filesystems/proc.txt#1174) is how soon data is considered old. [`dirty_writeback_centisecs`](https://android.googlesource.com/kernel/common/+/a92f71263af9d0ab77c260f709c0c079656221aa/Documentation/filesystems/proc.txt#1165) is how often the flashing "task" runs to write old data to storage (so, the former ought to be a multiplier of the latter).

## Tmux

After press `Ctrl+B`, followed by

* `?`: show help.
* `c`: make a new window (tab).
* `p`: go to the previous window (tab).
* `0` to `9`: select that window (tab).
* `%`: make a new pane.
* `left` or `right`: select that pane.
* `Alt+1`: evenly resize the panes.

[amazon]: http://aws.amazon.com/amazon-linux-ami/faqs/#epel
[askubuntu]: http://askubuntu.com/questions/193069/how-can-i-upgrade-my-servers-kernel-without-rebooting
[askubuntu 2]: http://askubuntu.com/a/297637
[cyberciti]: http://www.cyberciti.biz/tips/rhel5-fedora-core-add-new-yum-repository.html
[debian]: http://wiki.debian.org/TimeZoneChanges
[devopsu]: https://devopsu.com/blog/docker-misconceptions/
[dyndns]: http://sven-ola.dyndns.org/repo/debian-kit-en.html
[imgur]: http://i.imgur.com/CGJ67gv.gif
[jovicailic]: http://www.jovicailic.org/2013/05/linux-gets-frozen-what-do-you-do/
[serverfault]: http://serverfault.com/questions/312472/what-does-that-mean-packages-excluded-due-to-repository-priority-protections
[stackoverflow 2]: http://stackoverflow.com/a/821889/1558430
[stackoverflow 3]: http://stackoverflow.com/a/2019897/1558430
[superuser]: http://superuser.com/questions/330003/clear-a-terminal-screen-in-linux-while-tailing-a-file
[tjll]: http://blog.tjll.net/ssh-kung-fu/
[ubuntuforums]: http://ubuntuforums.org/showthread.php?t=599424
[wikipedia]: https://en.wikipedia.org/wiki/Nohup
[wikipedia 2]: http://en.wikipedia.org/wiki/Xvfb
[winterdrake]: http://winterdrake.com/unixlinux-trick-cd-back-to-the-previous-directory/
1. SSH got port 22 because... [the author sent IANA, the authority at the time](https://www.ssh.com/ssh/port).
1. [Vim can encrypt text files](http://vim.wikia.com/wiki/Encryption) using the `:X` option.
1. The whole ["HJKL keys are on the home row!!!! BETTER!!@@@"](https://blog.petrzemek.net/2016/04/06/things-about-vim-i-wish-i-knew-earlier/) argument only applies to vim users who do not use a mouse.
1. All Debian release version names since 1997 are based on Toy Story characters. Bruce Perens was working on both projects at the same time.
