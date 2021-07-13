from tkinter import *
import configparser
import imdb
ia = imdb.IMDb()

#Will  display search movie window
class render_search_movie_window:
    def __init__(self):
        self.search_movie_window = Tk()
        self.search_movie_window.resizable(False, False)
        self.search_movie_window.title("search movie by name")
        self.search_movie_window.geometry("800x500+120+120")
        self.search_movie_window.config(bg='white')

        self.line_frame = Frame(self.search_movie_window, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0, y=80)
        self.design_frame = Frame(self.search_movie_window, width=1000,height=70,bg="#E41752")
        self.design_frame.grid(row=0, column=0)

        # movie name input box
        self.movie_name_input = Text(self.search_movie_window, height=1, width=20)
        self.movie_name_input.place(x=300,y=30)

        # label
        self.enter_msg = Label(self.search_movie_window, text="enter movie name",bg="#E41752")
        self.enter_msg.place(x=190, y=30)

        # search button
        self.search_button = Button(self.search_movie_window, text="search", fg='black', bg='#b2babb', height=2, width=15,command=lambda:self.get_movie_by_name())
        self.search_button.place(x=500, y=22)

        #back button
        self.back_button=Button(self.search_movie_window, text="back", fg='black', bg='#E41752',bd=0,height=4, width=15,command=lambda:self.destroy_window())
        self.back_button.place(x=0, y=0)
        self.search_movie_window.mainloop()

    def destroy_window(self):
        self.search_movie_window.destroy()
        render_main_window()

    def get_movie_from_input_box(self):
        name=self.movie_name_input.get(1.0,"end-1c")
        return name

    def get_movie_by_name(self):

        global genre,director
        name=self.get_movie_from_input_box()
        raw_movie_res = ia.search_movie(name, results=1)

        #get movie id from name
        m_id = raw_movie_res[0].movieID

        #get movie instance by id
        movie = ia.get_movie(m_id)

        #get director info
        directors_list = []
        for director in movie['directors']:
            directors_list.append(director['name'])
            print(directors_list)

        #get genre info
        genre_list = []
        for genre in movie['genres']:
            genre_list.append(genre)
            print(genre_list)

        actors_list=[]
        for actor in movie['cast']:
            actors_list.append(actor['name'])

        data=f"movie name :{name}\ndirectors: {directors_list}\nmovie type: {genre_list}\nactors : {actors_list[:3]}"
        print(data)

        # show movie data
        self.display_movie_details = Label(self.search_movie_window,font=("Helvetica","15"),text=data,bg="white",wraplengt=800,justify=LEFT)
        self.display_movie_details.place(x=0, y=90)

#will display search by genre window
class render_genre_movie_window:
    def __init__(self):
        self.search_movie_by_genre_window = Tk()
        self.search_movie_by_genre_window.resizable(False, False)
        self.search_movie_by_genre_window.title("search movie by genres")
        self.search_movie_by_genre_window.geometry("800x500+120+120")
        self.search_movie_by_genre_window.config(bg='white')

        self.line_frame = Frame(self.search_movie_by_genre_window, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0, y=80)
        self.design_frame = Frame(self.search_movie_by_genre_window, width=1000,height=70,bg="#E41752")
        self.design_frame.grid(row=0, column=0)

        # movie name input box
        self.movie_name_input = Text(self.search_movie_by_genre_window, height=1, width=20)
        self.movie_name_input.place(x=300,y=30)

        # label
        self.enter_msg = Label(self.search_movie_by_genre_window, text="enter movie type",bg="#E41752")
        self.enter_msg.place(x=190, y=30)

        # search button
        self.search_button = Button(self.search_movie_by_genre_window, text="search", fg='black', bg='#b2babb', height=2, width=15,command=lambda:self.get_movie_by_genres())
        self.search_button.place(x=500, y=22)

        #back button
        self.back_button=Button(self.search_movie_by_genre_window, text="back", fg='black', bg='#E41752',bd=0,height=4, width=15,command=lambda:self.destroy_window())
        self.back_button.place(x=0, y=0)
        self.search_movie_by_genre_window.mainloop()

    def destroy_window(self):
        self.search_movie_by_genre_window.destroy()
        render_main_window()

    def get_type_from_input_box(self):
        name=self.movie_name_input.get(1.0,"end-1c")
        return name

    def get_movie_by_genres(self):
        t_result = ia.search_keyword(self.get_type_from_input_box())
        print(t_result)

        #data=f"movie name :{name}\ndirectors: {directors_list}\nmovie type: {genre_list}\nactors : {actors_list[:3]}"
        #print(data)

        # show movie data
        self.display_movie_details = Label(self.search_movie_by_genre_window,font=("Helvetica","15"),text="",bg="white")
        self.display_movie_details.place(x=190, y=110)
