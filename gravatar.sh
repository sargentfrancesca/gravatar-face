#!/bin/bash
echo -n Preparing to take a photo of YOUR FACE. PRESS ENTER TO TAKE PHOTO      : 
read prompt

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

vlc -I dummy v4l2:///dev/video0 --video-filter scene --no-audio --scene-path $DIR --scene-prefix face --scene-format png vlc://quit --run-time=1y </dev/null &>/dev/null &

echo Running Open BR Gender Estimation..
br -algorithm GenderEstimation -enroll face00001.png results.csv
echo Analysis completed.
killall vlc
echo Now running python file...
echo //\\//\\//\\//\\//\\
python run.py