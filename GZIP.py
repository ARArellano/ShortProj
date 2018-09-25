import gzip
with open(r'C:\Users\Ayra.Rosella\Desktop\feedback.txt' ,'r') as f_in, gzip.open(r'C:\Users\Ayra.Rosella\Desktop\feedback.txt.gz', 'r') as f_out:
    f_out.writelines(f_in)