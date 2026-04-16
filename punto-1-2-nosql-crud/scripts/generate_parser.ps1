# Regenera el código Python desde grammar/grammar1.g4 (requiere Java en PATH).
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$jar = Join-Path $root "tools\antlr-4.13.2-complete.jar"
if (-not (Test-Path $jar)) {
    New-Item -ItemType Directory -Force -Path (Split-Path $jar) | Out-Null
    Invoke-WebRequest -Uri "https://repo1.maven.org/maven2/org/antlr/antlr4/4.13.2/antlr4-4.13.2-complete.jar" -OutFile $jar
}
$out = Join-Path $root "src\nosql_dsl\generated"
$g4 = Join-Path $root "grammar\grammar1.g4"
Push-Location $root
try {
    & java -jar $jar -Dlanguage=Python3 -visitor -listener -o $out -Xexact-output-dir $g4
}
finally {
    Pop-Location
}
