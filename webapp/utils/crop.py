#creating dictionaries

crop_dict = {
	'rice': """You must grow Rice in your farm.
	<br/>Rice is the seed of the grass species Oryza sativa (Asian rice) or less commonly Oryza glaberrima (African rice). 
The name wild rice is usually used for species of the genera Zizania and Porteresia, both wild and domesticated,although the term may also be used for primitive or uncultivated varieties of Oryza.
        
        <br/><br/>Important Points:

        <br/>1.Climatic Condition: Requires hot and wet climatic conditions.

        <br/>2.Season:Kharif.

        <br/>3.Temperature: Rice requires high temperature above 200C-350C and high rainfall between 150 to 300 cm.

        <br/>4.Soil:Alluvial, fertile clayey and loamy soil""",

        


        'cotton': """You must grow Cotton in your farm.
        <br/>Cotton is a soft, fluffy staple fiber that grows in a boll, or protective case, 
 around the seeds of the cotton plants of the genus Gossypium in the mallow family Malvaceae.The fiber is almost pure cellulose. Under natural conditions,the cotton bolls will increase the dispersal of the seeds.
        
        <br/><br/>Important Points:

        <br/>1.Climatic Condition: Hot climate.

        <br/>2.Season:Kharif.

        <br/>3.Temperature: The cotton plant requires high temperature ranging between 210C to 300C. Moderate rainfall ranging between 50 -75 cm is 
        required fro the growth of plant. Rainfall more than 85cm can destroy the crop.

        <br/>4.Soil:Well drained clayey soil rich in lime and phosphate is suitable for the growth of cotton plant. 
        The deep black soil of the Plateau regions and Gujarat is also considered suitable for the growth of cotton plant.l""",



       'jute':"""You must grow Jute in your farm.
       <br/>Jute is a long, soft, shiny bast fiber that can be spun into coarse, strong threads. It is produced from flowering plants in the genus Corchorus, which is in the mallow family Malvaceae"

       	<br/><br/>Important Points:

       	<br/>1.Climatic Condition: Hot and Humid climate.

        <br/>2.Season:Kharif.

        <br/>3.Temperature: It requires temperature ranging between 240C to 350C and annual rainfall of more than 150cm.

        <br/>4.Soil:New alluvial soil is considered suitable for the growth of jute crop.""",



        'coffee':"""You must grow Coffee in your farm.
        <br/>Coffea is a genus of flowering plants in the family Rubiaceae. Coffea species are shrubs or small trees native to tropical and southern Africa and tropical Asia. 
The seeds of some species, called coffee beans, are used to flavor various beverages and products.
       
       	<br/><br/>Important Points:

       	<br/>1.Climatic Condition: Warm climate.

        <br/>2.Season:Harvesting varies from season to season.

        <br/>3.Temperature: Temperature: 150C to 280C.Rainfall: between 150cm to 200 cm

        <br/>4.Soil:Rich well drained friable loamy soil""",



        'coconut':"""You must grow Coconut in your farm.
        <br/>It is one of the most useful trees in the world and is often referred to as the "tree of life". It provides food, fuel, cosmetics, folk medicine and building materials, among many other uses. 
The inner flesh of the mature seed, as well as the coconut milk extracted from it, form a regular part of the diets of many people in the tropics and subtropics.

	<br/><br/>Important Points:

       	<br/>1.Climatic Condition: Equatorial climate with high humidity..

        <br/>2.Season:Harvesting varies from season to season.

        <br/>3.Temperature:It requires 27oC with 5-7o diurnal variation.Rainfall of 1300-2300 mm per annum 

        <br/>4.Soil: Laterite, alluvial, red sandy loam, coastal sandy and reclaimed soils""",



        'grapes':"""You must grow Grapes in your farm.
        <br/>The grape is the most important crop grown in the world. Mostly it grown for making wines and preparation of raisin and then as a table fresh fruit.While in India, it is mainly grown for table use. 

	<br/><br/>Important Points:

       	<br/>1.Climatic Condition: The ideal climate for grape growing is the Mediterranean climate.

        <br/>2.Season:Normal grape harvest season starts in February and continuous up to end of April.

        <br/>3.Temperature: Above 100C to 400C influence the yield and quality.

        <br/>4.Soil: The grape is widely adopted to various soil conditions, 
	but the yield and quality reach to the highest on good fertile soils have pH 6.5 to 8.5, organic carbon above 1.0%, free of lime and having a medium water holding capacity""",

		
	'watermelon':"""You must grow Watermelon in your farm.
	<br/>Watermelon (Citrullus lanatus) is a flowering plant species of the Cucurbitaceae family. A scrambling and trailing vine-like plant, it was originally domesticated in Africa. 
It is a highly cultivated fruit worldwide, with more than 1,000 varieties.


	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Grown in climates from tropical to temperate.

        <br/>2.Season:Harvesting varies from season to season.

        <br/>3.Temperature:higher than about 25 °C.

        <br/>4.Soil: loamy, somewhat-sandy, well-drained soil.""",



        'mango':"""You must grow Mango in your farm.
        <br/>A mango is an edible stone fruit produced by the tropical tree Mangifera indica which is believed to have originated from the region between northwestern Myanmar, Bangladesh, and northeastern India.

        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Grown in climates which is humid and dry conditions. I.

        <br/>2.Season:The mango season in India starts in March-April from the South West and moves towards the North East in June-July.

        <br/>3.Temperature:The ideal temperature range for mango is 24 -30 C during the growing season, along with high humidity.

        <br/>4.Soil:  Mango grows well on wide variety of soils, such as lateritic,alluvial, sandy loam and sandy""",


        'orange':"""You must grow Orange in your farm.
        <br/>The orange is the fruit of various citrus species in the family Rutaceae (see list of plants known as orange); it primarily refers to Citrus × sinensis,[1] which is also called sweet orange.


        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Arid and semi-arid regions of the southwest to humid tropical regions .

        <br/>2.Season:The ideal season for cultivation of sweet orange is July to September.

        <br/>3.Temperature:Between 15.5 and 29 °C (59.9 and 84.2 °F)—and require considerable amounts of sunshine and water

        <br/>4.Soil: Prefer light to medium textured soils, with good drainage and free from stagnant water""",

       

        'papaya':"""You must grow Papaya in your farm.
        <br/>The papaya is a small, sparsely branched tree, usually with a single stem growing from 5 to 10 m (16 to 33 ft) tall, with spirally arranged leaves confined to the top of the trunk.


        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Thrive in subtropical and tropical climates. .

        <br/>2.Season:The ideal season for cultivation of sweet orange is July to September.

        <br/>3.Temperature: Optimum temperature is 25 - 30° C and minimum 16° C.

        <br/>4.Soil: Deep, well drained sandy loam soil is ideal""",


        'banana':"""You must grow Banana in your farm.
        <br/>The banana plant is the largest herbaceous flowering plant.[8] All the above-ground parts of a banana plant grow from a structure usually called a "corm".
Plants are normally tall and fairly sturdy, and are often mistaken for trees, but what appears to be a trunk is actually a "false stem" or pseudostem.


		
        <br/><br/>Important Points:

       	<br/>1.Climatic Condition: essentially a humid tropical plant .

        <br/>2.Season: Kharif - June – July · Rabi - October – November.

        <br/>3.Temperature: Optimum temperature is range of 10° C to 40° C and an average of 23° C

        <br/>4.Soil:Deep,Alluvial, rich loamy soil with pH between 6.5 – 7.5 is most preferred """,



        'pineapple':"""You must grow Pineapple in your farm.
        <br/>Pineapples are tropical fruits that are rich in vitamins, enzymes and antioxidants.The fruit is made of many individual berries that grow together around a central core.


         <br/><br/>Important Points:

       	<br/>1.Climatic Condition: It is a tropical or near tropical plant limited (except in greenhouses) to low elevations between 30°N and 25°S.

        <br/>2.Season:  July to September is the main growing season in India and it takes almost 18-24 months to mature for harvesting

        <br/>3.Temperature: temperature range of 65°-95°F (18.33-45°C) is most favorable.

        <br/>4.Soil:well-aerated and free-draining loams, sandy loams and clay loams with no heavy clay or rock within one metre of the surface """,


        'maize':"""You must grow Maize in your farm.
        <br/>Maize is an annual grass in the family Gramineae, which includes such plants as wheat, rye, barley, rice, sorghum, and sugarcane. 
There are two major species of the genus Zea (out of six total): Zea mays (maize) and Zea diploperennis, which is a perennial type of teosinte.
    
		
	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Thrive in Warm and Humid climate.

        <br/>2.Season:In Kharif but also cultivated in Rabi.

        <br/>3.Temperature:A temperature of 21°C- 27°C and 50-100cm rainfall .

        <br/>4.Soil: It grows well in alluvial and red soils with good drainage.""",


        'chickpea':"""You must grow Chickpea in your farm.
        <br/>The chickpea or chick pea (Cicer arietinum) is an annual legume of the family Fabaceae, subfamily Faboideae. 
Its different types are variously known as gram or Bengal gram, garbanzo or garbanzo bean, or Egyptian pea. Chickpea seeds are high in protein.
   

	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:  It is a cool season annual crop and containing moisture.

        <br/>2.Season:grown in rabi (postrainy season) following a kharif (rainy season) crop or kharif fallow. The sowing is done in the month of October or November.

        <br/>3.Temperature: The crop performs better at 24-32 C temperature.

        <br/>4.Soil: are best suited to well-drained loam and clay loam soils that are neutral to alkaline (pH 6.0–9.0) and have good water holding capacity.""",
 


        'kidneybeans':"""You must grow Kidneybeans in your farm.
        <br/>The kidney bean is a variety of the common bean. It is named for its visual resemblance in shape and – for the red variety – colour to a human kidney.

  	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:   This crop grows well in tropical and temperate areas.

        <br/>2.Season:For spring season, best time for Kidney beans cultivation is February-March and for Kharif season, it is sown during May-June month.

        <br/>3.Temperature:  Ideal temperature for better yield is 15°C to 25°C

        <br/>4.Soil: It can be grown on wide range of soils from light sandy to heavy clay soils. Well drained loamy soil is good for kidney beans cultivation.""",   


   	'blackgram':"""You must grow Blackgram in your farm.
   	<br/>Vigna mungo, the black gram, urad bean, ulundu paruppu, minapa pappu, mungo bean or black matpe bean (māṣa) is a bean grown in South Asia. 
Like its relative, the mung bean, it has been reclassified from the Phaseolus to the Vigna genus.        	

  		

	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:  This crop prefers dry weather condition.

        <br/>2.Season:Second fortnight of June (15to 30 June) is the proper time of black gram sowing in kharif season.In summer, sowing should be done from third week of Feb. to First week of April.

        <br/>3.Temperature:The temperature in between 25 to 350 C is perfect for the black gram cultivation  .

        <br/>4.Soil: Black gram cultivation requires the black cotton soil, sandy loam, loam or heavy clay loam soils""",


        'mungbean':"""You must grow Mungbean in your farm.
        <br/>The mung bean, alternatively known as the green gram, maash, moong, monggo, or munggo, is a plant species in the legume family.


        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:  mung beans are adapted to warm, dry climates.

        <br/>2.Season:Optimum time for kharif sowing is first fortnight of July. Optimum time for summer moong cultivation is from March to April..

        <br/>3.Temperature:The crop needs high temperature, less humidity and moderate rainfall of about 60-80 cm .

        <br/>4.Soil: Mung beans are the ones love to grow in the soil which is fertile, loamy and sandy..""",


        'lentil':"""You must grow Lentil in your farm.
        <br/>The lentil (Lens culinaris or Lens esculenta) is an edible legume. It is an annual plant known for its lens-shaped seeds. 
It is about 40 cm (16 in) tall, and the seeds grow in pods, usually with two seeds in each.


		
        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:  Lentil requires cold climate usually grown in semi-arid climates without irrigation.

        <br/>2.Season:lentil is planted in the winter season in the months of November-December and thus is referred as Rabi crop.

        <br/>3.Temperature:The optimum temperature for growth is 18-30 C.

        <br/>4.Soil:Well drained, loam soils with neutral reaction are best for lentil cultivation.""",

        
        'mothbeans':"""You must grow Mothbean in your farm.
        <br/>Vigna aconitifolia is a drought-resistant legume, commonly grown in arid and semi-arid regions of India. It is commonly called mat bean, moth bean, matki or dew bean. The pods, sprouts and protein-rich seeds of this crop are commonly consumed in India.

			
	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:   arid and semi-arid regions with extreme weather and fewer rain.

        <br/>2.Season:The moth bean is a Kharif crop, and it is generally sown in May and June with onset of first monsoon showers. 

        <br/>3.Temperature:The ideal temperature level for growing Moth bean is between 24°C and 32°C .

        <br/>4.Soil: While dry sandy soil is most suitable for production.""",
        
        
        'apple':"""You must grow Apple in your farm.
        <br/>An apple is an edible fruit produced by an apple tree. Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today.


			
	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:   best in climates where it's cold in winter, moderate in the summer and has medium to high humidity.

        <br/>2.Season:Normally the apples are ready for harvest from September-October except in the Nilgiris where the season is from April to July.

        <br/>3.Temperature:The average summer temperature should be around 21-24oC during active growth period.

        <br/>4.Soil: Apples grow best on a well-drained, loam soils having a depth of 45 cm and a pH range of pH 5.5-6.5.""",



        'pomegranate':"""You must grow Pomegranate in your farm.
        <br/>The pomegranate is a fruit-bearing deciduous shrub in the family Lythraceae, subfamily Punicoideae, that grows between 5 and 10 m tall.


        <br/><br/>Important Points:

       	<br/>1.Climatic Condition:   The tree requires hot and dry climate during fruit development and ripening.

        <br/>2.Season:Pomegranates are available all year round in India, but we mainly export produce from August to October and from January to March. 

        <br/>3.Temperature: temperature ranging between 15-25° is considered ideal for growing pomegranates.

        <br/>4.Soil: Deep loamy or alluvial, well drain soil is highly recommended for pomegranate cultivation.""",


        'pigeonpeas':"""You must grow Pigeonpeas in your farm.
        <br/>The pigeon pea (Cajanus cajan), also known as arhar, tur, red gram, or gungo peas in Jamaica is a perennial legume from the family Fabaceae. 
Since its domestication in the Indian subcontinent at least 3,500 years ago.

		 

	<br/><br/>Important Points:

       	<br/>1.Climatic Condition: predominantly a crop of tropical areas mainly cultivated in semi arid regions of India.

        <br/>2.Season:Pigeonpea, a kharif season crop.In the rainy season (June to October) and 17° to 22°C in the postrainy (November to March) season.

        <br/>3.Temperature: Pigeonpea can be grown with a temperature ranging from 26°C to 30°C in the rainy season.

        <br/>4.Soil: It is successfully grown in black cotton soils, well drained.""",


        'muskmelon':"""You must grow Muskmelon in your farm.
        <br/>Muskmelon, also known as Cucumis melo, is a species of melon that belongs to the gourd family. It's closely related to other plants like squash, pumpkin,  and watermelon .
Muskmelon has a ribbed, tan skin and a sweet, musky flavor and aroma"
  		


	<br/><br/>Important Points:

       	<br/>1.Climatic Condition:is a hot and dry season crop and plenty sunshine.

        <br/>2.Season: Muskmelon's main season occurs in the summer months from April to July, though a few off-season cultivars may appear throughout the year.

        <br/>3.Temperature: best at the temperature of 28°C - 30 °C and grows well at 25°C - 35°C.

        <br/>4.Soil:  Sandy loam rich in organic matter with good drainage."""


   }

#print(dict["apple"])
#print(dict.keys())
