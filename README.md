# überfmt

Überfmt formats paragraphs of plain text so that each line is
close to the optimal length. It is an upgrade over [GNU fmt]
and [BSD fmt] in that it supports Unicode and automatically
recognizes comment-like formatting.

[bsd fmt]: https://man.freebsd.org/fmt
[gnu fmt]: https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html

For example überfmt will translate this badly formatted fragment
of text:

    /* Lorem ipsum dolor sit amet,
     * consectetur adipiscing elit. Aliquam placerat faucibus
     * luctus. Donec dolor lorem.
     */

into the following, all while preserving the comment structure:

    /* Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     * Aliquam placerat faucibus luctus. Donec dolor lorem.
     */

Überfmt is language-agnostic and will work equally well for
most conventionally-formatted comment styles: C, Shell, Pascal,
everything goes.

# How to use?

Pipe your text into the standard input of the `uberfmt` command,
collect the formatted text on the output.

The author also uses the following Vim shortcuts:

    nmap \f vap!uberfmt<CR>
    vmap \f !uberfmt<CR>

This way pressing `\f` inside a paragraph (or after selecting a
fragment of text) will reformat it with `uberfmt`.

# How to install?

Just download [uberfmt] from Github; it’s a single file program.
    
[pypi]: https://pypi.org/project/uberfmt/
[uberfmt]: https://raw.githubusercontent.com/magv/uberfmt/master/uberfmt
