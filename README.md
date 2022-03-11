# Remove-tos-tweet
Remove tweets including text '@tos'.

## Usage
```zsh
python -m Remove_tos_tweet
```

## Install
```zsh
conda develop .
```

## Uninstall
```zsh
conda develop . --uninstall
```

## Install to LaunchAgents (Run at intervals on mac)
```zsh
ln -s $(pwd)/com.github.y-muen.remove-tos-tweet.plist ~/Library/LaunchAgents/com.github.y-muen.remove-tos-tweet.plist
launchctl load ~/Library/LaunchAgents/com.github.y-muen.remove-tos-tweet.plist
```

if you modify the plist, use `cp` instead of `ln -s`.

## Uninstall from LaunchAgents
```zsh
launchctl unload ~/Library/LaunchAgents/com.github.y-muen.remove-tos-tweet.plist
```
