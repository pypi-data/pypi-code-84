import datetime
import shutil
import os
import sys
import getpass
import argparse
import logging
import os

logging.basicConfig(format="[%(levelname)s]: %(message)s", level=os.environ.get('CL_LOG_LEVEL', 20))

from requests import Session, Request, HTTPError

from caselockerapi.auth import CaseLockerToken
from caselockerapi.utils import format_url

class Client(object):
    def __init__(self, token=False):
        self.session = Session()
        if token:
            self.token = token

    def _auth_headers(self):
        if self.token.expires + datetime.timedelta(minutes=1) < datetime.datetime.now():
            self.token.refresh()
        return {
            'Authorization': 'Bearer {}'.format(self.token),
        }

    def authenticate(self, DOMAIN=None, USERNAME=None, PASSWORD=None):
        login_token = CaseLockerToken(subdomain=DOMAIN, username=USERNAME, password=PASSWORD)
        self.token = login_token

    def request(self, method, url, stream=False, **kwargs):
        prepped_url = url.format(self.token.subdomain)
        headers = self._auth_headers()
        request = Request(method, prepped_url,
                          headers=headers,
                          **kwargs)
        prepped = request.prepare()
        response = self.session.send(prepped, stream=stream)
        try:
            response.raise_for_status()
        except HTTPError as err:
            logging.error(err.response.content)
            #sys.exit(2)
        return response

    def search(self, url, search=None, ordering=None, page=None, per_page=None, **kwargs):
        kwargs_copy = kwargs.copy()
        params = kwargs_copy.pop('params', {})
        params.update({
            'search': search,
            'ordering': ordering,
            'page': page,
            'count': per_page,
        })
        data = self.request('GET', url, params=params, **kwargs_copy).json()
        return SearchResults(self, url, data,
                             search=search,
                             ordering=ordering,
                             per_page=per_page,
                             **kwargs)

class SearchResults(object):
    def __init__(self, client, url, data, search=None, ordering=None, per_page=None, **kwargs):
        self.client = client
        self.url = url
        self.search = search
        self.ordering = ordering
        self.per_page = per_page
        self.kwargs = kwargs
        self._load_data(data)

    def all_results(self):
        results = self
        while True:
            try:
                for result in results.results:
                    yield result
                if results.num_pages == results.page:
                    break
                else:
                    results = results.get_next_page()
            except:
                print("End of Results")
                break

    def _load_data(self, data):
        self.page = data['page_number']
        self.count = data['count']
        self.num_pages = data['num_pages']
        self.results = data['results']

    def get_page(self, page):
        return self.client.search(self.url,
                                   search=self.search,
                                   ordering=self.ordering,
                                   page=page,
                                   per_page=self.per_page,
                                   **self.kwargs)

    def get_next_page(self):
        return self.get_page(self.page + 1)

    def get_previous_page(self):
        return self.get_page(self.page - 1)

class CaseObject(object):
    BASE_URL = None
    def __init__(self, client):
        self.client = client

    def list(self, search=None, ordering=None, page=1, per_page=25, **kwargs):
        return self.client.search(format_url(self.BASE_URL), search, ordering, page, per_page, **kwargs)

    def get(self, pk, **kwargs):
        return self.client.request('GET', format_url(self.BASE_URL) + "{}/".format(pk), **kwargs).json()

    def post(self, obj, **kwargs):
        return self.client.request('POST', format_url(self.BASE_URL), json=obj, **kwargs).json()

    def patch(self, pk, obj, **kwargs):
        return self.client.request('PATCH', format_url(self.BASE_URL) + "{}/".format(pk), json=obj, **kwargs).json()

    def delete(self, pk, **kwargs):
        return self.client.request('DELETE', format_url(self.BASE_URL) + "{}/".format(pk), **kwargs)

    def put(self, pk, obj, **kwargs):
        return self.client.request('PUT', format_url(self.BASE_URL) + "{}/".format(pk), json=obj, **kwargs).json()

    def move(self, pk, location, **kwargs):
        return self.client.request('PUT', format_url(self.BASE_URL) + "{}/move/".format(pk), json={
            "to": location
        }, **kwargs).json()

