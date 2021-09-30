# MMO-keyboard-jiggler

This script activates keyboard inputs at a set time interval 


## Third Party Libraries
[pyautogui](https://pyautogui.readthedocs.io/en/latest/)

## Notes

- Currently set to move at 1m intervals (starting after movement completes). You can increase interval by changing numMin. I'll probably slowly increase via trial and error (per game) so it's triggered as minimally as feasible.

- Triggered wherever the mouse is focused. 

- Movement is a bit verbose in the code, but it is written so movement in game looks somewhat natural. Next steps will be to introduce random downtime intervals within a time frame, and more random types of movement so it is a little less obviously scripted. 

- Script runs until you manually stop it.



