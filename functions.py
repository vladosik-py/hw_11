import json


def load_candidates_from_json():
    """загружает данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidates_all():
    """возвращает список всех кандидатов"""
    return load_candidates_from_json()


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == id:
            return candidate
    return 'Not Found'


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            return candidate
    return 'Not Found'


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    result = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower():
            result.append(candidate)
    return result
