# Good sources
[Don't be afraid to commit](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html)

# To add a file or files
First, we put them in the staging environment

```shell
git add <filename>
```

or, for everything that's been changed,

```shell
git add --all
```

Then we commit

```shell
git commit -m "The -m means you're adding this message."
```

Then we push it to GitHub.

'''shell
git push -u origin master
'''

The `-u` stands for upstream, which I don't really understand. It forces a tracking update for already up-to-date files.


# To get files back from github

```shell
git pull origin master
```

# To make a branch

```shell
git branch [branch-name]
```


# The nutty trail to sign commits

First, you can't use `SSH `to sign commits locally, so I had to get `gpg`. using homebrew.

First get homebrew and then instal `gpg`"

```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install gnupg
```

If you look this up on-line, you'll see references to `gpg`, `gpg1`, and `gpg2`. These are no longer relevant. It seems `gpg2` has won, so there's just `gpg`. 

Now it's time to make a key:

```shell
gpg --full-generate-key
```

Good choices are

1. RSA and RSA
2. 4096
3. 0 (key does not expire)
4. Name and email, but skip comment. (Somewhere I saw that comments make verification complex.)
5. passcode - don't lose!
6. (mash your keyboard, move your mouse, click on stuff)

And voila! A new key born. The name will look something like `23668C9ED59FD340`.

To get your PGP block:

```shell
gpg --armor --export 23668C9ED59FD340
```

To set it up with GitHub, copy the PGP block into your settings on GitHub.

To make git on your computer auto-sign your commits, do this:

```shell
git config --global user.signingkey 23668C9ED59FD340
test -r ~/.bash_profile && echo 'export GPG_TTY=$(tty)' >> ~/.bash_profile
echo 'export GPG_TTY=$(tty)' >> ~/.profile
git config --global commit.gpgsign true
```

Some other stuff was needed. I don't know why:

```shell
brew install pinetry-mac
echo "pinentry-program /usr/local/bin/pinentry-mac" >> ~/.gnupg/gpg-agent
killall gpg-agent
```

Now, I found all that 'export GPG_TTY' stuff didn't work. Maybe I needed to reload profiles or something, but in the end I did it manually with:

```shell
export GPG_TTY=$(tty)
echo "test" | gpg --clearsign
```

The second line just tests that everything is good to go. It should return a PGP signature.

Now all your commits will be signed!
