{% extends "modules/modulefile.lua" %}
{% block footer %}
-- Access is granted only to specific groups, most likely because the software is licensed
if not isDir("{{ spec.prefix }}") then
    LmodError (
        "You don't have the necessary rights to run \"{{ spec.name }}\".\n\n",
        "\tPlease write an e-mail to 1234@epfl.ch if you need further information on how to get access to it.\n"
    )
end

-- Perform a second check to see if read access is granted to the
-- "{{ spec.prefix }}" directory.
-- This allows to use two Unix group access control modes:
-- * the first one, checked with isDir(), set with the Unix other read/execute
--   mode of the "{{ spec.prefix }}" parent's directory,
--   the original check above,
-- * and a second one, checked with isDirReadable(), set with the Unix other
--   read mode of the "{{ spec.prefix }}" directory, the added check below.
-- Access to the software is only permitted if both other check access mode
-- checks allow it.
function isDirReadable(name)
    local f=io.open(name,"r")
    if f~=nil then io.close(f) return true else return false end
end

if not isDirReadable("{{ spec.prefix }}") then
    LmodError (
        "You don't have the necessary rights to run \"{{ spec.name }}\".\n\n",
        "\tPlease write an e-mail to 1234@epfl.ch if you need further information on how to get access to it.\n"
    )
end

{% endblock %}
