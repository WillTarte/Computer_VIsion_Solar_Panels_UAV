




for index in range(0,256):
    if val[index-1] > val[index] < val[index +1]:
        #this is a valley
    elif val[index-1] < val[index] > val[index +1]:
        #this is a peak
    else:
        continue

for index in self.bin_edges[0:-1]:
    if self.histogram[index-1] > self.histogram[index] < self.histogram[index +1]:
        valleys.append(index)
    elif self.histogram[index-1] < self.histogram[index] > self.histograms[index +1]:
        peaks.append(index)
    else:
        continue



lastmax = peaks[-1]

min = len(valleys) - 1
while valleys[min] > lastmax:
    min -=1
