---
layout: post
title: emacs+latex环境配置 
tags: latex
---

## 安装 auctex 
使用 emacs 的包管理器，安装 auctex

## 配置 emacs
```
;; package: auctex 
(load "auctex.el" nil t t)
(setq TeX-auto-save t)
(setq TeX-parse-self t)
(setq-default TeX-master nil)

;; 使用 okular 来查看 pdf, 这里如果没有 Okular, 换成其他pdf工具也可以。
(setq TeX-view-program-list '(("okular" "okular %o")))
(setq TeX-view-program-selection '((output-pdf "okular")))

;; xelatex编译配置
(add-hook 'LaTeX-mode-hook
  (lambda()
  (add-to-list 'TeX-command-list '("XeLaTeX" "%`xelatex%(mode)%' %t" TeX-run-TeX nil t))
  (setq TeX-command-default "XeLaTeX")
  (setq TeX-save-querynil )
  (setq TeX-show-compilation t)
))
```

## 常用的快捷键
```
C-c C-c 编译
C-c C-v 预览pdf
```



