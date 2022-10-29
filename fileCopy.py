import os
import shutil

# Function to copy files, if they exist, from an input directory to an output directory
def copyFiles(inputDir, outputDir):
    files = os.listdir(inputDir)
    missingFiles = checkFiles(files, inputDir)
    for file in files:
        if file not in missingFiles:
            shutil.copy(inputDir + file, outputDir)
            print("File copied: " + file)


# function to check if files exist in the input directory. Returns a list of files that don't exist
def checkFiles(files, inputDir):
    missingFiles = []
    for file in files:
        if os.path.isfile(inputDir + file):
            print("File exists: " + file)
        else:
            print("File not found: " + file)
            missingFiles.append(file)
    return missingFiles


# inputDir = "C:\\Users\\duppu\\Pictures\\New folder (2)\\102MSDCF\\"
# outputDir = "C:\\Users\\duppu\\Pictures\\ForJohn\\HighRes\\"
# # files = ['DSC02827.JPG','DSC02829.JPG','DSC02834.JPG','DSC09690.JPG','DSC09758.JPG','DSC09869.JPG','DSC09874.JPG','IMG_20220803_120656.jpg','IMG_20220805_125409.jpg','DSC00222.JPG','DSC00313.JPG','DSC00340.JPG','DSC00342.JPG','DSC00352.JPG','DSC00369.JPG','DSC00400.JPG','DSC00402.JPG','DSC00409.JPG','DSC00461.JPG','DSC00462.JPG','DSC00465.JPG','DSC00468.JPG','DSC00477.JPG','DSC00478.JPG','DSC00575.JPG','DSC00592.JPG','DSC00688.JPG','DSC00762.JPG','DSC00838.JPG','DSC00846.JPG','DSC00900.JPG','DSC00951.JPG','DSC01061.JPG','DSC01125.JPG','DSC01147.JPG','DSC01159.JPG','DSC01187.JPG','DSC01195.JPG','DSC01229.JPG','DSC01249.JPG','DSC01254.JPG','DSC01273.JPG','DSC01303.JPG','DSC01313.JPG','DSC01323.JPG','DSC01372.JPG','DSC01404.JPG','DSC01419.JPG','DSC01423.JPG','DSC01425.JPG','DSC01427.JPG','DSC01431.JPG','DSC01432.JPG','DSC01441.JPG','DSC01451.JPG','DSC01465.JPG','DSC01475.JPG','DSC01477.JPG','DSC01487.JPG','DSC01551.JPG','DSC01555.JPG','DSC01565.JPG','DSC01567.JPG','DSC01576.JPG','DSC01596.JPG','DSC01606.JPG','DSC01624.JPG','DSC01646.JPG','DSC01647.JPG','DSC01659.JPG','DSC01660.JPG','DSC01676.JPG','DSC01688.JPG','DSC01718.JPG','DSC01727.JPG','DSC01738.JPG','DSC01741.JPG','DSC01754.JPG','DSC01758.JPG','DSC01762~2.JPG','DSC01767~2.JPG','DSC01846.JPG','DSC01855.JPG','DSC01870.JPG','DSC01875.JPG','DSC01880~2.JPG','DSC01887.JPG','DSC01890.JPG','DSC01912.JPG','DSC01932.JPG','DSC01935.JPG','DSC01973.JPG','DSC01982.JPG','DSC01991.JPG','DSC01992.JPG','DSC01993.JPG','DSC01998.JPG','DSC02014.JPG','DSC02016.JPG','DSC02022.JPG','DSC02024.JPG','DSC02028.JPG','DSC02031.JPG','DSC02046.JPG','DSC02063.JPG','DSC02071.JPG','DSC02073.JPG','DSC02086.JPG','DSC02091.JPG','DSC02102.JPG','DSC02108.JPG','DSC02119.JPG','DSC02124.JPG','DSC02139.JPG','DSC02147.JPG','DSC02168.JPG','DSC02170.JPG','DSC02172.JPG','DSC02182.JPG','DSC02234.JPG','DSC02235.JPG','DSC02242.JPG','DSC02245.JPG','DSC02255.JPG','DSC02258.JPG','DSC02260.JPG','DSC02279.JPG','DSC02281.JPG','DSC02283.JPG','DSC02316.JPG','DSC02318.JPG','DSC02319.JPG','DSC02335.JPG','DSC02365.JPG','DSC02367.JPG','DSC02383.JPG','DSC02401.JPG','DSC02402.JPG','DSC02413.JPG','DSC02414.JPG','DSC02415.JPG','DSC02416.JPG','DSC02419.JPG','DSC02420.JPG','DSC02445.JPG','DSC02446.JPG','DSC02464.JPG','DSC02476.JPG','DSC02480.JPG','DSC02489.JPG','DSC02502.JPG','DSC02530.JPG','DSC02559.JPG','DSC02613.JPG','DSC02614.JPG','DSC02625.JPG','DSC02671.JPG','DSC02677.JPG','DSC02768.JPG','DSC02782.JPG','DSC02789.JPG','DSC02803.JPG','DSC02813.JPG']
# files = ['DSC01762.JPG', 'DSC01767.JPG', 'DSC01880.JPG']
# copyFiles(files, inputDir, outputDir)

# missingFiles = checkFiles(files, outputDir)
# print(missingFiles)
# print(len(missingFiles))