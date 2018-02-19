#!/usr/bin/env bash

# Bash, and things like that

    # `bash` should be the default when scripting,
    # because `/bin/sh` is sometimes not actually `sh`.
    # http://askubuntu.com/a/141932

#### `.` is just a shortcut for `source`

    # source ~/.bashrc
    # . ~/.bashrc

#### Print out the entire script

    # set -v

#### Exit as soon as any line in the bash script fails

    # Unless the error happened in some kind of loop,
    # or in subshells in command substitution
    # https://blogs.janestreet.com/when-bash-scripts-bite/
    set -e

#### Exit as soon as something in a pipe goes wrong

    # https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
    set -o pipefail

#### Print a `+` in front of every *command* run

    # set -x

#### This ensures the entire script is downloaded

    # There needs to be at least one command in the block.
    {

#### Variables

        # Variables stay inside subshells
        (
            # No spaces allowed to the left and right of `=`
            A="Ehhhh"
        )
        echo "$A"  # (blank)

        # But wait, if you use curly brackets instead,
        # The variables leak out??
        {
            B="Hello";
        }
        echo $B;  # Hello
        echo '------'

#### Variables (2)

        # This turns text to lower case
        # http://stackoverflow.com/a/11392248/1558430
        echo ${B,,}  # hello

        # This turns text to upper case
        echo ${B^^}  # hello

        # Strings in double quotes are interpolated
        # Single quotes are not
        echo "$B world"  # Hello world
        echo '$B world'  # $B world

        # You can echo any series of quotes
        echo "Hello" '5' "world"  # Hello 5 world
        echo '------'

#### Variables (3)

        # Almost useless substitutions:
        # http://docs.codehaus.org/display/ninja/Bash+Default+Values
        FOO=
        # echo 'second' if FOO is null
        echo "The ${FOO-second} choice"  # The  choice
        # echo 'second' if FOO is null or empty
        echo "The ${FOO:-second} choice"  # The second choice

        # The 'second' can be commands wrapped in `$()`.
        echo '------'

#### Fun fact, `true` and `false` are binaries

        # ...in `/bin`.
        # These two lines will issue this warning:
        # "Useless echo? Instead of 'echo $(cmd)', just use 'cmd'."
        echo "$(which true)"
        echo "$(which false)"

        echo '------'

#### If statements and tests

        C='bash sucks balls';

        # Test if a string starts with something
        if [[ $C == "bash sucks"* ]]; then
            echo 'Yes, bash sucks';
        fi

        # Test if a string ends with something
        if [[ $C == *"sucks balls" ]]; then
            echo 'Yes, something sucks balls';
        fi

        # Test if a command is truthy
        # (in this case you use an unnecessary subshell)
        if (true); then
            echo 'The command is true';
        fi

        # Test if a command is falsy
        # (the space after `!` is required!)
        if ! (false); then
            echo 'The command is false';
        fi

        # Other fun ones:
        # https://devhints.io/bash
        # [ -z STRING ]  # Empty string
        # [ NUM -eq NUM ]  # Numbers equal
        # [ NUM -ne NUM ]  # Numbers not equal
        # [ NUM -lt NUM ]  # Less than
        # [ NUM -gt NUM ]  # More than
        # (( NUM < NUM ))  # Maths

        # You can just use the word 'test' if you
        # hate the square bracket notation
        if test -z $STRING; then
            echo 'STRING is empty';
        fi
        echo '------'

#### Arrays and loops

        # This is an array
        # http://tldp.org/LDP/abs/html/arrays.html
        ARRAY=(
            foo
            thing2
            thing3
            false  # Actually a string
        )

        # This is how you loop through it;
        # `${ARRAY[@]}` means "length of the array".
        for LINE in "${ARRAY[@]}"; do

            echo "$LINE";
        done  # Not "rof" because bash

        # This is how you count up.
        # `$()` is preferred over backticks (``) because
        # you can nest `$()`.
        # http://mywiki.wooledge.org/BashFAQ/082
        for I in $(seq 1 5); do
            #    ^`{1..5}` also works
            echo "I is now $I";
        done

        # This is how you count down
        # ( `((` and `))` do maths)
        G=5
        while (( --G >= 0 )); do
            echo "G is now $G";
        done  # Not "elihw" because bash

        # There is also an "until" loop.
        # http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html
        echo '------'

#### Switch/Case

        # This is how you do a switch/case
        B=73; case "$B" in
        [0-9])
            # This is how your case can fall through
            ;&
        [1-6]*)
            MESSAGE='B is between 0 to 69';
            # This is how you terminate a case
            # http://tldp.org/LDP/abs/html/special-chars.html
            ;;
        [7-9]*)  # These are actually "patterns"
            MESSAGE='B is between 70 to 99';
            ;;
        *)  # This is the default case
            MESSAGE='B is none of those things';
            ;;
        esac

        echo "$MESSAGE";
        echo '------'

#### Check if a command exists

        # Why it is not recommended:
        # `which bash_function` will return true.
        # https://stackoverflow.com/questions/592620/
        if which git > /dev/null; then
            echo "git exists 1 💩";
        fi

        # Recommended (`command -v` checks for existence
        # of a command.)
        if command -v git >/dev/null 2>&1; then
            echo "git exists 2 💯";
        fi
        echo '------'

#### Functions

        # Bash-specific functions can start with the
        # word `function`:
        # https://stackoverflow.com/a/7917086/1558430
        # But why would you do that?
        function poop3() {
            local MYMSG='called';
            # `$1` is the first argument
            # `$#` is the number of arguments
            # `$@` is all arguments
            echo "$MYMSG $1, $@";
        }

        # This is how you capture stdout as if it
        # were a return value
        RVAL=$(poop3 ayy lmao)
        echo "$RVAL";  # "called ayy, ayy lmao"

        # Shortest possible function in bash (noop)
        noop() {
            :
        }

        # Running a function requires no brackets.
        # Adding brackets redefines the function.
        noop
        echo '------'

#### Redirections

        # http://askubuntu.com/a/350216
        # `> file` redirects stdout to file
        # `1> file` redirects stdout to file
        # `2> file` redirects stderr to file
        # `&> file` redirects stdout and stderr to file

        # Does nothing in bash, but prints out the
        # file in zsh (in the shell, not a script)
        < .gitignore
        echo '------'

#### Magic variables

        bash -c "exit 123" || (
            # Code from last status
            # http://tldp.org/LDP/abs/html/exit-status.html
            echo $?
        )

#### This ensures the entire script is downloaded

    # Try commenting out this line. You will get:
    # syntax error: unexpected end of file
    }

#### More resources

    # https://www.shellcheck.net/
    exit 0
