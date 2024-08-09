## path
export HOMEBREW_NO_INSTALL_CLEANUP=True


## alias
alias l1='ls -1'
alias lh='ls -lh'
alias ll='ls -l'
alias la='ls -a'


## zsh
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster-mine"
# CASE_SENSITIVE="true"
# HYPHEN_INSENSITIVE="true"
# zstyle ':omz:update' frequency 13
# DISABLE_MAGIC_FUNCTIONS="true"
# DISABLE_LS_COLORS="true"
# DISABLE_AUTO_TITLE="true"
# ENABLE_CORRECTION="true"
# COMPLETION_WAITING_DOTS="true"
# DISABLE_UNTRACKED_FILES_DIRTY="true"
# HIST_STAMPS="mm/dd/yyyy"
# ZSH_CUSTOM=/path/to/new-custom-folder
setopt no_nomatch
plugins=(
    git
    zsh-syntax-highlighting
    zsh-autosuggestions
)
source $ZSH/oh-my-zsh.sh
