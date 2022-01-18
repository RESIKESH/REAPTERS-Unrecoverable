# Reapters
<img src="https://community.coreldraw.com/resized-image/__size/208x189/__key/communityserver-discussions-components-files/839/pastedimage1514673185189v1.jpeg" width="128"/>
### Problem Statement
Data recovery softwares can easily recover the deleted data from the Hard Disk. Develop an executable code snippet for Microsoft Windows environment to Securely Delete the given file. Deleted file should not be recoverable using any Forensic tool. Any of the common secure deletion practices may be used.


## Solution
The common method is using the [srm](https://en.wikipedia.org/wiki/Srm_(Unix)) but this is only for unix.

In windows whenever a file deleted from teh recycle bin, it remove its log entry thus removing its pointer indicating that this space could be resuable, but the whole file dosen't gets permanently deleted, thus recovery tools can retrive those file and thus its data.
So for the system using windows as their OS we need to use the [Gutmann Method](https://en.wikipedia.org/wiki/Gutmann_method) in order to delete a file securely. 
Thus using the [Gutmann Method](https://en.wikipedia.org/wiki/Gutmann_method) we get the data that should be overwritten into the file, before deleting it.
In order to run this file we need to have `python3.8` then in console type the following command
```console
python main.py
```
