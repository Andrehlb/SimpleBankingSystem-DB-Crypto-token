import json
def lambda_handler(event, context):
    #aqui simula processamento de transação
    transaction = event.get("transaction", {})
    user_id = transaction.get("user_id", "unknown")
    amount = transaction.get("amount", 0)

    #aqui vou simular uma resposta de sucesso da transação
    response = {
        "status": "success",
        "user_id": user_id,
        "processed_amount": amount,
        "message": "A transação foi feita com sucesso"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response, ensure_ascii=False)
    }