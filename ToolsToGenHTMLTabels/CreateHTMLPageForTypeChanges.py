import csv
from jinja2 import Environment, FileSystemLoader
import os

file_path = "/Users/malinda/Downloads/WebsiteContent.txt"
templates_dir="/Users/malinda/Documents/RectrofitinMLtoCode/Python/PYCOLLECTOR/FiveMinuteCodes"

def main():
    file_content = map(lambda x:[x[0],x[1],x[2],x[3],x[4].split(',')],
                       [g for g in csv.reader(open(file_path, 'r'), delimiter='\t') if len(g)>0])
    env = Environment(loader=FileSystemLoader(templates_dir))
    template1 = env.get_template('template1.html')
    template2 = env.get_template('template2.html')


    j=0
    for t in file_content:
        From_ = t[0]
        To_ = t[1]
        ProjectNumb_ = t[2]
        CommitNumb_ = t[3]

        temp2 = []
        i=1
        for g in t[4]:
            temp2.append((g,"Commit-"+str(i),"Example-"+str(i)))
            i+=1

        with open("table.html", 'a') as fh:
            fh.write(template1.render(
                From=From_,
                To=To_,
                Projects=ProjectNumb_,
                Commits=CommitNumb_,
                commits_links=temp2,
                num=j
            ))
            fh.write('\n')
        print(t)
        j+=1
if __name__ == '__main__':
    main()