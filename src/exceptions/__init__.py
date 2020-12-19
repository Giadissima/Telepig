class NoUsernameException(Exception):
  """
  Exception raised when the user who performed
  an action doesn't have username.
  """

  def __init__(self):
    self.message = "Devi impostare un username per poter creare un raid"
    super().__init__(self.message)

  def __str__(self):
    return self.message

class IncompleteRegistrationException(Exception):
  """
  Exception raised when the user who performed
  an action doesn't have completed the registration.
  """
  def __init__(self):
    self.message = "Completa la registrazione per usare questa funzionalità."
    super().__init__(self.message)
  
  def __str__(self):
    return self.message

class NoRaidFoundException(Exception):
  """
  Exception raised when the user who performed
  an action with any inexistent raid.
  """
  def __init__(self):
    self.message = "Non sono riuscito a trovare il raid che cerchi."
    super().__init__(self.message)
  
  def __str__(self):
    return self.message

class NoLanguageFoundException(Exception):
  def __init__(self):
    self.message = "Non sono riuscito a trovare il messaggio"
    super().__init__(self.message)

  def __str__(self):
    return self.message

class No (Exception):
  def __init__(self):
    self.message = "Non sono riuscito a trovare il messaggio"
    super().__init__(self.message)

  def __str__(self):
    return self.message

class Unknown(Exception):
  """
  Exception raised when we don't know what the fuck is going on.
  """
  def __init__(self, message = "Errore sconosciuto!"):
    self.message = message
    super().__init__(self.message)
  
  def __str__(self):
    return self.message
