def genreInc(genreData, genre):
    ''' increments the appropriate genre by 1
        or assigns it 1 if previously nonexistent'''
    if (genre in genreData):
        genreData[genre] += 1
    else:
        genreData[genre] = 1


def printDistributions(genreData, count, genreClasses):
    ''' gets the distributions of each genre and prints them out '''
    for genreClass in genreClasses:
        distr = genreData[genreClass] / count * 100
        print(genreClass + ": " + "{:.2f}".format(distr) + "%")


def getgenreData(nums, genreClasses):
    ''' assigns each dewey decimal number with a genre
        using its dewey decimal number
    '''
    genreData = {}

    for num in nums:
        deweyNum = int(num.split(".")[0])
        for i in range(0,10):
            if (deweyNum >= i * 100 and deweyNum < (i + 1) * 100):
                genreData[num] = genreClasses[i]
                genreInc(genreData, genreClasses[i])
                break
       
    return genreData, len(nums)


def getNums():
    ''' returns list of dewey decimal numbers from file '''
    with open("deweyNums.txt") as file:
        nums = file.read().split("\n")
        nums.remove("")
        return nums


def main():
    ''' The ten main classes are:
        000-099  Computer science, information & general works
        100-199  Philosophy & psychology
        200-299  Religion
        300-399  Social sciences
        400-499  Language
        500-599  Science
        600-699  Technology
        700-799  Arts & recreation
        800-899  Literature
        900-999  History & geography
    '''
    genreClasses = [
        "Computer science, information & general works",
        "Philosophy & psychology",
        "Religion",
        "Social sciences",
        "Language",
        "Science",
        "Technology",
        "Arts & recreation",
        "Literature",
        "History & geography"
    ]
    nums = getNums()
    genreData, count = getgenreData(nums, genreClasses)
    printDistributions(genreData, count, genreClasses)


def genAndWriteNums():
    ''' Generate dewey numbers and write to "deweyNums.txt" '''
    import random
    digits = [0,1,2,3,4,5,6,7,8,9]
    letters = [chr(e) for e in range(68,91)]
    with open("deweyNums.txt", "w") as fileOut:
        for i in range(0, 100):
            fileOut.write(str(random.choice(digits)) +
                          str(random.choice(digits)) +
                          str(random.choice(digits[1:])) + '.' +
                          str(random.choice(digits)) +
                          str(random.choice(digits)) + ' ' +
                          random.choice(letters) +
                          str(random.choice(digits)) +
                          str(random.choice(digits)) +
                          str(random.choice(digits)))
            fileOut.write("\n")

