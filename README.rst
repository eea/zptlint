zptlint
=======

Script that runs the pagetemplate parser and output errors

Installation
============

Because `zptlint` depends on `zope.pagetemplate`, it depends on a lot 
of other zope eggs.

To avoid polluting you system python, you can install `zptlint` in a
`virtualenv`::

  $ virtualenv --no-site-packages zptlint 
  $ cd zptlint/
  $ bin/easy_install zptlint

Then make a link to the right script::

  $ ln -s MYPATH/zptlint/bin/zptlint 

Configuration in .vimrc
=======================

::

  "page templates configuration
  autocmd BufNewFile,BufRead *.pt,*.cpt,*.zpt setfiletype zpt
  autocmd FileType zpt set makeprg=zptlint\ %
  autocmd FileType zpt set errorformat=%+P***\ Error\ in:\ %f,%Z%*\\s\\,\ at\ line\ %l\\,\ column\ %c,%E%*\\s%m,%-Q

  augroup filetype
    au BufWritePost,FileWritePost *.pt make
    au BufWritePost,FileWritePost *.cpt make
    au BufWritePost,FileWritePost *.zpt make
  augroup END


Because zpt is defined as a new file type, 
you may want to copy `syntax/html.vim` to `syntax/zpt.vim` 
and `ftplugin/html.vim` to `ftplugin/zpt.vim`.

or usage from command-line in vim::

  set makeprg=zptlint\ %
  set errorformat=%+P***\ Error\ in:\ %f,%Z%*\\s\\,\ at\ line\ %l\\,\ column\ %c,%E%*\\s%m,%-Q

Credits
=======

   * code by Balazs Ree, Greenfinity
   * eggified by Godefroid Chapelle, BubbleNet
