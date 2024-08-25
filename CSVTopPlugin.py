import sys
import PyPluMA

class CSVTopPlugin:
    def input(self, inputfile):
        innfile = open(inputfile, 'r')
        self.params = dict()
        for line in innfile:
            contents = line.strip().split('\t')
            self.params[contents[0]] = contents[1]
        self.infile = open(PyPluMA.prefix()+"/"+self.params["csvfile"], 'r')

    def run(self):
     self.results = []
     self.d = dict()
     self.firstline = self.infile.readline()
     for line in self.infile:
        contents = line.strip().split(',')
        metabolite = contents[0]
        self.d[metabolite] = line
        sum = 0
        for i in range(1, len(contents)):
           sum += float(contents[i])
        avg = sum / len(contents)
        self.results.append((avg, metabolite))

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        outfile.write(self.firstline)

        self.results.sort()
        self.results.reverse()

        for i in range(int(self.params["top"])):
           metab = self.results[i][1]
           print(metab+","+str(self.results[i][0]))
           outfile.write(self.d[metab])
        #for i in range(len(self.results)):
        #   metab = self.results[i][1]
