from paging import *


def pre_trial_message(trialNumber):
    print("Trial " + str(trialNumber) + ":")
    print("Executing program")
    print("Comparing output")


def trial_failure_message(expectedResult, foundResult, frameSize, pages):
    print("Output not correct")
    print("Expected: " + str(expectedResult))
    print("Found: " + str(foundResult))
    print("Input supplied to your program:")
    print("Pages:", pages)
    print("Size:", frameSize)


def trial_success_message():
    print("Output correct")


def fifo_trial_template(trialNumber, frameSize, pages, expectedOutput):
    pre_trial_message(trialNumber)
    trialResult = FIFO(frameSize, pages)
    if trialResult != expectedOutput:
        trial_failure_message(expectedOutput, trialResult, frameSize, pages)
    else:
        trial_success_message()
    print("")


def lru_trial_template(trialNumber, frameSize, pages, expectedOutput):
    pre_trial_message(trialNumber)
    trialTwo = LRU(frameSize, pages)
    if trialTwo != expectedOutput:
        trial_failure_message(expectedOutput, trialTwo, frameSize, pages)
    else:
        trial_success_message()
    print("")


def opt_trial_template(trialNumber, frameSize, pages, expectedOutput):
    pre_trial_message(trialNumber)
    trialTwo = OPT(frameSize, pages)
    if trialTwo != expectedOutput:
        trial_failure_message(expectedOutput, trialTwo, frameSize, pages)
    else:
        trial_success_message()


class pagingTests:
    sixteenPages = [8, 5, 6, 2, 5, 3, 5, 4, 2, 3, 5, 3, 2, 6, 2, 5]
    nineteenPages = [3, 2, 1, 3, 4, 1, 6, 2, 4, 3, 4, 2, 1, 4, 5, 2, 1, 3, 4]
    thirtyTwoPages = [8, 5, 6, 2, 5, 3, 5, 4, 2, 3, 5, 3, 2, 6, 2, 5,
                      6, 8, 5, 6, 2, 3, 4, 2, 1, 3, 7, 5, 4, 3, 1, 5]
    hundredPages = [3, 29, 23, 1, 38, 45, 28, 8, 2, 5, 45, 31, 36, 27, 28, 35, 16, 23, 43, 21, 10, 30, 40,
                    8, 5, 40, 18, 24, 26, 45, 47, 8, 17, 31, 10, 16, 8, 48, 32, 18, 46, 2, 33, 30, 18, 11,
                    17, 12, 0, 15, 46, 24, 29, 20, 5, 32, 8, 21, 19, 35, 44, 37, 21, 47, 7, 11, 14, 26, 28,
                    8, 30, 37, 15, 26, 17, 1, 3, 34, 1, 47, 8, 35, 44, 35, 18, 1, 35, 15, 18, 11, 29, 34, 9,
                    47, 33, 10, 48, 14, 48, 12]

    frameSizeOfOne = 1
    frameSizeOfTwo = 2
    frameSizeOfThree = 3
    frameSizeOfFive = 5
    frameSizeOfEight = 8
    frameSizeOfThirteen = 13
    frameSizeOfTwentyOne = 21
    frameSizeOfThirtyFour = 34

    def test_fifo_is_working_correctly(self):
        print("Working on the FIFO algorithm.")

        # Trial 1:
        fifo_trial_template(1, self.frameSizeOfThree, self.sixteenPages, 12)

        # Trial 2:
        fifo_trial_template(2, self.frameSizeOfThree, self.nineteenPages, 13)

        # Trial 3:
        fifo_trial_template(3, self.frameSizeOfThree, self.thirtyTwoPages, 25)

        # Trial 4:
        fifo_trial_template(4, self.frameSizeOfOne, self.hundredPages, 100)

        # Trial 5:
        fifo_trial_template(5, self.frameSizeOfTwo, self.hundredPages, 98)

        # Trial 6:
        fifo_trial_template(6, self.frameSizeOfThree, self.hundredPages, 96)

        # Trial 7:
        fifo_trial_template(7, self.frameSizeOfFive, self.hundredPages, 90)

        # Trial 8:
        fifo_trial_template(8, self.frameSizeOfEight, self.hundredPages, 87)

        # Trial 9:
        fifo_trial_template(9, self.frameSizeOfThirteen, self.hundredPages, 76)

        # Trial 10:
        fifo_trial_template(10, self.frameSizeOfTwentyOne, self.hundredPages, 59)

        # Trial 11:
        fifo_trial_template(11, self.frameSizeOfThirtyFour, self.hundredPages, 45)

    def test_lru_is_working_correctly(self):
        print("Working on the LRU algorithm.")

        # Trial 1:
        lru_trial_template(1, self.frameSizeOfThree, self.sixteenPages, 11)

        # Trial 2:
        lru_trial_template(2, self.frameSizeOfThree, self.nineteenPages, 14)

        # Trial 3:
        lru_trial_template(3, self.frameSizeOfThree, self.thirtyTwoPages, 23)

        # Trial 4:
        lru_trial_template(4, self.frameSizeOfOne, self.hundredPages, 100)

        # Trial 5:
        lru_trial_template(5, self.frameSizeOfTwo, self.hundredPages, 98)

        # Trial 6:
        lru_trial_template(6, self.frameSizeOfThree, self.hundredPages, 95)

        # Trial 7:
        lru_trial_template(7, self.frameSizeOfFive, self.hundredPages, 90)

        # Trial 8:
        lru_trial_template(8, self.frameSizeOfEight, self.hundredPages, 86)

        # Trial 9:
        lru_trial_template(9, self.frameSizeOfThirteen, self.hundredPages, 75)

        # Trial 10:
        lru_trial_template(10, self.frameSizeOfTwentyOne, self.hundredPages, 59)

        # Trial 11:
        lru_trial_template(11, self.frameSizeOfThirtyFour, self.hundredPages, 43)

    def test_opt_is_working_correctly(self):
        print("Working on the OPT algorithm.")

        # Trial 1:
        opt_trial_template(1, self.frameSizeOfThree, self.sixteenPages, 8)

        # Trial 2:
        opt_trial_template(2, self.frameSizeOfThree, self.nineteenPages, 10)

        # Trial 3:
        opt_trial_template(3, self.frameSizeOfThree, self.thirtyTwoPages, 16)

        # Trial 4:
        opt_trial_template(4, self.frameSizeOfOne, self.hundredPages, 100)

        # Trial 5:
        opt_trial_template(5, self.frameSizeOfTwo, self.hundredPages, 89)

        # Trial 6:
        opt_trial_template(6, self.frameSizeOfThree, self.hundredPages, 81)

        # Trial 7:
        opt_trial_template(7, self.frameSizeOfFive, self.hundredPages, 70)

        # Trial 8:
        opt_trial_template(8, self.frameSizeOfEight, self.hundredPages, 61)

        # Trial 9:
        opt_trial_template(9, self.frameSizeOfThirteen, self.hundredPages, 51)

        # Trial 10:
        opt_trial_template(10, self.frameSizeOfTwentyOne, self.hundredPages, 42)

        # Trial 11:
        opt_trial_template(11, self.frameSizeOfThirtyFour, self.hundredPages, 41)


if __name__ == "__main__":
    test = pagingTests()
    print("Paging tests in progress:")
    print("")
    test.test_fifo_is_working_correctly()
    print("")
    test.test_lru_is_working_correctly()
    print("")
    test.test_opt_is_working_correctly()
    print("")
    print("Paging tests completed.")
