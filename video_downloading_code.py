from pytube import YouTube 


link= str(input(" Enter the link of video :\n"))
yt = YouTube(link)
print(" Views : ", yt.views,"\n")
print(" Title : ", yt.title,"\n")

yd = yt.streams.get_highest_resolution()

 
path=r"_PATH_OF_DIRETORY_"
# \ in python used as a escape character so 'r' is to ignore

yd.download(output_path=path)





