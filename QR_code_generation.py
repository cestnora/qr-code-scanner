import qrcode

code1 = qrcode.make('This is the door of your dorm. Please pull to open.')
code1.save("scene1.png")

code2 = qrcode.make('This is a wall. Please turn right and go straight for the elevator.')
code2.save("scene2.png")

code3 = qrcode.make('This is the safety gate of your floor. Please press the switch and push to open the gate.')
code3.save("scene3.png")

code4 = qrcode.make('This is a wall. Please turn left and the elevator is on your right.')
code4.save("scene4.png")

code5 = qrcode.make('These are the elevator buttons. You can press one of them to go up or down.')
code5.save("scene5.png")

code6 = qrcode.make('Once when I was six years old I saw a magniﬁcent picture in a book, called True Stories from Nature, about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal. Here is a copy of the drawing.')
code6.save("page1.png")

code7 = qrcode.make('And after some work with a colored pencil I succeeded in making my ﬁrst drawing. My Drawing Number One. It looked like this. I showed my masterpiece to the grown-ups, and asked them whether the drawing frightened them.')
code7.save("page2.png")

code8 = qrcode.make('I drew the inside of the boa constrictor, so that the grown-ups could see it clearly. They always need to have things explained. My Drawing Number Two looked like this. The grown-ups’ response, this time, was to advise me to lay aside my drawings of boa constrictors.')
code8.save("page3.png")

code9 = qrcode.make('I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them.')
code9.save("page4.png")

code10 = qrcode.make('At a glance I can distinguish China from Arizona. If one gets lost in the night, such knowledge is valuable. In the course of this life I have had a great many encounters with a great many people who have been concerned with matters of consequence.')
code10.save("page5.png")
