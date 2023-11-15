# Cēzara šifrs
Cēzara šifrs ir viens no kriptogrāfijā pielietotajiem šifriem. To pirmais izmantoja Jūlijs Cēzars, kad vajadzēja nosūtīt kādu ziņu savai armijai. No tā arī cēlies šī šifra nosaukums. Cēzara šifrs ir salīdzinoši vienkāršs: katrs ziņojuma burts tiek aizvietots ar citu burtu, kas atrodas, piemēram, trīs vienības tālāk alfabētā.

![Cēzara šifrs](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caesar3.svg/600px-Caesar3.svg.png "Cēzara šifrs")

# Uzdevums
Uzlabot kodu un saglabāt izmaiņas savā repozitorijā.

## Uzrakstīt koda komentārus
Uzrakstīt komentārus katrai koda rindai, kura satur:  
- if, elif, else
- for
- funkcijas definēšanu
  
Komentāriem jābūt atsevišķā no koda rindā.  
Komentāriem jāapraksta - priekš kam dota koda rinda ir vajadzīga.  
Kas ir komentāri un kā tos rakstīt [Python Comments](https://www.w3schools.com/python/python_comments.asp)  

Kad šī uzdevuma daļa ir pabeigta - izmaiņas jasinhronizē ar repozitoriju:
- jānospiež "Commit Changes"
- "Commit message" jāieraksta izmaiņu būtību
- jānospiež "Commit Changes"

## Uzlabot koda stilu (bazēts uz PEP-8)
- mainīgajiem un funkcijām jābūt aprakstošiem nosaukumiem, nedrīkst būt saisinātiem [Hint](https://www.samanthaming.com/tidbits/36-bad-variable-names-to-avoid/)
- izvairies no viena rakstzīmju nosaukumiem, ja tas nav iterators
- mainīgo un funkciju nosaukumi jābūt rakstīti snake_case stilā [Snake Case](https://www.w3schools.com/python/python_variables_names.asp)
- izmanto 4 atstarpes katram atkāpes līmenim un izvairies no tabulācijas
- ierobežo visu rindu maksimālo garumu līdz 79 zīmēm

Kad šī uzdevuma daļa ir pabeigta - izmaiņas jasinhronizē ar repozitoriju.

## Pārbaudīt koda atbilstību specifikācijai
Kods ir izstrādāts, lai veiktu šifrēšanu un atšifrēšanu, izmantojot vienkāršu Cēzara šifru uz doto tekstu. Tas nodrošina lietotājam vadības saskarni, kurā izvēlēties starp šifrēšanu, atšifrēšanu un mēģinājumu izmēģināt visas iespējamās rotācijas.

1. Programma ņem lietotāja ievadi, lai noteiktu darbības režīmu. 
  Atkarībā no izvēlētā režīma programma turpmāk lūdz lietotāju ievadīt tekstu un rotācijas vērtības.

2. Režīms 1:  
  Lietotājam tiek prasīts ievadīt tekstu un rotāciju šifrēšanai.  
  Pēc tam tiek parādīts šifrētais teksts.  
  Ja rotācijas parametrs nav vesels skaitlis - tiek paradīts kļūdas paziņojums un netiek turpināta programmas izpilde.  

3. Režīms 2:  
  Lietotājam tiek prasīts ievadīt tekstu un rotāciju atšifrēšanai.  
  Pēc tam tiek parādīts atšifrētais teksts.  
  Ja rotācijas parametrs nav vesels skaitlis - tiek paradīts kļūdas paziņojums un netiek turpināta programmas izpilde.  

4. Režīms 3:  
  Programma izdrukā dešifrētas rotācijas no 1 līdz 26, formātā "{rotācijas numurs} {dešifrēts teksts}"

5. Ja ir ievadīts neatbilstošs režīms - tiek paradīts kļūdas paziņojums

6. Ja ievadīts teksts ir ar maziem būrtiem - konvertēt tos uz lielajiem burtiem.

Piemēri:
1. Ievads: režīms 1, teksts "TODAY IS MY FAVORITE DAY", rotācija 19. Izvads: "MHWTR BL FR YTOHKBMX WTR".  
2. Ievads: režīms 2, teksts "MHWTR BL FR YTOHKBMX WTR", rotācija 19. Izvads: "TODAY IS MY FAVORITE DAY".  
3. Ievads: režīms 1, teksts "Grunkle Stan is not what he seems", rotācija 3. Izvads: "JUXQNOH VWDQ LV QRW ZKDW KH VHHPV".
4. Ievads: režīms 1, teksts "TEV AFA VLR TOFQB QEFP?", rotācija -4. Izvads: "WHY DID YOU WRITE THIS".  
  
## Ieraksti neatbilstošus specifikācijas punktus zemāk un piemini kāpēc tie neatblist
Šeit:
 - When the rotation input is not an integer, the code does not proccess the error.
 - The code does not encode text if it is not uppercase.
 - 3rd mode "Bruteforcing" deos not exist.
 - When mode 1 is chosen with inputted text: "TEV AFA VLR TOFQB QEFP?" and rotation -4 the result is: "PAR WBW RHN PKBMX MABL?" while the correct output should be: "WHY DID YOU WRITE THIS". 
Izmaiņas saglabā savā repozitorijā (Commit changes).  

## Uzrādi uzdevumu rezultātu pedagogam  

## Uzlabo kodu un salabo režīmu 3  

# Piemēri no Gravity Falls
![Gravity Falls](http://themysteryofgravityfalls.com/images/credits/001.jpg "Gravity Falls") 
![Gravity Falls](http://themysteryofgravityfalls.com/images/credits/004.jpg "Gravity Falls")   
![Gravity Falls](http://themysteryofgravityfalls.com/images/credits/011.jpg "Gravity Falls")  
