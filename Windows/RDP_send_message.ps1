# $ConnectionBroker - Активный сервер RDCB.
# Если не указан, будет произведена попытка выявить его автоматически (для этого обязательно чтобы скрипт выполнялся на одном из серверов фермы RDS)
# $SessionHostCollection – Имя RD-коллекции в которой нужно вывести сообщение.


$ConnectionBroker = ""
$SessionHostCollection = "QuickSessionCollection"

$MessageTitle = "Сообщение от Администратора"
$MessageText = "ВНИМАНИЕ! Перезагрузка сервера через 2 минуты!"

If ($ConnectionBroker -eq "") {
 $HAFarm = Get-RDConnectionBrokerHighAvailability
 $ConnectionBroker = $HAFarm.ActiveManagementServer
}

$Sessions = Get-RDUserSession -ConnectionBroker $ConnectionBroker -CollectionName $SessionHostCollection
ForEach ($Session in $Sessions) {
Send-RDUserMessage -HostServer $Session.ServerName -UnifiedSessionID $Session.UnifiedSessionID -MessageTitle $MessageTitle -MessageBody $MessageText 
}