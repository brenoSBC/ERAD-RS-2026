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

apps = {
    "FD": FD,
    "SA": SA,
    "SD": SD,
    "TM": TM
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

        # FLINK
        path = f"./FLINK/flink_throughput_stream/{app_name}-{p}-throughput.txt"
        app["flink"].append(read_file(path))

        # OPENMPI
        path = f"./MPI/mpi_throughput/{app_name}-{p}-throughput.txt"
        app["openmpi"].append(read_file(path))

        # RESIPIPE
        path = f"./RESIPIPE/resipipe_throughput/{app_name}-{p}-throughput.txt"
        app["resipipe"].append(read_file(path))

populate(FD, "FD")
populate(SA, "SA")
populate(SD, "SD")
populate(TM, "TM")


# frameworks = ["flink", "openmpi", "resipipe"]

# for name, app in apps.items():
#     print(f"\n=== {name} ===")
    
#     for fw in frameworks:
#         print(f"\n--- {fw} ---")
        
#         for i in range(len(app["patterns"])):
#             pattern = app["patterns"][i]
#             data = app[fw][i]
            
#             print(f"{pattern}: {data}")

