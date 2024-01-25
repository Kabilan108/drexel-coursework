" vimrc
" Cobbled together from following sources:
" ~kss35/Public/.vimrc
" https://gist.github.com/ruph/1437650
" Use " to comment out a line so it isn't applied
" ---
set nocompatible                " Use vim instead of vi defaults, must come first in file
set encoding=utf8               " Allow us to use unicode characters here, mostly for listchar

syntax on                       " Syntax highlighting, detected from extension or shabang
set showmatch                   " Shows matching brackets/parentheses
set ruler                       " Show current line number/column in bottom right
set showmode                    " Always show what mode we're currently editing in
set hlsearch                    " Highlight search terms
set incsearch                   " Show search matches as you type
set visualbell                  " Show bell icon instead of beeping when doing something wrong
set noerrorbells                " Same
" set background=dark           " Enable if you want to use dark mode
set wrap                        " If text goes off side of terminal, wrap it
set backspace=indent,eol,start  " Allow backspacing over everything in insert mode

" Indents
set smarttab                    " Autotabs for certain code
set tabstop=4                   " Visual width of tab character
set shiftwidth=0                " Make this same as tabstop
set smarttab                    " Use shiftwidth, not tabstop for consistency
set shiftround                  " Use multiple of shiftwidth when indenting with < and >
set autoindent                  " If file has different indenting, use that
set copyindent                  " Copy the previous indentation on autoindenting

" Show line numbers, press F2 to toggle on and off
" Makes copy-pasting annoying so off by default
" If on macOS, need to hold fn key while pressing function button
nmap <f2> :set number! number? <cr>

" Make invisible whitespace visible, useful for debugging Python indentation issues
" Press F4 to toggle on and off
set listchars=eol:¬,tab:▸/,space:·,trail:×
nmap <f4> :set list! list? <cr>
