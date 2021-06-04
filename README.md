# überfmt

Did you ever have a source code file with badly formatted
comments? Something like this maybe:

    /* Lorem ipsum dolor sit amet,
     * consectetur adipiscing elit.
     * Aliquam placerat faucibus luctus. Donec dolor lorem.
     */

Reformatting it so that the lines all have similar width is a
pain. For plain text at least there are [GNU fmt] and [BSD fmt]
programs, so you can pipe the text through them, and the format
it. For comments though?

[bsd fmt]: https://man.freebsd.org/fmt
[gnu fmt]: https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html

This is where überfmt comes in. It recognized typical comment
prefix symbols, and only formats the text after them, so you
can pipe the fragment above through it, and get this on the output:

    /* Lorem ipsum dolor sit amet, consectetur adipiscing elit.
     * Aliquam placerat faucibus luctus. Donec dolor lorem.
     */
