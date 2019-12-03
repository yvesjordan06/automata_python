class AFD:
    def __init__(self, alphabet, etats, etat_initial, etat_finaux, transition):
        ###try:
        self.alphabet = self.ajouter_alphabet(alphabet)
        self.etats = self.est_etat(etats)
        self.etat_initial = self.est_initial(etat_initial, self.etats)
        self.etat_finaux = self.est_final(etat_finaux, self.etats)
        self.transition = self.transistion(transition, self.alphabet, self.etats)

        ##except:
        # print("ERReur !!! entrez correctement les champs")

    def ajouter_alphabet(self, alphabet):
        """
        Verifie si l'alphabet est correct
        """
        temps = []
        if alphabet:
            for i in alphabet:
                if isinstance(i, str):
                    temps.append(i)
                else:
                    temps.append(str(i))
            return set(temps)
        else:
            print("erreur alphabet vide")
            return set()

    def est_etat(self, etats):
        # verifie le structure de l'etat envoyer
        temps = []
        if etats:
            if isinstance(etats, list) or isinstance(etats, tuple):
                for i in etats:
                    if isinstance(i, str):
                        temps.append(i)
                    else:
                        temps.append(str(i))
                return set(temps)
            else:
                if isinstance(etats, str):
                    return set(etats)
                else:
                    return set(str(etats))
        else:
            print(" erreur liste d'etats vide")

    def est_initial(self, etat_initial, etats):
        # verifie la conformité de l'etat initial
        # -verifie l'unicité de l'etat initial
        # verifie si c'est un string et si il appartient a la liste d'etat
        # verifie si en converstisant en string il appartient a la liste d'etat
        if etat_initial:
            if etats:
                if isinstance(etat_initial, list) or isinstance(etat_initial, tuple) or isinstance(etat_initial, set):
                    if len(etat_initial) > 1 or len(etat_initial) < 1:
                        print("un seul etat initial est autoriséé")
                    else:
                        if str(etat_initial[0]) in etats:
                            return str(etat_initial[0])
                        else:
                            print(etats, "ERREUR d'etat veuillez resseyer", etat_initial)
                elif isinstance(etat_initial, str) and etat_initial in etats:
                    return etat_initial
                elif str(etat_initial) in etats and isinstance(etat_initial, str) == 0:
                    return str(etat_initial)
                else:
                    print("erreur d'etats")
            else:
                print("veuillez entrer la liste d'etat")
        else:
            print("veillez entrez une etat initial")

    def est_final(self, etat_finaux, etats):
        temp = []
        err = []
        if etat_finaux:
            if etats:
                if isinstance(etat_finaux, list) or isinstance(etat_finaux, tuple):
                    for i in etat_finaux:
                        if isinstance(i, str):
                            if i in etats:
                                temp.append(i)
                            else:
                                err.append(i)
                        elif str(i) in etats:
                            temp.append(str(i))
                        else:
                            err.append(i)
                    if err:
                        print(err, "ces etats ne font pas parti des etats connus")
                    else:
                        return temp
                    return str(etat_finaux)
                else:
                    print(err, "ces etats ne font pas parti des etats connus")
            else:
                print("liste d'etat absent ")
        else:
            print("vous n'avez pas entrez d'etat final")

    def transistion(self, transition, alphabet, etats):
        temps = []
        if transition:
            if alphabet and etats:
                if len(transition) <= (len(alphabet) * len(etats)):
                    # print(transition)
                    for i in transition:
                        if isinstance(i, list) or isinstance(i, tuple):
                            if len(i) == 3:
                                if i[0] in etats and i[2] in etats:
                                    if i[1] in alphabet:
                                        temps.append(i)
                                    else:
                                        print(i[1], "n'est pas un symbole de notre alphabet")
                                else:
                                    if i[0] in etats:
                                        print(i[1], "ne fait pas parti des etats")
                                    else:
                                        print(i[0], "ne fait pas parti des etats")
                            else:
                                print(i, "transistion mal defini : trop d'element ou pas assez d'element")
                        else:
                            print("transistions mal defini")
                else:
                    print("ERREUR,trop de transistion defini")
                if temps:
                    for i in temps:
                        for j in temps:
                            if i[0] == j[0] and i[1] == j[1] and i[2] != j[2]:
                                print("impossible que ces transisition existe au meme moment i=", i, "j=", j)
                                choix = input("entrez \n 1 -pour supprimer i \n ou 2- pour j")
                                if choix == 1:
                                    temps.remove()
                                elif choix == 2:
                                    temps.remove(j)
                            else:
                                print('ok')
                    if temps:
                        return set(temps)
                    else:
                        print("pas de transition valide 1")
                        # return None
                else:
                    print("pas de transition valide 2")
                    # return None

            else:
                print("aphabet ou liste d'etat absents \n veuillez les definir")


        else:
            print("pas de transistion defini")

    def ajouter_symboles(self, alphabet, symbol):
        if alphabet:
            if isinstance(symbol, list) or isinstance(symbol, tuple):
                for i in symbol:
                    if isinstance(i, str):
                        alphabet.add(i)
                    else:
                        alphabet.add(str(i))
            else:
                if isinstance(symbol, str):
                    alphabet.add(symbol)
                else:
                    alphabet.add(str(symbol))

    '''def ajoute_etat(self, etat , final=False, initial=False):
            if self.etats:
                if isinstance(etat ,set )or isinstance(etat,list) :#or isinstance(etat,tuple):
                    for i in etat:
                        self.etats.add(self.est_etat(i))
                else:
                    self.etats.add(self.est_etat(etat))

                self.etats=self.est_etat(etat)
                if final:
                    self.est_final(etat, self.etats)
                elif initial:
                    self.est_initial(etat, self.etats)
                else:
                    pass'''

    def reconnaitre_mot(self, mot):
        # ca prend un mot ca verifie si il est reconnue par l'automate
        # si un caractere n'appartient pas ca retourne False
        # si une seule transistion ne correspond pas ca retourne FALSE
        #end = list()
        courant = self.etat_initial
        for i in mot:
            if i in self.alphabet:
                end = list()
                for j in self.transition:
                    if j[0] == courant and j[1] == i:
                        courant = j[2]
                        end = courant
            else:
                return False
        if end in self.etat_finaux:
            return True
        return False


if __name__ == '__main__':
    automate = AFD(['1', '0'], ['a', 'b'], 'a', ['b'],
                        [('a', '0', 'a'), ('a', '0', 'b'), ('b', '1', 'b'), ('b', '0', 'a')])
    print('Bienvenue sur l\'Automate de Makamte')
    print('Vous allez definir votre automate')
    longeur = int(input('Entrez-la longeur de votre alphabet : '))
    alphabet = list()
    for i in range(longeur):
        alphabet.append(input('Entrez l\'alphabet : '))
    longeur = int(input('Entrez-la longeur de vos etats : '))
    etats = list()
    for i in range(longeur):
        etats.append(input('Entrez l\'etat : '))
    etat_initial = input('Entrez-la votre etat initial : ')
    longeur = int(input('Entrez-la longeur de vos etats finaux : '))
    etats_finaux = list()
    for i in range(longeur):
        etats_finaux.append(input('Entrez l\'etat : '))
    longeur = int(input('Entrez-la longeur de vos transitions : '))
    transition = list()
    for i in range(longeur):
        transition.append(tuple(input('Entrez la transition avec le format (depart, lecture, arriver) : ').split(',')))
    automate = AFD(alphabet, etats, etat_initial, etats_finaux, transition)