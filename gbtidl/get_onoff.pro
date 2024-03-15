pro get_onoff

path_config
path = !data_path

proj_list = ["AGBT15B_228_08",$
             "AGBT16B_392_01",$
             "AGBT17B_004_14",$
             "AGBT18B_354_03"$
            ]

scans = [29,$
         24,$
         34,$
         6$
        ]

s = size(proj_list)

for i=0,s[1]-1 do begin
    input  = path+proj_list[i]+"/"+proj_list[i]+".raw.vegas"
    output = path+proj_list[i]+"/gbtidl/"+proj_list[i]+".getps.vegas.fits"
    filein,input
    getps,scans[i]
    fileout,output
    keep
endfor

; ACS
proj_list = ["AGBT05B_047_01"]
scans = [51]
s = size(proj_list)

for i=0,s[1]-1 do begin
    input  = path+proj_list[i]+"/"+proj_list[i]+".raw.acs"
    output = path+proj_list[i]+"/gbtidl/"+proj_list[i]+".getps.acs.fits"
    filein,input
    getps,scans[i]
    fileout,output
    keep
endfor

end
