"""
2016_playoff v.0.1

Inspired with Playoff round of Euro 2016.

Description:
This console software allows you to input results of the playoff matches and depending on it move teams through the playoff stages to the final
Current version limited and gives you possibility to define winner of the 1/4 and display 1/2 stage.

Instruction:
First input playoff round (currently only 1/4 is available)
Then input scores of the rival teams
"""

from time import*

quarter_final = [{"pair_1":{"team_1": {"name":"Portugal", "score":0},"team_2":{"name":"Poland", "score":0}}},
                 {"pair_2":{"team_1": {"name":"Wales", "score":0},"team_2":{"name":"Belgium", "score":0}}},
                 {"pair_3":{"team_1": {"name":"Germany", "score":0},"team_2":{"name":"Italy", "score":0}}},
                 {"pair_4":{"team_1": {"name":"France", "score":0},"team_2":{"name":"Iceland", "score":0}}}]

semi_final = [{"pair_1":{"team_1":{"name":"", "score":0}, "team_2":{"name":"", "score":0}}},
              {"pair_2":{"team_1":{"name":"", "score":0}, "team_2":{"name":"", "score":0}}}]

final = [{"team_1":{"name":"", "score":0}}, {"team_2":{"name", "score"}}]

stages_name = ["1/4", "1/2", "final"]

stages_dict_list = [quarter_final, semi_final, final]

next_stage = 0

#--------functions section--------


def match (current_stage): #defining pair winner, adding it to the next stage
        b=0
        for i in current_stage:
                sleep(.2)
                current_stage[b]["pair_"+str(b+1)]["team_1"]["score"]=input("How much "+current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]+" scores? ")
                sleep(.2)
                current_stage[b]["pair_"+str(b+1)]["team_2"]["score"]=input("How much "+current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]+" scores? ")
                if current_stage[b]["pair_"+str(b+1)]["team_1"]["score"]>current_stage[b]["pair_"+str(b+1)]["team_2"]["score"]:
                        sleep(.5)
                        print(current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]+" was qualified to Semifinal!\n")
                        if current_stage[b]==quarter_final[0]:
                                semi_final[0]["pair_1"]["team_1"]["name"]=current_stage[b]["pair_1"]["team_1"]["name"]
                        elif current_stage[b]==quarter_final[1]:
                                semi_final[0]["pair_1"]["team_2"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]
                        elif current_stage[b]==quarter_final[2]:
                                semi_final[1]["pair_2"]["team_1"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]
                        elif current_stage[b]==quarter_final[3]:
                                semi_final[1]["pair_2"]["team_2"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]
                        else:
                                print("WRONG")
                                                     
                else:
                        sleep(.5)
                        print(current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]+" was qualified to Semifinal!\n")
                        if current_stage[b]==quarter_final[0]:
                                semi_final[0]["pair_1"]["team_1"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]
                        elif current_stage[b]==quarter_final[1]:
                                semi_final[0]["pair_1"]["team_2"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]
                        elif current_stage[b]==quarter_final[2]:
                                semi_final[1]["pair_2"]["team_1"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]
                        elif current_stage[b]==quarter_final[3]:
                                semi_final[1]["pair_2"]["team_2"]["name"]=current_stage[b]["pair_"+str(b+1)]["team_2"]["name"]
                        else:
                                print("WRONG")
                b+=1
        print(next_stage(chosen_stage))
           

def choose_stage(): #choseing current stage
        global current_stage
        global chosen_stage
        while True:
                for i in stages_name: #list of stages
                        print(i)
                chosen_stage = input("Please chose current playoff round: ")       
                if chosen_stage == "1/4":
                        current_stage = quarter_final
                        break
                elif chosen_stage == "1/2":
                        current_stage = semi_final
                        break
                elif chosen_stage == "final":
                        current_stage = final
                        break
                else:
                        print("Please type stage as it listed below!")
                        sleep(.5)
                


def pairs_list(current_stage): #displaying list of pairs for current stage 
        b=0
        for i in current_stage:
                sleep(.5)
                print((b+1), current_stage[b]["pair_"+str(b+1)]["team_1"]["name"]+" VS "+current_stage[b]["pair_"+str(b+1)]["team_2"]["name"])
                b+=1
        
              
def next_stage(stage): #list of pairs for the next stage  
        global next_stage_name
        next_stage_index = stages_name.index(stage)
        if stage == "1/4":
                print("\nHere are pairs for ",stages_name[(next_stage_index)+1]," playoff round: \n")
                print(pairs_list(stages_dict_list[(next_stage_index)+1]))
        
                
                

def main(): #main function
        print ("EURO 2016")
        print("This is playoff round!" )
        print("")
        choose_stage()
        print("\nHere are pairs of ",chosen_stage," playoff round!")
        sleep(.5)
        pairs_list(current_stage)
        sleep(1)
        print("\nPlease input final results of the listed above matches: \n" )
        sleep(1)
        match(current_stage)
        
      

main()

