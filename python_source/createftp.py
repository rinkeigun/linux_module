from ftplib import FTP
 
 
ftp = FTP('ftp.ncbi.nlm.nih.gov')
 
ftp.login()
 
ftp.cwd('pubchem/Substance/Daily/2018-02-17/XML/')
 
files = ftp.nlst('.')
 
for file in files:
 
    print(file)
    with open('pubchem/' + file, 'wb') as f:
        ftp.retrbinary('RETR %s' % file, f.write)
ftp.quit()
