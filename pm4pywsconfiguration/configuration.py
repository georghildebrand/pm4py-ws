enable_upload = False
enable_download = False
enable_load_local_path = True
enable_session = False
upload_as_temporary = True
session_duration = 86400
enable_bpmn = False
md5_password_backend = True
md5_password_frontend = True
static_folder = '../webapp2/dist'
files_path = 'files'
error_log_path = files_path + '/error_log/pm4pyws.log'
sql3_databases_path = files_path + '/databases'
event_logs_path = files_path + '/event_logs'
event_log_db_path = sql3_databases_path + '/event_logs.db'
users_db_path = sql3_databases_path + '/users.db'
parquet_performance_setting1 = True