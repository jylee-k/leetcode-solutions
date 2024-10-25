class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort() # this already sorts lexicologically, only need to check last appended folder if it's a parent folder
        unique_folder = [folder[0]]
        for f in folder:
            # print("f is", f)
            try:
                a = unique_folder[-1]
                if self.isSubfolder(a,f) or a == f: # then f is a subfolder of a
                    # print(f, "is subfolder of ", a)
                    raise Exception
            except:
                continue
            else:   
                # print(f, "is not subfolder of", a)
                unique_folder.append(f)
                # print(unique_folder)
        return unique_folder

    def isSubfolder(self,a,f):
        # check is f is subfolder of a
        # f must start with a
        # when split by / , len(f) must be smaller than len(a)
        # when a is replaced in f by "", the start of f must be a "/"
        if f.startswith(a):
            if len(f.split("/")) > len(a.split("/")):
                if f[len(a):].startswith("/"):
                    return True
        return False
            
