class Innings:
    __current_over: int
    __current_ball: int
    __current_wicket: int
    __current_score: int

    def set_current_over(self, current_over: int):
        self.__current_over = current_over

    def set_current_ball(self, current_ball: int):
        self.__current_ball = current_ball

    def set_current_wicket(self, current_wicket:int):
        self.__current_wicket = current_wicket

    def set_current_score(self, current_score: int):
        self.__current_score = current_score

    def get_current_over(self):
        return self.__current_over

    def get_current_wicket(self):
        return self.__current_wicket

    def get_current_ball(self):
        return self.__current_ball

    def get_current_score(self):
        return self.__current_score
