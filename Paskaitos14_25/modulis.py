class TxtAnalyzer():
    def __init__(self, pav, skirtukas):
        self.pavadinimas = pav
        self.skirt = skirtukas
        self.i = []
        self.u = []
        self.j = []
        self.p = []
        pass

    def TxtReader(self):
        fname = self.pavadinimas
        f = open(fname, mode='r', encoding='utf-8')

        tekstas = f.readlines()
        

        f.close()

        for x in tekstas[1:]:
            self.i.append(float(x.split(self.skirt)[0]))
            self.u.append(float(x.split(self.skirt)[1]))
            self.j.append(float(x.split(self.skirt)[2]))
            self.p.append(float(x.split(self.skirt)[3]))

    def getMaxP(self):
        MAX = (max(self.p))
        return MAX
    
    def getPCE(self):
        Pmax= self.getMaxP()
        pce = round((Pmax / 1000 * 100),2)
        return pce