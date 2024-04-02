import glpi_api

URL = 'http://172.16.2.10/glpi/apirest.php/'
APPTOKEN = '4Le7MHVAaFmslbZufNsmfrRdmkHbZMA9mWTmg9vH'
USERTOKEN = 'YOURUSERTOKEN'

try:
    with glpi_api.connect(URL, APPTOKEN, USERTOKEN) as glpi:
        print(glpi.get_config())
except glpi_api.GLPIError as err:
    print(str(err))

glpi = glpi_api.GLPI(url=URL,
                     apptoken=APPTOKEN,
                     auth=('glpi', '%Avia407'))
