from src.analysis import analyze_with_model, classify_text, extract_topics, extract_tags, rephrase_text

def process_text(text, analysis_type='summary'):
    """
    Procesa el texto según el tipo de análisis requerido.
    :param text: El texto a analizar.
    :param analysis_type: Tipo de análisis ('summary', 'classification', 'topics', 'tags', 'rephrase')
    :return: El resultado del análisis.
    """
    if analysis_type == 'summary':
        result = analyze_with_model(text)
    elif analysis_type == 'classification':
        result = classify_text(text)
    elif analysis_type == 'topics':
        result = extract_topics(text)
    elif analysis_type == 'tags':
        result = extract_tags(text)
    elif analysis_type == 'rephrase':
        result = rephrase_text(text)
    else:
        result = {'error': 'Invalid analysis type'}

    return result