# chpwd_cmd [![Python package](https://github.com/teddyyy/chpwd_cmd/workflows/Python%20package/badge.svg)](https://github.com/teddyyy/chpwd_cmd/actions)

## What is this?
chpwd_cmd executes the commands in the configuration file according to the
current working directory. It is intended to be called from the hook function of zsh, fish and so on. With this you will no longer need to type a command every time you move the directory.


## How to install
```
pip install chpwd-cmd
```


## Configuration
chpwd_cmd requires configuration file at runtime. Configuration file must be located `$HOME/.chpwd_cmd`. Configuration File is written in Toml format.

Configuration is written in every `workdir.name` table. If you write more than one `workdir.name`, the name must be unique.

### Configuration Item
|name|type|description|required|
|----|----|-----------|--------|
|dirpath|string|Specifies the directory of execution. The specification of the directory can be written using the glob pattern. If the directory path is the same as the other Workdir Both commands work.| True |
|cmd|string|Specifies the command to execute| True |

### Example of configuration file
```
[workdir.home]
dirpath = "/Users/hoge"
cmd = "ls"

[workdir.git]
dirpath = "~/Documents/git/*/*"
cmd = "git fetch -p"
```

## How to use
```
usage: chpwd_cmd [-h] [-c CWD] [-m {exec,dryrun,listdir}]

This program executes the commands in the configuration file according to the
current working directory

optional arguments:
  -h, --help            show this help message and exit
  -c CWD, --cwd CWD     current working directory
  -m {exec,dryrun,listdir}, --mode {exec,dryrun,listdir}
                        running mode (default:exec)
```

### Execution
If you specify a directory path in `exec` mode, chpwd_cmd execute it. The default mode of chpwd_cmd is `exec`.
```
chpwd_cmd -m exec -c $HOME
```
If you are using zsh, you will be able to call it as follows.

Adding to your .zshrc file.
```
function chpwd() {
  chpwd_cmd -c $PWD
}
```

If you are using fish, you will be able to call it as follows.

Adding to your ~/.config/fish/config.fish file.
```
function chpwd --on-variable PWD
  chpwd_cmd -c $PWD
end
```

### Dryrun
It is recommended to do a `dryrun` before running the mode `exec`.
You can check if a directory is targeted for execution by doing dryrun.
```
chpwd_cmd -m dryrun -c $HOME
```

### List Directory
You can list the directories for execution. It is useful if you specify the directory path as a wildcard.
```
chpwd_cmd -m listdir
```

## How to test
```
make test
```

## License

- MIT License
- Author: teddy@sfc.wide.ad.jp