#will display search movie by actor window
class render_actor_movie_window:
    def __init__(self):
        self.search_movie_by_actor_window = Tk()
        self.search_movie_by_actor_window.resizable(False, False)
        self.search_movie_by_actor_window.title("search movie by actors")
        self.search_movie_by_actor_window.geometry("800x500+120+120")
        self.search_movie_by_actor_window.config(bg='white')

        self.line_frame = Frame(self.search_movie_by_actor_window, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0, y=80)
        self.design_frame = Frame(self.search_movie_by_actor_window, width=1000,height=70,bg="#E41752")
        self.design_frame.place(x=0,y=0)

        # movie name input box
        self.movie_name_input = Text(self.search_movie_by_actor_window, height=1, width=20)
        self.movie_name_input.place(x=300,y=30)

        # label
        self.enter_msg = Label(self.search_movie_by_actor_window, text="enter actor name",bg="#E41752")
        self.enter_msg.place(x=190, y=30)

        # search button
        self.search_button = Button(self.search_movie_by_actor_window, text="search", fg='black', bg='#b2babb', height=2, width=15,command=lambda:self.get_movie_by_actor())
        self.search_button.place(x=500, y=22)

        #back button
        self.back_button=Button(self.search_movie_by_actor_window, text="back", fg='black', bg='#E41752',bd=0,height=4, width=15,command=lambda:self.destroy_window())
        self.back_button.place(x=0, y=0)
        self.search_movie_by_actor_window.mainloop()

    def destroy_window(self):
        self.search_movie_by_actor_window.destroy()
        render_main_window()

    def get_actor_from_input_box(self):
        name=self.movie_name_input.get(1.0,"end-1c")
        return name

    def get_movie_by_actor(self):
        movie_list = []
        global genre, director, actor_id
        name = self.get_actor_from_input_box()

        raw_actor_res = ia.search_person(name)
        actor_id = raw_actor_res[0].personID

        print(actor_id)
        actor_res = ia.get_person_filmography(actor_id)
        print(actor_res)
        try :
            movie = actor_res['data']['filmography']['actress']
        except:
            movie = actor_res['data']['filmography']['actor']
        print(movie)
        for i in movie:
            movie_list.append(i['title'])

        print(movie_list)
        data = f"movies acted by {name}\n\n{movie_list}"
        print(data)

        # show movie data
        self.display_movie_details = Label(self.search_movie_by_actor_window, text=data,font=("Helvetica", "15"),wraplengt=800,justify=LEFT,bg="white")
        #self.display_movie_details.insert('end', data)
        self.display_movie_details.place(x=0, y=90)
