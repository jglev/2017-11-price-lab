# To set up a shell environment with tmux so that I can have a private screen to read from:

UPDATE: Just use https://github.com/rgaiacs/swc-shell-split-window

	## In the standalone terminal window:

	`tmux new-session -s Software_Carpentry`

	## In Guake:

	`tmux attach -t Software_Carpentry`

	Then, in tmux, to hide the bottom border (following https://superuser.com/questions/265320/disable-the-status-bar-in-tmux/265324#265324):

	`Ctrl + b` `:set -g status off`

## To simplify the command prompt:

`PS1="\n$ " # The '\n' helps separate commands from one another for teaching, and is my own addition.`
