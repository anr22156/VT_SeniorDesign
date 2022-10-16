$link = "https://physionet.org/files/pulse-transit-time-ppg/1.1.0/csv/"
$fileslink = Invoke-WebRequest -Uri "$link"
$html = $fileslink.Content


$ProgressPreference = 'SilentlyContinue'
foreach ($line in $html.split("")) {

if ($line.indexOf("href=") -ge 0) {
    $file = $line.Substring( ("href=").Length + 1, $line.Length - $line.indexOf('">') - 6)
    Invoke-WebRequest -Uri "$link$file" -OutFile "C:\Users\nitar\Downloads\files\csv\$file"
}
}