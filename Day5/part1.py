class SeedConverter:

    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        self.seeds = []
        self.locations = []
        self.converters = {
            "seed-to-soil": [],
            "soil-to-fertilizer": [],
            "fertilizer-to-water": [],
            "water-to-light": [],
            "light-to-temperature": [],
            "temperature-to-humidity": [],
            "humidity-to-location": [],
        }
        self.conversion_order = []

    def parseFile(self):
        # grab the seeds
        first_line = self.file.readline()
        self.seeds = first_line.split(':')[1].strip().split(" ")
        
        # get rid of first newline
        line = self.file.readline()
        # while we still have lines to read
        while line != "":
            # if we have found a new range grouping
            if "to" in line:
                # grab the grouping name (our key) and get rid of newline
                to_name = line.split(" ")[0]
                self.conversion_order.append(to_name)
                line = self.file.readline()
                # print(to_name)
                # while we still have ranges to parse
                while line != "\n" and line != "":
                    # grab all ranges and iterate over the 3rd value, incrementing into our dict
                    ranges = line.strip().split(" ")
                    dest_start = int(ranges[0])
                    source_start = int(ranges[1])
                    size = int(ranges[2])
                    self.converters[to_name].append([dest_start, source_start, size])
                    line = self.file.readline()
            # print(line)
            line = self.file.readline()
        # for key, val in self.converters.items():
        #     print(key, val)
    
    def convertSeeds(self):
        for seed in self.seeds:
            cur = int(seed)
            for key in self.conversion_order:
                for range in self.converters[key]:
                    dest, source, size = range[0], range[1], range[2]
                    if cur >= source and cur < source + size:
                        cur = dest + cur-source
                        break
            self.locations.append(cur)
    
    def getMinimun(self) -> int:
        smallest = float('inf')
        for location in self.locations:
            smallest = min(smallest, location)
        return smallest




def main():
    seed_converter = SeedConverter("Day 5/small_input.txt")
    seed_converter.parseFile()
    seed_converter.convertSeeds()
    smallest = seed_converter.getMinimun()
    print(smallest)


if __name__ == "__main__":
    main()
