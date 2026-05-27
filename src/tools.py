def consultar_historico_paciente(paciente_id):
    return {
        "paciente_id": paciente_id,
        "idade": 42,
        "condicoes": ["hipertensão leve"],
        "alergias": ["dipirona"],
        "medicamentos": ["losartana 50mg"],
        "ultima_pressao": "135/85"
    }


def verificar_interacoes_medicamentosas(medicamentos):
    meds = [m.lower() for m in medicamentos]
    if "dipirona" in meds:
        return {"risco": "alto", "mensagem": "Paciente possui alergia registrada a dipirona."}
    if "ibuprofeno" in meds and any("losartana" in m for m in meds):
        return {"risco": "moderado", "mensagem": "Atenção ao uso de anti-inflamatório em paciente hipertenso."}
    return {"risco": "baixo", "mensagem": "Sem interação relevante na base simulada."}


def agendar_teleconsulta(paciente_id, especialidade, prioridade):
    return {
        "status": "agendado",
        "paciente_id": paciente_id,
        "especialidade": especialidade,
        "prioridade": prioridade,
        "data_hora": "2026-05-20 14:30"
    }
