<?php 
// Receive GET Parameters
 
$Company = $_GET["Company"]; 
$TypeName = $_GET["TypeName"]; 
$Inches = $_GET["Inches"]; 
$ScreenResolution = $_GET["ScreenResolution"]; 
$Cpu = $_GET["Cpu"]; 
$Ram = $_GET["Ram"]; 
$Memory = $_GET["Memory"]; 
$OpSys = $_GET["OpSys"]; 
system("/usr/anaconda/bin/python3 laptop_model.py ".$Company." ".$TypeName." ".$Inches." ".$ScreenResolution." ".$Cpu." ".$Ram." ".$Memory." ".$OpSys."  2>&1");

?>  