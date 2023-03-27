class results:
    name = ""
    phy = 0
    che = 0
    mat = 0
    total = 0
    per = 0

    def CalculateResults(self):
        self.total = self.phy + self.che + self.mat
        self.per = self.total * 100 / 450

    def ShowResults(self):
        print("Total Marks:", self.total, "/ 450")
        print("Percentage:", self.per, "%")


Jordan = results()
Jordan.phy = 115
Jordan.che = 68
Jordan.mat = 140
Jordan.CalculateResults()
Jordan.ShowResults()
