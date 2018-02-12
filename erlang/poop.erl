-module(poop).
-export([main/0]).

%% 1. compile with `erlc poop.erl`
%% 2. you'll get a `poop.beam`
%% 3. Then you run with `erl -noshell -s poop main -s init stop`

main() ->
    io:fwrite("Hello\n"),
    io:fwrite(integer_to_list(lol:add(1, 3))).
