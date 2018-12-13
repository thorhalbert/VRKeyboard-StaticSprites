# VR Keyboard and Menu System

This area is to handle the templates and the scripts to autogenerate the static sprites which are used for the VR keyboard project.
The sprites a the little hexagons that have the key images on them.

I like hexagons, and they going to become the basis of the menu system.

You can check out the visio drawings for some sketches of the keyboards that I did.

This repo is for a set of scripts that will enumerate the spreadsheet for the layout and play the template variables through a series of inkscape svg templates (very crudely - by pure text substitution at this point).   

These are inkscape template, so somebody with much more artistic skill than I could sculpt anything they want.

These will become sprites with a a collider which will generate the glyph that belongs to the key.
You can shoot it with a controller or (hopefully) strike the keys with a more complex rigged hand driven by a haptic glove or (and I'm going to try this), something like a leap motion rigged hand.

The idea is that objects in your world can be "keyboarded", and will have a little rotating hex with a keyboard on it, which you can press to point your keyboarding to it.  The menu button on your controller or some gesture in leap-motion will cause the keyboard to pop out near your hands or controllers.   This can pop out whatever type of keyboard or menu system that you like.  It can be keys, or 
since it's Inkscape, whatever you want to draw in SVG.

These scripts will generate a static set of png files.   The VRWorld browser will have the base keyboards generated statically, though it's possible that we can autogenerate keys (right now, I don't think that having a command line tool running in a service running Inkscape would be secure...  Most of the svg libraries/tools I've seen for Unity don't support fonts yet, but ultimately we want a tool like this can directly call internally)

![Left American1 Keyboard](https://https://github.com/thorhalbert/VRKeyboard-StaticSprites/Images/American1-L.png)