#will display search movie by rating window
class render_rating_movie_window:
    def __init__(self):
        self.search_movie_by_rating_window = Tk()
        self.search_movie_by_rating_window.resizable(False, False)
        self.search_movie_by_rating_window.title("search movie by rating")
        self.search_movie_by_rating_window.geometry("800x500+120+120")
        self.search_movie_by_rating_window.config(bg='white')

        self.line_frame = Frame(self.search_movie_by_rating_window, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0, y=80)
        self.design_frame = Frame(self.search_movie_by_rating_window, width=1000,height=70,bg="#E41752")
        self.design_frame.grid(row=0, column=0)

        # movie name input box
        self.movie_name_input = Text(self.search_movie_by_rating_window, height=1, width=20)
        self.movie_name_input.place(x=300,y=30)

        # label
        self.enter_msg = Label(self.search_movie_by_rating_window, text="enter movie rating limint",bg="#E41752")
        self.enter_msg.place(x=190, y=30)

        # search button
        self.search_button = Button(self.search_movie_by_rating_window, text="search", fg='black', bg='#b2babb', height=2, width=15,command=lambda:self.get_movie_by_actor())
        self.search_button.place(x=500, y=22)

        #back button
        self.back_button=Button(self.search_movie_by_rating_window, text="back", fg='black', bg='#E41752',bd=0,height=4, width=15,command=lambda:self.destroy_window())
        self.back_button.place(x=0, y=0)
        self.search_movie_by_rating_window.mainloop()

    def destroy_window(self):
        self.search_movie_by_rating_window.destroy()
        render_main_window()

    def get_actor_from_input_box(self):
        name=self.movie_name_input.get(1.0,"end-1c")
        return name

    def get_movie_by_actor(self):
        global genre,director
        name=self.get_actor_from_input_box()
        raw_movie_res = ia.search_movie(name, results=1)

        #get movie id from name
        m_id = raw_movie_res[0].movieID

        #get movie instance by id
        movie = ia.get_movie(m_id)

        #get director info
        directors_list = []
        for director in movie['directors']:
            directors_list.append(director['name'])
            print(directors_list)

        #get genre info
        genre_list = []
        for genre in movie['genres']:
            genre_list.append(genre)
            print(genre_list)

        actors_list=[]
        for actor in movie['cast']:
            actors_list.append(actor['name'])

        data=f"movie name :{name}\ndirectors: {directors_list}\nmovie type: {genre_list}\nactors : {actors_list[:3]}"
        print(data)

        # show movie data
        self.display_movie_details = Label(self.search_movie_by_rating_window,font=("Helvetica","15"),text=data,bg="white")
        self.display_movie_details.place(x=190, y=110)

