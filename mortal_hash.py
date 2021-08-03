#!/usr/bin/python3
import sys,hashlib,os,time
# sha1 md5 sha256 sha521 sha224 sha384 sha2_224 sha3_256

if sys.platform == 'linux':
    os.system('clear')
else:
    pass
    
print('[^-^] Hello Friend!! [*]')
time.sleep(2)
print('\t\t*[<->:MORTAL HASH:<->]*')
time.sleep(1)

mortal = '''           
                       _..gggggppppp.._                       
                  _.gd$$$$$$$$$$$$$$$$$$bp._                  
               .g$$$$$$P^^""j$$b""""^^T$$$$$$p.               
            .g$$$P^T$$b    d$P T;       ""^^T$$$p.            
          .d$$P^"  :$; `  :$; Mortal Kombat   "^T$$b.          
        .d$$P'      T$b.   T$b                  `T$$b.        
       d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b       
      d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b      
     d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b     
    d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P  Scorpion  T$$b    
   d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b   
  :$$$      .d$$$$Crack-Me$$$$$$$$$$$$$$$$$$$p._.g.     $$$;  
  $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$  
 :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$; 
 $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$ 
:$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
:$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
$$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
$$$;      $$$$$$$$$$$$$$$     Mortal Kombat      Tb    _  :$$$
:$$$     d$$$$$$$$$$$$$$$.    Mortal Hash          $b.__Tb $$$;
:$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
 $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$ 
 :$$$       T$$OccupyTheWeb$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$; 
  $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$  
  :$$$        $$$$$$$$$$$$$$$$$$sha1$$$$$$$$$$$$$$;     $$$;  
   T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P   
    T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P    
     T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P     
      T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P      
       T$$b.      '       $$$$$$$$md5$$$$$$$$$$$$$$$$$P       
        `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'        
          `T$$$$p..__..g$$$$$$$$$ Mortal $$$$$$$$$$$P'          
            "^$$$$$$$$$$$$$$$$$$$$ Hash $$$$$$$$$$$^"            
               "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"               
                   """^^^T$$$$$$$$$$P^^^"""'''

if len(sys.argv) !=4 :
    print('\n\nUsage: ./mortal_hash <wordlist> <hash algorithm> <hash>')
    print('\nExample: ./mortal_hash <md5 or sha1 or sha256 or sha384 or sha512> <hash> <wordlist>')
    print('Example: ./mortal_hash md5 5d41402abc4b2a76b9719d911017c592 /usr/share/wordlists/rockyou.txt')
    sys.exit(1)

algo = sys.argv[1]
passwd = sys.argv[2]
wordlist = sys.argv[3]

print(mortal)
print('[!] Please Wait [!]')

try:
    words = open(wordlist,'rb',buffering=2000000000)
    os.system('wc -l ' + wordlist)
    print('Word Loaded....')
except (IOError):
    print('Error: Your wordlist not found\n --Check your wordlist path\n')
    time.sleep(0.4)
    print('Good By Friend!!')
    sys.exit(1)

def algo_md5():
    for word in words:
        start = time.time()
        hash = hashlib.md5(word[:-1])
        value = hash.hexdigest()
        if passwd == value:
            word = str(word,'utf-8')
            print('Password|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))

            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)
        
def algo_sha1():
    for word in words:
        start = time.time()
        hash = hashlib.sha1(word[:-1])
        value = hash.hexdigest()
        if passwd == value:
            word = str(word,'utf-8')
            print('Password|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))
            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)

def algo_sha256():
    for word in words:
        start = time.time()
        hash = hashlib.sha256(word[:-1])
        value = hash.hexdigest()
        if passwd == value: 
            word = str(word,'utf-8')
            print('\nPassword|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))
            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)

def algo_sha384():
    for word in words:
        start = time.time()
        hash = hashlib.sha384(word[:-1])
        value = hash.hexdigest()
        if passwd == value:
            word = str(word,'utf-8')
            print('Password|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))
            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)

def algo_sha224():
    for word in words:
        start = time.time()
        hash = hashlib.sha224(word[:-1])
        value = hash.hexdigest()
        if passwd == value:
            word = str(word,'utf-8')
            print('Password|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))
            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)    

def algo_sha512():
    for word in words:
        start = time.time()
        hash = hashlib.sha512(word[:-1])
        value = hash.hexdigest()
        if passwd == value:
            word = str(word,'utf-8')
            print('Password|->->-> ' + str(word[:-1]))
            end = time.time()
            t_time = end - start
            print('Total runtime was --'+str(t_time))
            with open('cracked.txt','a') as c:
                c.write('\n Cracked Hashes\n\n')
                c.write(passwd+'\t\t')
                c.write(word[:-1]+'\n')
            time.sleep(0.4)
            print('\nGood By Friend!!')
            print('[*] This Script Created By: OccupyTheWeb')
            print('\t\t\t[+]Done![+]')
            sys.exit(1)    

if algo == 'md5':
    algo_md5()
elif algo == 'sha1':
    algo_sha1()
elif algo == 'sha224':
    algo_sha224()
elif algo == 'sha256':
    algo_sha256()
elif algo == 'sha384':
    algo_sha384()
elif algo == 'sha512':
    algo_sha512()
else:
    print(f'[!] {algo} Not Found [!]')
    print('["] Algorithms Available {md5-sha1-sha224-sha256-sha384-sha512} ["]')
    print('Example: /mortal_hash md5 5d41402abc4b2a76b9719d911017c592 /usr/share/wordlists/rockyou.txt')
    sys.exit(1)