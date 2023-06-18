import logging
import re
from urllib.parse import urljoin
from outputs import control_output

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

from constants import (
    BASE_DIR,
    MAIN_DOC_URL,
    STATUSES,
    PEP_URL,
    EXPECTED_STATUS)
from configs import configure_argument_parser, configure_logging
from exceptions import FileWriteError, MakingDirError
from utils import find_sibling
from utils import get_response, find_tag


def pep(session):
    response = get_response(session, PEP_URL)
    soup = BeautifulSoup(response.text, features='lxml')
    pep_list = find_tag(soup, 'section', attrs={'id': 'numerical-index'})
    tbody_tag = find_tag(pep_list, 'tbody')
    tr_tags = tbody_tag.find_all('tr')
    results = [('PEP', 'PEP Title', 'Status')]
    for section in tqdm(tr_tags):
        pep_status_tag = section.find('td')
        preview_status = pep_status_tag.text[1:]
        pep_num = find_sibling(pep_status_tag)
        pep_title = find_sibling(pep_num)
        pep_a_tag = find_tag(pep_title, 'a')
        pep_link = urljoin(PEP_URL, pep_a_tag['href'])
        response = get_response(session, pep_link)
        if response is None:
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        body = find_tag(soup, 'section', attrs={'id': 'pep-content'})
        dt = body.find_all('dt')
        for tag in dt:
            if 'Status' in tag.text:
                pep_status = find_sibling(tag)
                STATUSES[pep_status.text] += 1
                break
        results.append(
            (pep_num.text, pep_title.text, pep_status.text)
        )
        if preview_status:
            if pep_status.text not in EXPECTED_STATUS[preview_status]:
                logging.info(
                    f'Несовпадающий статус:'
                    f'{pep_link}'
                    f'Статус в карточке: {pep_status.text}'
                    f'Ожидаемые статусы: {EXPECTED_STATUS[preview_status]}'
                )
    pep_amount = len(results) - 1
    results.append((f'PEP in total = {pep_amount}',))
    for status in STATUSES:
        results.append((f'{status} in total = {STATUSES[status]}',))
    return results


def whats_new(session):
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    response = get_response(session, whats_new_url)
    if response is None:
        return None
    soup = BeautifulSoup(response.text, features='lxml')
    main_div = find_tag(soup, 'section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = find_tag(main_div, 'div',
                           attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all('li',
                                              attrs={'class': 'toctree-l1'})
    results = [('Ссылка на статью', 'Заголовок', 'Редактор, Автор')]
    for section in tqdm(sections_by_python):
        version_a_tag = find_tag(section, 'a')
        version_link = urljoin(whats_new_url, version_a_tag['href'])
        response = get_response(session, version_link)
        if response is None:
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        h1 = find_tag(soup, 'h1')
        dl = find_tag(soup, 'dl')
        dl_text = dl.text.replace('\n', ' ')
        results.append(
            (version_link, h1.text, dl_text)
        )
    return results


def latest_versions(session):
    response = get_response(session, MAIN_DOC_URL)
    if response is None:
        return None
    soup = BeautifulSoup(response.text, features='lxml')
    sidebar = soup.find('div', {'class': 'sphinxsidebarwrapper'})
    ul_elements = sidebar.find_all('ul')
    for ul_tag in ul_elements:
        if 'All versions' in ul_tag.text:
            version_links = ul_tag.find_all('a')
            break
        raise Exception('Ничего не нашлось')
    results = [('Ссылка на документацию', 'Версия', 'Статус')]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for version_link in version_links:
        link = version_link['href']
        text_match = re.search(pattern, version_link.text)
        version, status = text_match.groups() if text_match \
            else version_link.text, ''
        results.append((link, version, status))
    return results


def download(session):
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    response = get_response(session, downloads_url)
    if response is None:
        return
    soup = BeautifulSoup(response.text, features='lxml')
    main_tag = find_tag(soup, 'div', {'role': 'main'})
    table_tag = find_tag(main_tag, 'table', {'class': 'docutils'})
    pdf_a4_tag = find_tag(table_tag, 'a', {'href': re.compile(
        r'.+pdf-a4\.zip$')})
    pdf_a4_link = pdf_a4_tag['href']
    archive_url = urljoin(downloads_url, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    try:
        downloads_dir.mkdir(exist_ok=True)
    except:
        raise MakingDirError('Ошибка при попытке создания директории!')
    archive_path = downloads_dir / filename
    response = session.get(archive_url)
    try:
        with open(archive_path, 'wb') as file:
            file.write(response.content)
        logging.info(f'Архив был загружен и сохранён: {archive_path}')
    except:
        raise FileWriteError('Ошибка при загруке архива!')


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep,
}


def main():
    configure_logging()
    logging.info('Парсер запущен!')
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')
    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()
    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info('Парсер завершил работу.')


if __name__ == '__main__':
    main()
