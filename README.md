# VoxSRC Challenge

This repository contains the script to compute Equal Error Rates (EER) 


1. Download the list of validation pairs.
```
sh download_list.sh
```

2. The output should be formatted as below. See `data/veri_test_output.txt` for examples.
```
SCORE FILE1 FILE2
```

3. Run `evaluate.py` to compute the EER.
```
python evaluate.py --ground_truth=data/veri_test.txt --prediction=data/veri_test_output.txt --positive=0
```

Follow [this link](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/competition.html) for more information about the challenge.