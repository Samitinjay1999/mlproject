from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
  """
  params:
  take file_path as input.
  Returns:
  This function will returns the list of requiremants.
  """
  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readline()
    requirements = [req.replace('\,n','') for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
    
  return requirements


setup(
  name = 'mlproject',
  version='0.0.1',
  author='Samitinjay Mishra',
  author_email="samitinjay1999@gmail.com",
  packages=find_packages(),
  install_require=get_requirements('requirements.txt'),
)