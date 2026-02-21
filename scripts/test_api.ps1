$BaseUrl = "http://127.0.0.1:8001"

Write-Host "Testing API at $BaseUrl"

# health
$health = Invoke-RestMethod -Uri "$BaseUrl/health" -TimeoutSec 3 -Proxy $null
Write-Host "Health:"
$health

# predict
$body = @{
    sepal_length = 5.1
    sepal_width  = 3.5
    petal_length = 1.4
    petal_width  = 0.2
} | ConvertTo-Json

$pred = Invoke-RestMethod -Method Post `
  -Uri "$BaseUrl/predict" `
  -ContentType "application/json" `
  -Body $body `
  -TimeoutSec 3 `
  -Proxy $null

Write-Host "Predict:"
$pred | ConvertTo-Json -Depth 5

Write-Host "All checks passed"