#movie prediction window
class render_predict_movie_window:
    def __init__(self):
        self.predict_movie = Tk()
        self.predict_movie.resizable(False, False)
        self.predict_movie.title("movie prediction")
        self.predict_movie.geometry("800x500+120+120")
        self.predict_movie.config(bg='white')

        self.line_frame = Frame(self.predict_movie, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0, y=80)
        self.design_frame = Frame(self.predict_movie, width=1000,height=70,bg="#E41752")
        self.design_frame.grid(row=0, column=0)

        # label
        self.enter_msg = Label(self.predict_movie, text="choose your interest",bg="white")
        self.enter_msg.place(x=100, y=100)

        # predict button
        self.predict_button = Button(self.predict_movie, text="predict", fg='black', bg='#b2babb', height=2, width=15,command=lambda:self.predict_using_ds())
        self.predict_button.place(x=500, y=422)

        self.action = IntVar()
        self.adventure = IntVar()
        self.fantasy = IntVar()
        self.Science_Fiction = IntVar()
        self.drama = IntVar()
        self.Thriller = IntVar()
        self.Family = IntVar()
        self.comedy = IntVar()
        self.crime = IntVar()
        self.romance = IntVar()

        action_cb = Checkbutton(self.predict_movie, text="Action", variable=self.action, onvalue=1, bg="white",offvalue=0, height=1, width=10)
        action_cb.place(x=30, y=130)

        adventure_cb = Checkbutton(self.predict_movie, text="Adventure", variable=self.adventure, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        adventure_cb.place(x=38, y=170)

        fantasy_cb = Checkbutton(self.predict_movie, text="Fantasy", variable=self.fantasy, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        fantasy_cb.place(x=30, y=200)

        scifi_cb = Checkbutton(self.predict_movie, text="Science Fiction", variable=self.Science_Fiction, bg="white",onvalue=1, offvalue=0, height=1, width=10)
        scifi_cb.place(x=48, y=230)

        drama_cb = Checkbutton(self.predict_movie, text="drama", variable=self.drama, bg="white", onvalue=1, offvalue=0,height=1, width=10)
        drama_cb.place(x=25, y=270)
                                                    # ____________________________________#
        thriller_cb = Checkbutton(self.predict_movie, text="Thriller", variable=self.Thriller, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        thriller_cb.place(x=501, y=130)

        family_cb = Checkbutton(self.predict_movie, text="family", variable=self.Family, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        family_cb.place(x=500, y=170)

        comedy_cb = Checkbutton(self.predict_movie, text="comedy", variable=self.comedy, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        comedy_cb.place(x=505, y=200)

        crime_cb = Checkbutton(self.predict_movie, text="crime", variable=self.crime, bg="white", onvalue=1, offvalue=0,height=1, width=10)
        crime_cb.place(x=499, y=230)

        romance_cb = Checkbutton(self.predict_movie, text="romance", variable=self.romance, bg="white", onvalue=1,offvalue=0, height=1, width=10)
        romance_cb.place(x=505, y=270)

        #back button
        self.back_button=Button(self.predict_movie, text="back", fg='black', bg='#E41752',bd=0,height=4, width=15,command=lambda:self.destroy_window())
        self.back_button.place(x=0, y=0)

        self.predict_movie.mainloop()

    def predict_using_ds(self):
        self.user_choice=[]
        action=self.action.get()
        adventure=self.adventure.get()
        fantasy=self.fantasy.get()
        science_fiction=self.Science_Fiction.get()
        drama=self.drama.get()
        thriller=self.Thriller.get()
        family=self.Family.get()
        comedy=self.comedy.get()
        crime=self.crime.get()
        romance=self.romance.get()

        if action==1:
            self.user_choice.append("action")

        if adventure==1:
           self.user_choice.append("adventure")

        if fantasy==1:
            self.user_choice.append("fantasy")

        if science_fiction==1:
            self.user_choice.append("science Fiction")

        if drama==1:
            self.user_choice.append("drama")

        if thriller==1:
            self.user_choice.append("thriller")

        if family==1:
            self.user_choice.append("family")

        if comedy==1:
            self.user_choice.append("comedy")

        if crime==1:
            self.user_choice.append("crime")

        if romance==1:
            self.user_choice.append("romance")
        print(self.user_choice)

    def destroy_window(self):
        self.predict_using_ds()
        self.predict_movie.destroy()
        render_main_window()

#class to display main window
class render_main_window:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.resizable(False, False)
        self.main_window.title("movie recommendation system")
        self.main_window.geometry("800x500+120+120")
        self.main_window.config(bg='white')

        #design frame above the screen
        self.design_frame = Frame(self.main_window, width=1000, height=70, bg="#E41752")
        self.design_frame.grid(row=0, column=0)

        #line below the frame
        self.line_frame = Frame(self.main_window, width=1000, height=3, bg="#E41752")
        self.line_frame.place(x=0,y=80)

        #search_movie_by_name_button -> this will call destroy_window() method on trigger
        self.search_movie_button = Button(self.main_window, text="search movie by name", fg='white', bg='#E41752', height=5, width=20,command=lambda: self.movie_window_caller())
        self.search_movie_button.place(x=30, y=100)

        # search_movie_by_genres_button -> this will call destroy_window() method on trigger
        self.search_movie_by_genres_button = Button(self.main_window, text="search movie by genres", fg='white', bg='#E41752',height=5, width=20, command=lambda: self.genre_window_caller())
        self.search_movie_by_genres_button.place(x=230, y=100)

        # search_movie_by_actors_button -> this will call destroy_window() method on trigger
        self.search_movie_by_actors_button = Button(self.main_window, text="search movie by actors", fg='white', bg='#E41752',height=5, width=20, command=lambda: self.actor_window_caller())
        self.search_movie_by_actors_button.place(x=430, y=100)

        # search_movie_by_rating_button -> this will call destroy_window() method on trigger
        self.search_movie_by_actors_button = Button(self.main_window, text="search movie by rating", fg='white',bg='#E41752', height=5, width=20,command=lambda: self.rating_window_caller())
        self.search_movie_by_actors_button.place(x=620, y=100)

        # predict movie -> this will call destroy_window() method on trigger
        self.search_movie_by_actors_button = Button(self.main_window, text="predict movie", fg='white', bg='#E41752',height=5, width=48, command=lambda: self.predict_window_caller())
        self.search_movie_by_actors_button.place(x=230, y=230)
        self.main_window.mainloop()

    #this will destroy the present window and display the search_movie_window()
    def movie_window_caller(self):
        self.main_window.destroy()
        render_search_movie_window()

    def actor_window_caller(self):
        self.main_window.destroy()
        render_actor_movie_window()

    def genre_window_caller(self):
        self.main_window.destroy()
        render_genre_movie_window()

    def rating_window_caller(self):
        self.main_window.destroy()
        render_rating_movie_window()

    def predict_window_caller(self):
        self.main_window.destroy()
        render_predict_movie_window()

class render_survey_window:
    def __init__(self):
        self.c_file_handler=configparser.ConfigParser()
        print(self.c_file_handler.read('user_info.ini'))
        if self.c_file_handler.has_section('INFO'):
            print(self.c_file_handler.sections())
            print("not first time found these sections")
            render_main_window()

        else:
            self.survey_window = Tk()
            self.survey_window.resizable(False, False)
            self.survey_window.title("movie recommendation system user information")
            self.survey_window.geometry("800x500+120+120")
            self.survey_window.config(bg='white')

            # design frame above the screen
            self.design_frame = Frame(self.survey_window, width=1000, height=70, bg="#E41752")
            self.design_frame.grid(row=0, column=0)

            # label
            self.enter_msg = Label(self.survey_window,text="MOVIE RECOMMENDATION SYSTEM",font=("Helvetica", "32"), bg="#E41752")
            self.enter_msg.place(x=15, y=0)

            # line below the frame
            self.line_frame = Frame(self.survey_window, width=1000, height=3, bg="#E41752")

            # design bottom frame
            self.bottom_design_frame = Frame(self.survey_window, width=1000, height=45, bg="#E41752")
            self.bottom_design_frame.place(x=0, y=450)

            #next button
            self.search_movie_button = Button(self.survey_window, text="continue..",bd=0, fg='white', bg='#E41752',height=2, width=20, command=lambda: self.call_next_frame())
            self.search_movie_button.place(x=630, y=450)
            cpright="\u00A9"

            # label
            self.enter_msg = Label(self.survey_window, text=f"{cpright} Copyrights : Himmalay Devulapalli 190330057@klh.edu.in",font=("Helvetica","11"),bg="#E41752")
            self.enter_msg.place(x=50, y=460)

            self.survey_window.mainloop()

            self.c_file_handler.add_section("INFO")
            self.c_file_handler.add_section("USER_INTEREST")
            self.c_file_handler.set("INFO","isfirsttime","no")
            print("first time so i created it ")
            self.file_pointer = open('user_info.ini', 'w')
            self.c_file_handler.write(self.file_pointer)
            self.file_pointer.close()

    def call_next_frame(self):
        self.file_pointer = open('user_info.ini','w')
        self.c_file_handler.write(self.file_pointer)
        self.file_pointer.close()

        self.survey_window.destroy()
        render_main_window()

#call render_survey_window class to display survey window
render_survey_window()

