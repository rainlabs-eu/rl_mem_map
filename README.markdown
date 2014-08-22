# rl_mem_map

This app creates simple web based memory map of binary file (*.exe, *elf)

## Using

 Some basic of effects of this app looks can be found in demo of [Rainlabs webtreemap][rlwebtreemap] which is fork od [Martine's webtremap][martinewebtreemap]


### Setup

  This project uses some additional external dependencies, before you start using it you must do some preparation.
  There are two ways of doing them:
1. Run the setup.py file
2. If somehow this doesn't work follow these steps:
  -Download [Rainlabs bloat fork][rbloat] and [Rainlabs webtreemap fork][rlwebtreemap]
  -Copy bloat.py file to place where rl_mem_map.py is
  -Use index.html from bloat[rlbloat] and webtreemap.css and webtreemap.js from webtreemap[rlwebtreemap] to make such zip file:

```
bloat.zip
      +
      +--webtreemap
      +         +--webtreemap.css
      +         +--webtreemap.js
      +--index.html
```


### Running

  To run it just write in console: ```python rl_mem_map.py path1 path2 options``` or: ```./rl_mem_map path1 path2 options```
  
  It will generate new folder given by path2 with .html file which should be viewed in browser, and there you have your memory map.
  Optionally you can run it with ```-b``` option to open new made file directly in web browser.
  
  For more information check out code and/or run with ```-h```

### Providing other nm

  You have to have installed gcc with nm in order to run this app, in order to specify nm program to be run you can use specific option  (see ```-h``` or code) 

## About

  This project started because of need of making possible to visualize .map files. We found pre existent partial solutions, and decided not to use .map file, but to use nm program. Those solutions are [Martine's bloat][martinebloat] and [Martine's webtreemap][rlwebtreemap]. We developed simple app that joins together those projects. Our forks of those two can be found below.

## Related projects

* [JavaScript InfoVis Toolkit][thejit]
* [Martine's bloat project][martinebloat]
* [Martine's webtreemap project][martinewebtreemap]

[thejit]: http://thejit.org/
[martinebloat]: https://github.com/martine/bloat
[martinewebtreemap]: https://github.com/martine/webtreemap
[rlwebtreemap]: https://github.com/rainlabs-eu/webtreemap
[rlbloat]: https://github.com/rainlabs-eu/bloat
