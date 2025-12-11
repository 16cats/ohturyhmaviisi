Write-Host "== Ohturyhmaviisi asennus (Windows) =="

# Tarkista Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Virhe: Python ei löytynyt. Asenna Python 3.10+."
    exit 1
}

# Tarkista Poetry
if (-not (Get-Command poetry -ErrorAction SilentlyContinue)) {
    Write-Host "Poetry ei ole asennettuna. Asennetaan..."
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    Write-Host "Poetry asennettu!"
    Write-Host "Saatat joutua käynnistämään PowerShellin uudelleen."
}

Write-Host ""
Write-Host "== Asennetaan projektin riippuvuudet =="
poetry install --no-root

Write-Host ""
Write-Host "== Aktivoidaan Poetry-ympäristö =="

# Haetaan virtual environmentin polku
$venvPath = poetry env info --path

if (-not (Test-Path $venvPath)) {
    Write-Host "Virhe: virtual environment ei löydy!"
    exit 1
}

# Aktivointi Windowsin bin Scripts-kansiosta
$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"

if (-not (Test-Path $activateScript)) {
    Write-Host "Virhe: aktivointiscriptiä ei löytynyt!"
    exit 1
}

Write-Host "Aktivoidaan ympäristö: $venvPath"
. $activateScript

Write-Host ""
Write-Host "== Käynnistetään sovellus =="
python -m src.main