import csv, sys

class CsvWriter(object):

    def __init__(self):
        self.write_filename = None
        self.line_counter = 0

    def readFile(self, filename):

        lines = {}
        try:
            with open(filename, encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                line_number = 1
                for row in reader:
                    lines[line_number] = row
                    line_number += 1
        except FileNotFoundError:
            print("Wrong file or file path.")

        return lines

    def writeToFile(self, filename, csv_lines1, start_row1, finish_row1, csv_lines2, start_row2, finish_row2):

        with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
            _writer = csv.writer(f)
            
            # Write lines from 1st csv file
            for i in range(start_row1, finish_row1+1):
                _writer.writerow(csv_lines1[i])

            # Write lines from 2nd csv file
            for j in range(start_row2, finish_row2+1):
                _writer.writerow(csv_lines2[j])

    def startFromCommandLine(self):

        if len(sys.argv) != 8:
            print("Usage: output_filename.csv filename1.csv start_line1 end_line1 filename2.csv start_line2 end_line2")
            return -1

        else:
            # Get arguments
            write_filename = sys.argv[1]
            filename1 = sys.argv[2]
            start_line1 = int(sys.argv[3])
            end_line1 = int(sys.argv[4])
            filename2 = sys.argv[5]
            start_line2 = int(sys.argv[6])
            end_line2 = int(sys.argv[7])

            # Read lines
            lines1 = self.readFile(filename1)
            lines2 = self.readFile(filename2)

            # Write to a new file
            self.writeToFile(write_filename, lines1, start_line1, end_line1, lines2, start_line2, end_line2)


if __name__ == "__main__":
    writer = CsvWriter()
    writer.startFromCommandLine()
