# 6th Job Order Generator

---
Project made for maplestory's 6th job system (can be used for many other things as well). Easily generate good looking infographics for every class in the game.

---

# How to use the program
1. Download all the image files for the classes skills from [this](https://orangemushroom.net/2023/07/17/kms-ver-1-2-379-maplestory-new-age-6th-job/#6th5) blog post by Max (with a `.png` extension) and place them in a seperate folder along with the images for the hexa stats (they can be found in the repository with the naming scheme of `hs*.png`) and the `helper.exe` and `main.exe` programs.
2. Create an `order.txt` file, in the same directory as the downloaded images, on the basis of the example provided in the repository. The first line is the classes name (used for displaying it in the final image), all the other lines are made up of two elements. Firstly the leveled skill's name followed by the desired level seperated by a comma (ex. `lotd,4`). Make sure all the skill names match their respective image path (if the skill's name is lotd, the image file should be called `lotd.png`). If you wish to use hexa stats in your order you should use `hs` followed by the number of the hexa stat (ex. `hs1,5`)
3. Use the `helper.exe` program to calculate the height of the images.
4. Create a background image named `bg.png` (recommend using a frame from the 6th job animation, but you are free to use whatever  you wish), the width is a fixed `2000px` and the height is calcualted in `step 3`.
5. Run `main.exe` and you should be able to find a file named `order.png` which is the final image created by the program.
