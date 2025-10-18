# PlantUML Diagram Validation and Export Script
# Tests all .puml files in the diagrams directory

$plantumlJar = "C:\tools\plantuml\plantuml.jar"
$diagramsDir = "diagrams"
$exportsDir = "diagrams/exports"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PlantUML Diagram Validation & Export" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Create exports directory if it doesn't exist
if (-not (Test-Path $exportsDir)) {
    Write-Host "Creating exports directory: $exportsDir" -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $exportsDir | Out-Null
}

# Find all .puml files
$pumlFiles = Get-ChildItem -Path $diagramsDir -Filter *.puml -Recurse
Write-Host "Found $($pumlFiles.Count) PlantUML diagrams`n" -ForegroundColor Cyan

# Validate syntax
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PHASE 1: Syntax Validation" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$failedFiles = @()
$passedCount = 0

foreach ($file in $pumlFiles) {
    $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "")
    Write-Host "  Checking: $relativePath" -NoNewline

    $result = & java -jar $plantumlJar -syntax $file.FullName 2>&1 | Out-String

    if ($result -match "No diagram found|Error|Exception") {
        Write-Host " FAILED" -ForegroundColor Red
        $failedFiles += $file
        Write-Host "    Error: $result" -ForegroundColor Red
    } else {
        Write-Host " PASSED" -ForegroundColor Green
        $passedCount++
    }
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "PHASE 2: SVG Export Generation" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Generating SVG exports to $exportsDir..." -ForegroundColor Yellow
& java -jar $plantumlJar -tsvg "$diagramsDir/**/*.puml" -o $exportsDir 2>&1 | Out-Null
Write-Host "SVG export complete!`n" -ForegroundColor Green

# Summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SUMMARY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total diagrams:  $($pumlFiles.Count)" -ForegroundColor White
Write-Host "Passed:          $passedCount" -ForegroundColor Green
Write-Host "Failed:          $($failedFiles.Count)" -ForegroundColor $(if ($failedFiles.Count -eq 0) { "Green" } else { "Red" })
Write-Host "Exports:         $exportsDir" -ForegroundColor Cyan

if ($failedFiles.Count -eq 0) {
    Write-Host "`nAll diagrams validated successfully! " -ForegroundColor Green
    exit 0
} else {
    Write-Host "`nFailed files:" -ForegroundColor Red
    foreach ($file in $failedFiles) {
        Write-Host "  - $($file.FullName.Replace((Get-Location).Path + '\', ''))" -ForegroundColor Red
    }
    exit 1
}
