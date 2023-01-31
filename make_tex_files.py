import os

if __name__ == "__main__":

    files = os.listdir(".")

    print(files)

    prefix = "seance"

    files = [file for file in files if file.startswith(prefix)]

    for file in files:

        number = file[len(prefix):-4]

        exe_filename = f"TP_{number}.tex"
        sol_filename = f"TP_{number}_solution.tex"

        with open(file, "r") as f:

            content = f.readlines()
            content = [line for line in content if not r"\def\AvecSolutions{}" in line]

        os.remove(file)

        with open(exe_filename, "w") as f:

            f.writelines(content)

            print(exe_filename)

        with open(sol_filename, "w") as f:

            content.insert(1, r"\def\AvecSolutions{}")

            f.writelines(content)

            print(sol_filename)


