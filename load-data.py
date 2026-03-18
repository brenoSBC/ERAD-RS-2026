import os

FD = {
    "patterns": ['111', '121', '131', '141', '161', '181'],
    "openmpi": [],
    "resipipe": [],
    "flink": []
}

SA = {
    "patterns": ['111', '121', '131', '141', '161', '181'],
    "openmpi": [],
    "resipipe": [],
    "flink": []
}

SD = {
    "patterns": ['1111', '1221', '1331', '1441', '1641', '1861'],
    "openmpi": [],
    "resipipe": [],
    "flink": []
}

TM = {
    "patterns": ['1111', '1221', '1331', '1441', '1641', '1861'],
    "openmpi": [],
    "resipipe": [],
    "flink": []
}

def read_file(path):
  lines = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if line != "":
                lines.append(float(line))
    
    return lines

def populate(app, app_name):

    for p in app["patterns"]:

        # OPENMPI
        path = f"mpi_throughput/{app_name()}-{p}-throughput.txt"
        app["openmpi"].append(read_file(path))

        # RESIPIPE
        path = f"resipipe_throughput/{app_name()}-{p}-throughput.txt"
        app["resipipe"].append(read_file(path))

        # FLINK
        path = f"flink_throughput/{app_name()}-{p}-throughput.txt"
        app["flink"].append(read_file(path))


populate(FD, "FD")
populate(SA, "SA")
populate(SD, "SD")
populate(TM, "TM")

print(FD["openmpi"][0])