from transformers import pipeline
from src.consts import topics, labels


summarizer = pipeline("summarization" )
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
topic_extractor = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
tagger = pipeline("ner")
rephrasing_model = pipeline("text2text-generation", model="t5-small")

def analyze_with_model(text):
    """
    Analiza el texto utilizando un modelo de IA preentrenado.
    :param text: El texto a analizar.
    :return: El análisis realizado.
    """
    # Cargar el pipeline de Hugging Face

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']

def classify_text(text):
    """
    Clasifica el texto utilizando un modelo de IA preentrenado.
    :param text: El texto a clasificar.
    :return: La clasificación realizada.
    """
    result = classifier(text, candidate_labels=labels)

    print(result)

    # Filtrar solo las etiquetas con score > 0.6
    filtered_result = {
        "labels": [],
        "scores": []
    }

    for label, score in zip(result['labels'], result['scores']):
        if score > 0.4:
            filtered_result['labels'].append(label)
            filtered_result['scores'].append(score)

    # Retornar el resultado filtrado
    return filtered_result


def extract_topics(text):
    """
    Extrae los temas del texto utilizando un modelo de IA preentrenado.
    :param text: El texto del cual se extraerán los temas.
    :return: Los temas extraídos.
    """
    result = topic_extractor(text, candidate_labels=topics)
    return result

def extract_tags(text):
    """
    Extrae las etiquetas del texto utilizando un modelo de IA preentrenado.
    :param text: El texto del cual se extraerán las etiquetas.
    :return: Las etiquetas extraídas.
    """
    entities = tagger(text)
    tags = [entity['word'] for entity in entities]
    return tags

def rephrase_text(text):
    """
    Reescribe el texto utilizando un modelo de IA preentrenado.
    :param text: El texto a reescribir.
    :return: El texto reescrito.
    """
    result = rephrasing_model(text)
    return result[0]['generated_text']