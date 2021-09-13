# $ConnectionBroker - �������� ������ RDCB.
# ���� �� ������, ����� ����������� ������� ������� ��� ������������� (��� ����� ����������� ����� ������ ���������� �� ����� �� �������� ����� RDS)
# $SessionHostCollection � ��� RD-��������� � ������� ����� ������� ���������.


$ConnectionBroker = ""
$SessionHostCollection = "QuickSessionCollection"

$MessageTitle = "��������� �� ��������������"
$MessageText = "��������! ������������ ������� ����� 2 ������!"

If ($ConnectionBroker -eq "") {
 $HAFarm = Get-RDConnectionBrokerHighAvailability
 $ConnectionBroker = $HAFarm.ActiveManagementServer
}

$Sessions = Get-RDUserSession -ConnectionBroker $ConnectionBroker -CollectionName $SessionHostCollection
ForEach ($Session in $Sessions) {
Send-RDUserMessage -HostServer $Session.ServerName -UnifiedSessionID $Session.UnifiedSessionID -MessageTitle $MessageTitle -MessageBody $MessageText 
}