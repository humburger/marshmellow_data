"""
connects to DB, does sql query call, creates excel file from results
"""
# import the modules
from pymysql import*
import sys
import xlwt
import pandas.io.sql as sql

def mysql_to_excel(excel_name, sql_values, limit):
    
    # connect the mysql with the python
    con=connect(user="root",password="appropriate_password",host="localhost",database="dabasdati_lv")
    # read the data
    i = 1 # excel faila uzskaites skaitlis nosaukumā

    # limit = "10000" # excel faila limits normālai pārlasei
    # limit = "1000" # excel faila limits testam 

    id_value = "0"
    # id_value = "1717541"
    # id_value = "1143802"

    while (1): # excel datu izvilkumam
    # while (i<2): # for test
        try:
            sql.read_sql("drop view if exists data_to_excel;",con)
        # except: 
        except Exception as e:
            pass
            # print("Unknown error")
            # print(e)
        try:
            sql.read_sql("create view data_to_excel as " +
                    "SELECT d.id," +
                    "d.uid," +
                    "d.oid, " +
                    "d.timefrom, " +
                    "d.timetill, " +
                    "d.specie, " +
                    "d.amountmin, " +
                    "d.amountmax, " +
                    "d.statuss, " +
                    "d.gredzens, " +
                    "d.biotop, " +
                    "d.behaviour, " +
                    "d.identification_marks, " + 
                    "d.full_list, " +
                    "d.other_observer_name, " +
                    "d.data_type, " +
                    "d.notes, " +
                    "d.photo, " +
                    "d.mp3, " +
                    "d.credibility, " +
                    "d.sid, " +
                    "d.time, " +
                    "d.time_int, " +
                    "d.dimensions, " +
                    "d.zoomlevel, " +
                    "d.itemprotected, " +
                    "d.finish_status, " +
                    "d.unavailable, " +
                    "d.gis_time, " +
                    "d.interesting, " +
                    "d.interesting_comment, " +
                    "d.manual_coords, " +
                    "d.quadrant, " +
                    "d.input_source, " +
                    "d.uuid, " +
                    "d.quadrant_1x1, " +
                    "d.ba_form_id, " +
                    "d.ba_form_duration, " +
                    "d.ba_highest_level, " +
                    "d.forms_id, " +
                    "l.teksts as suga, " +
                    "(select lat.teksts from mushroom_pies lat where lat.valoda_id=10 and lat.atslega=s.value) as suga_latiniski," +
                    "s.value as sugas_identifikators, " +
                    "u.nick, " +
                    "concat(u.name,' ',u.surname) as user_name, " +
                    "y.teksts as statusa_apraksts, " +
                    "(SELECT group_concat(concat(g.x,':',g.y)) FROM candycrush_jummy as g WHERE g.oid=d.oid) as coords " +
                    ", cu.nick as changer_user_nick, concat(cu.name,' ',cu.surname) as changer_user_name " +
                    ", obc.credibility_id, obc.changed, obc.change_type_id, obc.old_value, obc.new_value, obc.old_text, obc.new_text " +	
                        "FROM mushroom_pies l, pineapple_jam_pancaces s, pineapples z, mushroom_pies y, strawberry_data d " +
                            "left join users u on u.id=d.uid " +
                            "left join observation_data_changes obc on d.id=obc.observation_id " +
                            "left join users cu on cu.id=obc.changer_user_id " +
                                "WHERE " +
                            "        d.id>" + id_value +
                            "		 AND s.id=d.specie " +
                            "        AND l.valoda_id=5 " +
                            "        AND l.atslega=s.value " +
                            "        AND d.specie IN " +
                            "(SELECT s.id FROM pineapple_jam_pancaces s " +                        
                                " where s.value IN (" + sql_values + ") )" +
                                
                    "AND d.finish_status = '1' " +
                    "AND d.statuss=z.id " +
                    "AND z.value=y.atslega " +
                    "AND y.valoda_id=5 " +
                    "AND d.credibility > '-1' " +
                    "order by d.id asc " +
                    "limit " + limit + ";",con)

        except Exception as e:
            pass
            # print("Unknown error")
            # print(e)
        # sys.exit()
        df = sql.read_sql("select * from data_to_excel;",con)

        # ja vairs nav datu ko atlasīt
        if df.empty == True:
            try:
                sql.read_sql("drop view if exists data_to_excel;",con)
            except:
                pass
            con.close()
            # print("con closed")
            break # GOES WITH WHILE LOOP

        df2 = sql.read_sql("select max(id) from data_to_excel;",con)   
        id_value_str = str(df2.loc[0]).split() 
        id_value = id_value_str[1]
        print(id_value)

        # export the data into the excel sheet
        df.to_excel(str(excel_name) + '_' + str(i) + '.xlsx', index=False, freeze_panes=(1,0))
        i = i + 1