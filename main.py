import dumper

if __name__ == '__main__':
    f = open("log.txt", "w")

    log = dumper.dump("base_data/Indian_pines_corrected.mat", "base_data/Indian_pines_gt.mat", "data/indian_pines.csv",'indian_pines_corrected','indian_pines_gt')
    f.write(str(log)+"\n")

    # log = dumper.dump("base_data/Pavia.mat", "base_data/Pavia_gt.mat", "data/pavia.csv",'pavia','pavia_gt')
    # f.write(str(log)+"\n")
    # #
    log = dumper.dump("base_data/PaviaU.mat", "base_data/PaviaU_gt.mat", "data/paviaU.csv",'paviaU','paviaU_gt')
    f.write(str(log)+"\n")

    log = dumper.dump("base_data/Salinas_corrected.mat", "base_data/Salinas_gt.mat", "data/salinas.csv",'salinas_corrected','salinas_gt')
    f.write(str(log)+"\n")

    # log = dumper.dump("base_data/SalinasA_corrected.mat", "base_data/SalinasA_gt.mat", "data/salinasA.csv",'salinasA_corrected','salinasA_gt')
    # f.write(str(log)+"\n")