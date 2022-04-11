#!/usr/bin/bash
set -e
WGET="wget --show-progress --progress=bar:force:noscroll"

pip3 install --no-cache-dir -r requirements.txt
python3 -c 'import nltk; nltk.download("punkt")'

cd resources
$WGET 'https://corpora.linguistik.uni-erlangen.de/someweta/german_newspaper_2020-05-28.model'
$WGET 'https://pub.cl.uzh.ch/users/sennrich/zmorge/transducers/zmorge-20150315-smor_newlemma.ca.zip'
unzip zmorge-20150315-smor_newlemma.ca.zip
$WGET 'https://www.cis.uni-muenchen.de/~schmid/tools/RNNTagger/data/RNNTagger-1.3.zip'
unzip -uo RNNTagger-1.3.zip
find ./RNNTagger/lib/ -type f ! -name '*german*' -delete # remove unncessesary models
$WGET 'http://www.redewiedergabe.de/models/models.zip' -O rwtagger_models.zip
unzip rwtagger_models.zip -d rwtagger_models

