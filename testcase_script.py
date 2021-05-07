import os

import functionlib.globalVariables as globals

#Test case 1: check that three photos got uploaded to main gallery:
# "city-rainy-day.jpg, lanterns-on-water.jpg, and otter.jpg"
correct_photos_in_dir_tc1 = False #tc2 => test case #1
for root,dirs,files in os.walk(globals.UPLOAD_FOLDER):
    tc1_photo_names = ["city-rainy-day.jpg", "lanterns-on-water.jpg","otter.jpg"]
    #this will count how many of the photos are in the Animals collection
    count = 0
    for p in tc1_photo_names:
        if  p in files:
            count += 1
    if count == len(tc1_photo_names):
        correct_photos_in_dir_tc1 = True
        
tc1_status = "FAIL"
if correct_photos_in_dir_tc1:
    tc1_status = "PASS"
print("Test case #1: Status - {}".format(tc1_status))

#Test case 2: check that the "Animals" collection folder was created and two photos named "otter.jpg" and "sloth.jpg" are there
animals_coll_created = False
correct_photos_in_dir_tc2 = False #tc2 => test case #2

for root,dirs,files in os.walk(globals.UPLOAD_FOLDER):
    #only need to check the directory name
    if "Animals" in dirs:
        animals_coll_created = True
    #when the Animals sub folder is visited, check if "otter" and "sloth" photos are there
    if "Animals" in root:
        tc2_photo_names = ["otter.jpg", "sloth.jpg"]
        #this will count how many of the photos are in the Animals collection
        count = 0
        for p in tc2_photo_names:
            if  p in files:
                count += 1
        if count == len(tc2_photo_names):
            correct_photos_in_dir_tc2 = True

tc2_status = "FAIL"
if correct_photos_in_dir_tc2 and animals_coll_created:
    tc2_status = "PASS"
print("Test case #2: Status - {}".format(tc2_status))
    