import glob, subprocess

def get_output_file(file_name):
    temp = filename.split("/")
    dir = '/'.join(temp[:-1])
    file = temp[-1].split(".")[0]
    return '{}/{}.html'.format(dir, file)

for filename in glob.iglob('./**/*.md', recursive=True):
    if filename.endswith("README.md"):
        continue
    
    cmd = 'pandoc -s -f markdown -t html --mathjax --quiet -o {} {}'.format(get_output_file(filename), filename)
    subprocess.run(cmd, shell=True)