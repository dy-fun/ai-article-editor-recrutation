Jak włączyć program?
  Aby korzystać z programu należy najpierw w tej samej lokalizacji co plik *.exe dodać plik ".env" zawierający klucz API.
  Klucz powinien zostać zapisany w sposób: OPENAI_API_KEY=<klucz do openai api>
Jak korzystać z programu?
  Po włączeniu programu należy wybrać plik tekstowy w którym znajduje się treść artykułu.
  Po wybraniu pliku zostanie wygenerowany plik artykuł.html z przetworzoną zawartością za pomocą ai.
W jaki sposób działa program?
  Program na początku pobiera klucz api z pliku .env oraz sprawdza czy jest poprawny.
  Po sprawdzeniu klucza, program prosi użytkownika o wybranie pliku tekstowego zawierającego treść artykułu
  Po wybraniu pliku, treść artykułu zostaje przetworzona przez openai api 
  Następnie program tworzy plik z przetworzoną zawartością artykułu
  Utworzenie pliku kończy działanie programu.
  