class Contact(CaseObject):
    BASE_URL = 'userforms/contacts/'

    def file_upload(self, pk, file, **kwargs):
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/uploadfile/'.format(pk), files=file, **kwargs).json()

    def add_user_form(self, pk, template, party_name='', form_number='', tags=[], **kwargs):
        obj = {
            "formtemplate_id": template,
            "party_name": party_name,
            "form_number": form_number,
            "tags": tags
        }
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/userforms/'.format(pk), json=obj, **kwargs).json()

    def send_invite(self, pk, message_text, **kwargs):
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/sendinvite/'.format(pk), json={"message_text": message_text}, **kwargs).json()

    #downloadFile

class UserForm(CaseObject):
    BASE_URL = 'userforms/userforms/'

    def resend_esign(self, pk, **kwargs):
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/resendesign/'.format(pk), **kwargs).json()

    def save_answer(self, pk, answer, **kwargs):
        return self.client.request('PUT', format_url(self.BASE_URL) + '{}/answer/'.format(pk), json=answer, **kwargs).json()

    def set_answer_status(self, pk, question, fieldtype, listId = None, status = None, **kwargs):
        struct = {
            "client_id": None,
            "fieldtype_id": fieldtype,
            "list_id": listId,
            "question_id": question,
            "status": status
        }
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/answerstatus/'.format(pk), json=struct, **kwargs).json()

    def drop_lists(self, pk):
        answer_dict = self.get_answers(pk)
        if "answerlists" in answer_dict and len(answer_dict['answerlists']) > 0:
            for key in answer_dict["answers"]:
                if key.count("-") == 2:
                    answerobj = None
                    if "text" in answer_dict["answers"][key]:
                        answerobj = ""
                    elif "options" in answer_dict["answers"][key]:
                        answerobj = []
                    elif "year" in answer_dict["answers"][key]:
                        answerobj = {
                            "year": None,
                            "month": None,
                            "day": None
                        }
                    
                    self.save_answer(pk, {
                        "fieldtype_id": key.split("-")[1],
                        "question_id": key.split("-")[0],
                        "list_id": key.split("-")[2],
                        "client_id": None,
                        "answer": answerobj
                    })
            for listobj in answer_dict["answerlists"]:
                question_id = listobj
                for listpart in answer_dict["answerlists"][listobj]:
                    deleteobject = {
                        "list_id": listpart,
                        "question_id": question_id
                    }
                    self.client.request('DELETE', format_url(self.BASE_URL) + '{}/deleterow/'.format(pk), json=deleteobject).json()
        else:
            pass

    def bulk_answer(self, pk, answer_key, options=None):
        map_list = {}
        for key in answer_key:
            try:
                answer = None
                clean_key = key.replace("L:", "").split(':')[1] if ':' in key.replace("L:", "") else key.replace("L:", "")
                if answer_key[key] is "":
                    continue
                if answer_key[key] is None:
                    continue
                question_id = clean_key.split("-")[0]
                fieldtype_id = clean_key.split("-")[1]
                list_uuid = None
                if "L:" in key:
                    if clean_key.split("-")[2]:
                        if "key:{}".format(clean_key.split("-")[2]) in map_list:
                            list_uuid = map_list["key:{}".format(clean_key.split("-")[2])]
                        else:
                            import uuid
                            map_list["key:{}".format(clean_key.split("-")[2])] = uuid.uuid4()
                            list_uuid = map_list["key:{}".format(clean_key.split("-")[2])]
                if "D:" in key:
                    if "/" in answer_key[key]:
                        answer = {
                            'month': int(answer_key[key].split('/')[0]),
                            'day': int(answer_key[key].split('/')[1]),
                            'year': int(answer_key[key].split('/')[2])
                        }
                    else:
                        answer = {
                            'month': None,
                            'day': None,
                            'year': int(answer_key[key])
                        }
                elif "O:" in key:
                    if fieldtype_id in options:
                        option_list = options[fieldtype_id]
                        for option in option_list['options']:
                            if option['text'] == answer_key[key]:
                                answer = option['id']
                    else:
                        raise Exception("Can't lookup answer for option")
                elif "C:" in key:
                    if fieldtype_id in options:
                        option_list = options[fieldtype_id]
                        if ";" in answer_key[key]:
                            answ_arr = answer_key[key].split(';')
                            answer = []
                            for answerstr in answ_arr:
                                optFound = False
                                for option in option_list['options']:
                                    if option['text'] == answerstr:
                                        optFound = True
                                        answer.append(option['id'])
                                if optFound == False:
                                    print("Warning: One or more option in import could not be found. Skipped {}!".format(answer_key[key]))
                                    answer = []
                        else:
                            optFound = False
                            for option in option_list['options']:
                                if option['text'] == answer_key[key]:
                                    optFound = True
                                    answer = [option['id']]
                            if optFound == False:
                                print("Warning: Option {} could not be found. Skipped!".format(answer_key[key]))
                                answer = []
                    else:
                        raise Exception("Can't lookup answer for option")
                else:
                    answer = answer_key[key]
                
                self.save_answer(pk, {
                    "fieldtype_clid": fieldtype_id,
                    "question_clid": question_id,
                    "list_id": None,
                    "client_id": str(list_uuid) if list_uuid else None,
                    "answer": answer
                })
            except:
                print("Error: Failed to save an answer; Skipping {} - {}".format(answer_key[key], key))

    def save_file_answer(self, pk, file, **kwargs):
        return self.client.request('PUT', format_url(self.BASE_URL) + '{}/answer/'.format(pk), files=file, **kwargs).json()

    def downloadFileAnswer(self, pk, fieldtype, question, path, list_id=None, **kwargs):
        with self.client.request('GET',
                          format_url('userforms/userforms/{}/download/'.format(
                              pk
                          )),
                          params={
                              'fieldtype_id': question,
                              'question_id': fieldtype,
                              'list_id': list_id
                          },
                          stream=True) as response:
            with open(path, 'wb') as fp:
                shutil.copyfileobj(response.raw, fp)

    #deleteRow

    #changeAnswerStatus

    #getNotes

    def get_esigns(self, pk, **kwargs):
        return self.client.request('GET', format_url(self.BASE_URL) + '{}/esign/'.format(pk), **kwargs).json()

    def get_activity(self, pk, **kwargs):
        return self.client.request('GET', format_url(self.BASE_URL) + '{}/activity/'.format(pk), **kwargs).json()

    def get_answers(self, pk, **kwargs):
        return self.client.request('GET', format_url(self.BASE_URL) + '{}/answers/'.format(pk), **kwargs).json()

    #downloadEsign

    #addNote

    #downloadPdf

    #downloadCsv

