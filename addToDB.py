import argparse
import os
import os.path
import commands

class SQLfileFinderAndAdder():
    def __init__(self, top_dir, db_name):
        self.top_dir = top_dir
        self.log_file_name = db_name + ".log"
        self.db_name = db_name
        if not os.path.isfile(self.log_file_name):
            create_logfile = open(self.log_file_name, 'w')
            create_logfile.close()
        
    def find_all_sql_files(self, top_dir):
        top_dir_content_relative_pathes = os.listdir(top_dir)

        def join_to_top_dir(rel_path):
            return os.path.join(top_dir, rel_path)

        top_dir_content_absolute_pathes = map(join_to_top_dir,
                                              top_dir_content_relative_pathes)
            
        sub_dirs = filter(os.path.isdir, top_dir_content_absolute_pathes)
        def issqlfile(path):
            return (path[-4:] == ".sql") and os.path.isfile(path)
        sql_files = filter(issqlfile, top_dir_content_absolute_pathes)

        for sub_dir in sub_dirs:
            sql_files = sql_files + self.find_all_sql_files(sub_dir)

        sql_files_abs_pathes = map(os.path.abspath, sql_files)
        return sql_files_abs_pathes

    def check_in_Logfile(self, paths):
        log_file = open(self.log_file_name, 'r')
        added_sql_files = log_file.readlines()
        def not_in_logfile(path):
            return not (path + '\n') in added_sql_files

        not_added_sqlfiles = filter(not_in_logfile, paths)
        log_file.close()
        return not_added_sqlfiles

    def add_to_DB_and_Logfile(self, app_name, paths):
        log_file = open(self.log_file_name, 'a')
        for path in paths:
            status = commands.getstatusoutput('%s "%s" < "%s"' %
                                              (app_name, self.db_name, path))
            if status[0] == 0:
                print "added %s" % path
                log_file.write(path + "\n")
            else:
                print ("%s not added to database %s and logfile %s" %
                       (path, self.db_name, self.log_file_name))
                print status[1]
        log_file.close()
    
def main():
    parser = argparse.ArgumentParser(description = 'Add to BIG database',
                                     epilog='Bye.')
    parser.add_argument('input_dir', action='store', nargs=1,
                        help='path/to/sql/files')
    parser.add_argument('db_name', action='store', nargs=1,
                        help='name of database')
    parser.add_argument('app', action='store', nargs=1,
                        help='application which will add sql to database')
    arg_data = vars(parser.parse_args(None))
    sql_file_finder = SQLfileFinderAndAdder(arg_data['input_dir'][0],
                                            arg_data['db_name'][0])
    all_sql_files = sql_file_finder.find_all_sql_files(sql_file_finder.top_dir)
    need_to_add_sqlfiles = sql_file_finder.check_in_Logfile(all_sql_files)
    print need_to_add_sqlfiles
    sql_file_finder.add_to_DB_and_Logfile(arg_data['app'][0], need_to_add_sqlfiles)
    
if __name__=='__main__':
    main()