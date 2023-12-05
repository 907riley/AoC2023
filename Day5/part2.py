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
        first_line = self.file.readline().split(':')[1].strip().split(" ")
        self.seeds = set([(int(first_line[i]), int(first_line[i+1])) for i in range(0, len(first_line), 2)])
        
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
                # while we still have ranges to parse
                while line != "\n" and line != "":
                    # grab all ranges and iterate over the 3rd value, incrementing into our dict
                    ranges = line.strip().split(" ")
                    dest_start = int(ranges[0])
                    source_start = int(ranges[1])
                    size = int(ranges[2])
                    self.converters[to_name].append([dest_start, source_start, size])
                    line = self.file.readline()
            line = self.file.readline()
    
    def convertSeeds(self):
        seed_ranges = self.seeds
        for key in self.conversion_order:
            new_seed_ranges = set()
            for cur_range in self.converters[key]:

                dest, source, size = cur_range[0], cur_range[1], cur_range[2]
                for seed_range in list(seed_ranges):
                    # grab the seed range [start, size]
                    seed_range_start = seed_range[0]
                    seed_range_size = seed_range[1]

                    cur_seed_range = [seed_range_start, seed_range_start+seed_range_size-1]
                    cur_convert_range = [source, source+size-1]

                    overlap, no_overlap = self.findOverlap(cur_seed_range, cur_convert_range)
                    old_seed_ranges = set([(non_overlapping_range[0], non_overlapping_range[1]-non_overlapping_range[0]+1) for non_overlapping_range in no_overlap])
                    
                    for old_seed_range in old_seed_ranges:
                        if old_seed_range not in seed_ranges:
                            seed_ranges.add(old_seed_range)

                    if seed_range not in old_seed_ranges:
                        seed_ranges.remove(seed_range)
                    
                    for overlapping_range in overlap:
                        new_seed_ranges.add((overlapping_range[0]-source+dest, overlapping_range[1]-overlapping_range[0]+1))

            seed_ranges = new_seed_ranges | seed_ranges
        self.locations = seed_ranges




    # returns a list [[overlap ranges], [non-overlap ranges]]
    # will then need to conver the overlap ranges
    # then push both back on to the deque
    def findOverlap(self, seed_range, convert_range):
        seed_start, seed_end = seed_range[0], seed_range[1]
        convert_start, convert_end = convert_range[0], convert_range[1]
        overlap = []
        no_overlap = []

        # seed start is less than convert start
        if seed_start < convert_start:
            # seed end is greater than or equal to convert start
            if seed_end >= convert_start:
                # CASE 1: low part
                if seed_end <= convert_end:
                    overlap.append([convert_start, seed_end])
                    no_overlap.append([seed_start, convert_start-1])
                # CASE 4: More than all in
                else:
                    overlap.append([convert_start, convert_end])
                    no_overlap.append([seed_start, convert_start-1])
                    no_overlap.append([convert_end+1, seed_end])
            # CASE 5: None (low end)
            else:
                no_overlap.append([seed_start, seed_end])
        # seed start is less than convert end
        elif seed_start <= convert_end:
            # CASE 3: All in
            if seed_end <= convert_end:
                overlap.append([seed_start, seed_end])
            # Case 2: High part
            else:
                overlap.append([seed_start, convert_end])
                no_overlap.append([convert_end+1, seed_end])
        # CASE 5: None (high end)
        else:
            no_overlap.append([seed_start, seed_end])
            
        return [overlap, no_overlap]
    
    def getMinimun(self) -> int:
        smallest = float('inf')
        for range in self.locations:
            smallest = min(smallest, range[0])
        return smallest




def main():
    # correct answer for full input is: 9622622
    seed_converter = SeedConverter("Day 5/input.txt")
    seed_converter.parseFile()
    seed_converter.convertSeeds()
    smallest = seed_converter.getMinimun()
    print(smallest)


if __name__ == "__main__":
    main()
