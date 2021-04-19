import requests


URL =   "https://api.movidesk.com/public/v1/tickets"
TOKEN = "63d11b3a-b64a-48ac-8ab1-62fc12ebcb90"

def request(status, order,filter_level):
    response = requests.get(URL+"?token="+TOKEN+"&$select=id,subject,category,status,ownerTeam,serviceFirstLevel,serviceFirstLevel,actionCount,serviceSecondLevel,serviceFirstLevelId,lastUpdate,lastActionDate&$filter=serviceFirstLevel eq '"+filter_level+"'  and status eq '"+status+"'&$orderby=actionCount "+order+"")
    return response.json()


