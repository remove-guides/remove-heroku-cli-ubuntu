[ ![Heroku](https://www2.assets.heroku.com/assets/logo-9ddfa622029bcad4fd1709b8045bb897b207d4d8c3005ee5e360abd5745341b2.svg) ](https://devcenter.heroku.com/articles/heroku-cli)

# Remove [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) from [Ubuntu](https://ubuntu.com/) based distros

## Remove all dependencies and remain files from Heroku CLI

<br />
<br />

To `run` use:

```bash
chmod +x remove-heroku-cli.py
sudo ./remove-heroku-cli.py

or 

sudo python3 remove-heroku-cli.py

```

`SUDO` is needed, without superuser access we can't remove some files and heroku cli configs

<br />
<br />


## Explanations

* This script will not remove plugins and files from vim, oh-my-zsh, and other files created by user, unless if these files are in any target directories.

* Be Careful, use this script if you know what are you doing, maybe it can break other stuffs that you might want to use


### Made with 🥰 by [Dpbm](https://github.com/Dpbm)
