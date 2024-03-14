pro get_summary

path_config
path = !data_path ;"/home/dysh/acceptance_testing/data/"

; VEGAS files
proj_list = ["AGBT14B_480_06",$
             "AGBT15B_228_08",$
             "AGBT16B_392_01",$
             "AGBT17B_004_14",$
             "AGBT18A_503_02",$
             "AGBT18B_354_03",$
             "AGBT19A_080_01",$
             "AGBT19A_473_41",$
             "AGBT19B_096_08",$
             "AGBT20B_336_01",$
             "AGBT22A_325_15"]

s = size(proj_list)

for i=0,s[1]-1 do begin
    input  = path+proj_list[i]+"/"+proj_list[i]+".raw.vegas"
    output = path+proj_list[i]+"/gbtidl/"+proj_list[i]+".summary"
    filein,input
    summary,output
endfor

; ACS files
proj_list = ["AGBT13A_240_03"]
s = size(proj_list)
for i=0,s[1]-1 do begin
    input  = path+proj_list[i]+"/"+proj_list[i]+".raw.acs.fits"
    output = path+proj_list[i]+"/gbtidl/"+proj_list[i]+".summary"
    filein,input
    summary,output
endfor

end
