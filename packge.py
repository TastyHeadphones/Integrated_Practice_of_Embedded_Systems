import shutil
def split_file(file, prefix = 20, max_size = 100, buffer=1024):
    """
    file: the input file
    prefix: prefix of the output files that will be created
    max_size: maximum size of each created file in bytes
    buffer: buffer size in bytes

    Returns the number of parts created.
    """
    if (shutil.copyfile(f'.//user0/{file}', f'.//user1/{file}')):
        pass
    else:
        with open(file, 'r+b') as src:
            suffix = 0
            while True:
                with open(prefix + '.%s' % suffix, 'w+b') as tgt:
                    written = 0
                    while written < max_size:
                        data = src.read(buffer)
                        if data:
                            tgt.write(data)
                            written += buffer
                        else:
                            return suffix
                    suffix += 1


def cat_files(infiles, outfile = 0, buffer=1024):
    """
    infiles: a list of files
    outfile: the file that will be created
    buffer: buffer size in bytes
    """
    if (shutil.copyfile(f'.//user1/{infiles}', f'.//user0/{infiles}')):
        pass
    else :
        with open(outfile, 'w+b') as tgt:
            for infile in sorted(infiles):
                with open(infile, 'r+b') as src:
                    while True:
                        data = src.read(buffer)
                        if data:
                            tgt.write(data)
                        else:
                            break

if __name__ == "__main__":
    shutil.copyfile('.//user0/1.txt', './/user1/1.txt')