# rl_mem_map

This app creates simple web based memory map of binary file (*.exe, *elf)

## Using



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

### Providing other nm

## About

## Related projects

* [JavaScript InfoVis Toolkit][thejit]
* [Martine's bloat project][martinebloat]
* [Martine's webtreemap project][martinewebtreemap]

[thejit]: http://thejit.org/
[martinebloat]: https://github.com/martine/bloat
[martinewebtreemap]: https://github.com/martine/webtreemap
[rlwebtreemap]: https://github.com/rainlabs-eu/webtreemap
[rlbloat]: https://github.com/rainlabs-eu/bloat
