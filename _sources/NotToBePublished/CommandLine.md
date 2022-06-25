ffmpeg -i tm.mov -vf "fps=5,scale=300:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 tm.gif

ffmpeg -i resources.mov -vf "fps=5,scale=1000:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 resources.gif

ffmpeg -i fetchbot_moving.mov -vf "fps=5,scale=1000:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 Fetchbot_Moving.gif
