# Bad Pass Gen
Generate a list of bad passwords or NTLM hashes.  
---
**Be mindful of your available resources and the amount of arguments you choose!**

### Usage  
---
Positional arguments:  
mask                    The password mask to use.  

Options:  
-h, --help              Show this help message and exit.  
-o OUTFILE, --outfile OUTFILE  
                        Write output to a file.  
--ntlm                  Output only NTLM.  
--both                  Output both clear text and NTLM.  
  
Password Mask Options:  
&nbsp;&nbsp;&nbsp;&nbsp;/d for digits  
&nbsp;&nbsp;&nbsp;&nbsp;/l for lowercase  
&nbsp;&nbsp;&nbsp;&nbsp;/u for uppercase  
&nbsp;&nbsp;&nbsp;&nbsp;/s for special characters  
&nbsp;&nbsp;&nbsp;&nbsp;/a for all of the previous options  
  
### Examples
---
- Mask: password/d/d
&nbsp;&nbsp;- Possible Password: password84  
&nbsp;&nbsp;- Possible NTLM: E9D68143E51CA2AE975BB4DA61183054  
- Mask: password/a/d
&nbsp;&nbsp;- Possible Password: passwordh8  
&nbsp;&nbsp;- Possible NTLM: 9FB8D457B23371A2069EB07009D3BC5A  
- Mask: password/u/l/s
&nbsp;&nbsp;- Possible Password: passwordNe*  
&nbsp;&nbsp;- Possible NTLM: 0502243BC8A1A8C3BA7F70B305564B03  

### To-do List  
---
- [ ] Add code to check for escapes.
- [ ] Other cool things.