class BulkMail(CaseObject):
    BASE_URL = 'notifications/to-client/'

    def send(self, pk, **kwargs):
        return self.client.request('POST', format_url(self.BASE_URL) + '{}/send/'.format(pk), **kwargs).json()

class EmailProblems(CaseObject):
    BASE_URL = 'notifications/problems/'

    #downloadCsv

class Section(CaseObject):
    BASE_URL = 'forms/sections/'

class Question(CaseObject):
    BASE_URL = 'forms/questions/'

class Paragraph(CaseObject):
    BASE_URL = 'forms/paragraphs/'

class Esignature(CaseObject):
    BASE_URL = 'forms/esignature/'

class OptionList(CaseObject):
    BASE_URL = 'forms/optionlists/'

    # addOptions

class FieldType(CaseObject):
    BASE_URL = 'forms/fieldtypes/'

    #named

class FormTemplate(CaseObject):
    BASE_URL = 'forms/templates/'

    def get_option_array(self, pk):
        id_array = {}
        template = self.get(pk)

        def PARSE_COMPLX_FT(question, subfieldtype):
            ft_arr = {}
            for part in subfieldtype:
                if part['option_list']:
                    ol_client = OptionList(self.client)
                    option_list = ol_client.get(part['option_list'])
                    ft_arr.update({
                        part['clid']: option_list
                    })
            return ft_arr

        def PARSE_QUESTION(question):
            if question['fieldtype']['atomic_type']:
                if question['fieldtype']['option_list_object']:
                    return {
                        question['fieldtype']['clid']: question['fieldtype']['option_list_object']
                    }
                return {}
            else:
                return PARSE_COMPLX_FT(question, question['fieldtype']['subfieldtypes'])

        def PARSE_SECTION(section):
            sec_id_array = {}
            for part in section['parts']:
                if part['part_type'] == "q" and part['archived'] == False:
                    sec_id_array.update(PARSE_QUESTION(part))
                elif part['part_type'] == "s" and part['archived'] == False:
                    sec_id_array.update(PARSE_SECTION(part))
            return sec_id_array

        for root in template['root_parts']:
            if root['part_type'] == "s" and root['archived'] == False:
                id_array.update(PARSE_SECTION(root))
        return id_array

    def import_form(self, json):
        def CREATE_TEMPLATE(template):
            template_client = FormTemplate(self.client)
            createdTemplate = template_client.post({
                'name': template['name'],
                'header_text': template['header_text'],
                'submission_fill_blank': template['submission_prop']['fill_blanks'],
                'submission_min_rows': template['submission_prop']['hide_blank_rows']
            })
            print('[DONE] Template `{}` Created!'.format(createdTemplate['name']))
            CREATE_ROOT_PARTS(template['parts'], createdTemplate['id'])

        def CREATE_ROOT_PARTS(root_parts, templateId):
            for object in root_parts:
                if object['type'] == "paragraph":
                    print('[WAIT] Creating Paragraph~')
                    CREATE_PARAGRAPH(object, templateId)
                    print('[DONE] Created Paragraph!')
                elif object['type'] == "section":
                    print('[WAIT] Creating Section `{}`~'.format(object['text']))
                    CREATE_SECTION(object, templateId)
                    print('[DONE] Created Section `{}`!'.format(object['text']))
                else:
                    throw("ERROR: ILLEGAL ROOT PART.")

        def CREATE_PART(parts, templateId, sectionId=None):
            if parts['type'] == "paragraph":
                print('[WAIT] Creating Paragraph~')
                CREATE_PARAGRAPH(parts, templateId, sectionId)
                print('[DONE] Created Paragraph!')
            elif parts['type'] == "section":
                print('[WAIT] Creating Section `{}`~'.format(parts['text']))
                CREATE_SECTION(parts, templateId, sectionId)
                print('[DONE] Created Section `{}`!'.format(parts['text']))
            elif parts['type'] == "question":
                print('[WAIT] Creating Question `{}`~'.format(parts['text']))
                CREATE_QUESTION(parts, templateId, sectionId)
                print('[DONE] Created Question `{}`!'.format(parts['text']))
            elif parts['type'] == "esign":
                print('[WAIT] Creating Esign `{}`~'.format(parts['text']))
                CREATE_ESIGN(parts, templateId, sectionId)
                print('[DONE] Created Esign `{}`!'.format(parts['text']))
            else:
                raise Exception("ERROR: ILLEGAL ROOT PART.")

        def CREATE_QUESTION(question, templateId, sectionId=None):
            question_client = Question(self.client)
            print(question['clid'])
            fieldtype = {}
            if 'fieldtype' in question and 'atomic_type' in question['fieldtype']:
                if question['fieldtype']['atomic_type'] == "text":
                    fieldtype = CREATE_BASIC_FIELDTYPE('text', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "textarea":
                    fieldtype = CREATE_BASIC_FIELDTYPE('textarea', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "date":
                    fieldtype = CREATE_BASIC_FIELDTYPE('date', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "harddate":
                    fieldtype = CREATE_BASIC_FIELDTYPE('harddate', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "number":
                    fieldtype = CREATE_BASIC_FIELDTYPE('number', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "currency":
                    fieldtype = CREATE_BASIC_FIELDTYPE('currency', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "file":
                    fieldtype = CREATE_BASIC_FIELDTYPE('file', question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "radio":
                    fieldtype = CREATE_OPTION_FIELDTYPE('radio', question['fieldtype']['options'], question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "checkbox":
                    fieldtype = CREATE_OPTION_FIELDTYPE('checkbox', question['fieldtype']['options'], question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                elif question['fieldtype']['atomic_type'] == "dropdown":
                    fieldtype = CREATE_OPTION_FIELDTYPE('dropdown', question['fieldtype']['options'], question['fieldtype']['clid'], question['fieldtype']['required'] if 'required' in question['fieldtype'] else False)
                question_object = {
                    'fieldtype': {},
                    'fieldtype_id': fieldtype['id'],
                    'is_list': False,
                    'min_rows': 1,
                    'number': question['number'] if 'number' in question else None,
                    'part_type': 'q',
                    'section': sectionId,
                    'template': templateId,
                    'text': question['text'] if 'text' in question else None,
                    'archived': question['archived'] if 'archived' in question else False,
                    'clid': question['clid'] if 'clid' in question else None,
                    'required': question['required'] if 'required' in question else False
                }
                question_result = question_client.post(question_object)
            elif 'fieldtype' in question and 'subfieldtypes' in question['fieldtype']:
                fieldtype = CREATE_COMPLEX_FIELDTYPE(question['fieldtype']['subfieldtypes'], question['fieldtype']['clid'])
                question_client.post({
                    'fieldtype': {},
                    'fieldtype_id': fieldtype['id'],
                    'is_list': question['is_list'] if 'is_list' in question else False,
                    'is_list_table': question['is_list_table'] if 'is_list_table' in question else False,
                    'min_rows': question['min_rows'] if 'min_rows' in question else 1,
                    'number': question['number'] if 'number' in question else None,
                    'part_type': 'q',
                    'section': sectionId,
                    'template': templateId,
                    'text': question['text'] if 'text' in question else None,
                    'archived': question['archived'] if 'archived' in question else False,
                    'clid': question['clid'] if 'clid' in question else None,
                    'required': question['required'] if 'required' in question else False
                })

        def CREATE_BASIC_FIELDTYPE(fieldType, clid=None, required=False):
            fieldtype_client = FieldType(self.client)
            print('[WAIT] Creating New FieldType `{}`~'.format(fieldType))
            return fieldtype_client.post({
                'atomic_type': fieldType,
                'option_list': None,
                'subfieldtypes': [],
                'clid': clid,
                'required': required
            })

        def CREATE_COMPLEX_FIELDTYPE(subFieldTypes, clid=None, required=False):
            fieldtype_client = FieldType(self.client)
            optionlist_client = OptionList(self.client)
            print('[WAIT] Creating New Complex FieldType~')
            subfieldarray = []
            for subfield in subFieldTypes:
                appendingArray = {
                    'atomic_type': subfield['atomic_type'],
                    'id': None,
                    'text': subfield['text'] if 'text' in subfield else None,
                    'clid': subfield['clid'] if 'clid' in subfield else None,
                    'required': subfield['required'] if 'required' in subfield else False
                }
                if 'options' in subfield:
                    option_list = optionlist_client.post({
                        'id': None,
                        'options': subfield['options']
                    })
                    appendingArray['option_list'] = option_list['id']
                subfieldarray.append(appendingArray)
            return fieldtype_client.post({
                'atomic_type': None,
                'option_list': None,
                'subfieldtypes': subfieldarray,
                'clid': clid,
                'required': required
            })

        def CREATE_OPTION_FIELDTYPE(fieldType, optionsToCreate, clid=None, required=False):
            fieldtype_client = FieldType(self.client)
            optionlist_client = OptionList(self.client)
            print('[WAIT] Creating New Select FieldType `{}`~'.format(fieldType))
            option_list = optionlist_client.post({
                'id': None,
                'options': optionsToCreate
            })
            return fieldtype_client.post({
                'atomic_type': fieldType,
                'option_list': option_list['id'],
                'subfieldtypes': [],
                'clid': clid,
                'required': required
            })

        def CREATE_PARAGRAPH(paragraph, templateId, sectionId=None):
            paragraph_client = Paragraph(self.client)
            paragraph_object = {
                'template': templateId,
                'part_type': 'p',
                'text': paragraph['text'],
                'archived': paragraph['archived'],
                'clid': paragraph['clid'] if 'clid' in paragraph else None
            }
            if sectionId is not None:
                paragraph_object['section'] = sectionId
            paragraph_client.post(paragraph_object)

        def CREATE_ESIGN(esign, templateId, sectionId=None):
            esign_client = Esignature(self.client)
            esign_object = {
                'template': templateId,
                'part_type': 'e',
                'text': esign['text'],
                'archived': esign['archived']
            }
            if sectionId is not None:
                esign_object['section'] = sectionId
            esign_client.post(esign_object)

        def CREATE_SECTION(section, templateId, sectionId=None):
            section_client = Section(self.client)
            print(section['clid'])
            section_object = {
                'template': templateId,
                'part_type': 's',
                'text': section['text'] if 'text' in section else None,
                'number': section['number'] if 'number' in section else None,
                'archived': section['archived'] if 'archived' in section else False,
                'clid': section['clid'] if 'clid' in section else None
            }
            if sectionId is not None:
                section_object['section'] = sectionId
            createdSection = section_client.post(section_object)
            for subsection in section['parts']:
                CREATE_PART(subsection, templateId, createdSection['id'])

        CREATE_TEMPLATE(json)

class Reports(CaseObject):
    BASE_URL = 'reports/reports/'

    #downloadReport

class Users(CaseObject):
    BASE_URL = 'users/users/'

    #resetPassword

class SuperOrgs(CaseObject):
    BASE_URL = 'users/admin-orgs/'

    def create_org(self, subdomain, name, **kwargs):
        obj = {
            "name": name,
            "subdomain": subdomain,
            "primary_color": "#4A90E2",
            "secondary_color": "#4A90E2",
        }
        return self.client.request('POST', format_url(self.BASE_URL), json=obj, **kwargs).json()

class SuperUsers(CaseObject):
    BASE_URL = 'users/admin-users/'

    def create_user(self, org, fname, lname, password, email, username, admin, **kwargs):
        obj = {
            "email": email,
            "username": username,
            "first_name": fname,
            "last_name": lname,
            "org": org,
            "password": password,
            "contacttag_subscriptions": [],
            "userformtag_subscriptions": [],
            "is_org_admin": admin
        }
        return self.client.request('POST', format_url(self.BASE_URL), json=obj, **kwargs).json()


class ClientHelper(Client):
    def __init__(self, token=None, parser=None, args=None):
        self.session = Session()
        if token:
            self.token = token
        else:
            if parser is None:
                parser = argparse.ArgumentParser(description='CaseLocker Python Library')
            subgroup = parser.add_argument_group("Authentication", "Authenticating with your CaseLocker Installation")
            subgroup.add_argument("--s", type=str, help="Your CaseLocker Domain and Subdomain Name (https://[DOMAIN]/)")
            subgroup.add_argument("--u", type=str, help="Your CaseLocker Username")
            subgroup.add_argument("--p", action="store_true", default=False, help="Prompt for Password")
            subgroup.add_argument("--password", type=str, help="Your CaseLocker Password; NOT RECOMMENDED (Commandline Passthrough is Insecure)")
            subgroup.add_argument("--debug", action="store_true", default=False, help="Debug Mode (Localhost Instance Testing)")
            subgroup.add_argument("--log", default=20, help="Specify log level (10 - Debug; 20 - Info [Default]; 30 - Warning; 40 - Error; 50 - Critical)")
            subgroup.add_argument("--port", type=int, default=8000, help="Localhost Port (Default: 8000)")
            self.args = parser.parse_args()

    def authenticate(self, DOMAIN=None, USERNAME=None, PASSWORD=None):
        if self.args.debug:
            os.environ['DEBUG'] = "TRUE"
            os.environ['DEBUG_PORT'] = "{}".format(self.args.port)
        else:
            os.environ['DEBUG'] = ""
        logging.getLogger().setLevel(self.args.log)
        if len(sys.argv) > 1:
            if self.args.s or self.args.u or self.args.p:
                if self.args.s:
                    DOMAIN = self.args.s
                else:
                    logging.error("Subdomain name not provided (--s SUBDOMAIN)")
                    sys.exit(1)
                if self.args.u:
                    USERNAME = self.args.u
                else:
                    logging.error("Username not provided (--u USERNAME)")
                    sys.exit(1)
                if self.args.password:
                    logging.warning("Command line password passthrough is insecure. RECOMMENDED passthrough env variable CASELOCKER_PASSWORD")
                    PASSWORD = self.args.password
                else:
                    if os.environ.get('CASELOCKER_PASSWORD'):
                        PASSWORD = os.environ.get('CASELOCKER_PASSWORD')
                    elif self.args.p:
                        PASSWORD = getpass.getpass(prompt="[INPT] CaseLocker Password for {}@{}: ".format(USERNAME, DOMAIN), stream=None)
                        if PASSWORD is None or PASSWORD is "":
                            logging.error("Password cannot be empty")
                            sys.exit(1)
                    else:
                        logging.error("Password/prompt not provided (--p OR --password PASSWORD OR env var CASELOCKER_PASSWORD)")
                        sys.exit(1)
        super(ClientHelper, self).authenticate(DOMAIN, USERNAME, PASSWORD)
